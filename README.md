# 🔐 Password Manager

A simple **command-line password manager built with Python** that encrypts stored passwords using **Fernet symmetric encryption** from the `cryptography` library.

The project allows users to add passwords for different accounts and view their saved passwords after they have been encrypted and stored locally.

## ✨ Features

* Add and store passwords for different accounts
* Encrypt passwords before storing them
* Decrypt passwords when viewing saved credentials
* Automatically generate an encryption key
* Store encrypted passwords locally
* Simple command-line interface
* Options to **New**, **View**, or **Quit**

## 🛠️ Technologies Used

* **Python 3**
* **Cryptography**
* **Fernet symmetric encryption**
* File handling

## 📂 Project Structure

```text
Password-Manager/
│
├── password_manager.py
├── key.key
├── passwords.txt
└── README.md
```

> `key.key` and `passwords.txt` are generated/used by the program to store the encryption key and encrypted passwords.

## 🔒 How It Works

### 1. Generate an Encryption Key

The program uses Fernet to generate a unique encryption key:

```python
key = Fernet.generate_key()
```

The key is saved locally in `key.key`.

### 2. Add a Password

When a new password is added, it is encrypted before being written to `passwords.txt`.

```python
fer.encrypt(pwd.encode())
```

This means the actual password isn't stored as plain text in the password file.

### 3. View Passwords

When viewing saved passwords, the program reads the encrypted value and decrypts it using the stored Fernet key.

```python
fer.decrypt(L_pwd.encode()).decode()
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone <your-repository-link>
```

### 2. Navigate to the project directory

```bash
cd Password-Manager
```

### 3. Install the required library

```bash
pip install cryptography
```

### 4. Run the program

```bash
python password_manager.py
```

## 💻 Usage

When the program starts, you'll see:

```text
Would you like to add a new password, view existing ones or quit?
[New/View/Quit]:
```

### Add a password

Choose:

```text
New
```

Then enter the account name and password.

### View saved passwords

Choose:

```text
View
```

The program decrypts and displays the saved passwords.

### Exit

Choose:

```text
Quit
```

to close the program.

## 📚 What I Learned

Through this project, I practiced:

* Working with Python functions
* File handling with `open()`
* Reading and writing files
* Using external Python libraries
* Generating and loading encryption keys
* Encrypting and decrypting data
* Using loops and conditional statements
* Handling user input
* Working with the `Fernet` encryption system


## ⚠️ Security Note

This project was created for **learning and educational purposes**. It should not be used to store real or highly sensitive passwords.

Keep `key.key` private. Anyone who has access to both the encrypted password file and the encryption key may be able to decrypt the stored passwords.

If uploading this project to GitHub, **do not commit your actual `key.key` or `passwords.txt` files**. Add them to `.gitignore` instead.


## 👩‍💻 Author

**Vanshika Batra**

GitHub: [@vanshikabatra36](https://github.com/vanshikabatra36)
