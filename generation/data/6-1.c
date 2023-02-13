#include <stdio.h>
int  square1(int a);
void square2(int *a);
int* square3(int *a);

int main(void)
{
    int k;
    while(1)
    {
        printf("k="); scanf("%d",&k);
        if(k<=0) break;

        printf("k value: %d\n",k);
        k=square1(k);

        printf("Now, k=%d\n",k);
        square2(&k);

        printf("Now, k=%d\n",k);
        square3(square3(&k));

        printf("Now, k=%d\n\n",k);
    }

    return 0;
}

int square1(int a)
{
    a=a*a;
    return a;
}

void square2(int *a)
{
    *a=(*a)*(*a);
}

int* square3(int *a)
{
    *a=(*a)*(*a);
    return a;
}