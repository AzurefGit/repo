#include <stdio.h>
#include <stdlib.h>

void revOdd(int n, int m, int tab[n][m])
{
    int temp = tab[4][2];
    for(int j = 0;j<m;j++){
        if(j%2==1){
            for(int i = 0;i<n/2;i++){
                temp = tab[i][j];
                tab[i][j] = tab[n-i-1][j];
                tab[n-i-1][j] = temp;
            }
        }
    }
}

int main()
{
    int tab[4][3] = {{2,3,-3},
                     {1,4,7},
                    {-3,-6,11},
                    {-2,8,23}};
    revOdd(4,3,tab);
    for(int i = 0;i<4;i++){
        for(int j = 0;j<3;j++){
            printf("%d ",tab[i][j]);

        }
        printf("\n");
    }
    return 0;
}
