import zipfile
import sys
import os
from tqdm import tqdm  # Make sure tqdm is imported

output_dir = os.path.join(os.getcwd(), "CrackedOutput")
os.makedirs(output_dir, exist_ok=True)

# The zipfile to crack
zip_path = sys.argv[1]

# The password list path you want to use
wordlist_path = sys.argv[2]

# Initialize the Zip file object
zip_file = zipfile.ZipFile(zip_path)

# Count the number of words in this wordlist
with open(wordlist_path, "rb") as f:
    words = list(f)
    n_words = len(words)

# Print the total number of passwords
print("Total passwords to test:", n_words)

# Try passwords
for word in tqdm(words, total=n_words, unit="word"):
    try:
        zip_file.extractall(path=output_dir,pwd=word.strip().strip(b'\r\n'))
    except:
        continue
    else:
        print("[+] Password found:", word.decode().strip())
        print(f"[+] Extracted files to: {output_dir}")
        exit(0)  # <-- fixed from exit(o)

print("[!] Password not found, try another wordlist")


