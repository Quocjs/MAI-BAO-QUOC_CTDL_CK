def CheckPalindrome(a): #Hàm kiểm tra Polidrome
    def Palindrome(a): #Kiểm tra chuỗi nghịch đảo có polidrome hay không
        return a == a[::-1] #Kiểm tra đồng thời chuỗi ban đầu với chuỗi đảo
    
    if not Palindrome(a): #Nếu kiểm tra chuổi đảo sai, nghĩa là hàm kiểm tra bên trên không đúng về logic
        return False #trả về False
    return True #trả về True


string = "madam" #chuỗi kiểm tra 
print(CheckPalindrome(string)) #in ra kết quả xem xét thử đúng hay sai

string1 = "radar" #chuỗi kiểm tra
print(CheckPalindrome(string1)) #in ra kết quả xem xét thử đúng hay sai

