#include <bits/stdc++.h>

int main(void) {
  int N = 8;
  int num[] = {31,15,11,20,13,8,5,9};
  std::vector<int> A;

    std::cout << (1 << N / 2) << "#" << std::endl;

    for (int bit = 0; bit < (1 << N / 2); bit++) {
        int sum = 0;
        for (int i = 0; i < (N / 2); i++) {
            int mask = 1 << i;
            if (bit & mask) {
                sum += num[i];
            }
        }
        A.push_back(sum);
    }

  for (int x : A) {
    std::cout << x << std::endl;
  }

}