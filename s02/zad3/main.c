#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct Telefon{
    char marka[15];
    int liczbaPolaczen;
};

struct Telefon * initTelefon(char marka2[15], int liczbaPolaczen2)
{
    if(strlen(marka2) <3 || liczbaPolaczen2<=50){
        return NULL;
    }
    struct Telefon * wsk = malloc(sizeof(struct Telefon));
    strcpy(wsk->marka, marka2);
    wsk->liczbaPolaczen = liczbaPolaczen2;
    return wsk;
}

void zwiekszLiczbePolaczen(struct Telefon * wsk)
{
    wsk->liczbaPolaczen+=10;
}

int main()
{
    struct Telefon *t1 = initTelefon("Auuduuu", 51);
    printf("%d\n", t1->liczbaPolaczen);
    zwiekszLiczbePolaczen(t1);
    printf("%d\n", t1->liczbaPolaczen);
    return 0;
}
