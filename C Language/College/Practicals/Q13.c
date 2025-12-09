#include<stdio.h>
int main(){

FILE *fp;
int ch, chars = 0, tabs = 0, spaces = 0, lines = 0;
fp = fopen("C:\\Users\\ashut\\OneDrive\\Desktop\\hello.txt", "r");
if(fp == NULL){
 printf("The file dosen't exist or the path is wrong.");
 return 1;
}

while((ch = fgetc(fp)) != EOF){
 chars++;
 if(ch == ' ')
  spaces++;
 else if(ch == '\t')
  tabs++;
 else if(ch == '\n')
  lines++;
}
fclose(fp);

printf("Characters: %d\n", chars);
printf("Spaces: %d\n", spaces);
printf("Tabs: %d\n", tabs);
printf("New lines: %d\n", lines);
return 0;
}
