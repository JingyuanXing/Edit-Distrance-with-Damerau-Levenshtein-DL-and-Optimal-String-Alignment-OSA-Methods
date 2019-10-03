#!/usr/bin/python


class TrieNode():

	def __init__(self):
		self.children = [None]*26
		self.endOfWord = False
		# add a single matrix row, of current letter from the dict word, 
		# with respect to the current raw word
		self.editRow = []
		self.temp = 0

class Trie():

	def __init__(self):
		self.root = self.createNode()

	def createNode(self):
		# return new trie node initialized to None
		return TrieNode()

	def charToIndex(self, ch):
		# return the index 0-25 of this charater of the dict word
		return ord(ch) - ord('a')

	def addNode(self, word_dict):
		# start to look down from root of Trie
		current_at = self.root
		# loop through each character of the word from dictionary
		for ch_position in range(len(word_dict)): 
			index = self.charToIndex(word_dict[ch_position])

			# if current character in the 26-cell-node is None,
			# meaning it's not added yet, create a new node for it
			if current_at.children[index] == None:
				current_at.children[index] = self.createNode()
			# change current_at to look at it's children (the list of 26 cells)
			current_at = current_at.children[index]
		# mark last node as leaf, when finished with this word from dictionary
		current_at.endOfWord = True


	def additionalDepth(self, current_at):
		if current_at.endOfWord == True:
			print("here")
			return 0
		compareList = []
		for i in range(len(current_at.children)):
			if current_at.children[i] != None:
				print(current_at.children[i])
				n = 1 + self.additionalDepth(current_at.children[i])
				compareList.append(n)
		result = min(compareList)

		return result

	def updateNode(self, word_raw):
		# start to look down the Trie from root
		current_at = self.root
		# initialize the first row
		current_at.editRow = []
		current_at.editRow.append([i for i in range(len(word_raw)+1)])
		# loop through each character of the word from raw data
		
		additional_length = 0
		for ch_position in range(len(word_raw)):
			index = self.charToIndex(word_raw[ch_position])
			print(current_at.editRow)
			print(word_raw[ch_position])

			# if None, meaning the current character does not match the dictionary structure 
			if current_at.children[index] == None:
				current_at.temp = 1
			# the current character IS a match
			else:
				current_at.temp = 0
			print("temp: ", current_at.temp)

			# add a row
			current_at.editRow.append([0 for i in range(len(word_raw)+1)])
			# initialize first column of each row
			current_at.editRow[-1][0] = ch_position+1
			for ch_position in range(len(word_raw)):
				current_at.editRow[-1][ch_position+1] = min(current_at.editRow[-1][ch_position]+1,
					                                        current_at.editRow[-2][ch_position+1]+1,
					                                        current_at.editRow[-2][ch_position]+current_at.temp)

			# change current_at to look at it's children (the list of 26 cells)
			try:
				current_at.children[index].editRow = current_at.editRow
				current_at = current_at.children[index]
			except:
				continue

		additional_length = self.additionalDepth(current_at)

		editD = current_at.editRow[-1][-1] + additional_length
		return editD


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
		implement your optimized edit distance function for task 4 here
		dictionary : path of dictionary.txt file 
		raw: path of raw.txt file
		return : a list of min_distance of each word in the raw.txt 
		compared with words in the dictonary 
	example return result : [0,1,0,2]
	"""

	# read files raw.txt and dictionary.txt
	with open(raw) as r:
		rawContent = r.readlines()
	rawContent = [x.strip() for x in rawContent]
	with open(dictionary) as d:
		dictionaryContent = d.readlines()
	dictionaryContent = [x.strip() for x in dictionaryContent]

	# create the Trie using dictionary words
	# with editRow for each character (node in Trie) initialized as []
	tr = Trie()
	for dic in dictionaryContent:
		tr.addNode(dic)
	
	# update editRow of Trie nodes using current word_raw
	result = []
	for word_raw in rawContent:
		# put current raw word into the Trie,
		# build one row of the matrix at each node of the Trie, corresponding to this raw word (inside the Trie)
		# build edit distance here, by puting the rows into a matrix
		print("DDDDD")
		print(word_raw)
		editD = tr.updateNode(word_raw)
		result.append(editD)
		print(result)

	return result

task4('dictionary.txt', 'raw.txt')



