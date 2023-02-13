#include <stdio.h>
#include <stdlib.h>

struct node
{
    int    val;
    struct node *next;
};
typedef struct node *LIST;


int lenL(LIST x)
{
    if(x == NULL)
        return 0;
    
    return 1 + lenL(x->next);
}


LIST cutL(LIST x, int p)
{
    LIST t = (LIST) malloc(sizeof(struct node));

    if(x == NULL)
        return NULL;

    else if(p == 1)
    {
        t       = x->next;
        x->next = NULL;
        return t;
    }

    else
    {
        t = x->next;
        cutL(t,p-1);
    }
}


void showL(char *m, LIST x)
{
    printf("%s:", m);
    while (x != NULL)
    {
        printf("%3d", x->val);
        x = x->next;
    }
    printf("\n");
}


LIST mergeL(LIST x, LIST y)
{
    LIST hozon1 = (LIST) malloc(sizeof(struct node));
    LIST hozon2 = (LIST) malloc(sizeof(struct node));
    
    if(x==NULL)
        return y;
    
    else if(y==NULL)
        return x;
    
    else
    {
        hozon1  = x->next;
        hozon2  = y->next;
        x->next = y;
        y->next = hozon1;
        mergeL(hozon1,hozon2);
        return x;
    }
}


LIST addL(LIST x, int v)
{
    LIST t = (LIST) malloc(sizeof(struct node));
    
    if (t == NULL)
    {
        printf("malloc failed");
        exit(-1);
    }
    
    t->val  = v;
    t->next = x;
    
    return t;
}


int main(void)
{
    int  i, len;
    LIST part1 = NULL;
    LIST part2;
    LIST mix;
    
    printf("length:");
    scanf ("%d", &len);
    
    for(i = len; i >= 1; i--)
        part1 = addL(part1, i);
    
    part2 = cutL(part1, lenL(part1) / 2);
    showL("part1", part1);
    showL("part2", part2);
    
    mix = mergeL(part2, part1);
    showL("mix  ", mix);
    
    return 0;
}