x = 10 
y = 20
z = 30

#Using 'and' operator
if x < y and y < z:
    print("x is less than y and y is less than z.")#True
    
#Using 'or' operator
if x < y or y > z:
    print("Either x is less than y or z is greater than z.")#true
    
#Using the 'not' operator
if not (x > y):
    print("x is not greater than y.")#true