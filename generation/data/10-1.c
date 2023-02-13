#include <stdio.h>
void printCitiesTree (int indent, struct cityTN *s);
void turnoverCities(struct cityTN *s);

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
  
    printf("Original: \n"); 
    printCitiesTree (0, root);
    
    printf("\n\nReversed: \n"); 
    turnoverCities(root);
    printCitiesTree (0, root); 
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
        for (i = 0; i < indent; i++) 
            printf(" ");
        
        printf("(%-10s: population = %6d) ", ct->name, ct->population);
        printCitiesTree(indent + 5, ct->left);
        printf(", ");
        printCitiesTree(indent + 5, ct->right);
        printf(") ");
    }
}


void turnoverCities(struct cityTN *s)
{
    struct cityTN *tmp;
    
    if(s!=NULL)
    {
        tmp      = s->left;
        s->left  = s->right;
        s->right = tmp;
        
        turnoverCities(s->right);
        turnoverCities(s->left);
    }
}