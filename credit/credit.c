#include <cs50.h>
#include <stdio.h>

int main(void)
{
    while (true)
    {
    long n = get_long ("Number\n");

    int sld = n % 100 /10*2;
    int fld = n % 10000 / 1000*2;
    int seld = n % 1000000 / 100000*2;
    int eld = n % 100000000 / 10000000*2;
    int tld = n % 10000000000 / 1000000000*2;
    int twld = n % 1000000000000 / 100000000000*2;
    int fold = n % 100000000000000 / 10000000000000*2;
    int sexld = n % 10000000000000000 / 1000000000000000*2;


    printf("sld %i\n fld %i\n seld %i\n eld %i\n tld %i\n twld %i\n fold %i\n sexld %i\n", sld, fld, seld, eld, tld, twld, fold, sexld);
    }
}
