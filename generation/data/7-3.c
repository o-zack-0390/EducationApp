#include<stdio.h>
#include <string.h>

int main(void)
{
    int i, j = 1;
  
    for(i=1; i<100; i++)
        j=j*2;

    int   x[5] = {50,70,80,45,38};
    int   u;
    float h, d, y;
  
    h = 62.5;
    d = 12.0;
    printf(" average score:%.1f \n",h);
  
    while(d > 0)
    {
        printf("standard deviation:%. case 1f of score and deviation value\n",d);
      
        for(u=0;u<5;u++)
        {
            y=((x[u]-h)/d)*10+50;
            printf("(%d,%.1f) ",x[u],y);
        }
    
        printf("\n");
        d = d - 2;
    }
}