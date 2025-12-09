// Write a program to find factorial of a number.
#include<stdio.h>
int main(){
int a, fact = 1, i;
printf("Enter a number: ");
scanf("%d", &a);

for(int i=1; i<=a; i++){
 fact = fact * i;
}
printf("Factorial is: %d", fact);
}