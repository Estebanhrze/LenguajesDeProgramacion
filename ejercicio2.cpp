#include <iostream>
#include <cstdlib>
#include <ctime>
using namespace std;

int main() {
    srand(time(0));
    int pares = 0, impares = 0;
    for (int i = 0; i < 500; i++) {
        int num = rand() % 51 + 50;
        if (num % 2 == 0) pares++;
        else impares++;
    }
    cout << pares << endl;
    cout << impares << endl;
    return 0;
}
