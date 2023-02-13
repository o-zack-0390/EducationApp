#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char buf[1000];
    FILE *fp;
    int  a[5];
    
    sprintf(buf,"data1.txt");
    
    if((fp=fopen(buf,"r"))==NULL)
        exit(1);

    while(fscanf(fp,"%d\t%d\t%d\t%d\t%d",&a[0],&a[1],&a[2],&a[3],&a[4]) != EOF)
        printf("%d\t%d\t%d\t%d\t%d\n",a[0],a[1],a[2],a[3],a[4]);
  
    fclose(fp);
    return 0;
}