#include<iostream>
#include<string>
using namespace std;
class bank
{
    private:
        string account_name;
        float account_number;
    public:
        //chuyển tiền vào tài khoản
        bank(string name = "noName",float number =0)
        {
            account_name =name;
            account_number =number;
        }
        void Deposit()
        {
            float x =0;
            cout<<"so tien chuyen vao: ";cin>>x;
            account_number += x;
            cout<<"nap tien thanh cong\n";
        }
        void Deposit(float x)
        {
            account_number +=x;
        }
        //rút tiền
        void Withdraw()
        {
            float x =0;
            cout<<"so tien muon rut: ";cin>>x;
            if(x>account_number) cout<<"tai khoan khong du tien\n";
            else{
                account_number -=x;
                cout<<"rut tien thanh cong\n";
            }
        }
        void Withdraw(float x)
        {
            if(x<= account_number) account_number -=x;
            else return;
        }
        // hiển thị tên và số dư
        void Display()
        {
            cout<<"account name: "<<account_name<<endl;
            cout<<"account number: "<<account_number<<endl;
        }
};

int main()
{
    bank doquanghung = bank("doquanghung");
    doquanghung.Display();


    return 0;
}