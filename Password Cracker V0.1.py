import base64 
import getpass

print(" ________  _________   ________  ________  ___  __    _______   ________          ___      ___ ________    _____")     
print("|\   ____\|\   __   \| \   __  \|\   ____\|\  \|\  \  |\  ___ \ |\   __  \       |\  \    /  /|\   __  \  / __  \ ")    
print("\ \  \___|\ \  \|\   \  \  \|\  \ \  \___|\ \  \/  /| \ \   __/|\ \  \|\  \      \ \  \  /  / | \  \|\  \|\/_|\  \ ") 
print(" \ \  \    \ \   _   _\  \   __  \ \  \    \ \    ___  \ \ \_|/ \ \   _  _\       \ \  \/  / / \ \  \/\  \|/ \ \  \ ")
print("  \ \  \____\ \  \ \  \ \ \  \ \  \ \  \____\ \  \ \ \  \ \ \_|\ \ \  \ \  \       \ \    / /   \ \    \  \ __\ \  \ ")
print("   \ \_______\ \__\ \ _\ \ \__\ \__\ \_______\ \__\ \ \__\ \______\ \__\ \ _\       \ \__/ /     \ \_______/\__\ \__\ ")
print("    \|_______|\|__| \|__| \|__|\|__|\|_______|\|__| \|__|\|_______|\|__|\|__|        \|__|/       \|_______\|__|\|__| ")

print("\nCracker V0.1\n")
print("This Program Uses The getpass Module To Obtain Usernames\n")
print("Modes Available: None\n")

user = getpass.getuser()
saveplace = input("Would You Like To Save Document To Desktop Or Documents Directory (Desk / Doc): ")

#Desktop Save
if saveplace == ("Desk"):
    f = open("C:/Users/" + user + "/Desktop/pwcracklog.txt", 'w')
    f.write("Cracker V0.1\nIGNORE MALFORMED STRINGS\nDecrypted Data: ")
    console = input(": ")
    consolec = console.encode('utf-8')

    #B16
    try:
        b16 = (base64.b16decode(consolec))
        print(b16)
        f = open("C:/Users/" + user + "/Desktop/pwcracklog.txt", 'a')
        f.write(("\nB16: ") + str(b16))
        f.close
    except:
        pass
    #B32
    try:
        b32 = (base64.b32decode(consolec))
        print (b32)
        f = open("C:/Users/" + user + "/Desktop/pwcracklog.txt", 'a')
        f.write(("\nB32: ") + str(b32))
        f.close
    except:
        pass
    #B64
    try:
        b64 = (base64.b64decode(consolec))
        print (b64)
        f = open("C:/Users/" + user + "/Desktop/pwcracklog.txt", 'a')
        f.write(("\nB64: ") + str(b64))
        f.close
    except:
        pass
    #B85
    try:
        b85 = (base64.b85decode(consolec))
        print (b85)
        f = open("C:/Users/" + user + "/Desktop/pwcracklog.txt", 'a')
        f.write(("\nB85: ") + str(b85))
        f.close
    except:
        pass


#Document Save
if saveplace == ("Doc"):
    f = open("C:/Users/" + user + "/Documents/pwcracklog.txt", 'w')
    f.write("Cracker V0.1\nIGNORE MALFORMED STRINGS\nDecrypted Data: ")
    console = input(": ")
    consolec = console.encode('utf-8')

    #B16
    try:
        b16 = (base64.b16decode(consolec))
        print(b16)
        f = open("C:/Users/" + user + "/Documents/pwcracklog.txt", 'a')
        f.write(("\nB16: ") + str(b16))
        f.close
    except:
        pass
    #B32
    try:
        b32 = (base64.b32decode(consolec))
        print (b32)
        f = open("C:/Users/" + user + "/Documents/pwcracklog.txt", 'a')
        f.write(("\nB32: ") + str(b32))
        f.close
    except:
        pass
    #B64
    try:
        b64 = (base64.b64decode(consolec))
        print (b64)
        f = open("C:/Users/" + user + "/Documents/pwcracklog.txt", 'a')
        f.write(("\nB64: ") + str(b64))
        f.close
    except:
        pass
    #B85
    try:
        b85 = (base64.b85decode(consolec))
        print (b85)
        f = open("C:/Users/" + user + "/Documents/pwcracklog.txt", 'a')
        f.write(("\nB85: ") + str(b85))
        f.close
    except:
        pass
