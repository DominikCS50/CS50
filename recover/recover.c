#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define BLOCK_SIZE 512

int main(int argc, char *argv[])
{

typedef uint8_t byte;
byte buffer[BLOCK_SIZE];
int n = 0;


//Open memory card
FILE *f = fopen(argv[1], "r");
//Repeat until end of card:
//Read 5112 bytes into a buffer
//fread(data, size, number, inptr);
//data - pointer tp where to store read data
//size- size of bytes
//number - number of elements
//inptr: File * to read from

while (fread(buffer, sizeof(byte), BLOCK_SIZE, f) == BLOCK_SIZE)
//fread (buffer, 1, 512, *argv);
//If start of new JPEG
if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&(buffer[3] & 0xf0) == 0xe0)
    {
//make a name, make a file, write it, until new starts, close this one and start next
sprintf(img.jpg, "%03i.jpg", n);
File *img = fopen(img.jpg, "w");
fwrite (buffer, byte, 512, File *img);
n ++;
// n is the number of ###
    }
// make JPEG and write new file

// Else
// Close the file that have been read
// Else
// If already found JPEG
// keep writing to JPEG in loop because it may be more than 512 bytes
// Close any remaining files
//###.jpg 000.jpg
}