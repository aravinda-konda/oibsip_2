weight=int(input('Enter Weight (in kilograms)  : '))
height=int(input('Enter Height (in centimetres) : '))

height_in_metres=height/100
bmi=weight/(height_in_metres**2)

if bmi<18.5:
    print('Hey,You are Underweight')
elif bmi>=18.5 and bmi<25:
    print('Hey,You are Normal Weight ')
elif bmi<=25 and bmi>30:
    print('Hey,You are Overweight')
else:
    print('You are Obese')
    
print('Maintaining Normal Weight reduces the risk of Health Problems\n')