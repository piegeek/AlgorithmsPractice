def longestCommonSubsequence(str1, str2):
	ret = 0

	# ret_arr = []

	for i in range(len(str1)):
		for j in range(len(str2)):
			if str1[i] == str2[j]:
				ret = max(ret, 1 + longestCommonSubsequence(str1[i+1:], str2[j+1:]))
				# lcs_len, lcs_arr = longestCommonSubsequence(str1[i+1:], str2[j+1:])
				# if ret <= lcs_len:
				# 	ret = lcs_len + 1
				# 	ret_arr = lcs_arr

				# ret_arr.append(str1[i])

	# return ret, ret_arr
	return ret

def longestCommonSubsequence(str1, str2):
    # ret = lcs(0, 0, str1, str2)

    # return reconstruct(0, 0, str1, str2)

    # return ret

	# LCS 2
	choices = [ -1 for _ in range(len(str1) + 1) ]

	ret = lcs_2(0, 0, str1, str2, choices)

	out = []

	reconstruct_2(0, str1, out, choices)

	return out

def lcs_2(s1, s2, str1, str2, choices):
	ret = 0
	best_next=  -1

	if s1 > len(str1) or s2 > len(str2):
		return 0

	for i in range(s1, len(str1)):
		for j in range(s2, len(str2)):
			if str1[i] == str2[j]:
				cand = 1 + lcs_2(i+1, j+1, str1, str2, choices)
				if cand > ret:
					ret = cand
					best_next = i

					# choices[s1+1] gets overwritten by multiple (s1, s2), (s1, s2') pairs
					choices[s1+1] = best_next

	return ret

def reconstruct_2(s1, str1, out, choices):
	if s1 > len(str1): 
		return
    
	if s1 > 0:
		out.append(str1[s1])
	next = choices[s1+1]
    
	if next != -1:
		reconstruct_2(next, str1, out, choices)

def lcs(s1, s2, str1, str2):
	ret = 0

	for i in range(s1, len(str1)):
		for j in range(s2, len(str2)):
			if str1[i] == str2[j]:
				ret = max(ret, 1 + lcs(i+1, j+1, str1, str2))
	return ret

def reconstruct(s1, s2, str1, str2):
	out = []
	
	ret = 0

	for i in range(s1, len(str1)):
		for j in range(s2, len(str2)):
			if str1[i] == str2[j]:
				f_val = 1 + lcs(i+1, j+1, str1, str2)
				if f_val > ret:
					ret = f_val
					out.append(str1[i])


	return out