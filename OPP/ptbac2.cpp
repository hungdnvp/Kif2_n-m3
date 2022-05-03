#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
using namespace std;
class pt_2
{
    private:
        float a,b,c;
    public:
        pt_2(float a=0,float b=0,float c=0)
        {this->a = a;this->b=b;this->c =c;}
        void set_a(float x) {a =x;}
        void set_b(float x) {b =x;}
        void set_c(float x) {c =x;}
        void tim_nghiem()
        {

        }
        float get_a(){ return a;}
};
// struct cmp1
// {
//     bool operator()(Nhanvien &a,Nhanvien &b)
//     {
//         return a.operator>>(b);
//     }
// };
int main()
{
    vector<pt_2> pt;
    pt_2 pt0 = pt_2(5,0,0);
    pt_2 pt1 = pt_2(2,3,1);
    pt_2 pt2 = pt_2(5,6,3);
    pt_2 pt3 = pt_2(12,-2,8);
    pt.push_back(pt0);
    pt.push_back(pt1);
    pt.push_back(pt2);
    pt.push_back(pt3);
    find(pt.begin(),pt.end(),pt0.get_a());
}