#include <iostream>
#include <string>
#include <vector>

using namespace std;

class SinhVien
{
private:
    int maSV;
    string hoten;
    float diemTB;

public:
    SinhVien() {}
    SinhVien(int ma, string ten, float diem)
    {
        maSV = ma;
        hoten = ten;
        diemTB = diem;
    }
    void show() { cout << "name: " << hoten << "\nmaSV: " << maSV << "\ndiemTB " << diemTB << endl; }
    friend int sosanhTen(const SinhVien &x, const SinhVien &y);
    float getdiemTB() { return diemTB; }
    string getName() { return hoten; }
};
int sosanhTen(const SinhVien &x, const SinhVien &y)
{
    int n = 0;
    if (x.hoten.length() > y.hoten.length())
    {
        n = y.hoten.length();
    }
    else
        n = x.hoten.length();
    int i = 0;
    while (i < n)
    {
        if (x.hoten[i] > y.hoten[i])
            return 2;
        if (x.hoten[i] < y.hoten[i])
            return 1;
        i++;
    }
    return 1;
}
class DSSV
{
private:
    vector<SinhVien> DS;

public:
    DSSV() {}
    DSSV(SinhVien a) { DS.push_back(a); }
    void add(SinhVien a) { DS.push_back(a); }
    void show();
    void sv_DTB_max();
    void sapxep();
};
void DSSV::show()
{
    if (DS.size() <= 0)
    {
        cout << "DS rong";
        return;
    }
    cout << "**************SHOW********\n";
    for (int i = 0; i < DS.size(); i++)
    {
        DS[i].show();
    }
}
void DSSV::sv_DTB_max()
{
    if (DS.size() <= 0)
    {
        cout << "DS rong";
        return;
    }
    SinhVien temp = DS[0];
    DSSV list = DSSV();
    for (int i = 0; i < DS.size(); i++)
    {
        if (DS[i].getdiemTB() >= DS[0].getdiemTB())
        {
            list.add(DS[i]);
            temp = DS[i];
        }
    }
    list.show();
}
void DSSV::sapxep()
{
    if (DS.size() <= 0)
        return;
    cout << "______sap xep______\n";
    SinhVien temp = DS[0];
    for (int i = 0; i < DS.size(); i++)
    {
        for (int j = i + 1; j < DS.size(); j++)
        {
            if (DS[j].getdiemTB() > DS[i].getdiemTB())
            {
                temp = DS[i];
                DS[i] = DS[j];
                DS[j] = temp;
            }
            else if (DS[j].getdiemTB() == DS[i].getdiemTB())
            {
                if (sosanhTen(DS[i], DS[j]) == 2)
                {
                    temp = DS[i];
                    DS[i] = DS[j];
                    DS[j] = temp;
                }
            }
        }
    }
}
int main()
{
    int n;
    cout << "nhap n:= ";
    cin >> n;
    DSSV danhsach = DSSV();
    // sinh vien
    string name_ = "";
    float diemTB_ = 0;
    int maSV_ = 0;
    for (int i = 0; i < n; i++)
    {
        cout << "sinh vien " << i + 1 << endl;
        cin.ignore();
        cout << "hoten: ";
        getline(cin, name_);
        cout << "maSV: ";
        cin >> maSV_;
        cout << "diemTB: ";
        cin >> diemTB_;
        danhsach.add(SinhVien(maSV_, name_, diemTB_));
    }
    danhsach.show();
    danhsach.sapxep();
    danhsach.show();
}