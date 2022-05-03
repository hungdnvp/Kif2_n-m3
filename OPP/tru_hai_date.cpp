#include<iostream>
using namespace std;

class Time
{
	private:
		int gio,phut,giay;
	public:
		Time(int a,int b,int c)
		{
			gio = (a>=0)? a : 0;
			phut = (b>=0)?b:0;
			giay = (c>=0)?c:0;
			
			if(giay >=60){
				phut += giay / 60;
				giay = giay%60;
			}
			if(phut>=60)
			{
				gio += phut / 60;
				phut = phut %60;
			}
		}
		int operator-(const Time& t)
		{
			return (gio - t.gio)*3600 + (phut - t.phut)*60 + (giay-t.giay);
		}
		
		friend ostream& operator<<(ostream&,const Time&);
		
};
ostream& operator<<(ostream& os,const Time& t)
{
	os<<t.gio<<":"<<t.phut<<":"<<t.giay<<endl;
	return os;
}
int main()
{
	Time t1 = Time(2,30,23);
	Time t2 = Time(0,1,45);
	cout<<t1;
	cout<<t1-t2;
	return 0;
}
