from Crypto.Cipher import AES  
from Crypto.Util.Padding import pad,unpad  
from Crypto.Util.strxor import strxor
from secret import key,flag ,iv
from os import *  

def encryptt(pt):  
    return (AES.new(key,AES.MODE_CBC,iv)).encrypt(pad(pt,16))   
   
def decryptt(ct):  
    if len(ct)%16 == 0:  
        return (AES.new(key,AES.MODE_CBC,iv)).decrypt(ct)  
    elif len(ct)%16 != 0:  
        return (unpad((AES.new(key,AES.MODE_CBC,iv)).decrypt(ct) , 16))                                                                                 
  
def verify_ivv(iv,iv_detected):
    if iv.hex() == iv_detected:
        print("Yooo... you are going good, move forward with some more courage")
        return True
    else:
        print("Don't lose hope buddy , you can get through this, try again ")
        return False

def sign(iv,key,message):
    try:
        cbc = AES.new(key, AES.MODE_CBC,iv)
        messageblocks = [message[i:i + 16] for i in range(0, len(message), 16)]
        tag = cbc.encrypt(messageblocks[0])
        for i in range(1,len(messageblocks)):   
            cbc1 = AES.new(key, AES.MODE_CBC,tag)
            tag = cbc1.encrypt(messageblocks[i])
        return tag.hex()
    except:
        print("\nNo padding done here !, try again ")
        exit()

 

def main():
    print("******************************Welcome to the john's CBC server************************")
    print("You really wanna get into the system? \n then search for IV ")
    print("Choose 1 option among four \n \t 1.Encrypt the plain text \n \t 2.Decrypt the ciphertext \n \t 3.feed IV \n \t 4.exit")
    op = int(input())
    if op == 1:
        print("I will provide the encrypted text for you")
        print("Input the plaintext in hex format\n")
        pt = input()
        ct = encryptt(bytes.fromhex(pt)).hex()
        print(f"cipher text for provided" , ct);
    if op == 2:
        print("I will provide the reasonable plaintext for you")
        print("Input the cipher text in bytes to decrypt")
        ct = input()
        pt = decryptt(bytes.fromhex(ct)).hex()
        print(f"decrypted text for provided" , pt);
    if op == 3:
        print("Provide reasonable IV to proceed further")
        iv_detected = input()
        verify_iv = verify_ivv(iv,iv_detected) 
        print(verify_iv)
        if verify_iv:
            print("Let me see whether you are worth enough to gain my gold coins.")
            print("To prove yourself, give me two different hex-encoded messages that could sign to the same tag.")
            print("Now press '0' to get your hex inputs signed and press 1 to submit two same messages")
            iv_detected = bytes.fromhex(iv_detected)
            x = input()
            if x == '0':
                print("Input hash encoded message:\n")
                msg = bytes.fromhex(input())
                x = sign(iv_detected,key,msg)
                print("\n Tag for your message")
                print(x)
            if x == '1':
                msg1 = bytes.fromhex(input("\nMessage #1: \n"))
                msg2 = bytes.fromhex(input("\nMessage #2: \n"))
                if(msg1 == msg2):
                    print("\nThis is not a correct way to do this, think again!!!")
                    exit()
                if(msg1 != msg2 and sign(iv_detected,key,msg1)==sign(iv_detected,key,msg2)):
                    print(flag)
                    exit()
                else:
                    print("\nOops! They don't match!...Better luck next time!")
                    exit()                
        if op==4:
            exit()          



if __name__ == '__main__':
    main()
