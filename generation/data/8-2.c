#include <stdio.h>
int main(void)
{
    FILE *fp;
    FILE *fp2;
    char s[256];
    char c;
    
    if ((fp = fopen("sampledata.txt", "r")) == NULL)
    {
        printf("file open error!!\n");
        return 1;
    }
    
    if((fp2 = fopen("secretdata.txt", "w")) == NULL)
    {
        printf("Can not create file %s", "secretedata.txt");
        return 1;
    }
                
    printf("\n------------------------------------------------------\n");
    printf("Read by fgets() ---------------------------------------\n");
                
    while (fgets(s, 256, fp) != NULL)
        printf("%s", s);
                
    printf("\n------------------------------------------------------\n");
    fseek(fp, 0, SEEK_SET);

    printf("Read by fscanf() --------------------------------------\n");
    
    while(fscanf( fp, "%s", s) != EOF)
        printf( "%s\n", s);
 
    printf("------------------------------------------------------\n");
    fseek(fp, 0, SEEK_SET);

    printf("Read by fetc() ----------------------------------------\n");
    printf("Save the data into a new file %s\n", "secretedata.txt");
    while((c = fgetc(fp)) != EOF)
        fputc(c+5, fp2);
        
    fclose(fp);
    fclose(fp2);
}