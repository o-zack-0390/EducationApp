#include <stdio.h>

int fn_roop(int a,int b,int c,int n);
int fn_recursion(int a,int b,int c,int n);


int main(void)
{
    int a,b,c,n;
    
    printf("Input a: ");
    scanf("%d",&a);
    printf("Input b: ");
    scanf("%d",&b);
    printf("Input c: ");
    scanf("%d",&c);
    printf("Input n: ");
    scanf("%d",&n);
    
    printf("Loop:\n");
    int i;
    
    for(i=1;i<=n;i++)
        printf("f(%d)=%d\n",i,fn_roop(a,b,c,i));
    
    printf("Recursion:\n");
    
    for(i=1;i<=n;i++)
        printf("f(%d)=%d\n",i,fn_recursion(a,b,c,i));
    
    return 0;
}


int fn_roop(int a,int b,int c,int n)
{
    int f=c;
        
    if(n==1)
        return c;

    else
    {
        for(int i=2;i<=n;i++)
            f=a+(b*f);
        return f;
    }
}


int fn_recursion(int a,int b,int c,int n)
{
    int f2=c;
        
    if(n==1)
        return c;

    else
    {
        f2=a+(b*f2);
        fn_recursion(a,b,f2,n-1);
    }
}