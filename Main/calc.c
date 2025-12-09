//G).C).B)Write a program to implement basic string operations without using in-built functions:
#include <stdio.h>
int my_strlen(char str[]) {
    int i = 0;
    while (str[i] != '\0')
        i++;
    return i;
}

void my_strcpy(char dest[], char src[]) {
    int i = 0;
    while (src[i] != '\0') {
        dest[i] = src[i];
        i++;
    }
    dest[i] = '\0';
}

int my_strcmp(char s1[], char s2[]) {
    int i = 0;
    while (s1[i] != '\0' && s2[i] != '\0') {
        if (s1[i] != s2[i])
            return s1[i] - s2[i];
        i++;
    }
    return s1[i] - s2[i];
}

void countFrequency(char str[]) {
    int freq[256] = {0};
    int i;

    for (i = 0; str[i] != '\0'; i++) {
        freq[(unsigned char)str[i]]++;
    }

    printf("\nCharacter Frequency:\n");
    for (i = 0; i < 256; i++) {
        if (freq[i] > 0)
            printf("'%c' = %d\n", i, freq[i]);
    }
}

void replaceSubstring(char str[], char old[], char new[]) {
    char result[500];
    int i = 0, j = 0, k, flag;

    while (str[i] != '\0') {
        flag = 1;
        for (k = 0; old[k] != '\0'; k++) {
            if (str[i + k] != old[k]) {
                flag = 0;
                break;
            }
        }

        if (flag == 1) {  
            for (k = 0; new[k] != '\0'; k++)
                result[j++] = new[k];
            i += my_strlen(old);
        } else {
            result[j++] = str[i++];
        }
    }
    result[j] = '\0';

    my_strcpy(str, result);
}


void findReplaceWord(char str[], char old[], char new[]) {
    replaceSubstring(str, old, new);  // uses same logic
}


int main() {
    char str[500], old[100], new[100], copy[500];
    int choice;

    printf("Enter a string: ");
    gets(str);

    while (1) {
        printf("\n------ MENU ------\n");
        printf("1. Count frequency of characters\n");
        printf("2. Replace substring\n");
        printf("3. Find & replace word\n");
        printf("4. Demonstrate strlen, strcpy, strcmp\n");
        printf("5. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        getchar(); 

        switch (choice) {
            case 1:
                countFrequency(str);
                break;

            case 2:
                printf("Enter substring to replace: ");
                gets(old);
                printf("Enter new substring: ");
                gets(new);
                replaceSubstring(str, old, new);
                printf("Updated String: %s\n", str);
                break;

            case 3:
                printf("Enter word to find: ");
                gets(old);
                printf("Enter replacement word: ");
                gets(new);
                findReplaceWord(str, old, new);
                printf("Updated String: %s\n", str);
                break;

            case 4:
                printf("\nLength = %d\n", my_strlen(str));

                my_strcpy(copy, str);
                printf("Copy = %s\n", copy);

                printf("Compare original & copy = %d\n",
                        my_strcmp(str, copy));
                break;

            case 5:
                return 0;

            default:
                printf("Invalid choice!\n");
        }
    }

    return 0;
}

Output:
Enter a string: Hello 

------ MENU ------
1. Count frequency of characters
2. Replace substring
3. Find & replace word
4. Demonstrate strlen, strcpy, strcmp
5. Exit
Enter your choice: 1

Character Frequency:
' ' = 1
'H' = 1
'e' = 1
'l' = 2
'o' = 1

------ MENU ------
1. Count frequency of characters
2. Replace substring
3. Find & replace word
4. Demonstrate strlen, strcpy, strcmp
5. Exit
Enter your choice: 2
Enter substring to replace: llo
Enter new substring: ll
Updated String: Hell 

------ MENU ------
1. Count frequency of characters
2. Replace substring
3. Find & replace word
4. Demonstrate strlen, strcpy, strcmp
5. Exit
Enter your choice: 3
Enter word to find: l
Enter replacement word: lo
Updated String: Helolo 

------ MENU ------
1. Count frequency of characters
2. Replace substring
3. Find & replace word
4. Demonstrate strlen, strcpy, strcmp
5. Exit
Enter your choice: 4

Length = 7
Copy = Helolo
Compare original & copy = 0

------ MENU ------
1. Count frequency of characters
2. Replace substring
3. Find & replace word
4. Demonstrate strlen, strcpy, strcmp
5. Exit
Enter your choice: 5