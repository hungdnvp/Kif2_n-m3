// ********************-->>> SAP XEP CHON <<<<---*************
#include<stdio.h>
void swap(int &a,int &b)
{
    int c =a;
    a=b;
    b=c;
}
void selection_Sort(int arr[],int size)
{
    for(int i = 0;i<size;i++)
    {
        // chọn index_min = i
        int minIndex =i;
        for(int j = i+1;j<size;j++)
        {
            if(arr[j]<arr[minIndex])
            {
                minIndex = j;
            }
        }
        swap(arr[i],arr[minIndex]);
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
    selection_Sort(arr,sizeof(arr)/sizeof(int));
    output(arr,sizeof(arr)/sizeof(int));
}