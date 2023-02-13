#include <stdio.h>
#define MAXLINE 1001

int main(int argc, char *argv[])
{
    int  i, j;
    int  f;
    char line[MAXLINE];
    FILE *file;
    
    if (argc != 3)
    {
        fprintf(stderr, "Error: too few or much arguments");
        return 1;
    }
      
    if ((file = fopen(argv[2], "r")) == NULL)
    {
        fprintf(stderr, "Error: cannot open %s", argv[2]);
        return 1;
    }
    
    while(fgets(line, MAXLINE, file) != NULL)
    {
        for(i = 0; line[i] != '\0'; i++)
        {
            f = 1;
            for(j = 0; argv[1][j] != '\0'; j++)
            {
                if(line[i + j] != argv[1][j])
                {
                    f = 0;
                    break;
                }
            }
            
            if(f == 1)
                break;
        }
        
        if(f == 1)
            printf("%s", line);
    }
    
    fclose(file);
    return 0;
}