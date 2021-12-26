
#include <iostream>
using namespace std;
#include <bits/stdc++.h>

bool help(char a[],int start, int end){
    
    if(start >=end )
        return true;
    
    if(a[start]!=a[end])
        return false;
   
    bool smallcheck= help(a,start+1,end-1);
        return smallcheck;
}


bool checkPalindrome(char input[]) {
    
 int start =0;
   // int end = sizeof(input)/sizeof(*input)-1;
    int end = strlen(input)-1;
    
    return help(input, start, end) ;
    
}
void dis(char input[]){
        for (int i = strlen(input); i >= 0; i--)
        {
            cout<<input[i];
        }
        
}
int main() {
    char input[50];
    cout<<"Enter Sring \n";
    cin >> input;
    cout<<"Reverse String is \n";
    dis(input);
    cout<<endl;
    if(checkPalindrome(input)) {
        cout << "Pallindrome" << endl;
    }
    else {
        cout << "Not Pallindrome" << endl;
    }
}
