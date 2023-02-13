#include <stdio.h>

int kaijou(int n)
{
    int r;
    printf(" 開始　n=%d\n",n);
    
    if(n==1)
        r=1;
    
    else
    {
        r=n*kaijou(n-1);
    }
        
    printf("終了n=%d,r=%d\n",n,r);
    return r;
}


int main(void)
{
    int x,k;
    printf("nを入力： ");
    scanf("%d",&x);
    k=kaijou(x );
    printf("%d の階乗は%d\n",x,k);
    return 0;
}