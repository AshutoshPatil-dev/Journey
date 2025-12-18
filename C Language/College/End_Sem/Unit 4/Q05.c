#include <stdio.h> 
 
void counter_function() { 
    static int count = 0; // Ini alized once, retains value [cite: 703] 
    int autoVar = 0;      // Re-ini alized every call 
 
    count++; 
    autoVar++; 
    printf("Sta c count: %d, Auto var: %d\n", count, autoVar); 
} 
 
int main() { 
    counter_function(); // Output: Sta c count: 1, Auto var: 1 
    counter_function(); // Output: Sta c count: 2, Auto var: 1 
    counter_function(); // Output: Sta c count: 3, Auto var: 1 [cite: 709] 
    return 0; 
} 