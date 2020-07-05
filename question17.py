try:
  input_1 = int(input('Enter first number: '))
  input_2 = int(input('Enter second number: '))

  operator = input('Enter operator (+,-,*,/) : ')

  if operator == '+':
    print("The sum of",input_1,"and",input_2,"is",input_1+input_2)
  elif operator == '-':
    print("The difference of",input_1,"and",input_2,"is",input_1-input_2)
  elif operator == '*':
    print("The product of",input_1,"and",input_2,"is",input_1*input_2)
  elif operator == '/':
    try:
        print("The division of",input_1,"and",input_2,"is",input_1/input_2)
    except ZeroDivisionError:
        print('Number cannot be divided by 0')
  else:
    print("Input number or operator is not valid")

except ValueError:
  print("Enter your input")