import  requests
import hashlib
class Passwords:
    @staticmethod
    def request_api_data(checker) -> requests:
        url: str = 'https://api.pwnedpasswords.com/range/' + checker
        res: requests = requests.get(url)
        if res.status_code != 200:
            raise RuntimeError(f'Error fetching from api: {res.status_code}')
            exit(0)
        return res

    @staticmethod
    def hash_password_for_api(password) -> tuple:
        sha1_passowrd = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
        sha1_passowrd, tail = sha1_passowrd[:5], sha1_passowrd[5:]
        return sha1_passowrd, tail
    

    @staticmethod
    def check_no_of_leaks(response: requests, tail: str) -> int:
        hashed_password = (line.split(':') for line in response.text.splitlines())
        for hash, leak_count in hashed_password:
            if hash == tail:
                return leak_count
        return 0
            
