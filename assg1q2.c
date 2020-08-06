/*Program to find the factorial of a number provided by the user. */
#include <stdio.h>
int main() {
    int n, i;
    unsigned long long s=1;
    printf("Enter a positive integer: ");
    scanf("%d", &n);

    if(n<0){
        printf("Error! The number is a negative number.");
    }
    else if (n==0){
        printf("The factorial of 0 is 1");
    }
    else{
        for (i = 1; i <= n; ++i) {
                s=s*i;
            }
        printf("The factorial of %d = %llu" , n , s);
        }
         return 0;
}
