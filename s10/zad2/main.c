#include <stdio.h>
#include <stdlib.h>

int floorSqrt(int liczba){
    int i = 1;
    while(i*i<=liczba){
        i++;
    }
    return i-1;
}

int reku(int n)
{
    if(n == 0 || n == 1){
        return 1;
    }
    if(n%2==0){
        return reku(n/2);
    }
    return floorSqrt(n-1);
}

int main()
{
    printf("%d ", reku(10));
    return 0;
}
