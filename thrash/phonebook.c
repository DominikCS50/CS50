#include <cs50.h>
#include <stdio.h>
#include <string.h>


typedef struct
{
    string name;
    string number;
}
person; // name of the structer

int main(void)
{

    person people[2];

    people[0].name = "Carter";
    people[0].number = "01";

    people[1].name = "David";
    people[1].number = "02";

// Searching for a number attached to the name (not by order, but by assignet int)
    for (int i = 0; i < 2; i++)
    {
            if (strcmp(people[i].name, "David") == 0)
            {
                printf("Found %s\n", people[i].number);
                return 0;
            }
    }
    printf("Not found\n");
    return 1;
}