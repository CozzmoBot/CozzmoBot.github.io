/* hi guys */
#include <iostream>
#include <string>
using namespace std;


int main(){
    cout << "Hi\n";
    cout << "This is cpp\n";
//    double myFloatNum = 5.99;    // Floating point number (with decimals)
//    char myLetter = 'D';         // Character
//    string myText = "Hello";     // String (text)
    int myNum = true;       // Number (true or false)
    ++myNum;


    cout << "I am " << myNum << " years old.\n";
    string input;
    cout << "Do you believe me? y/n: "; // Type a number and press enter
    cin >> input; // Get user input from the keyboard
    cout << "You said " << input; // Display the input value

    int x, y;
    int sum;
    cout << "\n\nType a number: ";
    cin >> x;
    cout << "\n\nType another number: ";
    cin >> y;
    if (y > x) {
        cout << y << " is greater than "<< x;
    } else if (x>y) {
        cout << x << " is greater than "<< y;
    } else {
        cout << "\nthe numbers are equal";
    }

    sum = x + y;
    cout << "\nThe sum of the numbers is " << sum;


    int day;
    cout << "\n\nwhat number day is it today?";
    cin >> day;
    switch (day) {
    case 1:
        cout << "\nMonday";
        break;
    case 2:
        cout << "\nTuesday";
        break;
    case 3:
        cout << "\nWednesday";
        break;
    case 4:
        cout << "\nThursday";
        break;
    case 5:
        cout << "\nFriday";
        break;
    case 6:
        cout << "\nSaturday";
        break;
    case 7:
        cout << "\nSunday";
        break;

    default:
        cout << "Looking forward to the Weekend";

}

    //cout << "\nSum is: " << sum;
    //string firstName = "\n\ni like ";
    //string lastName = "ya cut g";
    //string fullName = firstName.append(lastName);
    //fullName[5] = '3';
    //cout << fullName;
    // cout << fullName[0, 1, 2, 3, 4, 5, 6, 7];

    //int sheesh = fullName.size();
    //cout << "\n" << sheesh;
    //bool bruh = true;
    //cout << bruh;
    return 0;



}


