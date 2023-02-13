#include<stdio.h>
#include<stdlib.h>
#define N 3

list input(void);
list insert(int n, list l);
list mknode(int n, list l);
int  take(int n, list l);
void lfree(list l);

typedef struct lnode *list;
struct lnode
{
    int  val;
    list next;
};


int main(void)
{
    list = input();
    printf("%d", take(N, l));
    lfree(l);
    return 0;
}


list input(void)
{
    int n;
    list l;
    
    while(1)
    {
        scanf("%d", &n);
        
        if (n <= 0)
            return NULL;
        
        else
        {
            l = input();
            return insert(n, l);
        }
    }
}


list insert(int n, list l)
{
    list l1;
    printf("T=%d ",n);
    
    if (l == NULL || l->val < n)
        return mknode(n, l);
  
    printf("(%d,E=%d) ",n,l->val);
    if (l->val > n)
        l->next = insert(n, l->next);
  
    printf("%d ",l->val);
    return l;
}


list mknode(int n, list l)
{
    list l1;
    
    if((l1 = malloc(sizeof(struct lnode))) == NULL)
        exit(1);
    
    l1->val = n;
    l1->next = l;
    
    printf("q=%d ",l1->val);
    return l1;
}


int take(int n, list l)
{
    n--;
    
    if(l==NULL)
        return 0;
    
    else if(n==0)
        return l->val;
    
    else
        take(n,l->next);
}


void lfree(list l)
{
    list l2;
    
    if(l != NULL)
    {
        l2=l->next;
        free(l);
        l=l2;
        lfree(l);
    }
}