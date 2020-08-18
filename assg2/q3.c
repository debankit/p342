/* To read two matrices from text file and find the products. */
#include <stdio.h>
#include <stdlib.h>
int main()
{
    int matA[3] = {1,2,3};
    int i = 0;
    printf("Matrix A is: \n");
    for(i = 0; i<3; i++){
        printf("%d \n", matA[i]);
    }
    
    int matM[3][3] = {{0,0,0},{0,0,0},{0,0,0}};
    int matN[3][3] = {{0,0,0},{0,0,0},{0,0,0}};
    int matC[3][3] = {{0,0,0},{0,0,0},{0,0,0}};
    int matD[3] = {0,0,0};
    
    FILE *openM;
    
    openM = fopen("m.txt", "r+");
    for(int i = 0; i<3; i++){
        for(int j = 0; j<3; j++){
            fscanf(openM, "%d", &matM[i][j]  );
            
        }
        
    }
    fclose(openM);
    
    FILE *openN;
    
    openN = fopen("n.txt", "r+");
    for(int i = 0; i<3; i++){
        for(int j = 0; j<3; j++){
            fscanf(openN, "%d", &matN[i][j]  );
            
        }
        
    }
    fclose(openN);
    
    for (int i = 0; i < 3; i++) {
      for (int j = 0; j < 3; j++) {
        for (int k = 0; k < 3; k++) {
            matC[i][j] += matM[i][k]*matN[k][j];
        }
      }
    }
    printf("Matrix MN is: \n");
    for(int i =0; i<3; i++){
        for(int j = 0; j<3; j++){
        printf("%d ", matC[i][j]);
        
        }
    printf("\n");
    }
    
    for(int i = 0; i < 3; i++){
        for(int j =0; j<3; j++){
            matD[i] = matD[i] + matM[i][j]*matA[j];
        }
    }
        
    printf("Matrix MA is: \n");
    for(int i = 0; i<3; i++){
        printf("%d \n", matD[i]);
    }
    
    
    return 0;
}


/*Output
Matrix A is:                                                                                                                            
1                                                                                                                                       
2                                                                                                                                       
3                                                                                                                                       
Matrix MN is:                                                                                                                           
64 338 231                                                                                                                              
88 95 102                                                                                                                               
68 43 45                                                                                                                                
Matrix MA is:                                                                                                                           
50                                                                                                                                      
32                                                                                                                                      
22 
*/
