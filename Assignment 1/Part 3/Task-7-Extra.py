def passwordGenerator(pType):
    import string
    import random
    weakPasswords = ['Dog','Mark', 'Amber', 'Todd', 'Anita', 'Sandy']
    if(pType == 'weak'):
        return(''.join(random.choices(weakPasswords)))
    elif (pType == 'medium'):
        return(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits, k = 12)))
    elif (pType == 'strong'):
        return(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k = 16)))
    elif (pType == 'veryStrong'):
        return(''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation, k = 20)))
    else:
        print("Invalid choice")
        return ('')

def main():
    
    passwordType = ['weak', 'medium', 'strong', 'veryStrong']
    print(passwordType)
    print("Enter the password type from the above list")
    pType = input()
    password = passwordGenerator(pType)
    if(password != ''):
        print("Generated password is:",password)
if __name__ == "__main__":
    main()
