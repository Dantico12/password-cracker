import hashlib
import pyfiglet


#banner
banner=pyfiglet.figlet_format("DANTICO")
print(banner)
common_passwords = []

with open('common_passwords.txt', 'r') as f:
    common_passwords = f.read().splitlines()
    print(common_passwords)

user_hash_dict = {}  # Initialize the dictionary

with open('username_hashes.txt', 'r') as f:
    txt = f.read().splitlines()
    for user_hash in txt:
        username = user_hash.split(":")[0]
        hash_value = user_hash.split(":")[1]
        user_hash_dict[username] = hash_value

for password in common_passwords:
    hashed_passwords=hashlib.sha256(password.encode('utf-8')).hexdigest()
    for username,hash in user_hash_dict.items():
        if hashed_passwords==hash:
            print(f'HASH FOUND\n{username}:{password}')