#include <stdio.h>
#include <stdlib.h>

int productDiagonal(int n, int m, int tab[n][m])
{
    int suma = 1;
    for(int i = 0;i<n;i++){
        for(int j = 0;j<m;j++){
            if(i==j){
            suma*= tab[i][j];
            }
        }
    }
    return suma;
}

int main()
{
    int tab[2][3]={{3,4,-8},
                   {-3,-7,5}};
    printf("%d\n", productDiagonal(2, 3, tab));
    return 0;
}
