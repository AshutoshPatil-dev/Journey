#include<stdio.h>
int main(){
      int choice,bal=0, wtd, dep;
     
      while(1){
        printf("\nWelcome to the Bank:\n");
        printf("1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit\n");
        printf("Enter a number corresponding to the option given: ");
        scanf("%d", &choice);
       switch(choice){

        case 1:
         printf("\nEnter the amount you would like to deposit: ");
         scanf("%d", &dep);
         bal = bal + dep;   
         printf("\n%d have been deposited into your account\n", dep);
         break;

        case 2: 
         printf("\nEnter the amount you would like to withdraw: ");
         scanf("%d", &wtd);
         bal = bal - wtd;
         printf("\n%d have been debited from your account\n", wtd);
        break;

        case 3:
         printf("\n%d is the total amount of balance\n", bal);
         break;

        case 4:
         printf("\nYou have been exited from the portal\n");
         return 0;
        
        default:
         printf("\nYou have entered a invalid choice\n");
       }
    }
}