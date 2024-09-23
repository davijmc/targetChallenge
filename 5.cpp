#include <bits/stdc++.h>

using namespace std;

int main(){
    string s, rs;
    cout << "Digite a string: ";
    cin >> s;
    int n = s.size();
    rs.resize(n);
    for(int i=0; i<n; i++){
        rs[i] = s[n-i-1];
    }
    cout << rs << endl;
    return 0;
}