/*1. Write a program to take two numbers as input and perform basic arithmetic operations such as addition, 
subtraction, multiplication, and division.*/

#include<stdio.h>
int main(){
int a,b;

printf("Enter two numbers: ");
scanf("%d %d", &a, &b);
printf("\nAddition: %d\n", a+b);
printf("Substraction: %d\n", a-b);
printf("Multiplication: %d\n", a*b);
if(b != 0)
 printf("Division: %.2f \n", (float)a/b);
else
 printf("Can't divide by 0");
 
 return 0;
}