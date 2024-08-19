/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>
#include <math.h>
#include <stdlib.h>
#include <time.h>
#define ROWS 2
#define LEN 3

int add(int a,int b){
    
    int ans = a + b;
    
    return ans;
}

int main()
{   
    printf("ans:%d \n",add(2,3));
    
    int ans,gus;
    srand(time(0));
    //printf("%d",(rand() % 5) + 1);
    
    ans = (rand() % 5) + 1;
    printf("ans:%d",ans);
    printf("請輸入1-5數字:");
    scanf("%d",&gus);
    if (gus == ans){
        printf("正確");
    }else{
        printf("錯誤");
    }
    
    
    /*float x,y,z;
    printf("輸入底邊長");
    scanf("%f",&x);
    printf("輸入高邊長");
    scanf("%f",&y);
    z = sqrt(pow(x,2) +pow(y,2));
    printf("斜邊長:%.2f",z);*/
    
    /*int myArray[ROWS][LEN] = {
        {1,2,3},
        {4,5,6}
    };
    int i,j;
    
    for (i = 0;i < ROWS; i++){
        for ( j = 0; j < LEN;j++){
            printf("%d\t",myArray[i][j]);
        }
        printf("\n");
    }*/
    /*
    int myArray[6] = {8,9,11,7,6,18};
    int size = sizeof(int);
    int arraySize = sizeof(myArray);
    printf("size:%d\n",size);
    printf("myArray Size:%d\n",arraySize);
    int len= arraySize / size;
    

    int i;
    for(i = 0; i < len;i++){
        printf("%d ",myArray[i]);
    }*/
    
    
    /*int score[10] = {0};
    double weight[10] = {0.0};
    
    int score2[5] = {70,80,90,65,100};
    char values[5] = {'A','B','C','D','E'};
    printf("%d\n",score[0]);
    printf("%d\n",score2[1]);
    printf("%c\n",values[2]);*/
    
    
    /*int input = 0;
    
    do{
        
        printf("輸入 奇數:");
        scanf("%d",&input);
        
        if (input % 2 != 0){
            printf("%d是奇數",input);
            break;
        }
        printf("是偶數:在試一次!\n");
        
    }while(1);*/
    
    
    /*int score = 0;
    int sum = 0;
    int count = 0;
    int i;
    for (i = 0; i < 5; i++){
        printf("輸入分數:");
        scanf("%d",&score);
        if(score < 0 || score > 100){
            printf("錯誤的分數%d\n",score);
            continue;
        } 
        count++;
        sum += score;
    }
    
    printf("總分:%d",sum);*/
    
    
    /*int input = 0;
    int replay = 0;
    do{
        printf("請輸入整數值:");
        scanf("%d",&input);
        printf("輸入是否為奇數:%c\n",(input % 2)?'Y':'N');
        printf("1 繼續 0 結束?");
        scanf("%d",&replay);
                
    }while(replay);*/
    
    
    /*int x = 1;
    do{
        printf("%d ",x);
        x++;
    }while(x <= 10);*/
    
    //使用while 完成9x9
    
    /*int i=2,k=1;
    
    while(i <= 9){
        k = 1;
        while ( k <= 9){
            printf("%d*%d=%2d ",i,k,i*k);
            k++;
        }
        printf("\n");
        i++;
    }*/
    
    /*int score = 0;
    int sum = 0;
    int count = 0;
    while(score != -1){
        printf("輸入分數(-1結束)");
        scanf("%d",&score);
        if(score == -1){
           break;
        } 
        sum += score;
        count++;
    } 
    
    printf("sum:%d\n",sum);
    printf("avg:%.2f\n",(double)sum/count);*/
    
    
    /*int i = 1;
    while(i <= 10){
        printf("%d ",i);
        i++;
    }*/
    
    /*
    int i,k;
    
    for (i=1;i<=5;i++){
        
        for (k = 1; k <= i; k++){
            printf("*");
        }
        printf("\n");
        
    }*/
    /*int i,j;
    for ( i = 2; i < 10;i++){
        for ( j = 1; j < 10; j++){
            printf("%d*%d=%2d ",i,j,i*j);
        }
        printf("\n");
    }*/
    
   /* int i;
    for( i = 0; i < 10 ; i++){
        
        printf("%d ",i);
    }*/
     
    /*int score = 0;
    int level = 0;
    printf("輸入分數:");
    scanf("%d",&score);
    level = score / 10;
    switch(level){
        case 10:
        case 9:
            printf("A\n");
        break;
        case 8:
            printf("B\n");
        break;
        case 7:
            printf("C\n");
        break;
        case 6:
            printf("D\n");
        break;
        default:
            printf("F\n");
        break;
    }*/
    
    return 0;

   
}
