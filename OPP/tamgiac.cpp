#include<iostream>
using namespace std;
class tamgiac
{
private:
    int a,b,c;
public:
    bool istamgiac(int a,int b, int c )
    {
        return (a+b)>c && (a+c) >b && (b+c)>a;
    }
    tamgiac(int a,int b,int c)
    {
        if(istamgiac(a,b,c))
        {
            this->a = a;this->b =b;this->c = c;
        }
        else cout<<"ko hop le";
    }
static void dinhdang(tamgiac tg)
    {
        string result = (tg.a == tg.b && tg.a == tg.c)  ?"tg deu" : "not tg deu";
        cout<<result<<endl;
    }
};
int main()
{
    tamgiac a = tamgiac(5,5,20);
    tamgiac::dinhdang(a);
    
    return 0;
}