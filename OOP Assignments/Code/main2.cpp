# include<iostream>

using namespace std;

class complex{
    int a, b;

public:
    

    complex(int, int); 
    void printNumber()
    {
        cout << "The Number is " << a << "+" << b << "i" << endl;
    }
};

complex ::complex(int x, int y)  //  constructor
{
    a = 0;
    b = 0;
}

int main(){

    // Implicit call
    complex a(4,6);

    // Explicit call
    complex b = complex(7,7);
    
    a.printNumber();
    b.printNumber();

    return 0;
}