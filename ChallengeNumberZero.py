#!/usr/bin/env python
# -*- coding: utf-8 -*-]
import binascii
import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

def getBinary(word):
    return bin(int(binascii.hexlify(word), 16))

secretInput = raw_input("Enter the secret message: ")
textInput = raw_input("Enter the text to hide the secret in: ")
secretBinary = getBinary(secretInput)
secretBinary0Width = secretBinary

ZW_S = '\u200b'  #zero-width space
ZW_NJ = '﻿\uFEFF'  #zero-width non-joiner
#ZW_S = "1"
#ZW_NJ = "0"

secretBinary0Width = secretBinary0Width.replace("1",ZW_S)#zero-width space
secretBinary0Width = secretBinary0Width.replace("0",ZW_NJ)#zero-width non-joiner

length_textInput = len(textInput)
length_secretBinary0Width = len(secretBinary0Width)
numOf0WperChar = length_secretBinary0Width/length_textInput


output = textInput
i = 1;
while len(secretBinary0Width) > 0:
	chunk = secretBinary0Width[:numOf0WperChar]
	secretBinary0Width = secretBinary0Width[numOf0WperChar:]
	output = output[:i] + chunk + output[i:]
	i+=1
	i+=numOf0WperChar

print(output)
with open('output.txt', 'a') as the_file:
    the_file.write(output)





binaryData = ""
for letter in output:
	if letter == ZW_S:
		binaryData+="1"
	if letter == ZW_NJ:
		binaryData+="0"

x = output
import string
all=string.maketrans('','')
nodigs=all.translate(all, string.digits)
output = x.translate(all, nodigs)
print(output)


