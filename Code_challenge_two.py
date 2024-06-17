#En el MD5 Hash Generator puse mi nombre completo "Julián Felipe Rodríguez Díaz", el hash generado fue: cf700044d3cbdec4e3f895dc5610f804
S = 7

def sorted_squares(nums, S):
    max_square = int(str(S) * 2)
    print(max_square)
    squares = [num * num for num in nums if num * num <= max_square]

    n = len(squares)
    left, right = 0, n - 1
    result = [0] * n
    position = n - 1

    while left <= right:
        if squares[left] > squares[right]:
            result[position] = squares[left]
            left += 1
        else:
            result[position] = squares[right]
            right -= 1
        position -= 1

    return result

numbers_list = input("Ingrese una lista de números separados por comas: ").split(',')
numbers_list = [int(num.strip()) for num in numbers_list]


result = sorted_squares(numbers_list, S)
print(result)