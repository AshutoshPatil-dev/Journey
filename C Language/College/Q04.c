// Write a program to determine whether a number is even or odd.

#include<stdio.h>
int main(){
int a;
printf("Enter a number: ");
scanf("%d", &a);

if(a % 2 == 0 && a != 0)
    printf("Even");
else if(a == 0)
   printf("Zero");
else
   printf("Odd");
}
