// Write a program to check if a given number is positive, negative, or zero.
#include<stdio.h>
int main(){

int a;
printf("Enter a number: ");
scanf("%d", &a);

if(a>0)
 printf("Postive");
else if(a<0)
 printf("Negative");
else
 printf("Zero");
}