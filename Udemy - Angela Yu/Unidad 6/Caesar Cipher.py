alphabet=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

def encode(shift, message):
    code=""
    messsage_lower=message.lower()
    for letters in messsage_lower:
        if letters in alphabet:
            new_letter=alphabet.index(letters)+shift
            #shift%=len(alphabet)  En la resolución usan esto
            if new_letter > len(alphabet):
                new_letter=new_letter-int(len(alphabet))
            #print(f"{alphabet.index(letters)},{new_letter}")
            code=code+alphabet[new_letter]
    print(code)        

def decode(shift,message):
    code=""
    messsage_lower=message.lower()
    for letters in messsage_lower:
        if letters in alphabet:
            new_letter=alphabet.index(letters)-shift
            if new_letter < 0:
                new_letter=new_letter+int(len(alphabet))           
            #print(f"{alphabet.index(letters)},{new_letter}")
            code=code+alphabet[new_letter]
    print(code)  

def caesar(shift,message,type):     #Este usa en tandem las funciones encode y decode
         
    if type==2:
        shift *=-1
        
    code=""
    messsage_lower=message.lower()
    for letters in messsage_lower:
        if letters in alphabet:
            new_letter=alphabet.index(letters)+shift
            #shift%=len(alphabet)  En la resolución usan esto
            if new_letter > len(alphabet):
                new_letter=new_letter-int(len(alphabet))
            #print(f"{alphabet.index(letters)},{new_letter}")
            code=code+alphabet[new_letter]
    print(code)        


msg_input=input("Enter message:")
shift_input=int(input("Enter shift number:"))  # Mejorar con un TRY para confirmar que el input es un int
type_input=int(input(f"Want to code or decode?\n1:Encode\n2:Decode\nType 1 or 2:"))

caesar(shift_input,msg_input,type_input)






