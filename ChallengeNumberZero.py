#!/usr/bin/env python
# -*- coding: utf-8 -*-]
import binascii
import sys
reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

def getBinary(word):
	# The 0 at the beginning is a hack because the length of the string keeps coming out the wrong length for some reason.
	# Didn't have time to debug it.
    return '0' + bin(int(binascii.hexlify(word), 16))[2:]

secretInput = raw_input("Enter the secret message: ")
textInput = raw_input("Enter the text to hide the secret in: ")
secretBinary = getBinary(secretInput)
secretBinary0Width = secretBinary

ZW_S = unichr(int(0x200b))  #zero-width space
ZW_NJ = unichr(int(0x200c))  #zero-width non-joiner

secretBinary0Width = secretBinary0Width.replace("1",ZW_S)#zero-width space
secretBinary0Width = secretBinary0Width.replace("0",ZW_NJ)#zero-width non-joiner

length_textInput = len(textInput)
length_secretBinary0Width = len(secretBinary0Width)
numOf0WperChar = length_secretBinary0Width/length_textInput


output = textInput.decode("utf-8")
i = 1;
while len(secretBinary0Width) > 0:
	chunk = secretBinary0Width[:numOf0WperChar]
	secretBinary0Width = secretBinary0Width[numOf0WperChar:]
	output = output[:i] + chunk + output[i:]
	i+=1
	i+=numOf0WperChar

print(output)
with open('output.txt', 'w') as the_file:
    the_file.write(output)


output = output.replace('0', '')
output = output.replace(ZW_S, '1')
output = output.replace(ZW_NJ, '0')

with open('solve.txt', 'w') as the_file:
    the_file.write(output)


