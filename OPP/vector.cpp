#include<iostream>
#include<string>
#include<conio.h>
using namespace std;
class vector3D{
    private:
        double x;
        double y;
        double z;
        
    public:
        vector3D();
        ~vector3D(void);
        vector3D(const double &x0, const double &y0, const double &z0);
        double getX(){return x;};
        double getY(){return y;};
        double getZ(){return z;};
        void setX(const double &x0);
        void setY(const double &y0);
        void setZ(const double &z0);
        void PrintToScreen();
        vector3D operator +(vector3D &v)const;
        vector3D operator -(vector3D &v);
        double operator *(vector3D &)const;
        // nap chong toan tu 1 ngoi
        
};
vector3D::vector3D()
{
    x =0;
    y =0;
    z =0;
}
vector3D:: vector3D(const double &x0, const double &y0, const double &z0)
{
    x=x0;
    y=y0;
    z=z0;
}
vector3D::~vector3D(void)
{

}
void vector3D::setX(const double &x0)
{
    x =x0;
}
void vector3D::setY(const double &y0)
{
    y =y0;
}
void vector3D::setZ(const double &z0)
{
    z =z0;
}
void vector3D:: PrintToScreen()
{
    std::cout<<"vector"<<"("<<x<<","<<y<<","<<z<<")";
}
vector3D vector3D::operator +(vector3D &v) const
{
    vector3D ret_v;
    ret_v.x = this->x + v.x;
    ret_v.y = this->y + v.y;
    ret_v.z = this->z + v.z;
    return ret_v;
}
double vector3D::operator *(vector3D &c)const
{
    return this->x * c.x + this->y * c.y + this->z * c.z;
}
void operator!(vector3D)
{
    cout<<"toan tu ! bi nap chong"<<endl;
}
int main(){
	vector3D vt1,vt2,vt3;
	vt1= vector3D(3,2.2,5.3);
	vt2=vector3D(2,1.5,3.0);
	vt3.setZ(2.4);
	vector3D vt = vt1 + vt2 + vt3;
	vt.PrintToScreen();
    cout<<"\ntich cua hai vector vt1*vt2: "<<vt1*vt2<<endl;
    !vt1;
    getch();
    return 0;
}