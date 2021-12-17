from hashlib import sha256

pwd = "1234"

pwd_e_bytes = sha256(pwd.encode())

pwd_e_str = pwd_e_bytes.hexdigest()
print(pwd_e_str)

