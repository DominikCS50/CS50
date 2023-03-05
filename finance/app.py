import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
#from datetime import datetime

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        return render_template("index.html")

    # User reached route via GET (as by clicking a link or via redirect)
    else:

        # Query database for all stocks, grouped and ordered alphabetically
        stocks = db.execute(
            "SELECT symbol, name, shares, price, total, SUM(shares) AS shares, SUM(total) AS total FROM stocks WHERE userid = ? GROUP BY symbol ", session.get("user_id"))

        # Query database for user's cach value and sum of stocks he already has
        cash = (db.execute("SELECT cash FROM users WHERE id = ?", session.get("user_id"))[0]['cash'])
        sum = (db.execute("SELECT SUM(total) FROM stocks WHERE userid = ?", session.get("user_id"))[0]['SUM(total)'])

        # Checking if User has already got any stocks
        if isinstance(sum, type(None)):
            return render_template("index.html")

        # Render template with data
        else:
            total = sum + cash
            return render_template("index.html", stocks=stocks, cash=cash, total=total)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol", 400)

        # Ensure shares were submitted
        elif not request.form.get("shares") or not request.form.get("shares").isdigit():
            return apology("must provide shares", 400)

        # Ensure user provided data and the data has only letters
        elif not request.form.get("symbol").isalpha() or lookup(request.form.get("symbol")) is None:
            return apology("invalid symbol", 400)

        # Query database for user's cash
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session.get("user_id"))[0]['cash']

        # Calling lookup function to get data from API
        name = lookup(request.form.get("symbol"))["name"]
        symbol = lookup(request.form.get("symbol"))["symbol"]
        price = lookup(request.form.get("symbol"))["price"]
        shares = float(request.form.get("shares"))
        total = shares * price
        cash_new = cash - total
        # dd/mm/YY H:M:S
        #datetime = now.strftime("%d/%m/%Y %H:%M:%S")

        # Check if is enough cash
        if (cash < total):
            return apology("not enough cash")

        # If is enough cash, save stocks to db
        else:

            # Get time-stamp
            time = db.execute("SELECT CURRENT_TIMESTAMP")[0]['CURRENT_TIMESTAMP']
            db.execute("INSERT INTO stocks (symbol, name, shares, price, total, userid, time) VALUES (?, ?, ?, ?, ?, ?, ?)",
                       symbol, name, shares, price, total, session.get("user_id"), time)
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash_new, session.get("user_id"))
            return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():

    request.method == "GET"

    # Quesry database for user's stocks transactions
    stocks = db.execute("SELECT symbol, shares, price, time FROM stocks WHERE userid = ? ORDER BY time", session.get("user_id"))

    return render_template("history.html", stocks=stocks)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure user provided data and the data has only letters and is lookuple
        if not request.form.get("symbol") or not request.form.get("symbol").isalpha() or lookup(request.form.get("symbol")) is None:
            return apology("invalid symbol", 400)

        # Calling lookup function
        name = lookup(request.form.get("symbol"))["name"]
        symbol = lookup(request.form.get("symbol"))["symbol"]
        price = usd(lookup(request.form.get("symbol"))["price"])

        return render_template("quoted.html", name=name, symbol=symbol, price=price)

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 400)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 400)

        # Ensure the password_check was submitted
        elif not request.form.get("confirmation"):
            return apology("must confirm password", 400)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure if same username already exist
        if len(rows) == 1 and request.form.get("username") == rows[0]["username"]:
            return apology("username already exists", 400)

        # Ensure the password_check was proper
        if request.form.get("password") != request.form.get("confirmation"):
            return apology("passwords must match", 400)

        # Generate hash password
        # generate_password_hash(request.form.get("password"), pbkdf2:sha256, 8)

        # Query database for username and password
        rows = db.execute("INSERT INTO users (username, hash) VALUES (?, ?)", request.form.get(
            "username"), generate_password_hash(request.form.get("password"), 'pbkdf2:sha256', 8))

        # Remember which user has logged in
        session["user_id"] = rows

        # Redirect user to home page
        return redirect("/login")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # return render_template("buy.html")

        # Ensure symbol was submitted
        if not request.form.get("symbol"):
            return apology("must provide symbol", 403)

        # Ensure shares were submitted
        elif not request.form.get("shares"):
            return apology("must provide shares", 403)

        # Query database for user's data
        cash = db.execute("SELECT cash FROM users WHERE id = ?", session.get("user_id"))[0]['cash']
        raw = db.execute(
            "SELECT symbol, name, shares, price, total, SUM(shares) AS shares, SUM(total) AS total FROM stocks WHERE symbol = ? GROUP BY symbol", request.form.get("symbol"))
        symbol = raw[0]['symbol']
        name = raw[0]['name']
        shares = raw[0]['shares']
        price = raw[0]['price']
        total = raw[0]['total']
        shares_new = -int(request.form.get("shares"))
        total_new = shares_new * price
        cash_new = cash + price * int(request.form.get("shares"))
        # return render_template("quoted.html", name = cash,)

        # Check if user has enough shares to sell
        if shares < int(request.form.get("shares")):
            return apology("not enough shares")

        # Insert sold stock and make a change in chash db
        else:
            db.execute("INSERT INTO stocks (symbol, name, shares, price, total, userid) VALUES (?, ?, ?, ?, ?, ?)",
                       symbol, name, shares_new, price, total_new, session.get("user_id"))
            #db.execute("UPDATE stocks SET shares = ?, total = ? WHERE symbol = ?", shares, total, session.get("user_id"))
            db.execute("UPDATE users SET cash = ? WHERE id = ?", cash_new, session.get("user_id"))
            return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        symbols = db.execute("SELECT symbol FROM stocks WHERE userid = ? GROUP BY symbol ", session.get("user_id"))
        return render_template("sell.html", symbols=symbols)
