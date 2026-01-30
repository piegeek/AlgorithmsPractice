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