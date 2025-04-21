#!/bin/python



while True:
    
    print("\n----Names Menu----")

    print("")
    print("1) Read and show names")
    print("2) Add a new name")
    print("3) Exit")

    print("")

    Choice = input ("Choose your option (1-3)").strip()

    if Choice == '1':

        with open ("create names.txt","r") as file:
            content = file.read()
            print(content)

    elif Choice == "2":
        with open ("create names.txt", "a") as file:
            name = input ("Tell me your name:")
            file.write("\n" + name)

    elif Choice == "3":
        print ("Exiting. Thank you and Goodbye!")
        break
    else:
        print ("Invalid option. kindly choose 1,2 or 3.")

        

    



 





    














# with open("create names.txt","r") as file:
#     content = file.read()
#     print(content)

# print("-------------------------")


# with open("create names.txt","a") as file:
#     name = input("What is your name:")
#     file.write("\n" + name)

# print("---------------------------")

# with open ("create names.txt","r") as file:
#     content =file.read()
#     print(content)