#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void mbtree(NODE *pp, char *data);
int  btsearch( NODE *p, char *data);

typedef struct _nd
{
    char   data[20];
    struct _nd *left;
    struct _nd *right;
}NODE;


int main(void)
{
    char data[6][20] = {"this", "book", "good", "flower", "class", "base"};
    int  i;
    
    for (i = 0; i < 6; i++)
        printf("%s ", data[i]);  
    printf("\n");
        
    NODE *root, *top;
    root = (NODE *) malloc(sizeof(NODE));
        
    if(root == NULL)
    {
        printf("can not allocate memory\n");
        exit(-1);
    }
        
    strcpy(root->data, data[0]);
    root->left  = NULL;
    root->right = NULL;
    top         = root;
    printf("root: \"%s\"\n", root->data);
        
    for( i = 1; i < 6; i++)
        mbtree(top, data[i]);
    
    btsearch(top, "class");
    btsearch(top, "boot");
    btsearch(top, "book");
    btsearch(top, "bad");
    
    return 0;
}


void mbtree(NODE *p1, char *data)
{
    NODE *p2;

    p2 = (NODE *) malloc(sizeof(NODE));
    strcpy(p2->data, data);
    p2->left  = NULL;
    p2->right = NULL;
    
    if (p2 == NULL)
    {
        perror("can not allocate memory for a new node\n");
        exit(-1);
    }

    if(strcmp(p2->data,p1->data) > 0)
    {
        if (p1->right == NULL)
        {
            p1->right=p2;
            printf("(p:%s) r:\"%s\" \n", p1->data, data);
        } 
        
        else
            mbtree(p1->right, data);
    }
        
    else
    {
        if(p1->left==NULL)
        {
            p1->left=p2;
            printf("(p:%s) r:\"%s\" \n", p1->data, data);
        }
        
        else
            mbtree(p1->left,data);
    }
}


int btsearch(NODE *p, char *data)
{
    int chk;
    int chknum = 0;

    printf("\n search for \"%s\"\n", data);
    while (p != NULL)
    {
        chk = strcmp(data, p->data);
        chknum++;
                
        if (chk == 0)
        {
            printf("%sはみつかりました。チェックした回数:%d\n",data,chknum);
            return (-1);
        }
        
        else if (chk < 0)
        {
            p = p->left;
            printf("\"%s\" is checked goto left subtree\n");
        }
        
        else
        {
            p = p->right;
            printf("\"%s\" is checked goto right subtree\n");
        }
    }
    
    printf("\"%s\" はみつかりませんでした。チェックした回数:d\n", data,chknum);
    return (-1);
}