# -*- coding: utf-8 -*

from math import *

class French_Entropy():
	'''Je cherche à calculer l'entropie de la fable de la Fontaine,
	je ne vais compter ni les espaces, ni la ponctuation, ni les
	caractères spéciaux.'''

	def __init__(self):
		self.fable = "MaitreCorbeausurunarbrepercheTenaitensonbecunfromageMaitreRenardparlodeurallecheLuitintapeuprescelangageEtbonjourMonsieurduCorbeauQuevousetesjoliquevousmesemblezbeauSansmentirsivotreramageSerapporteavotreplumageVouseteslePhénixdeshotesdecesboisAcesmotsleCorbeaunesesentpasdejoieEtpourmontrersabellevoixIlouvreunlargebeclaissetombersaproieLeRenardsensaisitetditMonbonMonsieurApprenezquetoutflatteurVitauxdepensdeceluiquilecouteCetteleconvautbienunfromagesansdouteLeCorbeauhonteuxetconfusJuramaisunpeutardquonnelyprendraitplus".upper()
		self.texte = list(self.fable)
		self.unigram_correspondance = {"A" : 0, "B" : 1, "C" : 2, "D" : 3, "E" : 4, "F" : 5, "G" : 6, "H" : 7, "I" : 8, "J" : 9, "K" : 10, "L" : 11, "M" : 12, "N" : 13, "O" : 14, "P" : 15, "Q" : 16, "R" : 17, "S" : 18, "T" : 19, "U" : 20, "V" : 21, "W" : 22, "X" : 23, "Y" : 24, "Z" : 25}
		self.unigram_freq = self.freq_unigrame_calcul()
		self.digram_correspondance = self.digram_corres_calcul()
		self.digram_freq = self.freq_digrame_calcul()
		self.entropie_unigrame = self.entropie_unigrame_calcul()
		self.entropie_digrame = self.entropie_digrame_calcul()

	def digram_corres_calcul(self):
		'''Donne la correspondance des digrammes'''
		#generates the letters
		letters = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
		#generates the digrams
		digrames = []
		for i in range(26):
			for j in range(26):
				digrames = digrames + [letters[i]+letters[j]]
		numbers = [i for i in range(26**2)]
		digram_corres = {i : k for (i,k) in zip(digrames,numbers)}
		return(digram_corres)

	def entropie_unigrame_calcul(self):
		'''Calcul de l'entropie du texte avec les unigrammes'''
		#calcul de l'entropie en base 2
		entropie = 0
		for i in range(len(self.unigram_freq)):
			freq = self.unigram_freq[i]
			freqlogfreq = 0 if freq == 0 else freq*log(freq,2)
			entropie = entropie - freqlogfreq
		return(entropie)

	def entropie_digrame_calcul(self):
		'''Calcul de l'entropie du texte avec les unigrammes"'''
		#caclul de l'entropie en base 2
		entropie = 0
		for i in range(len(self.digram_freq)):
			#freq1 = self.unigram_freq[self.unigram_correspondance.get(texte[i],0)]
			freq2 = self.digram_freq[i]
			freq2logfreq2 = 0 if freq2 == 0 else freq2*log(freq2,2)
			entropie = entropie - freq2logfreq2
		for j in range(len(self.unigram_freq)):
			freq = self.unigram_freq[j]
			freqlogfreq = 0 if freq == 0 else freq*log(freq,2)
			entropie = entropie + freqlogfreq
		return(entropie)

	def freq_unigrame_calcul(self):
		'''Calcul des fréquences des lettres'''
		nb_lettres = 0
		unigram_freq = [0]*26
		for i in range(len(self.texte)):
			nb_lettres += 1
			unigram_freq[self.unigram_correspondance.get(self.texte[i],0)] +=1
		for i in range(len(unigram_freq)):
			unigram_freq[i] = unigram_freq[i]/nb_lettres
		return(unigram_freq)

	def freq_digrame_calcul(self):
		'''Calcul des fréquences des digrammes'''
		nb_lettres = 0
		digram_freq = [0]*(26**2)
		for t in range(len(self.texte)-1):
			nb_lettres += 1
			digram_freq[self.digram_correspondance.get(self.texte[t]+self.texte[t+1],0)] +=1
		for i in range(len(digram_freq)):
			digram_freq[i] = digram_freq[i]/nb_lettres
		return(digram_freq)
