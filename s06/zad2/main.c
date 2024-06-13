#include <stdio.h>
#include <stdlib.h>

void oddF(char * napis1, char * napis2)
{
    int j = 0;
    for(int i = 0;napis1[i]!=0;i++){
        if(i%2==0){
            napis2[j++] = napis1[i];
        }
    }
    napis2[j] = 0;

}

int main()
{
    char * napis1 = "abcdef";
    char * napis2;
    oddF(napis1, napis2);
    printf("%s\n", napis2);
    return 0;
}
