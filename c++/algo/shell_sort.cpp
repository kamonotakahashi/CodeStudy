#include <iostream>
using namespace std;

void trace(int A[], int N) {
  for (int i = 0; i < N; i++) {
    cout << A[i] << ' ';
  }
  cout << endl;
}

void sort(int A[], int N, int G) {
  int v, j;
  for (int i = G; i < N - 1; i++) {
    v = A[i];
    j = i - G;
    while ( j >= 0 && A[j] < v) {
      A[j+G] = A[j];
      j = j - G;
    }
    A[j+G] = v;
  }
}

int main(void) {

  int A[100];
  int N;
  cin >> N;
  for (int i; i < N; i++) scanf("%d", &A[i]);

  int G[] = {N-1, 1};

  trace(A, N);

  for ( int i = 0; i < sizeof(G)/sizeof(G[0]); i++) {
    sort(A, N, G[i]);
    trace(A, N);
  }

}