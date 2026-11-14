def welcomeUser():
    print("\nWelcome to the text analysis tool, i will mine and analyze a body of text from a file you give me!")
    

def getUsername():
    usernameFromInput = input("\nTo begin, please enter your username:\n")
    return usernameFromInput

def greetUser(name):
    print("Hello, " + name)

welcomeUser()
username = getUsername()
greetUser(username)
