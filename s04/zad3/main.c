#include <stdio.h>
#include <stdlib.h>

struct Ksiazka{
    char * tytul;
    int isbn;
};

int lowestPages(struct Ksiazka *tab, int n)
{
    int low = tab[0].isbn;
    for(int i=0;i<n;i++){
        if(low>tab[i].isbn){
            low = tab[i].isbn;
        }
    }
    return low;
}

int main()
{
    struct Ksiazka k1 = {"ABC",123};
    struct Ksiazka k2 = {"DEF",456};
    struct Ksiazka k3 = {"GHI",789};

    struct Ksiazka tab[] = {k1,k2,k3};
    printf("%d\n", lowestPages(tab, 3));
    return 0;
}
