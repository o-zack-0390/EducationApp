#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define WNUM 50
#define WLEN 50

TNode *tree(char *, TNode *, TNode *);
TNode *makebst(char *, TNode *);
TNode *bstinsert(TNode *, TNode *);
void  showtree(int, TNode *, char *);
void  bstunion(TNode *, TNode *);

struct TreeNode
{
    char   word[WLEN];
    struct TreeNode *left, *right;
};
typedef struct TreeNode TNode;


int main(void)
{
    int i;
    
    #ifdef EXE1
        char words_a[WNUM][WLEN] = {"This", "is", "a", "pen.", "\0"};
        char words_b[WNUM][WLEN] = {"That", "is", "an", "apple.", "\0"};
    
    #elif EXE2
        char words_a[WNUM][WLEN] = {"learn", "essential", "skills", "to", "become", "a", "leading", "engineer", "or", "creative", "researcher,", "to", "help", "support", "highly", "sophisticated", "information", "in", "society", "\0"};
        char words_b[WNUM][WLEN] = {"research","on","more","efficient","Filtering","for","safer","and","more","secure","computers","and","cellular","phones", "\0"};
        
    #else
        char words_a[WNUM][WLEN] = {"Canada", "America", "Brazil", "Mexico.", "\0"};
        char words_b[WNUM][WLEN] = {"India", "Japan", "China", "\0"};
    
    #endif
    
    TNode *tree_a, *tree_b;
    
    tree_a = tree(words_a[0], NULL, NULL);
    for(i=1; words_a[i][0] != '\0'; i++)
        makebst(words_a[i], tree_a);
    
    printf("[Tree A]\n");
    showtree(0, tree_a, "\0");
    printf("\n-----------------\n");
    
    tree_b = tree(words_b[0], NULL, NULL);
    for(i=1; words_b[i][0] != '\0'; i++)
        makebst(words_b[i], tree_b);
    
    printf("[Tree b]\n");
    showtree(0, tree_b, "\0");
    printf("\n-----------------\n");
    
    bstunion(tree_a, tree_b);
    printf("[Merge Tree]\n");
    showtree(0, tree_a, "\0");
    
    return 0;
}


TNode *tree(char *d, TNode *l, TNode *r)
{
    TNode *result;
    
    result       = (TNode *) malloc(sizeof(struct TreeNode));
    result->left = l;
    
    strcpy(result->word, d);
    result->right = r;
    
    return result;
}


void showtree(int indent, TNode *t, char *head)
{
    int i;
    
    if (t->right != NULL)
        showtree(indent+1, t->right, "/- ");
    
    for(i=0;i<indent;i++)
        printf("\t");
    
    printf("%s%s\n", head, t->word);
    
    if (t->left != NULL)
        showtree(indent+1, t->left, "\\- ");
}


TNode *makebst(char *str, TNode *t)
{
    int tmp;
    
    if(t == NULL)
        t = tree(str, NULL, NULL);
    
    else if((tmp=strcmp(str, t->word)) < 0)
        t->left = makebst(str, t->left);
    
    else if(tmp > 0)
        t->right = makebst(str, t->right);
    
    return t;
}


TNode *bstinsert(TNode *t, TNode *target)
{
    if(strcmp(t->word,target->word)<0)
    {
        if(t->right==NULL)
        {
            t->right=target;
            return t;
        }
        
        bstinsert(t->right,target);
    }
    
    else if(strcmp(t->word,target->word)>0)
    {
        if(t->left==NULL)
        {
            t->left=target;
            return t;
        }
        
        bstinsert(t->left,target);
    }
}


void bstunion(TNode *t_a, TNode *t_b)
{
    if(t_b->left!=NULL)
        bstunion(t_a,t_b->left);
    
    if(t_b->right!=NULL)
        bstunion(t_a,t_b->right);
    
    t_b->right = NULL;
    t_b->left  = NULL;
    
    bstinsert(t_a,t_b);
}