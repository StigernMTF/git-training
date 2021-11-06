import math
while (True):
	a=input('Что нужно сделать с числом? (+, -, *, /, %, //, округлить ч1, округлить ч2):')
	b=float(input('Первое число:'))
	c=float(input('Второе число:'))
	

	if a=='+':
		s= b + c
		print('Результат:' + str(s))
	elif a=='-':
		m=b - c
		print('Результат:' + str(m))
	elif a=='*':
		um=b*c
		print('Результат:' + str(um))
	elif a=='/':
		try:
			de=b/c 
		except ZeroDivisionError:
			print('Ошибка. На ноль делить нельзя')
		else:
			print('Результат:' + str(de))
	elif a=='%':
		ost=b%c 
		print(f'Результат:{str(ost)}')
	elif a=='//':
		cel=b//c
		print('Результат:' + str(cel))
	elif a=='округлить ч1':
		okr=round(b)
		print('Результат:' + str(okr))
	elif a=='округлить ч2':
		okr2=round(c)
		print('Результат:' + str(okr2))
	else:
		print('Выбран несуществующий вариант действий.')