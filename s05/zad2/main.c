#include <stdio.h>
#include <stdlib.h>

int recursiveF(char * napis)
{
    if(*napis == 0){
        return 0;
    }
    else{
        if(*napis >= 'A' && *napis <= 'Z'){
            return 1 + recursiveF(napis+1);
        }
        else{
            return recursiveF(napis+1);
        }
    }
}

int main()
{
    printf("%d", recursiveF("NaPiS"));
    return 0;
}
