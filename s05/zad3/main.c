#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Telefon{
    char marka[30];
    int iloscPolaczen;
};

struct Telefon initTelefon(char marka2[30], int iloscPolaczen2)
{
    struct Telefon temp;
    if(strlen(marka2) <3 || iloscPolaczen2 < 50){
        strcpy(temp.marka, "NIEZNANY");
        temp.iloscPolaczen = 100;
    }
    else{
        strcpy(temp.marka, marka2);
        temp.iloscPolaczen = iloscPolaczen2;
    }
    return temp;
}

int main()
{
    struct Telefon t1 = initTelefon("As", 34);
    struct Telefon t2 = initTelefon("OOOOOO", 343);

    printf("%s %d\n", t1.marka, t1.iloscPolaczen);
    printf("%s %d", t2.marka, t2.iloscPolaczen);
    return 0;
}
