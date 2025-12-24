/*8. Write a program to implement basic string operations without using in-built functions:
   a. Find the length of a string.
   b. Reverse a string.
   c. Concatenate two strings.
   d. Compare two strings.
   e. Palindrome check.
   f. Count number of words and vowels.
   g. Find and replace a word in a sentence.*/

#include <stdio.h>
int main(){
    char a[200], b[200], temp[200], old[50], neww[50], replace_out[300];
    int i, j, k, len=0, flag=1, words=1, vowels=0;

    printf("Enter first string: ");
    fgets(a, sizeof(a), stdin);

    printf("Enter second string: ");
    fgets(b, sizeof(b), stdin);

    // remove newline from a
    for(i=0; a[i]!='\0'; i++)
        if(a[i]=='\n') a[i]='\0';

    // remove newline from b
    for(i=0; b[i]!='\0'; i++)
        if(b[i]=='\n') b[i]='\0';

    // (a) LENGTH
    for(i=0; a[i]!='\0'; i++)
        len++;
    printf("\nLength = %d\n", len);

    // (b) REVERSE
    for(i=0; i<len; i++)
        temp[i] = a[len-i-1];
    temp[len]='\0';
    printf("Reverse = %s\n", temp);

    // (c) CONCAT
    for(i=0; a[i]!='\0'; i++); // end of a
    for(j=0; b[j]!='\0'; j++)
        a[i+j] = b[j];
    a[i+j]='\0';
    printf("Concatenation = %s\n", a);

    // (d) COMPARE a and b (after concat, b still original)
    flag = 1;
    for(i=0; a[i]!='\0' || b[i]!='\0'; i++)
        if(a[i]!=b[i]) flag = 0;

    if(flag) printf("Equal\n");
    else printf("Not Equal\n");

    // (e) PALINDROME using reverse (temp)
    flag = 1;
    for(i=0; a[i]!='\0' && temp[i]!='\0'; i++)
        if(a[i]!=temp[i]) flag = 0;

    if(flag) printf("Palindrome\n");
    else printf("Not Palindrome\n");

    // (f) WORDS + VOWELS
    words = 1; vowels = 0;
    for(i=0; a[i]!='\0'; i++){
        if(a[i]==' ') words++;

        if(a[i]=='a'||a[i]=='e'||a[i]=='i'||a[i]=='o'||a[i]=='u' ||
           a[i]=='A'||a[i]=='E'||a[i]=='I'||a[i]=='O'||a[i]=='U')
            vowels++;
    }
    printf("Words = %d  Vowels = %d\n", words, vowels);

    // (g) FIND & REPLACE (simple logic)
    printf("\nEnter word to find: ");
    fgets(old, sizeof(old), stdin);
    printf("Enter replacement word: ");
    fgets(neww, sizeof(neww), stdin);

    // remove newlines
    for(i=0; old[i]!='\0'; i++)
        if(old[i]=='\n') old[i]='\0';

    for(i=0; neww[i]!='\0'; i++)
        if(neww[i]=='\n') neww[i]='\0';

    // build replace_out manually
    k = 0;
    for(i=0; a[i]!='\0'; i++){
        flag = 1;
        for(j=0; old[j]!='\0'; j++){
            if(a[i+j] != old[j]){
                flag = 0;
                break;
            }
        }
        
        if(flag){
            for(j=0; neww[j]!='\0'; j++)
                replace_out[k++] = neww[j];
            i = i + j - 1;
        }
        else{
            replace_out[k++] = a[i];
        }
    }
    replace_out[k] = '\0';

    printf("After replace = %s\n", replace_out);

    return 0;
}