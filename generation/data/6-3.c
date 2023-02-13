#include <stdio.h>
void minmax(int *data, int size, int *min, int *max);

int main(void)
{
    int data[] = {3,16,1,0,14,2,15,-2,-4,-5};
    int size   = 10;
    int min;
    int max;


    minmax(data,size,&min,&max);
    printf("index of min data: %d\n",min);
    printf("index of max data: %d\n",max);

    return 0;
}


void minmax(int *data, int size, int *min, int *max)
{
    int i;
    int min2;
   
    min2 = data[0];
    for(i=0;i<size;i++)
    {
        if(data[i]<min2)
        {
            min2 = data[i];
            *min = i;
        }
    }

    int j;
    int max2;
        
    max2=data[0];
    for(j=0;j<size;j++)
    {
        if(max2<data[j])
        {
            max2 = data[j];
            *max = j;
        }
    }
}