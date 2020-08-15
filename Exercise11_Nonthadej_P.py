number = int(input('Enter a number:'))
text = ""
for i in range(number):
    text =(2*i+1)*"*"
    print((number-i-1)*" "+text)