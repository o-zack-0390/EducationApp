#include <stdio.h>
void printStrings(char **p,int n);
void swapStrings(char **p,int i,int j);

int main(void)
{
    char *p[100];
    char Orange[] = "orange", Apple[] = "apple", Peach[] = "peach", Grape[] = "grape", Melon[] = "melon";
    int  i,j;
    
    p[0] = Orange; 
    p[1] = Apple; 
    p[2] = Peach; 
    p[3] = Grape; 
    p[4] = Melon;
    printStrings(p,5);
    
    while(1)
    {
        printf("Input a pair of integers: ");
        scanf ("%d %d",&i,&j);
        
        if(i<0 || i>4 || j<0 || j>4) 
            break;
                
        swapStrings(p,i,j);
        printStrings(p,5);
    }
    
    return 0;
}


void printStrings(char **p,int n)
{
    int i;
        
    printf("------begin: print_string------\n");
    for(i=0;i<n;i++)
        printf("要素%d:%p %p %s\n",i,&p[i],p[i],p[i]);
    printf("------ end: print_string------\n");
}


void swapStrings(char **p,int i,int j)
{
    int   k;
    char *tmp;
    tmp  = p[i];
    p[i] = p[j];
    p[j] = tmp;
}