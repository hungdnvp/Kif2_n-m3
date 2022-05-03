#include<iostream>
using namespace std;
class A{
    public:
        void show()
        {
            cout<<"show A\n";
        }
};
class B:public A
{
public:
    void show()
    {
        cout<<"show B\n";
    }
};
class C:public A
{
public:
    void show()
    {
        cout<<"show C\n";
    }
    void display()
    {
        cout<<"display C\n";
    }
};
int main()
{

    A a;
    B b;
    C c;
    B *ptr_b = new B();
    ptr_b->show();  // show B

    C *ptr_c;
    ptr_c = &c;
    ptr_c->show(); // show C

    A *ptr_a;
   // A *p = new C();  // con tro kieu cha co the tro toi doi tuong con
    ptr_a = &b;
    ptr_a->show(); // show A  để khắc phục thì thêm virtual vao A::show()
    return 0;
}