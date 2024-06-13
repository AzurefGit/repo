#include <stdio.h>
#include <stdlib.h>

int foo(wchar_t * napis)
{
    int li = 0;
    for(int i = 0;napis[i]!=0;i++){
        if(napis[i]>=L'0' && napis[i]<=L'9'){
            li = li * 10 +(napis[i] - L'0');
        }
        else{
            return 0;
        }
    }
    return li;
}

int main()
{
    wchar_t *napis = L"546";
    printf("%d\n", foo(napis));
    return 0;
}
