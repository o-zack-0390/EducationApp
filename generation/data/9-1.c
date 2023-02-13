#include <stdio.h>
#define NLEN 14
#define Lsize (sizeof(list)/sizeof(struct town))

struct town
{
    int  area;
    int  pop; 
    char name[NLEN+1]; 
};


double getDens(struct town t)
{
    double x;
    x = (double)t.pop / (double)t.area;
    return x;
}


void printTown(struct town t)
{
    printf("area=%d,pop=%d,dens=%.2f,name=%s\n",t.area,t.pop,(double)t.pop/(double)t.area,t.name);
}


int main(void)
{
    struct town list[] = {
      {33,22,"honmachi"}, {30,17,"kishine" }, {40,18,"kosugi" },
      {12,11,"kouen"   }, {27,35,"fujisawa"}, {50,11,"kouza"  },
      {17,90,"musashi" }, {36,13,"oono"    }, {40,53,"ootsuka"},
      {15,86,"sagami"  }, {20,67,"shibuya" }, {34,15,"uehara" },
      {18,60,"yoyogi"  } };
      
    int i,j;
    double max;
    double maxtown = 0;
    
    for(i=0;i<Lsize;i++)
    {
        max = getDens(list[i]);
        
        if(maxtown<max)
        {
            maxtown = max;
            j       = i;
        }
    }

    printTown(list[j]);
    return 0;
}