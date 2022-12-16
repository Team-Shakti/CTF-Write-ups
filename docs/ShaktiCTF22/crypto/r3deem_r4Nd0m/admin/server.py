from r3d33m_r4Nd0m import sp,sq,sr,h,e,n,ct
from Crypto.Util.number import * 
from secret import flag,p,q,r

def crt(sp1,sq1,sr1,p,q,r):
    s1 = (sp1*q*r*(inverse((q*r),p)))%n
    s2 = (sq1*p*r*(inverse((p*r),q)))%n
    s3 = (sr1*p*q*(inverse((p*q),r)))%n 
    s = (s1+s2+s3)%n 
    return s1,s2,s3,s 
    
def server():
    print(f"Welcome to this small crt game\nI am a poor kid, I am here to do a small job which can help me to coverup my small expenses.\nSo, My job is to do some simple calulations for inputs provided.\n\nAs part of game rules, intially I will give you some parameters, using that parameters and this server try to get me the flag , then you can get the treasure\nParameters provided\nn = {n}\ne = {e}\nh = {h}\nct = {ct}\nPlease try to give valid input, if I am unable do good calulations, my boss will fire me :( \nYou have two options:\n\n1. Input '1' to get sp,sq,sr values and it's computation values from our server\n2. Input '2' to input your own sp,sq,sr and get corresponding computatuion values" )
    
    x = input()
    if x == '1':
        print(f"sp = {sp}\nsq = {sq}\nsr = {sr}")
        s1,s2,s3,s = crt(sp,sq,sr,p,q,r)
        print(f"s1 = {s1}\ns2 = {s2}\ns3 = {s3}\ns = {s}")
    if x == '2':
        print("Get customized s1,s2,s3 and s values.")
        print("Input sp,sq,sr values")
        sp_u = int(input("\nInput your sp value: "))
        sq_u = int(input("\nInput your sq value: "))
        sr_u = int(input("\nInput your sr value: "))
        s1_u,s2_u,s3_u,s_u = crt(sp_u,sq_u,sr_u,p,q,r)
        print(f"s1 = {s1_u}\ns2 = {s2_u}\ns3 = {s3_u}\ns = {s_u}")

if __name__ == '__main__':
    server()

    