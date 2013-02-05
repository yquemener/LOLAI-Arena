#include <iostream>

using namespace std;


int main ()
{

    cout << "OK" << endl;

    string ans("C\n");
    string other("C\n");

    string master;
    cin >> master;
    cout << "master: " << master << endl;

    while(master != "Q\n"){
        cout << "nouvelle boucle" << endl;
        ans = other;
        cout << ans << endl;
        cin >> other;
        cin >> master;
    }

    return 0;
}


