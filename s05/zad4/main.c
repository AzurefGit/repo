#include <stdio.h>
#include <stdlib.h>

struct node {
int i;
struct node * next;
};

void pftamid(struct node * list)
{
    if(list==NULL){return;}
    else{
        struct node *wsk = list;
        while(wsk->next!=NULL){
            wsk = wsk->next;
        }
        wsk->next = malloc(sizeof(struct node));
        wsk->next->i = wsk->i;
        wsk->next->next = NULL;
    }
}

int main()
{
    struct node * list = malloc(sizeof(struct node));

    list->i = 3;
    list->next = malloc(sizeof(struct node));
    list->next->i = 4;
    list->next->next = malloc(sizeof(struct node));
    list->next->next->i = 5;
    list->next->next->next = NULL;
    pftamid(list);
    struct node* wsk = list;
    while(wsk != NULL){
        printf("%d ", wsk->i);
        wsk = wsk->next;
    }

    return 0;
}

