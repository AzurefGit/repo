#include <stdio.h>
#include <stdlib.h>

enum Day{Poniedzialek, Wtorek, Sroda, Czwartek, Piatek};

void print_days(enum Day day, int n)
{
    const char* day_names[] = {
        "Poniedzialek",
        "Wtorek",
        "Sroda",
        "Czwartek",
        "Piatek",
        "Sobota",
        "Niedziela"
    };
    printf("Dzien %d: %s\n", n, day_names[day]);

    if(n>1){
        enum Day next_day = (day + 1)%7;
        print_days(next_day, n - 1);
    }
}


int main()
{
    print_days(Poniedzialek, 5);
    return 0;
}
