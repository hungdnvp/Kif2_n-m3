#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

class Nguoi
{
private:
    string ho_ten;
    int ngay_sinh, thang_sinh, nam_sinh;
    string que_quan;

public:
    void input();
    void output();
    bool operator<(const Nguoi &x);
    bool operator>(const Nguoi &x);
};
bool Nguoi::operator<(const Nguoi &x)
{
    if (this->nam_sinh > x.nam_sinh)
        return true;
    else if (this->nam_sinh < x.nam_sinh)
        return false;
    else
    {
        if (this->thang_sinh > x.thang_sinh)
            return true;
        else if (this->thang_sinh < x.thang_sinh)
            return false;
        else
        {
            if (this->ngay_sinh > x.ngay_sinh)
                return true;
            else if (this->ngay_sinh < x.ngay_sinh)
                return false;
            else
                throw "bang tuoi -.-";
        }
    }
}
bool Nguoi::operator>(const Nguoi &x)
{
    if (this->nam_sinh > x.nam_sinh)
        return false;
    else if (this->nam_sinh < x.nam_sinh)
        return true;
    else
    {
        if (this->thang_sinh > x.thang_sinh)
            return false;
        else if (this->thang_sinh < x.thang_sinh)
            return true;
        else
        {
            if (this->ngay_sinh > x.ngay_sinh)
                return false;
            else if (this->ngay_sinh < x.ngay_sinh)
                return true;
            else
                throw "bang tuoi -.-";
        }
    }
}
void Nguoi::input()
{
    fflush(stdin);
    cout << "enter ho_ten: ";
    getline(cin, ho_ten);
    cout << "enter ngay_sinh: ";
    cin >> ngay_sinh;
    cout << "enter thang_sinh: ";
    cin >> thang_sinh;
    cout << "enter nam_sinh: ";
    cin >> nam_sinh;
    cout << "enter que_quan: ";
    cin.ignore(3200, '\n');
    getline(cin, que_quan);
}
void Nguoi::output()
{
    cout << "ho_ten: " << ho_ten << " ngay-thang-nam sinh: " << ngay_sinh
         << "-" << thang_sinh << "-" << nam_sinh << endl;
    cout << "que_quan: " << que_quan << endl;
}

class Nhanvien : public Nguoi
{
private:
    int tien_luong;
    string chuc_vu;

public:
    void input();
    void output();
    bool operator <<(const Nhanvien& x);
    bool operator >>(const Nhanvien& x);
    int get_()
    {
        return tien_luong;
    }
};

bool Nhanvien:: operator <<(const Nhanvien& x)
{
    if(this->tien_luong < x.tien_luong) return true;
    else return false;
}
bool Nhanvien::operator >>(const Nhanvien& x)
{
    if(this->tien_luong > x.tien_luong) return true;
    else return false;
}
void Nhanvien::input()
{
    Nguoi::input();
    cout << "enter chuc vu: ";
    getline(cin, chuc_vu);
    cout << "enter tien luong: ";
    cin >> tien_luong;
}
void Nhanvien::output()
{
    Nguoi::output();
    cout << "tien_luong: " << tien_luong << " chuc_vu: " << chuc_vu << endl;
}
//
struct cmp1
{
    bool operator()(Nhanvien &a,Nhanvien &b)
    {
        return a.operator>>(b);
    }
};
struct  cmp2
{
    bool operator()(Nhanvien &a,Nhanvien &b)
    {
        return a.operator<(b);
    }
};
struct cmp3
{
    bool operator()(Nhanvien &a,Nhanvien &b)
    {
        return a.operator<<(b);
    }
};

Nhanvien* nhanvien = new Nhanvien[20];
int i=0;
void Show()
{
    for(int j=0;j<i;j++)
    {
        (nhanvien+j)->output();
    }
}
int main()
{

    char choice;
    do
    {
        system("cls");
        cout<<"NHAP THONG TIN NHAN VIEN:\n";
        (nhanvien+i)->input();
        i++;
        cout<<"enter y de tiep tuc  ";cin>>choice;cin.ignore();
    } while (i<20 && choice =='y');
// ham sap xep
    sort(nhanvien,nhanvien+i,cmp1());
    system("cls");
    cout<<"*******DANH SACH GIAM DAN CUA LUONG****\n";
    Show();
    system("pause");
    system("cls");
    cout<<"*******DANH SACH TANG DAN CUA TUOI****\n"; 
    sort(nhanvien,nhanvien+i,cmp2());
    Show();
    system("pause");
    system("cls");
    cout<<"*******DANH SACH TANG DAN CUA LUONG****\n"; 
    sort(nhanvien,nhanvien+i,cmp3());
    Show();
    system("pause");
    system("cls");
// find max tien_luong
    cout<<"*******DANH SACH NHAN VIEN LUONG CAO NHAT****\n"; 
    for(int m = 0;m<i;m++)
    {
        if((nhanvien+m)->get_() == (nhanvien +i-1)->get_() )
            (nhanvien+m)->output();
    }

    return 0;
}