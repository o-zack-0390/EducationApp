#include <string.h>
#define LEN 10

int main()
{
    char sentence[] = "ATGCATGAATTGCCAATGGAGCCCCTCGAAGCGTCCGAGTAA";
    char query[LEN+1];
    char result[LEN+1];
    int  length;
    int  stop;
    int  i, j;
    
    printf("input seach character :");
    scanf ("%s", query);
    
    length = strlen(query);
    stop   = 0;
    
    for(i=0; stop == 0; i++)
    {
        for(j=0; j<length; j++)
        {
            if(sentence[i+j] == '\0')
            {
                stop = 1;
                break;
            }
            
            else
            {
                if((query[j] != '.') && (query[j] != sentence[i+j]))
                    break;
                          
                else
                    result[j] = sentence[i+j];
            }
        }
          
        if (j == length)
        {
            result[j] = '\0';
            printf("Detect: %2d %s\n", i, result);
        }
    }
    
    return 0;
}