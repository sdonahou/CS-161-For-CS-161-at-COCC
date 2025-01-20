#1   Print out the value of a variable in binary and decimal form.
x = int(31)

print("Decimal:",(x))
print("Binary:", bin(x))
print("Hexidecimal:", hex(x))


#2 Identify the error when giving an incorrect input type.
#TypeError: 'float' object cannot be interpreted as an integer#
#The error was thrown because I used 'float', the number used was not an integer. "bin" and "hex" only work with "int()" operations.
x = (18)

print("Decimal:",(x))
print("Binary:", bin(x))
print("Hexidecimal:", hex(x))

#3 Assigning a binary or hex value to a variable.
y = 0b1011
z = 0xA3

print("Binary to Hexidecimal:", hex(y))
print("Hexidecimal to Binary:", bin(z))

#4  You can add numbers in any representation.

x = 8            # Decimal value for 8
y = 0b11011      # Binary value of 27
z = 0x7C8        # Hexidecimal value of 1992
w = x + y + z

print('the sum is ', w)

#Compression

#1 Choose meaningful variable names.
original_size_1 = 240
dictionary_size_1 = 25
compressed_text_size_1 = 140

percent_compression_1 = 1 - ((compressed_text_size_1 + dictionary_size_1) / original_size_1) # (100% = 1)

print("Percent Compression:", percent_compression_1 * 100, "%")

#2  Assign values to your variables.  Calculate the result.
original_text_size_2 = 240
dictionary_size_2 = 25
compressed_text_size_2 = 148


percent_compression_2 = 1 - ((compressed_text_size_2 + dictionary_size_2) / original_text_size_2) # (100% = 1)

print("Percent Compression", percent_compression_2 * 100, "%")

#3  Print out your result.
original_text_size_3 = 300
dictionary_size_3 = 27
Total_3 = 192
compressed_text_size_3 = 147
Compression = 32.27

print(' 	Dictionary size:', str(dictionary_size_3), 'characters')
print(' 	Dictionary size:', str(original_text_size_3), 'characters')
print(' 	Dictionary size:', str(Total_3), 'characters')
print(' 	Dictionary size:', str(Compression),"%", 'characters')



