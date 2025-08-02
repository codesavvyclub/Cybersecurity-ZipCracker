# 🔓 ZipCracker - Python Zip Password Cracker

This project demonstrates how to crack password-protected `.zip` files using Python. It uses a brute-force dictionary attack by testing a list of potential passwords (wordlist) against the ZIP archive.

Supports both:
- Standard ZipCrypto-encrypted ZIP files (Python's built-in `zipfile`)
- AES-encrypted ZIP files (via `pyzipper`)

---

## 🚀 Features

- ✅ Supports ZipCrypto and AES encryption
- ✅ Brute-force dictionary attack using a wordlist
- ✅ Progress bar with `tqdm`
- ✅ Automatic password detection and file extraction
- ✅ Easy to configure paths and output directories

---

## 🛠 Requirements

- Python 3.6+
- Install dependencies:

```bash
pip install pyzipper tqdm
