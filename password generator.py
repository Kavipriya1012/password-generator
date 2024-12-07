
import string

def generate_password(length, use_uppercase=True, use_digits=True, use_special_chars=True):

    char_pool = string.ascii_lowercase

    if use_uppercase:
        char_pool += string.ascii_uppercase
    if use_digits:
        char_pool += string.digits
    if use_special_chars:
        char_pool += string.punctuation

    password = ''.join(random.choice(char_pool) for _ in range(length))

    return password


def get_user_input():
    print("Welcome to the Password Generator!")

    length = int(input("Enter the desired password length: "))

    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'


    use_digits = input("Include numbers? (y/n): ").lower() == 'y'


    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'


    password = generate_password(length, use_uppercase, use_digits, use_special_chars)

    print("\nYour generated password is:", password)


def main():
    get_user_input()


if __name__ == "__main__":
    main()

