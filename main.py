import pyzipper
import sys
from tqdm import tqdm
import os

# Handle arguments
if len(sys.argv) < 3:
    print("Usage: python main.py <zipfile> <wordlist>")
    sys.exit(1)

zip_path = sys.argv[1]
wordlist_path = sys.argv[2]

# Define output path to Desktop
desktop = os.path.join(os.path.expanduser("~"), "OneDrive\Desktop")
output_dir = os.path.join(desktop, "CrackedOutput")
os.makedirs(output_dir, exist_ok=True)

# Load wordlist
with open(wordlist_path, "rb") as f:
    words = list(f)
    print("[*] Total passwords to test:", len(words))

# Attempt to crack
with pyzipper.AESZipFile(zip_path) as zf:
    for word in tqdm(words, total=len(words), unit="word", desc="Cracking"):
        pwd = word.strip()
        try:
            zf.extractall(path=output_dir, pwd=pwd)
        except RuntimeError:
            continue
        except Exception as e:
            print(f"[!] Error: {e}")
            continue
        else:
            print(f"[+] Password found: {pwd.decode(errors='ignore')}")
            print(f"[+] Files extracted to: {output_dir}")
            sys.exit(0)

print("[-] Password not found. Try another wordlist.")




