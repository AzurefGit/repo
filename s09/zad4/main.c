#include <stdio.h>
#include <stdlib.h>

struct node {
int a;
struct node * next;
};

void printAdr(struct node * list)
{
    struct node * wsk = list;
    int sum = 0;
    int counter = 0;
    while(wsk!=NULL){
        sum += wsk->a;
        counter++;
        wsk = wsk->next;
    }
    double avg=sum/counter;

    wsk = list;
    while(wsk!=NULL){
        if(wsk->a > avg){
        printf("%p ", wsk);
        }
        wsk = wsk->next;
    }

}

int main()
{
    struct node * list = malloc(sizeof(struct node));
    list->a = 1;
    list->next = malloc(sizeof(struct node));
    list->next->a = 2;
    list->next->next = malloc(sizeof(struct node));
    list->next->next->a = 3;
    list->next->next->next = malloc(sizeof(struct node));
    list->next->next->next->a = 4;
    list->next->next->next->next = NULL;

    printAdr(list);
    return 0;
}
