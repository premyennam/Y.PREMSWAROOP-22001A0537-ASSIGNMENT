str=input('Enter the string: ')
v=0
c=0
s=0
d=0
for i in str:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        v+=1
    elif(i=='0' or i=='1' or i=='2' or i=='3' or i=='4' or i=='5' or i=='6' or i=='7' or i=='8' or i=='9'):
        d+=1    
    elif(i==' ' or i=='!' or i=='@' or i=='#' or i=='$' or i=='%' or i=='^' or i=='&' or i=='*' or i=='(' or i==')' or i=='+' or i=='-' or i=='=' or i=='/' or i=='?' or i=='.' or i==',' or i=='<' or i=='>' or i==':' or i==':' or i=='{' or i=='}' or i=='[' or i==']' or i=='~' or i=='`' or i=='|'):
        s+=1
    else:
        c+=1
print('No.of vowels in the given text :',v)
print('No.of consonants in the given text :',c)
print('No.of speial characters in the given text :',s)
print('No.of digits in the given text :',d)