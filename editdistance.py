#!/usr/bin/python

class EditDistance():
	
	def __init__(self):
		"""
		Do not change this
		"""
	
	def calculateLevenshteinDistance(self, str1, str2):
		"""
			take two strings and calculate their Levenshtein Distance for task 1 
			return an integer which is the distance
		"""
		editM = [[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]
		for i in range(len(str1)+1):
			for j in range(len(str2)+1):
				if i == 0 and j == 0:
					editM[j][i] = 0
				elif i == 0 and j > 0:
					editM[j][i] = j
				elif i > 0 and j == 0:
					editM[j][i] = i
				else:
					if str1[i-1] == str2[j-1]:
						temp = 0
					else:
						temp = 1
					editM[j][i] = min(editM[j][i-1]+1, #deletion
									  editM[j-1][i]+1, #insertion
									  editM[j-1][i-1]+temp) #substitution

		return editM[len(str2)][len(str1)]

		
	def calculateOSADistance(self, str1, str2):
		"""
			take two strings and calculate their OSA Distance for task 2 
			return an integer which is the distance
		"""
		editM = [[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]
		for i in range(len(str1)+1):
			for j in range(len(str2)+1):
				if i == 0 and j == 0:
					editM[j][i] = 0
				elif i == 0 and j > 0:
					editM[j][i] = j
				elif i > 0 and j == 0:
					editM[j][i] = i
				else: # i >= 1, j >= 1
					if str1[i-1] == str2[j-1]:
						temp = 0
					else:
						temp = 1

					if str1[i-2] == str2[j-1] and str1[i-1] == str2[j-2]:
						editM[j][i] = min(editM[j][i-1]+1, #deletion
									  editM[j-1][i]+1, #insertion
									  editM[j-1][i-1]+temp, #substitution
									  editM[j-2][i-2]+1) # transposition
					else: 
						editM[j][i] = min(editM[j][i-1]+1, #deletion
										  editM[j-1][i]+1, #insertion
										  editM[j-1][i-1]+temp) # substitution

		return editM[len(str2)][len(str1)]

		
	def calculateDLDistance(self, str1, str2):
		"""
			take two strings and calculate their DL Distance for task 3 
			return an integer which is the distance
		"""
		
		# this part exact the same as task 1
		editM = [[0 for i in range(len(str1)+1)] for j in range(len(str2)+1)]
		for i in range(len(str1)+1):
			for j in range(len(str2)+1):
				if i == 0 and j == 0:
					editM[j][i] = 0
				elif i == 0 and j > 0:
					editM[j][i] = j
				elif i > 0 and j == 0:
					editM[j][i] = i
				else: # i >= 1, j >= 1
					if str1[i-1] == str2[j-1]:
						temp = 0
					else:
						temp = 1

					editM[j][i] = min(editM[j][i-1]+1, #deletion
									  editM[j-1][i]+1, #insertion
									  editM[j-1][i-1]+temp) #substitution

		# Get correct result, by forcefully subtracting 1, except for identical words
		res = editM[len(str2)][len(str1)]
		if res == 0:
			return res
		else:
			return res-1


#ed = EditDistance()

