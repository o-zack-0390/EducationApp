#include <stdio.h>
int copyN(char *out,int pos,char *in,int num);
int maxip(char *s);

int main(void)
{
    char *strs[4] = {"v4va","4j4k8ghx","4j4kl23","2006456"};
    char outb[80] = {0};
    int  p=0, i, n;
        
    for(i=0;i<4;i++)
    {
        n = maxip(strs[i]);
        p = copyN(outb,p,strs[i],n);
        printf("%s\n",outb);
    }
    
    printf("outb=\"%s\"\n",outb);
    return 0;
}


int copyN(char *out,int pos,char *in,int num)
{
    int i, n = pos;
        
    for(i=0;i<num;i++)
    {
        out[n]=in[i];
        n++;
    }
    out[n]='\0';
        
    return pos + num;
}


int maxip(char *s)
{
    int j;
    int max_val = 0, max_index, count = 0;

    for(j=0;s[j]!='\0';j++)
    {
        if('0' <= s[j] && s[j] <= '9')
        {
            if(max_val < s[j])
            {
                max_val   = s[j];
                max_index = j;
            }
            
            count++;
        }
    }

    if(count == 0)
        max_index = 1;

    return max_index;
}