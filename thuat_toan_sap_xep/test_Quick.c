#include<stdio.h>
#include<stdlib.h>
void swap(int *a,int *b)
{
    int temp = *a;
    *a = *b;
    *b = temp;
}
int pratition(int arr[],int left,int right)
{
    int l = left;
    int r = right;
    int pi = (r + l)/2;
    while(l<r)
    {
        while(l < r && arr[l] < arr[pi]) l++;
        while( r > l && arr[r] > arr[pi]) r--;
        if(l<=r)
        {
            swap(&arr[l],&arr[r]);
            l++;
            r--; 
        }
    }
    if(l < right){
        pratition(arr,l,right);
    }
    if(r > left)
    {
        pratition(arr,left,r);
    }
}
void output(int arr[],int size)
{
    for(int i=0;i<size;i++)
    {
        printf("%d ",arr[i]);
    }
}
int main()
{
    int arr[] = {1,5,19,7,8,35,26,10,21,3,12};
    pratition(arr,0,sizeof(arr)/sizeof(int)-1);
    output(arr,sizeof(arr)/sizeof(int));

}