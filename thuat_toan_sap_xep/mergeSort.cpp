#include<stdio.h>
#include<stdlib.h>

void merge(int arr[],int l,int m,int r)
{
    int n1 = m - l +1;
    int n2 = r - m;
    // tạo các mảng tạm
    int L[n1],R[n2];
    for(int i =0;i<n1;i++)
    {
        L[i]=arr[l+i];
    }
    for(int j = 0;j<n2;j++)
    {
        R[j]= arr[m+j+1];
    }
    // gộp hai mảng vừa tạo
    int i =0,j=0;
    int k =l;
    while(i<n1 && j <n2)
    {
        if(L[i] <=R[j])
        {
            arr[k] =L[i];
            i++;
        }else{
            arr[k] = R[j];
            j++;
        }
        k++;
    }
    while(i<n1){
        arr[k]=L[i];
        i++;
        k++;
    }
    while(j<n2)
    {
        arr[k]=R[j];
        j++;
        k++;
    }
}
void mergeSort(int arr[],int l, int r)
{
    if(l<r)
    {
        int m = (l+r)/2;
        mergeSort(arr,l,m);
        mergeSort(arr,m+1,r);
        merge(arr,l,m,r);
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
    int arr[] = {1,5,19,8,35,10,21,12,14,6,11,3,24,13};
    mergeSort(arr,0,sizeof(arr)/sizeof(int) -1);
    output(arr,sizeof(arr)/sizeof(int));
}