#include <stdio.h>
#include <stdlib.h>

void printarray(int heap[], int size);
void swapvalue(int heap[], int i, int j);
void upvalue(int heap[], int i);
void downvalue(int heap[], int i, int size);


int main(void)
{
    int data[] = {8, 98, 87, 36, 35, 54, 11, 33, 6, 79}, size = 10;
    int *heap, i;
    
    heap = (int *) malloc(sizeof(int)*size);
    for(i = 0; i < size; i++)
    {
        heap[i] = data[i];
        upvalue(heap, i);
    }
        
    printarray(heap, size);
    heap[0] = heap[--size];
    downvalue(heap, 0, size);
    printarray(heap, size);
    
    return 0;
}


void printarray(int heap[], int size)
{
    for (int i = 0; i < size; i++)
        printf("%2d%c", heap[i], i == size-1 ? '\n': ' ');
}


void swapvalue(int heap[], int i, int j)
{
    int tmp = heap[i];
    heap[i] = heap[j];
    heap[j] = tmp;
}


void upvalue(int heap[], int i)
{
    int j = i;
    
    if(i%2==1)
        while(1)
        {
            if( ((i-1) / 2) < 0 )
                break;
            
            if(heap[i]<=heap[(i-1)/2])
                swapvalue(heap,i,(i-1)/2);
                i--;
        }
        
        i = j;
        
        if(i%2 == 0)
            while(1)
            {
                if( ((i-2) / 2) < 0 )
                    break;
                
                if(heap[i]<=heap[(i-2)/2])
                    swapvalue(heap,i,(i-2)/2);
                    i--;
            }
}


void downvalue(int heap[], int i, int size)
{
    for(;i<size;i++)
        upvalue(heap,i);
}