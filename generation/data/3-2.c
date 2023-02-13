#include <stdio.h>
#include <stdlib.h>
int calculate(int query, int data[], int size);

int main(void)
{
    int data[] = {8,98,87,36,35,54,11,33,6,79}
    int size   = 10;
    int query, min;
    
    while(1)
    {
        printf("query = ");
        scanf("%d",&query);
        
        if(query<0)
            break;
        
        min=calculate(query,data,size);
        printf("query=%d,minimum difference=%d\n",query,min);
    }
    
    return 0;
}


int calculate(int query, int data[], int size)
{
    int i, mainasu, minimum;
    minimum = abs(query-data[0]);
    
    for(i=0; i<size; i++)
    {
        mainasu = abs(query-data[i]);
        
        if(mainasu < minimum)
            minimum = mainasu;
    }
    
    return minimum;
}