# include<iostream>

using namespace std;


class complex{
    int a,b;
    public:
    // constructor is a special function
    // It is automatically involed when an object is created
    
    complex(void); // constructor declaration
    void printNumber(){
        cout<<"The Number is "<< a <<"+"<<b<<"i"<<endl;
    }

};

complex :: complex(void){
    a=0;
    b=0;
}



int main(){
    complex c1,c2,c3;
    c1.printNumber();
    c2.printNumber();
    c3.printNumber();
    return 0;
}
/*
//-->  charachteristics 

// 1.  should be a public function
// 2.  should be a void function
// 3.  should have no return type
// 4.  should have no parameters  in default constructor
// 5.  cannot reffer to the address 

*/


