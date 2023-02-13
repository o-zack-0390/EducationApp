#include <stdio.h>
void   printCities(struct cityLN *ct);
struct cityLN * reverseCities(struct cityLN *ct);
struct cityLN * reverseCitiesRecursive(struct cityLN *ct,struct cityLN *bt);

struct cityLN
{
    char   name[20];
    int    population;
    struct cityLN *next;
};


int main()
{
    struct cityLN c1 = {"Hiratuka",257829,NULL},
                  c2 = {"Odawara"  ,190391,NULL },
                  c3 = {"Yokosuka" ,395706,NULL},
                  c4 = {"Kamakura" ,172311,NULL},
                  c5 = {"Chigasaki",241991,NULL},
                  c6 = {"Fujisawa" ,434110,NULL};
                  
    struct cityLN *head=NULL;
    head    = &c1; 
    c1.next = &c2; 
    c2.next = &c3; 
    c3.next = &c4; 
    c4.next = &c5; 
    c5.next = &c6;
    
    printf("Original: \n");
    printCities(head);
    printf("Reversed: \n");

    head = reverseCitiesRecursive(head,NULL);
    printCities(head);
    return 0;
}


void printCities(struct cityLN *ct)
{
    if(ct!=NULL)
    {
        printf("(%-10s: population=%6d)",ct->name,ct->population);
        printf("%s",(ct->next!=NULL)?"->\n":"");
        printCities(ct->next);
    }
    
    else
        putchar('\n');
}


struct cityLN * reverseCities(struct cityLN *ct)
{
    struct cityLN *bt,*dt;
    
    if(ct==NULL) 
        return NULL;
    
    if(ct->next==NULL)
        return ct;
    
    bt       = ct;
    ct       = ct->next;
    bt->next = NULL;
    
    while(1)
    {
        dt       = ct->next;
        ct->next = bt;
        
        if(dt==NULL) 
            return ct;
                
        bt = ct;
        ct = dt;
    }
}


struct cityLN * reverseCitiesRecursive(struct cityLN *ct,struct cityLN *bt)
{
    struct cityLN *tmp=NULL;
    
    if(ct==NULL)
    return bt;

    tmp      = ct->next;
    ct->next = bt;

    return reverseCitiesRecursive(tmp,ct);
}