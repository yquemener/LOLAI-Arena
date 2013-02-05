#include <iostream>

using namespace std;


int main ()
{

    cout << "OK" << endl;

    string ans("C");
    string other("C");

    string master;
    cin >> master;
    cerr << "master: " << master << endl;

    while(master != "Q\n"){
        cerr << "nouvelle boucle" << endl;
        ans = other;
        cout << ans << endl;
        cin >> other;
        cin >> master;
    }

    return 0;
}


