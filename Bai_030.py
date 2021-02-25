
# Hãy kiểm tra số nguyên dương n có toàn chữ số lẻ hay không

def Toan_Le(n):
    if n==0:
        return 1
    if (n%10)%2==0:
        return 0
    return Toan_Le(n//10)
n = int(input('Nhập n: '))
if Toan_Le(n)==0:
    print(n,'khong toan le.')
else:
    print(n, 'toan le.')

print('Loc dep trai vai dai')
print('You have my word...')
print('You have my word...')
print("Dao Le Tan Loc")
