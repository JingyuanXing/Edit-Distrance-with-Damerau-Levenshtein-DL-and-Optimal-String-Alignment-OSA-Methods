#!/usr/bin/python

def calculateOSADistance(raw, dic):
		"""
			take two strings and calculate their OSA Distance for task 2 
			return an integer which is the distance
		"""
		editM = [[0 for i in range(len(raw)+1)] for j in range(len(dic)+1)]
		for i in range(len(raw)+1):
			for j in range(len(dic)+1):
				if i == 0 and j == 0:
					editM[j][i] = 0
				elif i == 0 and j > 0:
					editM[j][i] = j
				elif i > 0 and j == 0:
					editM[j][i] = i
				else: # i >= 1, j >= 1
					if raw[i-1] == dic[j-1]:
						temp = 0
					else:
						temp = 1

					if raw[i-2] == dic[j-1] and raw[i-1] == dic[j-2]:
						editM[j][i] = min(editM[j][i-1]+1, #deletion
									  editM[j-1][i]+1, #insertion
									  editM[j-1][i-1]+temp, #substitution
									  editM[j-2][i-2]+1) # transposition
					else: 
						editM[j][i] = min(editM[j][i-1]+1, #deletion
										  editM[j-1][i]+1, #insertion
										  editM[j-1][i-1]+temp) # substitution

		return editM[len(dic)][len(raw)]

def task4(dictionary, raw):
	"""
	TODO:
		implement your optimized edit distance function for task 4 here
		dictionary : path of dictionary.txt file 
		raw: path of raw.txt file
		return : a list of min_distance of each word in the raw.txt 
		compared with words in the dictonary 
	example return result : [0,1,0,2]
	"""
	with open(raw) as r:
		rawContent = r.readlines()
	rawContent = [x.strip() for x in rawContent]
	with open(dictionary) as d:
		dictionaryContent = d.readlines()
	dictionaryContent = [x.strip() for x in dictionaryContent]
	
	result = []
	for word in rawContent:
		
		editD = len(word)
		for dic in dictionaryContent:
			print(calculateOSADistance(word, dic))
			editD = min(editD, calculateOSADistance(word, dic))
		result.append(editD)
		# print(result)

	return result

task4('dictionary.txt', 'raw.txt')