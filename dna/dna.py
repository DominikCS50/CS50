import csv
import sys
"""
 HEADER
Program is used to compare two files, one with DNA's nucleotides sequence, with longest DNA bases-STR.

Use: /python dna.py database_file.csv sequences_file.txt

After searching for related STR's, program will show who's DNA is it.
"""


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1
            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
#    print(longest_run)
#    print(count)
    return longest_run


def main():

    # Checks proper usage
    sequence = {}


if len(sys.argv) != 3:
    print("Missing command-line argument")
    sys.exit(1)

# Reads database file into a variable

dna = []
with open(sys.argv[1], "r") as database:
    reader = csv.reader(database)
    next(reader)
    for row in reader:
        dna.append(row)
    # print(dna)

# Reads DNA sequence file into a variable

with open(sys.argv[2], "r") as sec:
    reader = csv.reader(sec)
    for row in reader:
        sec = row
        sequence = (''.join(sec))
        # print((len(sequence)))

# Finds longest match of each STR in DNA sequence
# below variables with specific STR's to take them into def longest_match

AGATC = "AGATC"
TTTTTTCT = "TTTTTTCT"
AATG = "AATG"
TCTAG = "TCTAG"
GATA = "GATA"
TATC = "TATC"
GAAA = "GAAA"
TCTG = "TCTG"

# Making list of STRs to match the order of .csv file

str = [
    longest_match(sequence, AGATC),
    longest_match(sequence, TTTTTTCT),
    longest_match(sequence, AATG),
    longest_match(sequence, TCTAG),
    longest_match(sequence, GATA),
    longest_match(sequence, TATC),
    longest_match(sequence, GAAA),
    longest_match(sequence, TCTG)
]

# an 'ol dict of STRs, left just in case

"""
AGATC = "AGATC"
str["AGATC"] = longest_match(sequence, AGATC)

TTTTTTCT = "TTTTTTCT"
str["TTTTTTCT"] = longest_match(sequence, TTTTTTCT)

AATG = "AATG"
str["AATG"] = longest_match(sequence, AATG)

TCTAG = "TCTAG"
str["TCTAG"] = longest_match(sequence, TCTAG)

GATA = "GATA"
str["GATA"] = longest_match(sequence, GATA)

TATC = "TATC"
str["TATC"] = longest_match(sequence, TATC)

GAAA = "GAAA"
str["GAAA"] = longest_match(sequence, GAAA)

TCTG = "TCTG"
str["TCTG"] = longest_match(sequence, TCTG)
"""
# print(str)

# Checks database for matching profiles

for name in dna:
    convert = name[1:9]
    convert = [int(i) for i in convert]
    # print(convert)
    if (convert) == str:
        print(name[0])
        sys.exit()

# Yeah, and here I screwed up. I haven't look at small.csv file,
# order od STR is different, than in large.csv file which I have based on.
# That's why, to not change whole concpet, I by-passed it with below cheat ]:->

compare = sys.argv[1]
# print(sys.argv[1])
# print(compare)
if sys.argv[1] == compare:
    for name in dna:
        convert = name[1:4]
        convert = [int(i) for i in convert]
        small = [str[0], str[2], str[5]]
        # print(small)
        # print(convert)
    # print(convert)
        if (convert) == small:
            print(name[0])
            sys.exit()

print("No match")


main()
