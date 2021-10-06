    # include<iostream>

using namespace std;

class complex{
    int a,b;
    public:
        void setNumber(int r1,int r2){
            a = r1;
            b = r2;
        }
        void printNumber(){
            cout<<"Your Number is "<<a<<" +"<<b<<"i"<<endl;
        }
};

int main()
{   


    return 0;
}