/* to find the average distance between points in 2-d grid containing 36 points */
#include <stdio.h>
#include <stdlib.h>
int main(){
    int n=36, total = n*n;
    float sum = 0.0;
    for(int xi = 0; xi<6; xi++){
        for(int yi = 0; yi<6; yi++){
            for(int xf = 0; xf<6; xf++){
                for(int yf = 0; yf<6; yf++){
                    sum = sum + abs(xi-xf) + abs(yi-yf);
                }
            }
        }
    }
    printf("Average distance between two points = %f", sum/total);
}

/* Output
Average distance between two points = 3.888889  */
