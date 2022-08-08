list1=list(input('enter List: '))
String1=[]
String2=[]
for i in list1:
    String1.append(i)
    String2.append(i)
String1.reverse()
if String1 == String2:
        print('list is palindrome')
else:
        print('list is not palindrome')
