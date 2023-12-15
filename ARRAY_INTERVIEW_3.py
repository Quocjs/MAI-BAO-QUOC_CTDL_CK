def Reverse_Number(a):
    if type(a) != int: #kiểm tra a có phải là số hay không, vì lỡ đâu người dùng nhập a = "so1"
        return False #nếu không thì trả về False
    else: #nếu True
        return int(str(a)[::-1]) #ép về string để dùng [::-1] để đảo, sau đó ép chuỗi về int

number = 12345
print(Reverse_Number(number))


