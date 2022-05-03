//*************************SAP XEP NOI BOT*********************
#include<stdio.h>
void swap(int &a,int &b)
{
    int c=a;
    a=b;
    b=c;
}
void output(int arr[],int size)
{
    for(int i=0;i<size;i++)
    {
        printf("%d ",arr[i]);
    }
    printf("\n");
}
void sapXep(int arr[],int n)
{
    for(int i=0;i<n;i++)
    {

        bool key = false;
        for(int j=0;j<n-1;j++)
        {
            if(arr[j]>arr[j+1])
            {
                swap(arr[j],arr[j+1]);
                key = true;
            }
        }
        if(key == false)
        {
            break;
        }
    }
}

int main()
{
    int arr[] = {13,5,9,20,2,19,8,35,10,21,12};
    sapXep(arr,sizeof(arr)/sizeof(int));
    output(arr,sizeof(arr)/sizeof(int)); 
}