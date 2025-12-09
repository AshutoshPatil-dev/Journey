/* 11.	Define a structure Student with the members roll_no, name, gender, and marks. Write a program to perform the following operations for n students:
a.	Input and display student details.
b.	Sort and display the students' data in descending order based on their percentage.
c.	Search for a student's details using their roll number. */

#include <stdio.h>
#include <string.h>

struct Student {
    int roll_no;
    char name[50];
    char gender;
    float marks;   // percentage
};

int main() {
    struct Student s[100];
    int n, i, j, searchRoll, found = 0;

    printf("Enter number of students: ");
    scanf("%d", &n);

    // ---- Input student details ----
    for(i = 0; i < n; i++) {
        printf("\nEnter details of student %d\n", i + 1);

        printf("Roll No: ");
        scanf("%d", &s[i].roll_no);

        printf("Name: ");
        scanf("%s", s[i].name);

        printf("Gender (M/F): ");
        scanf(" %c", &s[i].gender);

        printf("Marks (Percentage): ");
        scanf("%f", &s[i].marks);
    }

    // ---- Display student details ----
    printf("\n--- Student Details ---\n");
    for(i = 0; i < n; i++) {
        printf("%d\t%s\t%c\t%.2f\n",
               s[i].roll_no, s[i].name, s[i].gender, s[i].marks);
    }

    // ---- Sorting in descending order of marks ----
    for(i = 0; i < n - 1; i++) {
        for(j = i + 1; j < n; j++) {
            if(s[i].marks < s[j].marks) {
                struct Student temp = s[i];
                s[i] = s[j];
                s[j] = temp;
            }
        }
    }

    // ---- Display after sorting ----
    printf("\n--- Students Sorted by Percentage (Descending) ---\n");
    for(i = 0; i < n; i++) {
        printf("%d\t%s\t%c\t%.2f\n",
               s[i].roll_no, s[i].name, s[i].gender, s[i].marks);
    
        }
    // ---- Search by roll number ----
    printf("\nEnter roll number to search: ");
    scanf("%d", &searchRoll);

    found = 0;
    for(i = 0; i < n; i++) {
        if(s[i].roll_no == searchRoll) {
            found = 1;
            printf("\n--- Student Found ---\n");
            printf("Roll No: %d\nName: %s\nGender: %c\nMarks: %.2f\n",
                   s[i].roll_no, s[i].name, s[i].gender, s[i].marks);
            break;
        }
    }

    if(!found)
        printf("\nStudent with Roll No %d not found.\n", searchRoll);

    return 0;
}
