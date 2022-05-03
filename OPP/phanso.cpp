#include <iostream>
#include<vector>
#include<algorithm>
using namespace std;
class phanso
{
private:
    int tu;
    int mau;
public:
    phanso(){tu = 0;mau = 1;}
    phanso(int a, int b)
    {
        if(b==0) phanso();
        else{this->tu = a;this->mau =b;}
    }
    void setTu(int a) { tu = a; }
    void setMau(int b) {if(b==0) mau =1;else mau = b; }
    // nap chong toan tu
    operator float();  // toan tu chuyen kieu float
    friend phanso operator+(const phanso& a,const int& i);
    friend phanso operator+(const int& i,const phanso& a);
    phanso operator+(phanso const &obj);
    phanso operator++(int);  // a++
    friend phanso operator++(phanso& a); //++a
    friend phanso operator--(phanso& a); // --a
    friend phanso operator-(phanso const &obj, phanso const &obj2);
    phanso operator*(phanso const &obj);
    bool operator>(phanso& obj);
    bool operator<(phanso& obj);
    // nap chong nhap xuat  
    friend ostream& operator<<(ostream &os, phanso const &x);
    friend istream& operator>>(istream &is, phanso &x);
    // ham phụ
    int UCLN(const int& a,const int& b)
    {
        // ap dung thuat toan Euclid
        int r0,r1,r2;
        r0 = a;
        r1 = b;
        r2 = r0 % r1;
        while(r2 !=0)
        {
            r0 = r1;
            r1 = r2;
            r2 = r0 % r1;
        }
        return r1;
    }    
    void Rut_gon()
    {
        int x =UCLN(tu, mau);
        tu /= x;
        mau /= x;
    }
};

phanso::operator float()
{
    return (float)this->tu/this->mau;
}
phanso operator--(phanso& a)
{
    a.tu = a.tu - a.mau;
    return a;
}
phanso operator+(const phanso& a,const int& i)
{
    phanso tong;
    tong.tu = a.tu + a.mau*i;
    tong.mau = a.mau;
    return tong;
}
phanso phanso::operator+(phanso const &obj)
{
        phanso tong;
        tong.tu =tu * obj.mau + obj.tu * mau;
        tong.mau = mau * obj.mau;
        tong.Rut_gon();
        return tong;
}
phanso operator+(const int& i,const phanso& a)
{
    return a+i;
}
phanso phanso::operator++(int)
{
    phanso a = *this;
    this->tu = this->tu + this->mau;
    return a;
}
phanso operator++(phanso& a)
{
    a.tu +=a.mau;
    return a;
}
bool phanso::operator>(phanso& obj)
{
    return (float)*this > (float)obj ;
}
ostream& operator<<(ostream& os, phanso const &x)
{
        os << x.tu << "/" << x.mau << endl;
        return os;
}
istream& operator>>(istream& is,phanso &x)
 {
        cout << "nhap vao tu so: ";
        is >> x.tu;
        cout << "nhap vao mau so: ";
        is >> x.mau;
        return is;
}

phanso phanso::operator*(phanso const &obj)
{
        phanso tich;
        tich.tu =tu * obj.tu;
        tich.mau = mau * obj.mau;
        tich.Rut_gon();
        return tich;
}
phanso operator-(phanso const &obj1, phanso const &obj2)
{
    phanso hieu;
    hieu.tu = obj1.tu * obj2.mau - obj2.tu * obj1.mau;
    hieu.mau = obj1.mau * obj2.mau;
    return hieu;
}
// ****************so sanh*******
struct cmp_tang
{
    bool operator()(phanso &a,phanso &b)
    {
        return (float)a < (float)b;
    }
};
class listPS
{
    public:
        vector<phanso>lst;
    public:
        void addPS(phanso a){lst.push_back(a);}
        void addPS(int a,int b)
        {if(b==0) b=1;lst.push_back(phanso(a,b));}
        int Size(){return lst.size();}
        void sapxep_tangdan()
        {
            sort(lst.begin(),lst.end(),cmp_tang());
        }
        void show(){
            for(int i=0;i<lst.size();i++)
            {
                cout<<lst[i];
            }
        }

};
int main()
{
    phanso ps1 = phanso(5,4);
    phanso ps2 = phanso(2,3);
    cout<<ps1++;
    cout<<endl<<ps1;
    return 0;
}