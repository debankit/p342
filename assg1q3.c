/* Sum over 1+ 1/2 + 1/3 + ..... till 1/1000 */
#include <stdio.h>
int main() {
    double s=0.0;
    for(int i =1; i<1000; ++i){
        s= s+ (1.0/i);
    }
    printf("Sum = %lf", s);
    return 0;
}
