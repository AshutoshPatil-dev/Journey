// The distance between two cities (in Km) is input through the keyboard. 
// Write a program to convert and print this distance in meters, feet, inches and centimetres?

#include<stdio.h>
int main(){

float km, m, cm, feet, inch;

printf("Enter the distance in km: ");
scanf("%f", &km);
m = km * 1000;
cm = m * 100;
feet = m * 3.28;
inch = cm / 2.54;

printf("Meter: %.2f\n", m);
printf("Centimeters: %.2f\n", cm);
printf("Feet: %.2f\n", feet);
printf("Inches: %.2f\n", inch);

return 0;
}