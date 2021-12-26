                                            # #To display word with the longest length
str1=input("Enter any string:")
list1=str1.split()
m=0
word=0
print(list1)
for i in range(len(list1)):
    if m<len(list1[i]):
        m=len(list1[i])
        word=i
print("Word with longest length is:",len(list1[word]))


                                            # #To count of Occurrence of word in the string:
str1=input("Enter the string : ")
char=input("Enter character : ")
counter=0
for i in range(len(str1)):
    if(char==str1[i]):
        counter+=1
print("Character",char,"is present",counter,"times in string")


                                            # # Check whether given string is palindrome:
string1=input("Enter the string : ")
string2=string1[::-1]
if(string1==string2):
    print("Given string is palindrome")
else:
    print("Sorry, Given string is not palindrome")


                                            # Display index of first appearance of the substring :-
string=input("Enter the string : ")
substring=input("Enter a particular part of the string :")
index=0
m=0
for i in range(len(string)):
    if(substring[m]==string[i]):
        m=m+1
        if(m==len(substring)):
            index=i-(len(substring)-1)
            break
        else:
            m=0
            print(substring,"is at index",index+1,"in the given string")


                                            # Count occurrence of each word in a given string:-
str =input("Enter Any String : ")
str1 = str.split()         
str2 = []
    
for i in str1:
    if i not in str2:
        str2.append(i) 
              
for j in range(0, len(str2)):
    print('Frequency of', str2[j], 'is :', str.count(str2[j])) 


