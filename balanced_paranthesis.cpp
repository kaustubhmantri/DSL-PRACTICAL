#include<iostream>
#include<stack>
using namespace std;
bool isBalanced(string expression) 
{
    stack <char> s1;

    for (int i = 0; expression[i] != '\0'; i++)
    {
        if(expression[i] == '{' || expression[i]=='[' || expression[i] == '(') s1.push(expression[i]);

        if(s1.empty() && (expression[i] ==')' || expression[i] == '}')) return false;

        if(expression[i] == '}'){

            if(s1.top() == '{'){
                s1.pop();
            }
            else return false;
        }
        if(expression[i] == ']'){

            if(s1.top() == '['){
                s1.pop();
            }
            else return false;
        }
        if(expression[i] == ')'){

            if(s1.top() == '('){
                s1.pop();
            }
            else return false;
        }
    
    }
    if(s1.empty()) return true;
    else return false;
}
int main(){

    string inp;
    cin>>inp;

    cout<<((isBalanced(inp)) ? "True" : "False");

    

return 0;
}