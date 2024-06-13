#include <stdio.h>
#include <stdlib.h>

int iSum(int n, int tab[n][n])
{
    int min_el = tab[0][0];
    int suma = 0;
    for(int i = 0;i<n;i++){
        for(int j = 0;j<n;j++){
            if(min_el>=tab[i][j]){
                min_el = tab[i][j];
                suma += (i+1)+(j+1);
            }
        }
    }
    return suma;

}

int main()
{
    int tab[3][3] = {{1,2,3},
                     {4,5,6},
                     {7,1,9}};
    printf("%d", iSum(3, tab));
    return 0;
}
