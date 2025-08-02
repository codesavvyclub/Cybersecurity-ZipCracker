# 🔓 Zip Password Cracker (Python)

## 📖 Overview

This project demonstrates how to crack password-protected ZIP files using Python. It performs a dictionary-based brute-force attack by trying each password in a given wordlist. The tool supports both standard ZipCrypto and AES-encrypted ZIP files using the `zipfile` and `pyzipper` libraries respectively.

This project is part of the **Cybersecurity learning path** and is intended for **educational purposes only**.

## ✨ Features

- Crack password-protected `.zip` files using a dictionary attack
- Supports both ZipCrypto and AES encryption
- Progress bar with `tqdm` for real-time feedback
- Automatically extracts files upon successful crack
- Handles file path issues and provides useful feedback
- Written in pure Python (cross-platform compatible)

## 🧰 Installation

Clone the repository and install dependencies:

```bash
git clone https://github.com/yourusername/zip-password-cracker.git
cd zip-password-cracker
pip install -r requirements.txt
```

Or manually install:

```bash
pip install pyzipper tqdm
```

## ▶️ Usage

Run the script with:

```bash
python main.py "path/to/target.zip" "path/to/wordlist.txt"
```

### Example:

```bash
python main.py "FilesToCrack/YouCrackedMe.zip" "FilesToCrack/rockyou.txt"
```

Paths with spaces must be enclosed in double quotes.

## 🧪 Testing

Use a simple wordlist file such as:

```
123456
letmein
password
secret
correcthorsebatterystaple
```

Create a test ZIP file with one of those passwords and try to crack it using the script.

## 📚 Documentation

### File Structure

```
zip-password-cracker/
├── main.py             # Main password cracker script
├── README.md           # Project documentation
└── requirements.txt    # Required Python packages
```

### How It Works

1. Loads the ZIP file and the wordlist
2. Tries each password in the wordlist against the ZIP archive
3. If successful, extracts the files to the working directory (or a subfolder)
4. Displays the cracked password

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change or add.

## ⚖️ License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 📞 Contact

**Project Author**: Code Savvy  
**Email**: info@codesavvy.club 
**GitHub**: [https://github.com/codsavvyclub](https://github.com/codesavvyclub)

## 🔗 Project Link

[https://github.com/codesavvyclub/zip-password-cracker](https://github.com/codesavvyclub/zip-password-cracker)

