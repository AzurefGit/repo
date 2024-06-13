#include <stdio.h>
#include <stdlib.h>

struct Node {
int x;
struct Node * next;
};

int * nowaTab(struct Node * list)
{
    if(list == NULL){
        return NULL;
    }
    else{
        int i = 0;
        int * tab = malloc(4*sizeof(int));
        struct Node * wsk = list;
        while(wsk!=NULL){
            tab[i++] = wsk->x;
            wsk = wsk->next;
        }
        tab[i] = 0;
        return tab;
    }
}

int main()
{
    struct Node * list = malloc(sizeof(struct Node));
    list->x = 1;
    list->next = malloc(sizeof(struct Node));
    list->next->x = 2;
    list->next->next = malloc(sizeof(struct Node));
    list->next->next->x = -3;
    list->next->next->next = NULL;

    for(int i = 0;nowaTab(list)[i]!=0;i++){
        printf("%d\n",nowaTab(list)[i]);
    }
    return 0;
}
