# def PalindromeCreator(str):
#   if str == str[::-1] and len(str) >= 3:
#     return "palindrome"

#   for i in range(len(str)):
#     temp_str = str[:i] + str[i+1:]
#     if temp_str == temp_str[::-1] and len(temp_str) >= 3:
#       return str[i]

#   # Attempt to create palindrome by removing 2 characters
#   for i in range(len(str) - 1):
#     temp_str = str[:i] + str[i+2:]
#     if temp_str == temp_str[::-1] and len(temp_str) >= 3:
#       return str[i] + str[i+1]

#   # No palindrome possible
#   return "not possible"

# # Example usages
# print(PalindromeCreator("ammop"))  # Output: jc
# # print(PalindromeCreator("aabbaa"))  # Output: palindrome
# # print(PalindromeCreator("abcd"))     # Output: not possible

def palindromer(words:str):
	if words == words[::-1]:
		return "palindrome"
	start = 0
	end = len(words) - 1
	starter = ender = palindrome_start = palindrome_end = ""
	while start < end:
		if words[start] != words[end]:
			if words[start+1] == words[end]:
				starter = f"{starter}{words[start]}"
				start += 1
			else:
				ender = f"{words[end]}{ender}"
				end -= 1
		else:
			palindrome_start = f"{palindrome_start}{words[start]}"
			palindrome_end = f"{words[end]}{palindrome_end}"
			start+=1
			end-=1
	palindrome_start = f"{palindrome_start}{words[start]}"
	palindrome = palindrome_start + palindrome_end
	result = starter + ender
	print(f"removed: {result}")
	print(f"palindrome: {palindrome}")
	return result if len(palindrome) > 3 else "not possible"


print(f"\nFinal Result: {palindromer('mmop')}")