#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<int> valores(10);
    int suma = 0;
    for (int i = 0; i < 10; i++) {
        cin >> valores[i];
        suma += valores[i];
    }
    double promedio = (double)suma / 10;
    cout << suma << endl;
    cout << promedio << endl;
    return 0;
}
