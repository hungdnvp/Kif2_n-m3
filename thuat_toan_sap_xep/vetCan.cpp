#include<iostream>
#define MAX 20
using namespace std;
int Bool[MAX] ={1};
int x[MAX];
int n;
void xuat()
{
    for(int i=1;i<=n;i++)
        cout<<x[i]<<" ";
    cout<<endl;
}
void Try(int k)
{
    for(int i=1;i<=n;i++)
    {
        if(Bool[i])
        {
            x[k] =i;
            Bool[i] = 0;
            if(k==n) xuat();
            else
                Try(k+1);
            Bool[i] =1;
        }
    }
}
int main()
{
    n=4;
    Try(1);
}