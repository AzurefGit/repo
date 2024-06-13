#include <stdio.h>
#include <stdlib.h>

int is_positive(int li)
{
    if(li>0){
        return 1;
    }
    else{
        return -1;
    }
}

int positive_count(int n, int tab[n], int is_positive())
{
    int counter = 0;
    for(int i = 0;i<n;i++){
        if(is_positive(tab[i])>0){
            counter++;
        }
    }
    return counter;
}

int main()
{
    int tab[5] = {1,2,-3,-4,5};
    printf("%d\n", positive_count(5, tab, *is_positive));
    return 0;
}
