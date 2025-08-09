# Code	Meaning	Result (ogada)

# word[::1]	Every character from start to end               	ogada

# word[::2]	Every 2nd character starting from index 0       	oaa

# word[1::2]	Every 2nd character starting from index 1   	gd

# word[::-1]	Reverse the word	                            adago

# word[1:-1]	All characters except the first and last    	gad

# word[:3]	First 3 characters	                                oga

# word[-3:]	Last 3 characters	                                ada

# word[0:4:2]	From index 0 to 3 (exclusive), taking every 2nd character	oa

# ✅ Notes:

# Syntax: word[start:stop:step]

# Start → Where slicing begins (inclusive)

# Stop → Where slicing ends (exclusive)

# Step → Number of steps to move ahead

# Negative step reverses the string.
