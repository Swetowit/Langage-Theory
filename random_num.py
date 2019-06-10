# -*- coding: utf-8 -*



class Random_Gen():
	'''Générateur de paires de symboles A, B et C.
	P(A) = 9/27 33 %
	P(B) = 16/27 60 %
	P(C) = 2/27 7 %
	PA(A) = 0
	PA(B) = 4/5
	PA(C) = 1/5
	PB(A) = 1/2
	PB(B) = 1/2
	PB(C) = 0
	PC(A) = 1/2
	PC(B) = 2/5
	PC(C) = 1/10'''
	def __init__(self):
		self.lotterie = [1,2,4,2,9,6,3,5,2,7,7,4,6,0,8,0,1,5,4,9,0,0,7,9,3,2,8,3,5,4,6,1,2,1,8,9,5,7,8,2,6,3,9,4,0,5,8,1,2,8]
		#Le numéro est la position à laquelle on se trouve dans le tableau
		#lotterie. Il est incrémenté de 2 à chaque passage.
		self.numero = 0

	def tir_lotterie(self):
		'''Fait un tirage de lotterie. On prend des nombres à deux chiffres'''
		return(self.lotterie[self.numero]*10+self.lotterie[self.numero+1])

	def quel_symbole_init(self):
		'''Dit quelle paire va être générée à partir du tir dans la lotterie.
		On tire au sort, en fonction de l'intervalle dans lequel on atterit,
		on retourne une certaine paire de symboles.'''
		tir = self.tir_lotterie()
		if tir<=32 :
			symbole = "A"
		elif tir>=33 and tir<=92 :
			symbole = "B"
		elif tir>=93 and tir<=100 :
			symbole = "C"
		self.numero = 2
		return(symbole)

	def quel_symbole(self, symbole):
		'''Trouve le symbole suivant en fonction du numéro dans la chaine
		et du symbole précédent.
		Pourvu qu'on sache le symbole précédent, on procède à des tirages au sort.'''
		if symbole == "A":
			#PA(A) = 0
			#PA(B) = 4/5
			if (self.tir_lotterie() <= 79):
				self.numero +=2
				if self.numero >= 49:
					self.numero -=50
				return("B")
			#PA(C) = 1/5
			elif (self.tir_lotterie() >= 80):
				self.numero +=2
				if self.numero >= 49:
					self.numero -=50
				return("C")
		elif symbole == "B" :
			#PB(A) = 1/2
			if (self.tir_lotterie() <= 49):
				self.numero +=2
				if self.numero >= 49:
					self.numero -=50
				return("A")
			#PB(B) = 1/2
			elif (self.tir_lotterie() >= 50):
				self.numero +=2
				if self.numero >= 49:
					self.numero -=50
				return("B")
			#PB(C) = 0
		elif symbole == "C" :
			#PC(A) = 1/2
			if (self.tir_lotterie() <= 49):
				self.numero +=2
				if self.numero >= 49:
					self.numero -=50
				return("A")
			#PC(B) = 2/5
			elif (self.tir_lotterie() >= 50) and (self.tir_lotterie()<=89):
				self.numero +=2
				if self.numero >= 49:
					self.numero -=50
				return("B")
			#PC(C) = 1/10
			elif (self.tir_lotterie() >= 90):
				self.numero +=2
				if self.numero >= 49:
					self.numero -=50
				return("C")
		return(res)

	def generateur(self):
		'''Génère 60 symboles'''
		symboles = ""
		last_symbol = ""
		# Premier tirage
		symboles = symboles + self.quel_symbole_init()
		# Tous les autres tirages
		for i in range(58):
			last_symbol = list(symboles)[-1]
			symboles = symboles + self.quel_symbole(last_symbol)
		return(symboles)