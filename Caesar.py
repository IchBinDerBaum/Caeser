alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
maxkey = len(alphabet)

def getMode():
    while True:
        print("Do you want to (D) decode, (C) code or (crack) crack the code?")
        answer1 = input().lower()
        if answer1 in ["d", "c", "crack"]:
            return answer1
        else:
            print("You didn't decide what to do! Try again")
def getMessage():
    message = input("Please enter your message that is supposed to be translated.")
    return message
def getKey():
    while True:
        print(f"Please enter the Key. (1-{maxkey})")
        Key = int(input())
        if Key > maxkey or Key < 0:
            print("This cant be true! Please enter the right key.")
        elif Key < maxkey and Key > 0:
            return Key
def gettranslatedmessage(mode, key, message):
    if mode == "d" or mode == "crack":
        key = -key
    TranslatedMessage = ""
    for i in message:
        if i not in alphabet:
            TranslatedMessage += i
        else:
            symbolindex = alphabet.find(i)
            symbolindex += key
            if symbolindex >= len(alphabet):
                symbolindex -= len(alphabet)
            elif symbolindex < 0:
                symbolindex += len(alphabet)
            TranslatedMessage += alphabet[symbolindex]
    return TranslatedMessage


mode = getMode()
message = getMessage()
if mode != "crack":
    key = getKey()
    print(gettranslatedmessage(mode, key, message))
else:
    for key in range(1, maxkey + 1):
        print(key, gettranslatedmessage(mode, key, message))