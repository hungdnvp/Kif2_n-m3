#include <iostream>
#include<algorithm>
#include<math.h>
using namespace std;

class date
{
private:
    int d;
    int m;
    int yyyy;

public:
    static int sum;
    date(int day, int month, int year)
    {
        sum +=1;
        d = day;
        m = month;
        yyyy = year;
    }
    static int thisIsMagic(int year, int month, int day)
    {
        if (month < 3)
        {
            year--;
            month += 12;
        }
        return 365 * year + year / 4 - year / 100 + year / 400 + (153 * month - 457) / 5 + day - 306;
    }
    // 25-10-2001  ******  30-5-2020
    static int distance_date(date a, date b)
    {
        return abs(thisIsMagic(a.yyyy,a.m,a.d) - thisIsMagic(b.yyyy,b.m,b.d));
    }
};
int date::sum =0;
int main()
{
    date::sum =0;
    date a = date(25,10,2021);
    date b = date(1,1,2021);
    // cout<< date::distance_date(a,b);
    cout<<endl<<a.sum;
    date::sum =0;
    cout<<endl<<a.sum;
    return 0;
}