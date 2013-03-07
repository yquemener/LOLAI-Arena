#include <iostream>

using namespace std;


int main ()
{

    cout << "OK" << endl;

    string ans("C");
    string other("C");

    string master;
    cin >> master;
    
    while(master != "Q"){
        ans = other;
        cout << ans << endl;
        cin >> other;
        cin >> master;
    }

    return 0;
}


