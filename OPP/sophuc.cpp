#include <iostream>
using namespace std;
class SP
{
    int x;
    int y;

public:
    SP()
    {
        x = 0;
        y = 0;
    };
    // ~SP();
    SP(int a, int b)
    {
        x = a;
        y = b;
    }
    void setX(int a) { x = a; };
    void setY(int b) { y = b; }; 
    int getX() { return x; };
    int getY() { return y; };
    SP operator+(const SP &);
    SP operator-(const SP &);
    friend ostream &operator<<(ostream &out, SP &sp);
    friend istream &operator>>(istream &in, SP &sp);
};
SP SP::operator+(const SP &sp)
{
    SP next;
    next.x = this->x + sp.x;
    next.y = this->y + sp.y;
    return next;
}
SP SP::operator-(const SP &sp)
{
    SP next;
    next.x = this->x - sp.x;
    next.y = this->y - sp.y;
    return next;
}
ostream &operator<<(ostream &out, SP &sp)
{
    if (sp.y == 0)
    {
        out << sp.x;
    }
    else if (sp.y > 0)
    {
        out << sp.x << "+" << sp.y << "i";
    }else
    {
        out<<sp.x<<sp.y<<"i";
    }
    return out;
}
istream &operator>>(istream &is, SP &sp)
{
    cout << "nhap vao phan thuc: ";
    is >> sp.x;
    cout << "nhap vao phan ao: ";
    is >> sp.y;
    return is;
}
int main()
{
    SP sp1, sp2, sp3;
    sp1 = SP(5, 3);
    sp2.setX(2);
    sp2.setY(7);
    cin >> sp3;
    cout << sp3;
    SP sp4 = sp1 + sp2;
    cout << endl
         << sp4;
    return 0;
}