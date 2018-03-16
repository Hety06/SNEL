#random_file_writer
import random

def generate_random_text(num_chars):
    text = ""

    for i in range(num_chars):
        r = random.randint(32, 126)
        text += chr(r)
    
    return text

contents = generate_random_text(15000)
filenumber = random.randint(1, 3000)
filename = "random_file_" + str(filenumber) + ".txt"

with open(filename, 'w+') as f:
    f.write(contents)
