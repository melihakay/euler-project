def generate_pandigital(x):
    i = 1
    number = ""
    while True:
        multiple = x * i 
        str_mul = str(multiple)
        number = number + str_mul
        
        if not len(set(number)) == len(number):
            return "Repeated number"

        if len(number) == 9:
            return int(number)
        
        elif len(number) > 9:
            return "Length exceeds"
        i += 1
        
for i in range(100000000, 1, -1):
    result = generate_pandigital(i)
    if isinstance(result, int):
        print(i, result)
