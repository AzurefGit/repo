#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int lenPP(char * napis)
{
    int counter = 0;
    for(int i = 0;napis[i]!=0;i++){
        if(napis[i]%2==0){
            counter++;
        }
    }
    return strlen(napis)+counter;
}

int main()
{
    printf("%d\n", lenPP("od2468"));
    printf("%d\n", lenPP("bc13"));
    printf("%d\n", lenPP("2468"));
    printf("%d\n", lenPP("wmii"));
    return 0;
}
