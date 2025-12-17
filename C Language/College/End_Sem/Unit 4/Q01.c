/*Q1. Write a function int add(int a, int b) that returns the sum of two numbers. Show how to declare 
  define, and call it in main().*/

#include<stdio.h>

int add(int, int);

int add(int a, int b){
 return a+b;
}

int main(){
    int a,b;
    printf("Enter a number: ");
    scanf("%d", &a);
    printf("Enter another number: ");
    scanf("%d", &b);
    printf("Sum: %d", add(a,b));

    return 0;
}
