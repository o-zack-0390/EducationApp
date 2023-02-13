#include <stdio.h>
#include <stdlib.h>
#define  MAX 100

struct listNode *addNode(struct listNode *node, int num);
int    sumListNum(struct listNode *node);
int    countListOdd(struct listNode *node);

struct listNode
{
    int    n;
    struct listNode *next;
};


int main(void)
{
    int    data[MAX];
    struct listNode *head;
    int    i = 0;
    int    sum, odd;
    
    head = NULL;
    
    while (1)
    {
        printf("input number: ");
        scanf("%d", &data[i]);
        
        if(data[i] == 0)
            break;
    
        else
            head = addNode(head, data[i++]);
    }
    
    printf("sum: %d\n", sum = sumListNum(head));
    printf("odd num: %d\n", odd = countListOdd(head));
    
    return 0;
}


struct listNode *addNode(struct listNode *node, int num)
{
    struct listNode *newnode, *head;

    head       = node;
    newnode    = (struct listNode *)malloc(sizeof(struct listNode));
    newnode->n = num;

    if(node == NULL)
    {
        newnode->next = NULL;
        head          = newnode;
    }
  
    else
    {
        newnode->next = head;
        head          = newnode;
    }
  
    return head;
}


int sumListNum(struct listNode *node)
{
    if(node==NULL)
        return 0;
    
    else
        return sumListNum(node->next)+(node->n);
}


int countListOdd(struct listNode *node)
{
    if(node==NULL)
        return 0;
    
    else
    {
        if((node->n)%2==0)
            node->n=0;
        
        else if((node->n)%2==1)
            node->n=1;
        
        return countListOdd(node->next)+(node->n);
    }
}