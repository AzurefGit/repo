#include <stdio.h>
#include <stdlib.h>

struct elem {
    int t;
    struct elem * next;
};

int por(struct elem * l1, struct elem * l2)
{
    int counter = 0;
    while (l1->next != NULL && l2->next != NULL) {
        if (l1->t == l2->t) {
            counter++;
        }
        l1 = l1->next;
        l2 = l2->next;
    }
    return counter;
}

int main()
{
    struct elem * list1 = malloc(sizeof(struct elem));
    struct elem * list2 = malloc(sizeof(struct elem));

    list1->next = malloc(sizeof(struct elem));
    list1->next->t = 3;
    list1->next->next = malloc(sizeof(struct elem));
    list1->next->next->t = 4;
    list1->next->next->next = malloc(sizeof(struct elem));
    list1->next->next->next->t = 5;
    list1->next->next->next->next = NULL;

    list2->next = malloc(sizeof(struct elem));
    list2->next->t = 3;
    list2->next->next = malloc(sizeof(struct elem));
    list2->next->next->t = 2;
    list2->next->next->next = malloc(sizeof(struct elem));
    list2->next->next->next->t = 5;
    list2->next->next->next->next = NULL;

    printf("%d\n", por(list1, list2));
    return 0;
}
