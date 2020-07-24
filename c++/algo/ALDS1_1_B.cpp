#include <iostream>
using namespace std;
void gcd(int v, int A[]) {
  int cnt = 0;
  for (int i = 1; i <= v; i++) {
      if (v % i == 0) {
        A[cnt++] = i;
      }
  }
}
int main (void) {
    int x, y;
    cin >> x >> y;
    int Xl[1000];
    int Yl[1000];
    int ans[1000];
    for(int i = 0; i < sizeof(Xl)/sizeof(Xl[0]); i++) Xl[i] = -1;
    for(int i = 0; i < sizeof(Yl)/sizeof(Yl[0]); i++) Yl[i] = -1;
    for(int i = 0; i < sizeof(ans)/sizeof(ans[0]); i++) ans[i] = -1;
    gcd(x, Xl);
    gcd(y, Yl);
    int cnt = 0;
    for(int i=0;i < sizeof(Xl)/sizeof(Xl[0]); i++) {
      if (Xl[i] == -1) break;
      for(int j=0;j < sizeof(Yl)/sizeof(Yl[0]); j++) {
        if (Yl[j] == -1) break;
        if(Xl[i] == Yl[j]) {
          ans[cnt] = Xl[i];
          cnt++;
        }
      }
    }
    for(int i=0;i < sizeof(ans)/sizeof(ans[0]); i++) {
      if(ans[i] == -1) {
        cout << ans[i - 1] << endl;
        break;
      }
    }
    return 0;
}