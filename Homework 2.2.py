print("Введите 5-значнное число:")
user_input = input()
int(user_input)
number1 = int(user_input)
number2 =(number1 % 10)
number3 = (number1 % 100 // 10)
number4 = (number1 % 1000 // 100)
number5 = (number1 % 10000 // 1000)
number6 = (number1 // 10000) #я тестил с %10000 // 10000,но пришел к выводу,что получится число деленное на 1 :)
print(number2,number3,number4,number5,number6)