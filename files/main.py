from password_checker import Passwords as password_checker

password = input('Enter Your Password: ')
hash = password_checker.hash_password_for_api(password)
response = password_checker.request_api_data(hash[0])
num = password_checker.check_no_of_leaks(response, hash[1])
print(f'Your Password: {password} has been compromised: {num} times')