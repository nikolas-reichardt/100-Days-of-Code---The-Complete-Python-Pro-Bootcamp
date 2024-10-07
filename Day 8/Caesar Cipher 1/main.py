alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'encrypt()' that takes 'original_text' and 'shift_amount' as 2 inputs.

def encrypt(text, shift_amount):
    # Convert the input text to a list of characters
    list_text = list(text)
    alpha_count = 0
    count = 0
    while alpha_count < len(alphabet) and count < len(list_text):
        if alphabet[alpha_count] == list_text[count]:
            list_text[count] = alphabet[(alpha_count+shift_amount)]
            alpha_count = 0
            count += 1
        else:
            alpha_count += 1
    print(list_text)

# TODO-2: Inside the 'encrypt()' function, shift each letter of the 'original_text' forwards in the alphabet
#  by the shift amount and print the encrypted text.



# TODO-4: What happens if you try to shift z forwards by 9? Can you fix the code?

# TODO-3: Call the 'encrypt()' function and pass in the user inputs. You should be able to test the code and encrypt a
#  message.

print(len(alphabet))
encrypt(text, shift)