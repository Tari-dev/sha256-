import hashlib

plaintext =  input("imput your values : ")
#gives the address and giving the hexadecimal value
hashObj = hashlib.sha256(plaintext.encode())

digestObj =  hashObj.hexdigest()

print(digestObj)
