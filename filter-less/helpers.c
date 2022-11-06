#include <math.h>
#include "helpers.h"

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{

    for (int i = 0; i < height; i++)
{
    for (int j = 0; j < width; j++)
    {
        float gray_temp = (image[i][j].rgbtBlue + image[i][j].rgbtGreen + image[i][j].rgbtRed) / 3.0;
        int gray = roundf(gray_temp);
        image[i][j].rgbtBlue = gray;
        image[i][j].rgbtGreen = gray;
        image[i][j].rgbtRed = gray;

    }
}

// 3 kolory mają mieć taką samą wartość, bierzemy średnią z nich, zaokrąglamy do int i tyle.

    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{

    for (int i = 0; i < height; i++)
{
    for (int j = 0; j < width; j++)
    {
        RGBTRIPLE org_image = image[i][j];
                int red = roundf(.393 * org_image.rgbtRed + .769 * org_image.rgbtGreen + .189 * org_image.rgbtBlue);
                      if (red > 255)
            {
                image[i][j].rgbtRed = 255;
            }
                else
                image[i][j].rgbtRed = red;

        int green = roundf(.349 * org_image.rgbtRed + .686 * org_image.rgbtGreen + .168 * org_image.rgbtBlue);
            if (green > 255)
        {
            image[i][j].rgbtGreen = 255;
        }
            else
            image[i][j].rgbtGreen = green;

         int blue = roundf(.272 * org_image.rgbtRed + .534 * org_image.rgbtGreen + .131 * org_image.rgbtBlue);
                if (blue > 255)
            {
                image[i][j].rgbtBlue = 255;
            }
            else
        image[i][j].rgbtBlue = blue;


    }
}

    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{

    for (int i = 0; i < height; i++)
{
    for (int j = 0; j < width / 2; j++)
    {
        RGBTRIPLE swap = image[i][j];
        image[i][j] = image [i][width-j];
        image [i][width-j] = swap;
    }
}
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    RGBTRIPLE org_image[height][width];
    for (int i = 0; i < height; i++)
{
    for (int j = 0; j < width; j++)
    {
        RGBTRIPLE org_image[i][j] = image [i][j];
    }
}
    for (int k = 0; k < height; k++)
{
    for (int l = 0; l < width; l++)
    {
//        if (i > 0 && j > 0)
//        image[k][l]
        image[k][l].rgbtRed = roundf(org_image[k-1][l-1].rgbtRed + org_image[k-1][l].rgbtRed + org_image[k-1][l+1].rgbtRed + org_image[k][l-1].rgbtRed + org_image[k][l].rgbtRed + org_image[k][l+1].rgbtRed + org_image[k+1][l-1].rgbtRed + org_image[k+1][l].rgbtRed + org_image[k+1][l+1].rgbtRed) / 9;
    }
}

    return;
}
