alphabet = " aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ123456789!@#$%^&*()_+-=,./<>?;:'\"[]{}\\|~`" 
key = " plmkoijnbhuygvcftrdxsezawqQAZXWSEDCRFVG_BTNYJHUMKILOP*&^%$#()-+1236,./<>?;:'\"[]{}\\|~`54789@!="
alphabet2 = " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
key2 =      "`1234567890-=qwertyuiop[]\\asdfghjkl;'zxcvbnm,./~!@#$%^&*()_+QWERTYUIOP{}|ASDFGHJKL:\"ZXCVBNM<>? " 
def encrypt(message):
    result = ""

    for letter in message:
        loc = alphabet.find(letter)
        result += key[loc]

    return result

def decrypt(message):
    result = ""

    for letter in message:
        loc = key2.find(letter)
        result += alphabet2[loc]

    return result


unencrypted_message = "Apples can taste sour \ sweet, but Timmy says that some apples are both sour and sweet! What do you think?"
encrypted_message = encrypt(unencrypted_message)
decrypted_message = decrypt(encrypted_message)


'''
print(unencrypted_message)
print(encrypted_message)
print(decrypted_message)
'''


new = '!>=.q_i>wMW-j%|A"`A"`GP""Y}P`{ACPw`b7G`:XHHAH}`JXZ`J{`"ZX{{`ZJ`V:AZPw`vP:P7"`"JGP`KFY}Y:A"G`{:JG`*ADAKPOAYa`$z%bj|JGP`82$z%b`YZ`|JGP29`A"`YH`bHZP:HPZqUY"PO`KXUFAI`CJFXHZPP:`IJGKXZAH}`K:JSPIZ`PGKFJNAH}`Z|P`l~b/;`"J{ZVY:P`KFYZ{J:G=`|J"ZPO`UN`Z|P`$KYIP`$IAPHIP"`,YUJ:YZJ:N=`YZ`Z|P`^HACP:"AZN`J{`;YFA{J:HAY=`lP:DPFPN=`AH`Z|P`^HAZPO`$ZYZP"w`$z%b`A"`YH`YI:JHNG`{J:`Z|P`$PY:I|`{J:`zBZ:Yq%P::P"Z:AYF`bHZPFFA}PHIPw`bZ"`KX:KJ"P`A"`ZJ`YHYFNMP`:YOAJ`"A}HYF"=`"PY:I|AH}`{J:`"A}H"`J{`PBZ:Y`ZP::P"Z:AYF`AHZPFFA}PHIP=`YHO`A"`JHP`J{`GYHN`YIZACAZAP"`XHOP:ZYDPH`Y"`KY:Z`J{`$z%bwxPn2B(;G[)(gU\\udK*XkuN/Cu?'
decrypt2 = decrypt(new)

print(decrypt2)
