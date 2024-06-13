#include <stdio.h>
#include <stdlib.h>

struct Programista{
    char * nazwisko;
    int doswiadczenie;
};

char * mocneNaz(struct Programista * tab, int n)
{
    int moc = tab[0].doswiadczenie;
    char * moc_naz = tab[0].nazwisko;
    for(int i=0;i<n;i++){
        if(moc<tab[i].doswiadczenie){
            moc = tab[i].doswiadczenie;
            moc_naz = tab[i].nazwisko;
        }
    }
    return moc_naz;
}

int main()
{
    struct Programista p1 = {"Ololo", 2};
    struct Programista p2 = {"Ali", 5};
    struct Programista p3 = {"Kqo", 1};

    struct Programista tab[] = {p1,p2,p3};
    printf("%s", mocneNaz(tab,3));
    return 0;
}
