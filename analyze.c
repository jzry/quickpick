#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <ctype.h>

//// Scan for the total number of lottery numbers.
//int scan_for_total(int *data)
//{
//    int total;
//
//
//    return total;
//}
//
//// Display statistics of numbers.
//void display_percent(int *data, int total)
//{
//
//}

int main(void)
{
    FILE *ifp, *ofp;
    int *data, digit;
    char *buffer, c;

    // File that we will take lottery numbers from.
    ifp = fopen("numbers.txt", "r");

    // File that we will write statistics to.
    ofp = fopen("stats.txt", "w");

    while (fscanf(ifp, "%c", &c) != EOF)
    {
        if (iscntrl(c) == 0 || c != ' ')
        {
            digit = atoi(&c);
            printf("%d", digit);
        }
        else
        {
            printf(" ");
        }
    }

//    scan_for_total(ifp)
//    display_percent(ifp)

    return 0;
}
