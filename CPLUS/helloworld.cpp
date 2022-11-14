/* hi guys */
#include <iostream>
using namespace std;


int main(){
    cout << "Hi\n";
    cout << "This is cpp\n";
    double myFloatNum = 5.99;    // Floating point number (with decimals)
    char myLetter = 'D';         // Character
    string myText = "Hello";     // String (text)
    bool const myBoolean = true;       // Boolean (true or false)


    cout << "I am " << myBoolean << " years old.\n";
    string input;
    cout << "Do you believe me? y/n: "; // Type a number and press enter
    cin >> input; // Get user input from the keyboard
    cout << "You said " << input; // Display the input value

    int x, y;
    int sum;
    cout << "\n\nType a number: ";
    cin >> x;
    cout << "\nType another number: ";
    cin >> y;
    sum = x + y;
    cout << "\nSum is: " << sum;
    return 0;


}


