/*7.Accept two 2D matrices and perform matrix addition, multiplication and transpose.*/

#include <stdio.h> 
int main() { 
int a[10][10], b[10][10], sum[10][10], mul[10][10], t[10][10]; 
int r, c, i, j, k; 
printf("Enter rows and columns: "); 
scanf("%d %d", &r, &c); 

printf("Enter matrix A:\n"); 
for(i=1;i<=r;i++) 
for(j=1;j<=c;j++) 
scanf("%d", &a[i][j]); 

printf("Enter matrix B:\n"); 
for(i=1;i<=r;i++) 
for(j=1;j<=c;j++) 
scanf("%d", &b[i][j]); 

printf("\nMatrix A:\n");
for(i=1; i<=r; i++){
 for(j=1;j<=c;j++){
    printf("%d ", a[i][j]);
 }
 printf("\n");
}

printf("\nMatrix B:\n");
for(i=1; i<=r; i++){
 for(j=1;j<=c;j++){
    printf("%d ", b[i][j]);
 }
 printf("\n");
}

printf("\nMatrix Addition:\n"); 
for(i=1;i<=r;i++){ 
for(j=1;j<=c;j++){ 
sum[i][j] = a[i][j] + b[i][j]; 
printf("%d ", sum[i][j]); 
} 
printf("\n"); 
} 

printf("\nMatrix Multiplication:\n"); 
for(i=1;i<=r;i++){ 
 for(j=1;j<=c;j++){ 
    mul[i][j] = 0; 
 for(k=1;k<c;k++){ 
mul[i][j] += a[i][k] * b[k][j]; 
} 
    printf("%d ", mul[i][j]); 
} 
    printf("\n"); 
} 

printf("\nTranspose of Matrix A:\n"); 

for(i=1;i<=c;i++){ 
 for(j=1;j<=r;j++){ 
  t[i][j] = a[j][i]; 
    printf("%d ", t[i][j]); 
} 
    printf("\n"); 
} 

printf("\nTranspose of Matrix B:\n"); 

for(i=1;i<=c;i++){ 
 for(j=1;j<=r;j++){ 
    t[i][j] = b[j][i]; 
    printf("%d ", t[i][j]); 
} 
    printf("\n"); 
} 
return 0; 
}