/* Finding sum and dot product of two matrices */
#include <stdio.h>

void main(){
    int a[3] = { 7, 15, 3}, b[3] = {3, 10, 10};
    int sum[3], dot=0;
    for(int i = 0; i<3; i++){
        sum[i] = a[i] + b[i];
        dot = dot + (a[i]*b[i]);
    }
    printf("Sum of the Matrices: \n");
    for(int i = 0; i <3; i++){
        printf("%d\n", sum[i]);
    }
    printf("Dot product of Matrices = %d", dot);
}
