#include <stdio.h>
int main(void)
{
    int i,j,tmp;
    int data[12];
    int total;
    
    printf("入力する数値の総数 = ");
    scanf("%d",&total);
    
    if(12<total)
    {
        printf("総数を12個に変換\n");
        total=12;
    }

    printf("%d個の数値を入力\n",total);
    for(i=0;i<total;++i)
        scanf("%d",&data[i]);

    for(i=0;i<total;++i)
    {
        for(j=i+1;j<total;++j)
        {
            if(data[j]<data[i])
            {
                tmp=data[i];
                data[i]=data[j];
                data[j]=tmp;
           }
        }
    }

    printf("昇順ソートした数値\n");
    for(i=0;i<total;++i)
        printf("%d ",data[i]);
    printf("\n");
    
    return 0;
}