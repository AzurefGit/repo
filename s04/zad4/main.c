#include <stdio.h>
#include <stdlib.h>

struct node {
float value;
struct node * next;
};

float biggestNum(struct node * list)
{
    if(list->next==NULL){
        return 0;
    }
    else{
        struct node * wsk = list->next;
        int lowest = wsk->value;
        while(wsk!=NULL){
            if(lowest<wsk->value){
                lowest = wsk->value;
            }
            wsk = wsk->next;
        }
        return lowest;
    }
}

int main()
{
    struct node * list = malloc(sizeof(struct node));

    list->next = malloc(sizeof(struct node));
    list->next->value = 1;
    list->next->next = malloc(sizeof(struct node));
    list->next->next->value = -11;
    list->next->next->next = malloc(sizeof(struct node));
    list->next->next->next->value = 100;
    list->next->next->next->next = malloc(sizeof(struct node));
    list->next->next->next->next->value = 12;
    list->next->next->next->next->next = NULL;

    printf("%f", biggestNum(list));
    return 0;
}
