# -*- coding: utf-8 -*

class English_Generator():
	'''Generates an english text based on digramm frequencies
	available in Shannon's article (Math Comp theory)'''

	def __init__(self):
		'''My table is 100 inches long baby.
		Numbers from 0 to 270.'''
		self.rand_table = [113, 101, 119, 116, 56, 222, 205, 51, 151, 92, 119, 5, 91, 136, 169, 89, 126, 157, 162, 25, 159, 148, 199, 108, 65, 86, 196, 251, 157, 43, 236, 1, 90, 143, 97, 66, 203, 159, 244, 256, 217, 241, 211, 186, 85, 12, 198, 232, 238, 78, 38, 101, 84, 160, 155, 146, 72, 150, 79, 82, 19, 37, 206, 207, 242, 225, 130, 146, 52, 51, 102, 80, 267, 183, 12, 54, 94, 113, 194, 142, 126, 121, 187, 79, 189, 30, 248, 15, 193, 151, 68, 135, 211, 64, 143, 78, 19, 79, 199, 226]
		# position in table at the start
		self.n = 0

	def rand_result(self):
		'''Picks a number in the random table'''
		res = self.rand_table[self.n]
		# Sets the loop, the size of the table is 100 units
		if self.n >=100 :
			self.n -= 100
		return(res)

	def switcher_zero_order(self, x):
		''' How to transform a table into a dictionnary
		I've made a table of 270 units, lol = ["A"]*10 + 
		["B"]*10 + ect... and then
		fields = { i : lol[i] for i in range(len(lol))}'''
		switcher = {0: 'A', 1: 'A', 2: 'A', 3: 'A', 4: 'A', 5: 'A', 6: 'A', 7: 'A', 8: 'A', 9: 'A',
		10: 'B', 11: 'B', 12: 'B', 13: 'B', 14: 'B', 15: 'B', 16: 'B', 17: 'B', 18: 'B', 19: 'B',
		20: 'C', 21: 'C', 22: 'C', 23: 'C', 24: 'C', 25: 'C', 26: 'C', 27: 'C', 28: 'C', 29: 'C',
		30: 'D', 31: 'D', 32: 'D', 33: 'D', 34: 'D', 35: 'D', 36: 'D', 37: 'D', 38: 'D', 39: 'D',
		40: 'E', 41: 'E', 42: 'E', 43: 'E', 44: 'E', 45: 'E', 46: 'E', 47: 'E', 48: 'E', 49: 'E',
		50: 'F', 51: 'F', 52: 'F', 53: 'F', 54: 'F', 55: 'F', 56: 'F', 57: 'F', 58: 'F', 59: 'F',
		60: 'G', 61: 'G', 62: 'G', 63: 'G', 64: 'G', 65: 'G', 66: 'G', 67: 'G', 68: 'G', 69: 'G',
		70: 'H', 71: 'H', 72: 'H', 73: 'H', 74: 'H', 75: 'H', 76: 'H', 77: 'H', 78: 'H', 79: 'H',
		80: 'I', 81: 'I', 82: 'I', 83: 'I', 84: 'I', 85: 'I', 86: 'I', 87: 'I', 88: 'I', 89: 'I',
		90: 'J', 91: 'J', 92: 'J', 93: 'J', 94: 'J', 95: 'J', 96: 'J', 97: 'J', 98: 'J', 99: 'J',
		100: 'K', 101: 'K', 102: 'K', 103: 'K', 104: 'K', 105: 'K', 106: 'K', 107: 'K', 108: 'K', 109: 'K',
		110: 'L', 111: 'L', 112: 'L', 113: 'L', 114: 'L', 115: 'L', 116: 'L', 117: 'L', 118: 'L', 119: 'L',
		120: 'M', 121: 'M', 122: 'M', 123: 'M', 124: 'M', 125: 'M', 126: 'M', 127: 'M', 128: 'M', 129: 'M',
		130: 'N', 131: 'N', 132: 'N', 133: 'N', 134: 'N', 135: 'N', 136: 'N', 137: 'N', 138: 'N', 139: 'N',
		140: '0', 141: '0', 142: '0', 143: '0', 144: '0', 145: '0', 146: '0', 147: '0', 148: '0', 149: '0',
		150: 'P', 151: 'P', 152: 'P', 153: 'P', 154: 'P', 155: 'P', 156: 'P', 157: 'P', 158: 'P', 159: 'P',
		160: 'Q', 161: 'Q', 162: 'Q', 163: 'Q', 164: 'Q', 165: 'Q', 166: 'Q', 167: 'Q', 168: 'Q', 169: 'Q',
		170: 'R', 171: 'R', 172: 'R', 173: 'R', 174: 'R', 175: 'R', 176: 'R', 177: 'R', 178: 'R', 179: 'R',
		180: 'S', 181: 'S', 182: 'S', 183: 'S', 184: 'S', 185: 'S', 186: 'S', 187: 'S', 188: 'S', 189: 'S',
		190: 'T', 191: 'T', 192: 'T', 193: 'T', 194: 'T', 195: 'T', 196: 'T', 197: 'T', 198: 'T', 199: 'T',
		200: 'U', 201: 'U', 202: 'U', 203: 'U', 204: 'U', 205: 'U', 206: 'U', 207: 'U', 208: 'U', 209: 'U',
		210: 'V', 211: 'V', 212: 'V', 213: 'V', 214: 'V', 215: 'V', 216: 'V', 217: 'V', 218: 'V', 219: 'V',
		220: 'W', 221: 'W', 222: 'W', 223: 'W', 224: 'W', 225: 'W', 226: 'W', 227: 'W', 228: 'W', 229: 'W',
		230: 'X', 231: 'X', 232: 'X', 233: 'X', 234: 'X', 235: 'X', 236: 'X', 237: 'X', 238: 'X', 239: 'X',
		240: 'Y', 241: 'Y', 242: 'Y', 243: 'Y', 244: 'Y', 245: 'Y', 246: 'Y', 247: 'Y', 248: 'Y', 249: 'Y',
		250: 'Z', 251: 'Z', 252: 'Z', 253: 'Z', 254: 'Z', 255: 'Z', 256: 'Z', 257: 'Z', 258: 'Z', 259: 'Z',
		260: " ", 261: " ", 262: " ", 263: " ", 264: " ", 265: " ", 266: " ", 267: " ", 268: " ", 269: " "}
		# Return the value in the switcher or else
		return(switcher.get(x, 'Not Found'))

	def gen_zero_order(self):
		'''Generates an english sentence with the 26 letters of the
		latin alphabet + space equiprobably distributed. Generate
		64 symbols for some reason.'''
		#initalization
		self.n = 0
		res = ""
		for i in range(64):
			res = res + self.switcher_zero_order(self.rand_result())
			self.n += 1
		return(res)

	def switcher_first_order(self, x):
		'''Now the letters appear proportionnaly to their frequencies
		in the english language.'''
		switcher = {0: 'E', 1: 'E', 2: 'E', 3: 'E', 4: 'E', 5: 'E', 6: 'E', 7: 'E', 8: 'E', 9: 'E', 10: 'E', 11: 'E', 12: 'E', 13: 'E', 14: 'E', 15: 'E', 16: 'E', 17: 'E', 18: 'E', 19: 'E', 20: 'E', 21: 'E', 22: 'E', 23: 'E', 24: 'E', 25: 'E', 26: 'E', 27: 'E',
		28: 'T', 29: 'T', 30: 'T', 31: 'T', 32: 'T', 33: 'T', 34: 'T', 35: 'T', 36: 'T', 37: 'T', 38: 'T', 39: 'T', 40: 'T', 41: 'T', 42: 'T', 43: 'T', 44: 'T', 45: 'T', 46: 'T', 47: 'T', 48: 'T',
		49: 'A', 50: 'A', 51: 'A', 52: 'A', 53: 'A', 54: 'A', 55: 'A', 56: 'A', 57: 'A', 58: 'A', 59: 'A', 60: 'A', 61: 'A', 62: 'A', 63: 'A', 64: 'A', 65: 'A', 66: 'A',
		67: 'O', 68: 'O', 69: 'O', 70: 'O', 71: 'O', 72: 'O', 73: 'O', 74: 'O', 75: 'O', 76: 'O', 77: 'O', 78: 'O', 79: 'O', 80: 'O', 81: 'O', 82: 'O', 83: 'O',
		84: 'I', 85: 'I', 86: 'I', 87: 'I', 88: 'I', 89: 'I', 90: 'I', 91: 'I', 92: 'I', 93: 'I', 94: 'I', 95: 'I', 96: 'I', 97: 'I', 98: 'I', 99: 'I', 100: 'I',
		101: 'N', 102: 'N', 103: 'N', 104: 'N', 105: 'N', 106: 'N', 107: 'N', 108: 'N', 109: 'N', 110: 'N', 111: 'N', 112: 'N', 113: 'N', 114: 'N', 115: 'N', 116: 'N',
		117: 'S', 118: 'S', 119: 'S', 120: 'S', 121: 'S', 122: 'S', 123: 'S', 124: 'S', 125: 'S', 126: 'S', 127: 'S', 128: 'S', 129: 'S', 130: 'S', 131: 'S',
		132: 'R', 133: 'R', 134: 'R', 135: 'R', 136: 'R', 137: 'R', 138: 'R', 139: 'R', 140: 'R', 141: 'R', 142: 'R', 143: 'R', 144: 'R', 145: 'R',
		146: 'H', 147: 'H', 148: 'H', 149: 'H', 150: 'H', 151: 'H', 152: 'H', 153: 'H', 154: 'H', 155: 'H', 156: 'H',
		157: 'L', 158: 'L', 159: 'L', 160: 'L', 161: 'L', 162: 'L', 163: 'L', 164: 'L', 165: 'L',
		166: 'D', 167: 'D', 168: 'D', 169: 'D', 170: 'D', 171: 'D', 172: 'D', 173: 'D', 174: 'D',
		175: 'C', 176: 'C', 177: 'C', 178: 'C', 179: 'C', 180: 'C', 181: 'C',
		182: 'U', 183: 'U', 184: 'U', 185: 'U', 186: 'U', 187: 'U',
		188: 'M', 189: 'M', 190: 'M', 191: 'M', 192: 'M', 193: 'M',
		194: 'F', 195: 'F', 196: 'F', 197: 'F', 198: 'F',
		199: 'P', 200: 'P', 201: 'P', 202: 'P', 203: 'P',
		204: 'G', 205: 'G', 206: 'G', 207: 'G',
		208: 'W', 209: 'W', 210: 'W', 211: 'W',
		212: 'Y', 213: 'Y', 214: 'Y', 215: 'Y',
		216: 'B', 217: 'B', 218: 'B',
		219: 'V', 220: 'V',
		221: 'K',
		222: 'X',
		223: ' ', 224: ' ', 225: ' ', 226: ' ', 227: ' ', 228: ' ', 229: ' ', 230: ' ', 231: ' ', 232: ' ', 233: ' ', 234: ' ', 235: ' ', 236: ' ', 237: ' ', 238: ' ', 239: ' ', 240: ' ', 241: ' ', 242: ' ', 243: ' ', 244: ' ', 245: ' ', 246: ' ', 247: ' ', 248: ' ', 249: ' ', 250: ' ', 251: ' ', 252: ' ', 253: ' ', 254: ' ', 255: ' ', 256: ' ', 257: ' ', 258: ' ', 259: ' ', 260: ' ', 261: ' ', 262: ' ', 263: ' ', 264: ' ', 265: ' ', 266: ' ', 267: ' ', 268: ' '}
		# Return the value in the switcher or else
		return(switcher.get(x, 'Not Found'))

	def gen_first_order(self):
		'''Genrates 64 english characters, including spaces'''
		self.n = 0
		res = ""
		for i in range(64):
			res = res + self.switcher_first_order(self.rand_result())
			self.n += 1
		return(res)
