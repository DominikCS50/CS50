#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <stdlib.h>
#include <string.h>

bool only_digits(string s);
char rotate(char c, int n);

int main(int argc, string argv[])
{
    if (argc == 2 && only_digits(argv[1]))
    {
        printf("%s\n", argv[1]);
        int k = atoi(argv[1]);
        string text = get_string("plaintext:");
        printf("ciphertext: ");
        for (int i = 0; i < strlen(text); i++)
        {
            char c = rotate(text[i], k);
            printf("%c", c);
        }
        printf("\n");
        return 0;
    }
    //%s", cipher
    printf("Usage: ./caesar key\n");
    return 1;
//    rotate(text)
//    for ( c; strlen; i++)
}

// atoi <stdlib.h> - changes string argv[] = int

bool only_digits(string s)
{
    for (int i = 0; i < strlen(s); i++)
    {
        if (! isdigit(s[i]))
        {
            return false;
        }
    }

// for dajemy tylko do pętlenia i liczymy wystarczy do dwóch
    // if dajemy do sprawdzenia warunków, to czy true czy false dajemy na koeiec pjednej i drugiej pętli
    //if
    //return true;
    return true;
}

char rotate(char c, int n)
{
    // take char (text) as input and move it by int (k)
    int x = 0;
    if (isalpha(c) && isupper(c))
    {
        c = c - 65;
        x = (c + n) % 26;
        if (x > 25)
        {
            x = x - 26;
        }
        x = x + 65;
    }
    else if (isalpha(c) && islower(c))
    {
        c = c - 97;
        x = (c + n) % 26;
        if (x > 25)
        {
            x = x - 26;
        }
        x = x + 97;
    }
    else
    {
        return c;
    }
    return x;
}
// zrobiłem tak że x to musi być a albo A i jeśli wychodzi poza litery to przewija.
// nie wiem czy działa, do sprawdzenia. dorobić resztę

//c = (p +k) % 26;
//



//     if (i > 48 && i < 57)


//    int k = 0;
//    if (argc == 2 || isdigit(k))
//    {
//        int key = argv[1];
//    }
//    else;
//   {
//        printf("Usage: ./caesar key");
//    }
//    string text = get_string("");
//    printf("plain text: %s\n", text);


