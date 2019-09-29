#!/usr/bin/python

class EditDistance():
	
	def __init__(self):
		"""
		Do not change this
		"""
	
	def calculateLevenshteinDistance(self, str1, str2):
		"""
		TODO:
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
						mismatch = 0
					else:
						mismatch = 1
					editM[j][i] = min(editM[j][i-1]+1, editM[j-1][i]+1, editM[j-1][i-1]+mismatch)

		return editM[len(str2)][len(str1)]

		
	def calculateOSADistance(self, str1, str2):
		"""
		TODO:
			take two strings and calculate their OSA Distance for task 2 
			return an integer which is the distance
		"""
		raise NotImplementedError

		
	def calculateDLDistance(self, str1, str2):
		"""
		TODO:
			take two strings and calculate their DL Distance for task 3 
			return an integer which is the distance
		"""
		raise NotImplementedError



ed = EditDistance()
print(ed.calculateLevenshteinDistance("colleg", "college"))