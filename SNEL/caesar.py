def shift(letter, shift_amount):
    unicode_value = ord(letter) + shift_amount

    if unicode_value > 126:
        new_letter = chr(unicode_value - 95)
    else:
        new_letter = chr(unicode_value)

    return new_letter

def encrypt(message, shift_amount):
    result = ""

    for letter in message:
        result += shift(letter, shift_amount)

    return result


def decrypt(message, shift_amount):
    result = ""
    
    for letter in message:
        result += shift(letter, -shift_amount +95)

    return result


message = "why is it wrong"
encrypted_message = '!>=.q_i>wMW-j%|A"`A"`GP""Y}P`{ACPw`b7G`:XHHAH}`JXZ`J{`"ZX{{`ZJ`V:AZPw`vP:P7"`"JGP`KFY}Y:A"G`{:JG`*ADAKPOAYa`$z%bj|JGP`82$z%b`YZ`|JGP29`A"`YH`bHZP:HPZqUY"PO`KXUFAI`CJFXHZPP:`IJGKXZAH}`K:JSPIZ`PGKFJNAH}`Z|P`l~b/;`"J{ZVY:P`KFYZ{J:G=`|J"ZPO`UN`Z|P`$KYIP`$IAPHIP"`,YUJ:YZJ:N=`YZ`Z|P`^HACP:"AZN`J{`;YFA{J:HAY=`lP:DPFPN=`AH`Z|P`^HAZPO`$ZYZP"w`$z%b`A"`YH`YI:JHNG`{J:`Z|P`$PY:I|`{J:`zBZ:Yq%P::P"Z:AYF`bHZPFFA}PHIPw`bZ"`KX:KJ"P`A"`ZJ`YHYFNMP`:YOAJ`"A}HYF"=`"PY:I|AH}`{J:`"A}H"`J{`PBZ:Y`ZP::P"Z:AYF`AHZPFFA}PHIP=`YHO`A"`JHP`J{`GYHN`YIZACAZAP"`XHOP:ZYDPH`Y"`KY:Z`J{`$z%bwxPn2B(;G[)(gUudK*Xk'


def count_characters(text, counts):
    for c in text:
        n = ord(c)
        counts[n] += 1

counts = [0] * 127
count_characters(encrypted_message, counts)

max = 0
index = 0
for i in range(0, len(counts)):
    if counts[i] > max:
        max = counts[i]
        index = i

freq = chr(index)

shift2 = (ord(freq) - 32)

decrypted_message = decrypt(encrypted_message, shift2)
print(encrypted_message)
print(decrypted_message)
