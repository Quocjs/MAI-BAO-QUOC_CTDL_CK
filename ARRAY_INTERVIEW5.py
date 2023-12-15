def Dudicate(arr, n):
    list = [] #tạo mảng rỗng để chứa các giá trị bị lặp lại
    arr = sorted(arr) #sắp xếp lại mảng
    for i in range(n): #tạo vòng lặp quét cả mảng
        if arr[i] == arr[i+1]: #nếu bị trùng lại thì chắc chắn giá trị tại index và index+1 sẽ giống nhau
            list.append(arr[i]) #gán phần tử bị trùng vào mảng đã tạo
    return list #trả về mảng dùng để chứa giá trị
        
A = [0, 2, 3, 1, 2, 3] 
print(Dudicate(A, 5))

