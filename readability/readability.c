#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <math.h>

// Program is to perform "readability test" of Coleman-Liau index. It's designed to output that (U.S.) grade level that is needed to understand some text.

int count_letters(string s);
int count_words(string s);
int count_sentences(string s);

int main(void)
{
    string text = get_string("Text:\n");
    float letters = count_letters(text);
    float words = count_words(text);
    float sentences = count_sentences(text);
//    printf("Letters: %f\n", letters);
//    printf("Words: %f\n", words);
//    printf("Sentences: %f\n", sentences);

    float L = letters / words * 100;
    float S = sentences / words * 100;
    float index = 0.0588 * L - 0.296 * S - 15.8;

    if (index > 1 && index < 16)
    {
        printf("Grade %i\n", (int) round(index));
    }
    else if (index < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade 16+\n");
    }
}

int count_letters(string s)
{
    int i = 0;
    int letters = 0;
    while (s[i] != '\0')
    {
        char c = s[i];
        if (isalpha(c))
        {
            letters++;
        }
        i++;
    }
    return letters;
}

int count_words(string s)
{
    int i = 0;
    int words = 1;
    while (s[i] != '\0')
    {
        int c = s[i];
        if (c == 32)
        {
            words++;
        }
        i++;
    }
    return words;
}

int count_sentences(string s)
{
    int i = 0;
    int sentences = 0;
    while (s[i] != '\0')
    {
        int c = s[i];
        if (c == 33 || c == 46 || c == 63)
        {
            sentences++;
        }
        i++;
    }
    return sentences;
}


// L is the average number of letters per 100 words in the text
// S is the average number of sentences per 100 words in the text

// we take text as array, and with for loop we count it up. We need to erase \0
// s[text]
// string as an array of characters
// use variable letters to count how may characters there are
