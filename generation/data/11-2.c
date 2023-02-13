#include <stdio.h>
#include <stdlib.h>
void mbtree(NODE *p1, int num);

typedef struct _nd
{
    int    num;
    struct _nd *left;
    struct _nd *right;
}NODE;


int main(void)
{
    int data[] = {5, 2, 8, 7, 5, 3, 9, 2, 10};
    int dsize;
    int i;
    NODE *root, *top;
	
    dsize = sizeof(data)/sizeof(int);
    for (i = 0; i < dsize; i++)
        printf("%d ", data[i]);
	
    printf("\n");
    root = (NODE *) malloc(sizeof(NODE));
	
    if(root == NULL)
    {
        printf("can not allocate memory\n");
        exit(-1);
    }
    
    root->num   = data[0];
    root->left  = NULL;
    root->right = NULL;
    top         = root;
        
	printf("root: %d\n", root->num);
    for(i = 1; i < dsize; i++)
    {
        printf("i= %d :", i);
        mbtree(top, data[i]);
    }
	
    return 0;
}


void mbtree(NODE *p1, int num)
{
    NODE *p2;
    p2 = (NODE *)malloc(sizeof(NODE));
	
    if(p2 == NULL)
    {
        printf("can not allocate memory for mbtree\n");
        exit(-1);
    }
        
    p2->num   = num;
    p2->left  = NULL;
    p2->right = NULL;

    if (p1->num < num)
    {
        if (p1->right == NULL)
        {
            p1->right = p2 ;
            printf("(p)%d (r)%d\n",p1->num,p2->num);
        }
        
        else
            mbtree(p1->right,p2->num);
    }
	
    else
    {
        if(p1->left==NULL)
        {
            p1->left=p2;
            printf("(p)%d (l)%d\n",p1->num,p2->num);
        }
		
        else
            mbtree(p1->left,p2->num);
    }
}