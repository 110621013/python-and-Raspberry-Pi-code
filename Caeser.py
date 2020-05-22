key_number = input('要啥金鑰?(大寫英文)')
key_length = len(key_number)

plaintext = input('要加密啥字串?(任意)')


def Vigenere(text, key, mode):
    if mode == 0:  # decrypt
        key = -key
    elif mode == 1:  # encrypt
        key = key
    else:
        print("mode: 0 = decrypt, 1 = encrypt")
        
    if text.isalpha():  #檢測是否都是字母
        num = ord(text)   
        numm = ord(text)
        #print (num,key)
        num += key
        
        if numm <= ord('Z') and numm >= ord('A') and num > ord('Z') :
            num -= 26
        elif numm <= ord('Z') and numm >= ord('A') and num < ord('A'):
            num += 26
        
        if numm <= ord('z') and numm >= ord('a') and num > ord('z') :
            num -= 26
        elif numm <= ord('z') and numm >= ord('a') and num < ord('a'):
            num += 26
        
        new_text = chr(num)
        
    else:
        new_text = text
        

    return new_text

def conn(s):
    if s.isalpha():
        con = 0
    else :
        con = 1
    return con



print(plaintext)

translated = "" #令其為字串
counter = 0
con = 0
for s in plaintext: #字串後面.upper()回傳大寫字串
    current_key = ord(key_number[counter % key_length])-65
    con = conn(s)
    counter = counter+1-con
    translated += Vigenere(s, current_key, 1)

print(translated)

encode = ""
counter = 0
con = 0
for s in translated: #字串後面.upper()回傳大寫字串
    current_key = ord(key_number[counter % key_length])-65
    con = conn(s)
    counter = counter+1-con
    encode += Vigenere(s, current_key, 0)

print(encode)