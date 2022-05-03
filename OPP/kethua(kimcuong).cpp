#include<iostream>
using namespace std;
class A
{
    public:
        void show()
        {
            cout<<"show A\n";
        }
};
class B : virtual public A
{};
class C:virtual public A
{};
class D: public B,public C
{};
int main()
{
    D d;
    d.show();
}
