import random

def is_binary(path):
    bytes = open(path, 'rb').read(1024)
    textchars = bytearray({7,8,9,10,12,13,27} | set(range(0x20, 0x100)) - {0x7f})
    return bool(bytes.translate(None, textchars))

def encrypt(text):
    encrypted = ""
    key = random.randint(1000,9999)
    for i in text:
        letter_code = ord(i)
        new_letter_code = letter_code*key
        new_letter = chr(new_letter_code)
        
        encrypted += new_letter
    return encrypted+chr(key)
    
def decrypt(text):
    decrypted = ""
    key = ord(text[len(text)-1])
    text = text[:len(text)-1]
    for i in text:
        letter_code = ord(i)
        decrypted_letter_code = int(letter_code/key)
        decrypted_letter = chr(decrypted_letter_code)
        
        decrypted += decrypted_letter
    return decrypted

def encrypt_file(path):
    
    if is_binary(path):
        print("This type of file can not be encrypted!")
    else:
        print("\n###########\n\nEncrypting your file...\n")
        f = open(path, "r")
        encrypted = encrypt(f.read())
        f.close()
        with open(f'{path}.fenc',"w") as f:
            f.write(encrypted)
            
        print("Your file is encrypted successfully!")
    
def decrypt_file(path):
    if path.endswith('.fenc') == False:
        print("This file is not encrypted by fenc!")
        return
    if is_binary(path):
        print("This type of file can not be decrypted!")
    else:
        print("\n###########\n\nEncrypting your file...\n")
        f = open(path, "r")
        decrypted = decrypt(f.read())
        f.close()
        with open(path[:len(path)-5],"w") as f:
            f.write(decrypted)
        
        print("Your file is decrypted successfully!")

if __name__ == "__main__":
    choice = input("What would you like to do?\n1. Encrypt a message\n2. Decrypt a message\n3. Encrypt a file\n4. Decrypt a file\n0. exit\nEnter your choice:")
    if choice == "1":
        txt = input("\n###########\n\nEnter your text:")
        print(f"\n###########\n\nEncryted text: {encrypt(txt)}\n\n###########\n")
    elif choice == "2":
        txt = input("\n###########\n\nEnter your text:")
        print(f"\n###########\n\nDecryted text: {decrypt(txt)}\n\n###########\n")
    elif choice == "3":
        path = input("\n###########\n\nEnter path of the file:")
        encrypt_file(path)
        
    elif choice == "4":
        path = input("\n###########\n\nEnter path of the file:")
        decrypt_file(path)
    elif choice == "0":
        pass
    else:
        print("Invalid choice!")
