import  requests
import hashlib
class Passwords:
    @staticmethod
    def request_api_data(checker: str) -> requests:
        url: str = 'https://api.pwnedpasswords.com/range/' + checker
        res: requests = requests.get(url)
        if res.status_code != 200:
            raise RuntimeError(f'Error fetching from api: {res.status_code}')
        return res

    @staticmethod
    def hash_password_for_api(password: str) -> tuple:
        sha1_password: str = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        sha1_password, tail = sha1_password[:5], sha1_password[5:]
        return sha1_password, tail
    

    @staticmethod
    def check_no_of_leaks(response: requests, tail: str) -> int:
        hashed_password = (line.split(':') for line in response.text.splitlines())
        for hash_key, leak_count in hashed_password:
            if hash_key == tail:
                return leak_count
        return 0
            
if __name__ == '__main__':    
    password = input('Enter Your Password: ')
    hash = Passwords.hash_password_for_api(password)
    response = Passwords.request_api_data(hash[0])
    num = Passwords.check_no_of_leaks(response, hash[1])
    print(f'Your Password: {password} has been compromised: {num} times')