//kurde nie wiem jak zrobic zeby dla kazdej list dzialalo xD
#include <stdio.h>
#include <stdlib.h>

struct node {
int a;
struct node * next;
};

void fun(struct node * list)
{
    struct node * wsk = list;
    while(wsk->next!=NULL){
        if (wsk->next->a > 0) {
            wsk->next->a = list->next->next->next->next->next->a;
        }
        wsk = wsk->next;
    }
}

void printL(struct node * list)
{
    struct node * wsk = list->next;
    while(wsk!=NULL){
        printf("%d ", wsk->a);
        wsk = wsk->next;
    }
    printf("\n");
}

int main()
{
    struct node * list = malloc(sizeof(struct node));
    list->next = malloc(sizeof(struct node));
    list->next->a = 3;
    list->next->next = malloc(sizeof(struct node));
    list->next->next->a = 4;
    list->next->next->next = malloc(sizeof(struct node));
    list->next->next->next->a = -5;
    list->next->next->next->next = malloc(sizeof(struct node));
    list->next->next->next->next->a = 3;
    list->next->next->next->next->next = malloc(sizeof(struct node));
    list->next->next->next->next->next->a = 6;
    list->next->next->next->next->next->next = NULL;

    fun(list);
    printL(list);
    return 0;
}
