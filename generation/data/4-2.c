#include <stdio.h>

void printarray(int data[], int size);
void sortarray(int data[], int size);
int  binarysearcharray(int query, int data[],int size);

int main(void)
{
    int data[]={8,98,87,36,35,54,11,33,6,79}, size=10;
    int query;
    printarray(data,size);
    sortarray(data,size);
    printarray(data,size);
    
    while(1)
    {
        printf("query = ");
        scanf ("%d",&query);
        
        if(query<0)
            break;
        
        if(binarysearcharray(query,data,size)==1)
            printf("yes\n");
                
        else 
            printf("no\n");
    }
    
    return 0;
}


void printarray(int data[],int size)
{
    int i;
        
    for(i=0;i<size;i++)
        printf("%d%c",data[i],i==size-1?'\n':' ');
}


void sortarray(int data[],int size)
{
    int i,j,tmp;
        
    for(i=0;i<size-1;i++)
    {
        for(j=i+1;j<size;j++)
        {
            if(data[i]>data[j])
            {
                tmp    =data[i];
                data[i]=data[j];
                data[j]=tmp;
            }
        }
    }
}


int binarysearcharray(int query, int data[],int size)
{
    int u=0,v=size-1,m;
        
    while(u<v)
    {
        m=(u+v)/2;
                
        if(data[m]==query)
            return 1;
                
        else if(data[m]<query)
            u=m+1;
        
        else if(data[m]>query)
            v=m-1;
    }
}