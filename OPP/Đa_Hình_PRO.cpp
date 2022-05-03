#include <iostream>
#include <string>
#include <vector>
#include<algorithm>
using namespace std;
/*
    hai lớp book và tape kế thừa lớp publication để sử dụng đa hình
    khi con trỏ kiểu publication trỏ đến được cả 2 đối tượng trên
*/
/*
2 phuong thuc getdata() va putdata() để là virtual để mảng con trỏ kiểu publication
khi trỏ các đối tượng kiểu book và tape đều gọi được đến getdata() và putdata() của
lớp dẫn xuất ấy chứ không phải là của lớp cha- publication
*/
class publication  // nha xuat ban
{
protected:
    string ten;
    float gia;

public:
    virtual void getdata()
    {
        cout << "enter ten: ";
        fflush(stdin);
        getline(cin, ten);
        cout << "enter gia: ";
        cin >> gia;
    }
    float get_gia()
    {
        return gia;
    }
    virtual void putdata()
    {
        cout << "ten: " << ten << "\n";
        cout << "gia: " << gia << "\n";
    }
};

class book : public publication
{
private:
    int sotrang;

public:
    void getdata()
    {
        publication::getdata();
        cout << "enter so trang: ";
        cin >> sotrang;
    }
    void putdata()
    {
        publication::putdata();
        cout << "so trang: " << sotrang << "\n";
    }
};

class tape : public publication
{
private:
    float a_playing_time;

public:
    void getdata()
    {
        publication::getdata();
        cout << "enter a_playing_time: ";
        cin >> a_playing_time;
    }
    void putdata()
    {
        publication::putdata();
        cout << "a_playing_time: " << a_playing_time << "\n";
    }
};


// dinh nghia kieu sap xep
struct cmp
{
    bool operator()(publication* a,publication* b)
    {
        return a->get_gia()<b->get_gia();
    }
};
int main()
{
    vector<publication*>arr;
    int i = 0;
    char choice;
    do
    {
        cout << "nhap vao thong tin book or tape(b/t)\n";
        cin >> choice;
        if (choice == 'b')
        {
            arr.push_back(new book());
        }
        else
        {
            arr.push_back(new tape());
        }
        arr[i]->getdata();
        i++;
        cout << "tiep tuc nhap [y/n]\n";
        cin >> choice;
    } while (choice == 'y');
    // sap xep theo gia tu nho den lon
    sort(arr.begin(),arr.end(),cmp());
    for (int j = 0; j < i; j++)
    {
        arr[j]->putdata();
    }

    return 0;
}