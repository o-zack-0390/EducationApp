#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define LEN 50

LNode *cons(int, char *);
void   print_sentence(LNode *);
void   add_node(LNode *, LNode *);

struct ListNode
{
    int    order;
    char   word[LEN];
    struct ListNode *next;
};
typedef struct ListNode LNode;


int main()
{
    LNode *ltop;
    LNode *ladd;
    char word[LEN];
    int  order;
    
    ltop = cons(0, "\0");
    
    while(scanf("%s %d", word, &order) == 2)
    {
        ladd = cons(order, word);
        add_node(ltop, ladd);
    }
    
    print_sentence(ltop->next);
    return 0;
}


LNode *cons(int order, char *word)
{
    LNode *nd;
    nd = (LNode *)malloc(sizeof(struct ListNode));
    
    if (nd == NULL)
    {
        printf("malloc error!!\n");
        exit(-1);
    }
    
    nd->order = order;
    strcpy(nd->word, word);
    nd->next = NULL;
    
    return nd;
}


void print_sentence(LNode *lnode)
{
    printf("%s", lnode->word);
    lnode = lnode->next;

    while(lnode != NULL)
    {
        printf(" %s", lnode->word);
        lnode = lnode->next;
    }
    
    printf("\n");
}


void add_node(LNode *lnode, LNode *ladd)
{
    if(lnode->next == NULL)
        lnode->next = ladd;
    
    else if (lnode->next->order > ladd->order)
    {
        ladd->next  = lnode->next;
        lnode->next = ladd;
    }

    else
        add_node(lnode->next, ladd);
}