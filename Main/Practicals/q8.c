#include <stdio.h>

int main(){
    char a[200],b[100];
    int i,j;

    gets(a);
    gets(b);

    for(i=0; a[i]!='\0'; i++);
    for(j=0; b[j]!='\0'; j++)
        a[i+j]=b[j];

    a[i+j]='\0';

    printf("Concatenation = %s",a);
}