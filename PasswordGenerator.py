import random
import string

def get_random_password(length):
    """
    Generate a random password of the given length.

    The password will be a mix of uppercase and lowercase letters, numbers,
    and special characters.

    Args:
        length (int): The desired length of the password.

    Returns:
        str: A random password of the specified length.
    """
    all_chars = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_chars) for i in range(length))
    return password

def generate_passwords(num_passwords, password_length):
    """
    Generate the specified number of random passwords.

    Each password will be a mix of uppercase and lowercase letters, numbers,
    and special characters.

    Args:
        num_passwords (int): The number of passwords to generate.
        password_length (int): The length of each password.

    Returns:
        list: A list of randomly generated passwords.
    """
    passwords = []
    for i in range(num_passwords):
        password = get_random_password(password_length)
        passwords.append(password)
    return passwords

def main():
    """
    Generate and display random passwords.

    This function prompts the user to enter the number of passwords to generate
    and the length of each password. It then generates the specified number of
    passwords and prints them out.
    """
    num_passwords = int(input("Enter the number of passwords to generate: "))
    password_length = int(input("Enter the length of each password: "))

    if num_passwords <= 0 or password_length <= 0:
        print("Both inputs must be positive integers.")
    else:
        passwords = generate_passwords(num_passwords, password_length)
        for i, password in enumerate(passwords):
            print(f"Generated Password {i+1}: {password}")

if __name__ == "__main__":
    main()