#include <stdio.h>
#include <stdlib.h>

void revSndEnd(int n, int m, int tab[n][m])
{
    if(n<4){
        return;
    }
    else{
        for(int j = 0;j<m;j++) {
            int temp = tab[1][j];
            tab[1][j] = tab[n-2][j];
            tab[n-2][j] = temp;
    }
}
}
int main()
{
    int tab[4][3] = {{2,3,-3},
                     {1,4,7},
                    {-3,-6,11},
                    {-2,8,23}};

    revSndEnd(4,3,tab);
    for(int i = 0;i<4;i++){
        for(int j = 0;j<3;j++){
            printf("%d ",tab[i][j]);

        }
        printf("\n");
    }
    return 0;
}
