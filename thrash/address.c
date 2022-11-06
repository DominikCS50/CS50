#include<stdio.h>
#include<cs50.h>

int main(void)
{
    char *s = "HI!";
    printf("%p\n", s);
    printf("%p\n", &s[0]);
    printf("%p\n", &s[1]);
    printf("%p\n", &s[2]);
    printf("%p\n", &s[3]);
//    int n = 50;
//    int *p = &n;
//    printf("%p\n", p);
//    printf("%i\n", *p); //*p - not declaring variable, only going to its address
}