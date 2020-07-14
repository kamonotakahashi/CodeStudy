#include <iostream>
using namespace std;
int pn(int n) {
    int p[n];
    int cnt = 0, j = 0, hit = 0;
    bool cb = true;
    for (int i = 0; i < sizeof(p)/sizeof(p[0]); i++) {
        p[i] = -1;
        j = 0;
        if(i < 2) {
            continue;
        }
        while (j < cnt) {
            if(i % p[j++] == 0){
                cb = false;
                break;
            }
        }
        if (cb == 1) {
            p[cnt++] = i;
        }
        cb = true;
    }
    for (int i = 0; i < sizeof(p)/sizeof(p[0]); i++) {
        if(p[i] == -1) {
            break;
        }
        if (hit!=0 && hit%10==0) {
            cout<<endl;
        }
        cout<<p[hit++]<<" ";
    }
    cout<<endl;
    return n;
}
int main(void) {
    int n;
    cout<<"探したいN値を入力してください。Nの中から素数を見つけます。>";
    cin>>n;
    pn(n);
    return 0;
}