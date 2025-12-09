/*10. Write programs to calculate the factorial of a number entered by the user, 
using both an iterative function and a recursive function*/
#include<stdio.h>
long long iter_func(long long a){
  long long fact = 1;
  for(long long i = 1; i<=a; i++){
    fact = fact * i;
  }
  return fact;
}

long long rec_func(long long a){
 if(a == 1 || a == 0)
  return 1;
 return a * rec_func(a-1);
}

int main(){
long long a;
printf("Enter a number: ");
scanf("%lld", &a);

printf("%lld\n", iter_func(a));

printf("%lld\n", rec_func(a));
}
