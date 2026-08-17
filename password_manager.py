from cryptography.fernet import Fernet


def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

write_key()


def load_key():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key



key = load_key() 
fer = Fernet(key)



def view():
    with open('passwords.txt','r') as f:
        for line in f.readlines():
            data = line.rstrip()
            L_user, L_pwd = data.split(": ")
            print("User:", L_user, ", Password:", fer.decrypt(L_pwd.encode()).decode())

def new():
    name = input("Account name: ")
    pwd = input("Password: ")

    with open('passwords.txt','a') as f:
        f.write(name + ": " + fer.encrypt(pwd.encode()).decode() + "\n")

while True:
    mode = input("Would you like to add a new password, view existing ones or quit? [New/View/Quit]: ").lower()

    if mode == 'quit':
        break

    if mode == 'new':
        new()
    elif mode == 'view':
        view()
    else:
        print("Invalid. Please try again.")
        continue