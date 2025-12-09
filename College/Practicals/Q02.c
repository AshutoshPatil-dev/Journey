/*2.Write a program to convert Fahrenheit temperature to Celsius. Get the value of 
Fahrenheit temperature from the user?*/

#include<stdio.h>
int main(){
float cel, fer;

printf("Enter value in fareheit: ");
scanf("%f", &fer);

cel = (fer - 32) * 5/9;

printf("Celcius: %.2f", cel);
}