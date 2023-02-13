#include <stdio.h>
#define L 27
int copyN(char *out,int pos,char *in,int num);

int main(void)
{
    char inbuf[20];
    char outbuf[L];
    int  i, p, p2, n;
        
    for(i=0;i<L;i++)
        outbuf[i]='A'+i;
    
    outbuf[L-1]='\0';
    printf("in:");  scanf("%s",inbuf);
    printf("pos:"); scanf("%d",&p);
    printf("num:"); scanf("%d",&n);
    p2=copyN(outbuf,p,inbuf,n);

    for(i=0;i<L;i++)
    {
        if(outbuf[i]==0)
            printf("outbuf[%d]=null\n",i);
                
        else
            printf("outbuf[%d]='%c'\n",i,outbuf[i]);
    }
        
    printf("pos=%d num=%d ret=%d outbuf=\"%s\"\n",p,n,p2,outbuf);
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
    
    return pos+num;
}