#include <stdio.h>
#define MAX 100

int main(void)
{
    int stack[MAX], stackPtr=0;
    int num,data;

    while(1)
    {
        printf("input number 0:quit 1:push 2:pop 3:print\n");
        scanf ("%d",&num);
            
        if(num==0)
            return 0;
               
        else if(num==1)
        {
            printf("input data");
            scanf("%d",&stack[stackPtr]);
            stackPtr++;
        }
                
        else if(num==2)
        {
            if(stackPtr<=0)
                printf("no number\n");
                        
            else
            {
                printf("out data : %d\n",stack[stackPtr-1]);
                stackPtr--;
            }
        }
                
        else if(num==3)
        {
            if(stackPtr==0)
                printf("stack is empty\n");
                
            for(int i=stackPtr-1;i>=0;i--)
                printf("%d\n",stack[i]);
        }
    }
}