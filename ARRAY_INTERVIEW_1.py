def Reverse_Array(arr, n):
    reverse_array = arr[::-1] #đảo ngược toàn bộ thành phần của arr, với step là -1
    return reverse_array #trả về array bị đảo ngược

A = [1, 2, 3, 4, 5] #array truyền vào
print(Reverse_Array(A, 5)) #in ra hàm bị đảo ngược

