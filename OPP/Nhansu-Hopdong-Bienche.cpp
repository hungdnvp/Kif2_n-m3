#include <iostream>
#include <string>
#include <vector>
#include<algorithm>
using namespace std;

class NhanSu
{
protected:
    string ma_nhan_su;
    string ho_ten;
    string gioi_tinh;
public:
    virtual void input()
    {
        cout<<"enter ma_nhan_su: ";cin>>ma_nhan_su;
        cin.ignore(300,'\n');
        cout<<"enter ho_ten: ";getline(cin,ho_ten);
        cout<<"enter gioi_tinh: ";cin>>gioi_tinh;
    }
    virtual void output()
    {
        cout<<"ma_nha_su: "<<ma_nhan_su<<" ; ho_ten: "<<ho_ten<<" ; gioi_tinh: "<<gioi_tinh<<endl;
    }
    string get_ID(){return ma_nhan_su;}
};

class HopDong:public NhanSu
{
private:
    string loai_hop_dong;
public:
    void input()
    {
        NhanSu::input();
        cout<<"loai_hop_dong (ngan_han OR dai_han): ";cin>>loai_hop_dong;
    }
    void output()
    {
        NhanSu::output();
        cout<<"loai_hop_dong: "<<loai_hop_dong<<endl;
    }
};

class BienChe:public NhanSu
{
private:
    int nam_bien_che;
public:
    static int count;
    BienChe(){count++;};
    void input()
    {
        NhanSu::input();
        cout<<"nam_bien_che: ";cin>>nam_bien_che;
    }
    void output()
    {
        NhanSu::output();
        cout<<"nam_bien_che: "<<nam_bien_che<<endl;
    }
};
int BienChe::count=0;
int main()
{
    vector<NhanSu*>nhansu;
    int i = 0;
    string find;
    char choice;
    do
    {
        cout << "nhap vao hop dong(1) OR bien che(#1)\n";
        cin >> choice;
        cin.ignore(3200,'\n');
        if (choice == '1')
        {
            nhansu.push_back(new HopDong());
        }
        else
        {
            nhansu.push_back(new BienChe());
        }
        nhansu[i]->input();
        i++;
        cout << "tiep tuc nhap [y/n]\n";
        cin >> choice;
        cin.ignore(3200,'\n');
    } while (choice == 'y');
    // SHOW
    system("pause");
    for(int i=0;i<nhansu.size();i++)
    {
        nhansu[i]->output();
    }

    // tim kiem
    system("pause");
    system("cls");
    bool detect = false;
    cout<<"nhap vao ma nhan su tim kiem: ";cin>>find;
    for(int i=0;i<nhansu.size();i++)
    {
        if(nhansu[i]->get_ID() == find)
        {
            nhansu[i]->output();
            detect = true;
            break;
        }
    }
    if(!detect) cout<<"khong tim thay nhan su co ma nhap vao\n";
    system("pause");
    system("cls");
    // dem so luong nhan su
    cout<<"so luong bien che trong nha may: "<<BienChe::count;
    return 0;
}
