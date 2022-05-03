// ************************************--SAP-XEP-CHEN--**********************
#include<stdio.h>
void insertion_Sort(int arr[],int n)
{
    
    for(int i =1;i<n;i++){
        int key = arr[i];
        int j = i-1;
        while(arr[j]>key && j>=0){
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1]= key;
    }
}
void output(int arr[],int size)
{
    for(int i=0;i<size;i++)
    {
        printf("%d ",arr[i]);
    }
}
int main(){
    int arr[] = {1,5,19,8,35,10,21,12};
    insertion_Sort(arr,sizeof(arr)/sizeof(int));
    output(arr,sizeof(arr)/sizeof(int));
}