#include <stdio.h>
void calculate(int *data, int size, int *min, int *max, double *avg);

int main(void)
{
    int data[] = {8, 98, 87, 36, 35, 54, 11, 33, 6, 79}, size = 10;
    int min, max;
    double avg;
        
    calculate(data,size,&min,&max,&avg);
    printf("min = %d, max = %d, avg = %.1f\n", min, max, avg/size);
    
    return 0;
}


void calculate(int *data, int size, int *min, int *max, double *avg)
{
    int i;
    int min2;
  
    min2 = data[0];
    *min = 0;
  
    for(i=0;i<size;i++)
    {
        if(min2>data[i])
        {
            min2 = data[i];
            *min = min2;
        }
    }

    int j;
    int max2;
  
    max2 = data[0];
    *max = 0;
  
    for(j=0;j<size;j++)
    {
        if(max2<data[j])
        {
            max2 = data[j];
            *max = max2;
        }
    }


    int arv2=0;
    for(i=0;i<size;i++)
    {
        arv2 = arv2 + data[i];
        *avg = arv2;
    }
}