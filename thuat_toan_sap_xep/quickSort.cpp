#include<stdio.h>
void swap(int &a,int &b)
{
    int c =a;
    a=b;
    b=c;
}
// thuat toan phan doan
int partition(int arr[],int low,int high)
{
    // phan tu pivot o cuoi
    int pivot = arr[high];
    int left = low;
    int right = high -1;
    while(true)
    {
        while(left<=right && arr[left] < pivot) left++;
        while(right>=left && arr[right] > pivot) right--;
        if(left >= right) break;
        swap(arr[left], arr[right]);
        right--;
        left++;
    }
    swap(arr[left],arr[high]);
    return left; // trả về vị trí của phần tử cuối đã đúng vị trí
}
void quickSort(int arr[],int low,int high)
{
    if(low<high)
    {
        int pi = partition(arr,low,high);
        // đệ qui 2 mảng con 2 bên
        quickSort(arr,low,pi-1);
        quickSort(arr,pi+1,high);
    }

}
void output(int arr[],int size)
{
    for(int i=0;i<size;i++)
    {
        printf("%d ",arr[i]);
    }
}
// cach 2
void quic_Sort(int arr[],int left,int right)
{
    int i = left;
    int j = right;
    int p= arr[(left + right)/2];
    while(i<j){
        while(arr[i]<p){
            i++;
        }
        while(arr[j] > p){
            j--;
        }
        if(i<=j){
            int temp = arr[i];
            arr[i]=arr[j];
            arr[j]=temp;
            i++;
            j--;
        }
    }
    if(i< right){
        quic_Sort(arr,i,right);
    }
    if(j> left){
        quic_Sort(arr,left,j);
    }
}
int main()
{
    int arr[] = {1,5,19,7,8,35,26,10,21,3,12};
    quic_Sort(arr,0,sizeof(arr)/sizeof(int) - 1);
    output(arr,sizeof(arr)/sizeof(int));
}