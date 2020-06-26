#include<stdio.h>
int main(){
  int x=0,i=0,cnt=0,count=1,arr[100000];
  int n=100000000;
  while(n!=0){
    arr[i++]=n%10;
    cnt+=1;
    n/=10;
    }
  for(i=cnt-1;i>=0;i--){
  if(arr[i]==arr[i-1] && i-1>=0)
    count+=1;
  else{
    x=x*10+count;
    x=x*10+arr[i];
    cnt-=count;
    count=1;
    }
  }
  if(cnt>0){
    x=x*10+count;
    x=x*10+arr[i];
   }
  printf("%d",x);
}
