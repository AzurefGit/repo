#include <stdio.h>
#include <stdlib.h>
#include <math.h>
void kw(const int * stala, int * zmienna)
{
    *zmienna = pow(*stala, 2);
}

int main()
{
    const int stala = 5;
    int zmienna = 0;
    kw(&stala, &zmienna);
    printf("%d", zmienna);
    return 0;
}
