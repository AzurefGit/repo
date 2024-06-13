#include <stdio.h>
#include <stdlib.h>
#include <math.h>

struct node{
int i;
struct node * next;
};

void power(struct node * list)
{
    if(list == NULL){
        printf("Empty list");
    }
    else{
        struct node * wsk = list;
        while(wsk!=NULL){
            int sqrt_i = (int)sqrt(wsk->i);
            if(sqrt_i * sqrt_i == wsk->i){
                printf("%d\n", wsk->i);
            }
            wsk = wsk->next;
        }
    }
}

int main()
{
    struct node * list = malloc(sizeof(struct node));
    list->i = 4;
    list->next = malloc(sizeof(struct node));
    list->next->i = 5;
    list->next->next = malloc(sizeof(struct node));
    list->next->next->i = 6;
    list->next->next->next = malloc(sizeof(struct node));
    list->next->next->next->i = -34;
    list->next->next->next->next = malloc(sizeof(struct node));
    list->next->next->next->next->i = 0;
    list->next->next->next->next->next = malloc(sizeof(struct node));
    list->next->next->next->next->next->i = 25;
    list->next->next->next->next->next->next = malloc(sizeof(struct node));
    list->next->next->next->next->next->next->i = 11;
    list->next->next->next->next->next->next->next = NULL;

    power(list);
    return 0;
}
