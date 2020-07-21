#include <iostream>
using namespace std;

void trace(int A[], int N) {
  for (int i = 0; i < N; i++) {
    cout << A[i] << ' ';
  }
  cout << endl;
}

void sort(int A[], int N) {
  int v, j;
  for (int i = 1; i < N; i++) {
    v = A[i];
    j = i - 1;
    while(j >= 0 && A[j] > v) {
      A[j + 1] = A[j];
      j--;
    }
    A[j + 1] = v;
    trace(A, N);
  }
}

int main(void) {

  int A[100];
  int N;
  cin >> N;
  for (int i; i < N; i++) cin >> A[i];

  trace(A, N);

  sort(A, N);

  return 0;
}