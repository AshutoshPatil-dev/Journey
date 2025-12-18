#include<stdio.h>


void callbyvalue(int a,int b){
    int temp;
    temp = a;
    a = b;
    b = temp;
}

void callbyref(int *a, int *b){
    int temp;
    temp = *a;
    *a = *b;
    *b = temp;
}

int main(){
 int a = 1, b = 2;
 callbyvalue(a, b);
 printf("%d %d\n", a, b);

 callbyref(&a, &b);
 printf("%d %d", a, b);
}


