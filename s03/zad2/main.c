#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int wieloWar(int n, int tab[n], int x)
{
    int suma = 0;
    for(int i = 0;i<n;i++){
        suma+=tab[i]*pow(x, i);
    }
    return suma;
}

int main()
{
    int tab[4] = {1,3,-4,5};
    printf("%d\n", wieloWar(4, tab, 2));
    return 0;
}
