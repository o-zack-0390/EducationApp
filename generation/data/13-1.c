#include <stdio.h>
void printCitiesTree(int indent, struct cityTN *s);
struct cityTN *addCity(struct cityTN *ct, char *str, int num);

struct cityTN
{
    char   name[20];
    int    population;
    struct cityTN *left;
    struct cityTN *right;
};


int main()
{
    struct cityTN c1 = {"Hiratsuka", 257829, NULL, NULL},
                  c2 = {"Odawara"  , 190391, NULL, NULL},
                  c3 = {"Yokosuka" , 395706, NULL, NULL},
                  c4 = {"Kamakura" , 172311, NULL, NULL},
                  c5 = {"Chgasaki" , 241991, NULL, NULL},
                  c6 = {"Fujisawa" , 434110, NULL, NULL};
                  
    struct cityTN *root = NULL;
    root     = &c1; 
    c1.left  = &c2;  
    c1.right = &c3; 
    c2.left  = &c4; 
    c2.right = &c5; 
    c3.right = &c6;
  
    char str[20];
    int num;
    printf("input a city name and its population : ");
    scanf ("%s %d", str, &num);
  
    root = addCity(root, str, num);
    printCitiesTree(0, root);
    printf("\n");
  
    printf("input a city name and its population: ");
    scanf ("%s %d", str, &num);
  
    root = addCity(root, str, num);
    printCitiesTree(0, root);
    printf("\n");
  
    return 0;
}


void printCitiesTree(int indent, struct cityTN *ct)
{
    int i;
    
    if (ct == NULL) 
        printf("NULL");
    
    else 
    {
        printf("\n");
        
        for(i = 0; i < indent; i++) 
            printf(" ");
        
        printf("(%-10s: population = %6d) ", ct->name, ct->population);
        printCitiesTree(indent + 5, ct->left);
        printf(", ");
        printCitiesTree(indent + 5, ct->right);
        printf(") ");
    }
}


struct cityTN *addCity(struct cityTN *ct, char *str, int num)
{
    struct cityTN *bt=NULL;
    bt = (struct cityTN *)malloc(sizeof(struct cityTN));
    strcpy(bt->name,str);
    
    bt->population = num;
    bt->left       = NULL;
    bt->right      = NULL;
        
    if(ct->population<num)
    {
        if(ct->right==NULL)
            ct->right=bt;
        
        addCity(ct->right,str,num);
    }
    
    else if(ct->population>num)
    {
        if(ct->left==NULL)
            ct->left=bt;
        
        addCity(ct->left,str,num);
    }
        
    return ct;
}