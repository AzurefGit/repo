#include <stdio.h>
#include <stdlib.h>

struct node {
int a;
struct node * next;
};

int liLen(struct node * list){
    struct node * wsk = list;
    int counter = 0;
    while(wsk!=NULL){
        counter++;
        wsk = wsk->next;
    }
    return counter;
}

int liEq(struct node * list1, struct node * list2)
{
    if(list1 == NULL || list2 == NULL){
        return 0;
    }
    if(liLen(list1)==liLen(list2)){
        return 1;
    }
    else{
        return 0;
    }
}

int main()
{
    struct node * list1 = malloc(sizeof(struct node));
    struct node * list2 = malloc(sizeof(struct node));

    list1->a = 1;
    list1->next = malloc(sizeof(struct node));
    list1->next->a = 1;
    list1->next->next = malloc(sizeof(struct node));
    list1->next->next->a = 1;
    list1->next->next->next = NULL;

    list2->a = 1;
    list2->next = malloc(sizeof(struct node));
    list2->next->a = 1;
    list2->next->next = malloc(sizeof(struct node));
    list2->next->next->a = 1;
    list2->next->next->next = NULL;

    printf("%d", liEq(list1, list2));
    return 0;
}
