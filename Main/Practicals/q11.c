/* 11. Write a program to:  
    a. Declare and initialize a pointer to an integer variable.
    b. Demonstrate pointer arithmetic (increment, decrement, addition, and subtraction).
    c. Print the memory addresses of an array's elements using pointers. */

#include<stdio.h>
int main(){
int x, *p;

x = 10;

// Adding Adress of x to p
p = &x;

// Printing value of x
printf("\nValue of x: %d\n\n", x);

// Printing adress of x
printf("Adress of x: %p\n", p);


// Arithmetic

printf("Increment: %p\n", ++p);
printf("Decrement: %p\n", --p);
printf("Addition: %p\n", p + 1);
printf("Substraction: %p\n\n",  p - 1);

int arr[5] = {1,2,3,4,5,6};
int *m = arr;
for(int i = 0; i<6; i++){
    printf("Memory address of arr[%d] is: %p\n", i, (m+i));
}
}