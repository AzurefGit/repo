#include <stdio.h>
#include <stdlib.h>

struct element {
    int a;
    struct element * next;
};

struct element * addFirstTwo(struct element * list1, int a, int b)
{
    struct element * wsk = malloc(sizeof(struct element));
    wsk->a = a;
    wsk->next = malloc(sizeof(struct element));
    wsk->next->a = b;
    wsk->next->next = list1;
    return wsk;
}

void printList(struct element *list) {
    while (list != NULL) {
        printf("%d\n", list->a);
        list = list->next;
    }
    printf("---\n");
}

int main() {
    struct element * list1 = malloc(sizeof(struct element));
    list1->a = 3;
    list1->next = malloc(sizeof(struct element));
    list1->next->a = -4;
    list1->next->next = NULL;
    printList(list1);
    list1 = addFirstTwo(list1, 5, 3);
    printList(list1);
    return 0;
}
