#include <stdio.h>
#define MAX 15

int bin_coef(int n, int p)
{
    if(p>n)
        return 0;
        
    else if(n==1)
        return 1;
        
    else if(p==0)
        return bin_coef(n-1,p);
        
    else
        return bin_coef(n-1,p)+bin_coef(n-1,p-1);
}


int main(void)
{
    int n,p;
    
    for(n=1; n<=MAX; n++)
    {
        for(p=0;p<=n;p++)
            printf("%-5d",bin_coef(n,p));
        printf("\n");
    }
    
    return 0;
}