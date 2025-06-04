#/bin/python

from cryptography.fernet import Fernet

def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("key.key", "rb").read()


while True:

    key = load_key()
    fernet = Fernet(key)

    print ("\n Menu")

    print("1) Generate your Key")

    print("2) Read your Key")

    print("3) Encrypt Message")

    print("4) Decrypt Message")

    print("5) Encrypt a File")

    print("6) Decrypt a File")

    print("7) Exit")


    Choice= input ("Choose your option (1-7)").strip ()

    if Choice == "1":
        write_key()
        print("Your key as been generated")

    elif Choice == "2":
        key = load_key()
        print("Your key is: " + str(key.decode('utf-8')))

    elif Choice == "3":
       message = input("type your message:")
       bytes = message.encode()
       encrypted = fernet.encrypt(bytes)
       print("Ciphertext is " + encrypted.decode('utf-8'))

    elif Choice == "4":
       encryptedmessage = input("type your encrypted message:")
       bytes = encryptedmessage.encode()
       decrypted = fernet.decrypt(bytes)
       print("Plaintext is " + str(decrypted.decode('utf-8')))

    elif Choice == "5":
        with open ("carta.txt", "rb") as file:
            original= file.read()
            encrypted= fernet.encrypt (original)
            with open("carta_encrypted.txt", "wb") as encrypted_file:
                encrypted_file.write (encrypted)
            print("Your File is Encrypted")          

    elif Choice == "6":
        with open ("carta_encrypted.txt","rb") as enc_file:
            encrypted= enc_file.read() 
            decrypted= fernet.decrypt(encrypted) 
            with open("carta_decrypted.txt", "wb") as dec_file:
                dec_file.write(decrypted) 
            print ("Your file is Decrypted")
               
                

    elif Choice == "7":
        print ("Exiting...see you soon!") 
        break

    else:
        print("oops! looks like you made a mistake")

          


