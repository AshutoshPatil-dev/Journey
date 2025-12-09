#include <stdio.h>
int main() {
    int a,b,c;
    printf("Enter integer no. 1: ");
    scanf("%d", &a);
    printf("Enter integer no. 2: ");
    scanf("%d", &b);
    printf("Enter integer no. 3: ");
    scanf("%d", &c);
    
    if(a>b && a>c){
        printf("%d is the largest", a);}
    if(b>a && b>c){
        printf("%d is the largest", b);}
    if(c>a && c>b){
        printf("%d is the largest", c);}
    }