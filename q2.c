#include <stdio.h>
int main() {
    int n, i, s=1;
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
        printf("The factorial of %d = %d" , n , s);
        }
         return 0;
}
