#include <cs50.h>
#include <stdio.h>

int main(void)

{
    int n;
    do
    {
      n = get_int("Height:\n");
    }
  while (n < 1 || n > 8);

// For each row
  for (int i=0; i <n; i++)
  {

    // Print spaces for each column
      for (int j=i; j < n-1; j++)
      {
          printf(" ");
      }
    // Print Hashes for each column
      for (int j=-1; j < i; j++)
      {
          printf("#");
      }
      printf("\n");
  }
}