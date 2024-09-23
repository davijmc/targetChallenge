#include <bits/stdc++.h>

using namespace std;

int main(){
    int n;
    int a = 0, b = 1, c = 0;
    cout << "Digite o n° a ser verificado: ";
    cin >> n;
    while(c < n){
        c = a + b;
        a = b;
        b = c;
    }
    if(c == n){
        cout << n << " pertence a sequencia de Fibonacci" << endl;
    }else{
        cout << n << " nao pertence a sequencia de Fibonacci" << endl;
    }
    return 0;
}