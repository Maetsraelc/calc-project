def get_number(prompt):
	while True:
		try:
			return float(input(prompt))
			except ValueError:
				print ("Ошибка: введите число")

def add(a, b):
	return a + b

def substract(a, b):
	return a - b

def multiply(a, b):
	return a * b

def divide(a, b):
	if b != 0:
	return a / b
	else:
	return "Ошибка"

def power(a, b):
	return a ** b

def square_root(a):
	return a ** 0.5
print ("Простой калькулятор")
print ("Доступные операции: +, -, *, /, ^, sqrt")
