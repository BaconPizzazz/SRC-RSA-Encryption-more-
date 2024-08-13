import math
import time

def sdf(a,b): # Den største fælles divisor bliver udregnet vha. euklids algoritme, som lyder således: 
    # a = q0 * b + r0
    # b = q1 * r0 + r1
    # r0 = q2 * r1 + r2 
    # r1 = q3 * r2 + r3
    # r_n-2 = q_n * r_n-1 + r_n 
    # Dette fortsættes så indtil r_n = 0, hvorefter den største fælles divisor så er r_n-1, dette ser vi også repræsenteret af while loopet. 
    a = int(input("indsæt første værdi: "))
    b = int(input("indsæt anden værdi: "))
    if a <= b - 1:
        temp = a
        a = b
        b = temp
    r = a%b 
    q = int(a%b)
    while (r!=0):
        a = b 
        b = r 
        q = int(a/b)
        r = a - (b * q) 
    print(b) 

def EncryptionRSA():
    q = int(input("Indtast det første primtal: "))
    p = int(input("Indtast det andet primtal: ")) 
    # Tjekker først om tallet er over 2, hvis ikke starter man forfra 
    if q <= 1 or p <= 1:
        print("Dine valgte q eller p værdier er ikke større end 1, starter forfra.") 
        time.sleep(10)
        EncryptionRSA() 
        # løber igennem løkken fra 2 til n//2. 
        for i in range(2, math.sqrt(q) + 1):
            if q % i == 0:
                print("Den valgte q værdi er ikke et primtal, starter forfra.")
                time.sleep(10)
                return EncryptionRSA() 
        # kør videre hvis ovenover er korrekt
        for i in range(2, math.sqrt(p) + 1):
            if p % i == 0:
                print("Den valgte p værdi er ikke et primtal, starter forfra.")
                time.sleep(10)
                return EncryptionRSA() 
        # Udregner nu n værdien, vha. p * q 
        n = p * q 
        # Nu kan værdien af eulers totientfunktion udregnes vha. følgende formel: phi(n)=(p-1)*(q-1) 
        phiN = (p-1) * (q-1) 
        # Nu skal vi så få en e værdi, denne skal både være mindre end phi(n) og indbyrdes primisk med den, altså (e,phi(n))=1 
        e = int(input("Indtast en positiv e værdi, som er mindre end phi(n) og indbyrdes primisk med phi(n)"))
        if e < phiN:
            print("Den valgte e værdi er mindre end e, prøv igen.") 
        if sdf(e,phiN) >= 2: 
            print("Valgte e værdi er ikke imbyrdes primisk med phiN, prøv igen.")       

EncryptionRSA() 
