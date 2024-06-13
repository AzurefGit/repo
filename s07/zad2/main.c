#include <stdio.h>
#include <stdlib.h>

int retNum(char * napis)
{
    int counter = 0;
    for(int i = 0;napis[i]!=0;i++){
        if((napis[i]>='A' && napis[i]<='F') || (napis[i]>='0' && napis[i]<='9')){
            counter++;
        }
    }
    return counter;
}

int main()
{
    printf("%d", retNum("123ghj0fghFAB"));
    return 0;
}
