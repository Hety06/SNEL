#message_finder

def mean(counts):
    total = 0
    for c in counts:
        total += c
        
    avg = total / len(counts)

    return avg

def chi_square(counts):
    expected = mean(counts)
    
    X = 0

    for observed in counts:
        top = observed - expected
        X += (top)**2

    return X / expected


def count_characters(text):
    counts = [0] * 127
    for c in text:
        n = ord(c)
        counts[n] += 1

    return counts[32:]


def get_filename(num):
    length = len(str(num))
    test = 6 - int(length)
    zero = ""
    if test == 1:
        zero += "0"
    elif test == 2:
        zero += "00"
    elif test == 3:
        zero += "000"
    elif test == 4:
        zero += "0000"
    else:
        zero += "00000"
    

    return "file_" + zero + str(num) + ".txt"




for i in range(18000):
    filename = get_filename(i)
    with open ("text_files/" + filename,'r') as f:
        contents = f.read()
    counts = count_characters(contents)
    chi_value = chi_square(counts)
    if chi_value < 55 or chi_value > 140:
        print(filename, chi_value)

'''
    with open("chi_values.txt", 'a') as c:
        c.write(filename + " " + str(chi_value) + "\n")
'''


print("done")
