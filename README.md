# Challenge Number Zero

This challenge makes use of zero width characters.
https://en.wikipedia.org/wiki/Zero-width_space

For this challenge 2 different types of zero width characters were used, they are shown below and are actually in the quotes. If you copy and paste the characters below and put them into https://www.diffchecker.com/ you can see them. The 2 characters were used to represent binary data, the binary data is in the description text below.

ZW_S = '​' #zero-width space
ZW_NJ = '‌' #zero-width non-joiner

## Description:

000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000

# How to Generate Challenge

    cat challengegen.txt | python ChallengeNumberZero.py

# How to Solve

The 3 lines of python code required to solve the challenge can be found at the end of the challenge generator. Specifically all you need to do is remove all 0's from the file, replace all zero width non-joiner `0x200c` characters with 0 and all zero width space characters `0x200b` with 1. Then paste the text into any online binary to ASCII converter.

# Flag

flag is: MCA{W@ttchYEE_Cl1p_B00rd!.?}
