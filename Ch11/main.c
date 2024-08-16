/******************************************************************************

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

*******************************************************************************/
#include <stdio.h>

int main()
{
    int action = 0;
    printf("輸入動作:\n");
    printf("1 Play:\n");
    printf("2 Stop:\n");
    printf("3 Exit:\n");
    scanf("%d",&action);
    
    switch(action){
        case 1:
            printf("Play");
        break;
        case 2:
            printf("Stop");
        break;
        case 3:
            printf("Exit");
        break;
        default:
            printf("Error");
        break;
    }
    /*if(action == 1){
        printf("%s","Play");
    }else if(action == 2){
        printf("%s","Stop");
    }else if(action == 3){
        printf("%s","Exit");
    }else{
        printf("%s","Error");
    }*/
    
    
    /*int score = 0;
    printf("輸入分數");
    scanf("%d",&score);
    if (score >= 90){
        printf("%s","得A");
    }else if(score >= 80 && score < 90){
        printf("%s","得B");
    }else if(score >= 70 && score < 80){
        printf("%s","得C");
    }else if (score >= 60 && score < 70){
        printf("%s","得D");
    }else{
        printf("%s","得F");   
    }*/
    
    
   /* int score = 0;
    printf("輸入成績");
    scanf("%d",&score);
    //可補考 不及格 大於等於40 
    printf("是否需要補考%c\n",(score <60 && score >= 40) ? 'Y':'N');*/
    
    /*int score = 0;
    printf("請輸入分數:");
    scanf("%d",&score);
    printf("是否及格?%c\n",score >= 60 ? 'Y':'N');*/
    
    
    /*int number = 0;
    printf("請輸入整數:");
    scanf("%d",&number);
    printf("是否為奇數:?%c",number % 2 == 0? 'N':'Y') ;*/
    
    /*int number = 0;
    printf("請輸入整數:");
    scanf("%d",&number);
    if (number % 2 == 0){
        printf("偶數");
    }else{
        printf("奇數");
    }*/
        
    
    /*int v1 = 1;//true
    int v2 = 0;//false
    printf("%d AND %d = %d\n",v1,v2,v1&&v2);
    printf("%d OR %d = %d\n",v1,v2,v1 || v2);
    printf("!%d = %d",v1,!v1);*/
    
    //printf("c:%d\n",c++);
    //printf("c:%d\n",c);
    
    /*int i = 0;
    i++;
    printf("i=%d\n",i);
    ++i;
    printf("i=%d\n",i);
    i--;
    printf("i=%d\n",i);
    i+=2;
    printf("i=%d\n",i);*/
   /* int input1;
    float input2;
    char input3[10];
    printf("輸入整數");
    scanf("%d",&input1);
    printf("輸入的數字是:%d\n",input1);
    printf("輸入浮點數");
    scanf("%f",&input2);
    printf("輸入的浮點數是:%.2f\n",input2);
    printf("輸入文字:");
    scanf("%10s",&input3);
    printf("輸入的文字是:%s",input3);*/
    
    
    /*
    int a = 3 , b = 55;
    double c1 = 3.4,c2 = 15.678;
    printf("a = %02d b = %8d\n",a,b);
    printf("c1 = %.2f c2 = %8.2f",c1,c2);*/
    
    /*printf("顯示字元:%c\n",'A');
    printf("顯縣市字元編碼:%d\n",'A');
    printf("顯示字元:%c\n",65);
    printf("顯示十進位:%d\n",15);
    printf("顯示八進位:%o\n",15);
    printf("顯示十六進位:%x\n",15);
    printf("顯示科學記號:%e\n",0.001234);*/
    
    //printf("Hello World");
    
    return 0;
}
