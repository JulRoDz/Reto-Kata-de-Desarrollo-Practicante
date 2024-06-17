#En el MD5 Hash Generator puse mi nombre completo "Julián Felipe Rodríguez Díaz", el hash generado fue: cf700044d3cbdec4e3f895dc5610f804
S = 7

def process_list(numbers, S):
    def filter_digits(number, S):
        filtered_number = ''.join([digit for digit in str(number) if int(digit) < S])
        return int(filtered_number) if filtered_number else None
    
    filtered_numbers = [filter_digits(num, S) for num in numbers]
    filtered_numbers = [num for num in filtered_numbers if num is not None]
    
    result = filtered_numbers[::-1]
    
    print(result)

numbers_list = input("Ingrese una lista de números separados por comas: ").split(',')
numbers_list = [int(num.strip()) for num in numbers_list]


process_list(numbers_list, S)