#include <stdio.h>
#include <stdlib.h>

struct element {
int i;
struct element * next;
};

int length(struct element *list)
{
    int counter = 0;
    while(list!=NULL){
        counter++;
        list = list->next;
    }
    return counter;
}

int eqLi(struct element * list1, struct element * list2)
{
    if(list1->next ==  NULL || list2->next == NULL){
        return 0;
    }
    if(length(list1) == length(list2)){
        return 1;
    }
    else{
        return 0;
    }

}

int main()
{
    struct element * list1 = malloc(sizeof(struct element));
    struct element * list2 = malloc(sizeof(struct element));

    list1->next = malloc(sizeof(struct element));
    list2->next = malloc(sizeof(struct element));

    list1->next->i = 1;
    list2->next->i = 2;

    list1->next->next = malloc(sizeof(struct element));
    list2->next->next = malloc(sizeof(struct element));

    list1->next->next->i = 4;
    list2->next->next->i = -2;

    list1->next->next->next = NULL;
    list2->next->next->next = NULL;
    printf("%d", eqLi(list1, list2));
    return 0;
}
