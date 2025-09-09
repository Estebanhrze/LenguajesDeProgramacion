#include <iostream>
#include <vector>
#include <string>
using namespace std;

int main() {
    vector<string> sucursales(25);
    vector<int> ventas(25);
    int suma = 0;
    for (int i = 0; i < 25; i++) {
        sucursales[i] = "Sucursal_" + to_string(i + 1);
        cin >> ventas[i];
        suma += ventas[i];
    }
    double promedio = (double)suma / 25;
    cout << promedio << endl;
    for (int i = 0; i < 25; i++) {
        if (ventas[i] > promedio) {
            cout << sucursales[i] << " " << ventas[i] << endl;
        }
    }
    return 0;
}
