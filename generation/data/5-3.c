#include <stdio.h>
#define WLEN 20
#define WNUM 10
int main()
{
    char words[WNUM][WLEN] = {"Yokohama","Hiratuka","Sagamihara","Atsugi","Fujisawa","Chigasaki","Odawara","Kawasaki","Yamato","Yokosuka"};
    char tmp;
    int  src, dest;
    int  i;

    for(i=0;i<WNUM;i++)
        printf("%d:%s\n",i,words[i]);

    printf("Replace\n");
    scanf ("%d %d",&src,&dest);
    
    if(src == dest || src<0 || WNUM<src || dest<0 || WNUM<dest){
        printf("Replace: %d %d\n",src,dest);
        printf("Invalid inputs(s)\n");
        return 1;
    }
        
    printf("Replace: %d %d\n",src,dest);
    printf("Replace: %s <-> %s\n",words[src],words[dest]);

    for(i=0;;i++)
    {
        if(words[src][i]=='\0' && words[dest][i]=='\0')
            break;
                
        tmp            = words[src][i];
        words[src][i]  = words[dest][i];
        words[dest][i] = tmp;
    }

    for(i=0;i<WNUM;i++)
        printf("%d:%s\n",i,words[i]);

    return 0;
}