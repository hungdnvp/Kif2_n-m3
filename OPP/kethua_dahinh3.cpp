#include<iostream>
using namespace std;

class Sinhvien
{

};
class SV_nganhdien: virtual public Sinhvien
{

};
class SV_nganhco: virtual public Sinhvien
{

};
class Cuu_SV: public SV_nganhco,SV_nganhdien
{

};

int main()
{
    
}