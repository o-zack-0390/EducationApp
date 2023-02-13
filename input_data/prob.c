#include <stdio.h>
#define N 3
int main(void){
	int a[1000];
	int count;
	int h;
	for(h=0;;h++){
		scanf("%d",/* ○ ○ ○ */a[h]);
		if(a[h]<=0){
			break;
		}
	}
	count=h;
	if(count<N-1){
		printf("0\n");
		return 0;
	}
	int tmp;
	for(int j=0;j<=count;++j){
		for(int k=j+1;k<=count;++k){
			if(a[j]<a[k]){
				tmp=a[j];
				/* □ □ □ */[j]=/* □ □ □ */[k];
				a[k]=/* □ □ □ */;
			}
		}
	}
	/* □ □ □ */ stock=a[0];
	int count2=1;
	for(int /* □ □ □ */=0;/* □ □ □ */<=count;/* □ □ □ */++){
		if(stock/* ○ ○ ○ */a[m]){
			stock=a[m];
			count2++;
		}
		if(count2/* ○ ○ ○ */N){
			break;
		}
	}
	printf("number%d=%d\n",N,stock);
	return 0;
}