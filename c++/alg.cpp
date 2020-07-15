#include <bits/stdc++.h>
using namespace std;

int main(void) {
  int n;
  cin >> n;
  int cnt = 0;
  vector<int> one_case;
  for (int i= 1; i <= n ; i++) {
    one_case.emplace_back(i);
  }

  do {
    for (auto num : one_case) {
      cout << num << " ";
    }
    cout << '\n';
    cnt++;
  } while (next_permutation(one_case.begin(), one_case.end()));
  cout << cnt << endl;
  return 0;

}