/* to find the average distance between points in a straight line containing 6 points */
#include <stdio.h>
#include <stdlib.h>
int main(){
    int n = 6, total = n*n;
    float sum = 0.0; 
    for(int x=0; x<n; x++){
        for(int y = 0; y<n; y++){
            sum = sum+ abs (x-y);
        }
    }
    printf("Average distance between two points = %f", sum/total);
}

/* Output
Average distance between two points = 1.9444448 */
