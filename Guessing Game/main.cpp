#include <iostream>

using namespace std;

int main()
{

 int guess;
 int number;
 int guesslimit;
 string input;
 guesslimit = 0;
 number = 7;

 cout << "------Type out one option  to start the game---- :)"<< endl;
 cout << "      1.Ready      " << endl;
 cout << "      2.Rules      " << endl;
 cout << "Enter your option: ";
 cin >> input;

 if (input == "2"){
    cout << "" << endl;
    cout << "The rules are simple" << endl;
    cout << "" << endl;
    cout << " #  The computer Guesses a number between (1 -10)" << endl;
    cout << " #  You have to guess the number within three chances" << endl;
    cout << "             -----\\\\\\\\\\\\\\\\\-----        " << endl;
 }


 while(guesslimit < 3 && guess != number && (input == "1" || input == "2")){
    if (guess != number){
        cout << "" <<endl;
        cout << "Enter your guess: ";
        cin >> guess;
        guesslimit++;
        }
 }
 if (guess == number && guesslimit <= 3){
    cout << "" << endl;
     cout <<"---------You Won---------";
 }
 else if (guesslimit >= 3 && guess != number){
     cout << "" << endl;
     cout << "----------You are out of chances----------" ;
 }

    return 0;
}
