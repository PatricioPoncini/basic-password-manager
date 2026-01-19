menu = ""
shift = 2  # TODO: Esto puede pasar a una const o un .env por ejemplo

def encrypt(data, shift):
    encrypted = ""
    for i in range(len(data)):
        char = data[i]
        if char.isupper():
            encrypted += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            encrypted += chr((ord(char) + shift - 97) % 26 + 97)
        elif char.isdigit():
            number = (int(char) + shift) % 10
            encrypted += str(number)
        else :
            encrypted += char
    return encrypted

def decrypt(data, shift):
    decrypted = ""
    for i in range(len(data)):
        char = data[i]
        if char.isupper():
            decrypted += chr((ord(char) - shift - 65) % 26 + 65)
        elif char.islower():
            decrypted += chr((ord(char) - shift - 97) % 26 + 97)
        elif char.isdigit():
            number = (int(char) - shift) % 10
            decrypted += str(number)
        else:
            decrypted += char
    return decrypted


while menu != "1" or menu != "2":
    menu = input("Would you like to save a new password or view your old ones?"
                 "\n1. New password"
                 "\n2. View passwords"
                 "\n3. Exit"
                 "\n")
    if menu == "1":
        softwareName = input("Enter the name of the software you are using: ")
        username = input("Enter the username for this software: ")
        password = input("Enter your password: ")
        file = open("securePasswordData.txt", "a")
        file.write(encrypt(softwareName,shift)+";|"+encrypt(username,shift)+";|"+encrypt(password,shift)+"\n") # TODO: esto seguro se puede mejorar, esta linea del ;|
        file.close()
    if menu == "2":
        file = open("securePasswordData.txt", "r")
        print("Software\tUsername\tPassword")
        for line in file:
            data = line.split(";|")
            print(decrypt(data[0], shift)+"\t\t"+decrypt(data[1], shift)+"\t\t"+decrypt(data[2], shift)) # TODO: esto seguro se puede mejorar, esta linea del ;|
    if menu == "3":
        exit()
