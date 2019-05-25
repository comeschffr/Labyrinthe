import tkinter as tk
class Labyrinthe:
	def __init__(self, lab, coord):
		self.lab = lab
		self.height = len(lab)
		self.length = len(lab[0])
		self.place = '0'
		self.coord = coord
		while self.place == '0':
			self.movement = input()
			if self.movement == 'z':
				if not self.lab[self.coord[1]-1][self.coord[0]] =='X':
					self.coord[1] -= 1
					self.place == self.lab[self.coord[1]][self.coord[0]]
				else:
					print('Ce déplacement est impossible !')
			elif self.movement == 's':
				if not self.lab[self.coord[1]+1][self.coord[0]] =='X':
					self.coord[1] += 1
					self.place == self.lab[self.coord[1]][self.coord[0]]
				else:
					print('Ce déplacement est impossible !')
			elif self.movement == 'q':
				if not self.lab[self.coord[1]][self.coord[0]-1] =='X':
					self.coord[0] -= 1
					self.place == self.lab[self.coord[1]][self.coord[0]]
				else:
					print('Ce déplacement est impossible !')
			elif self.movement == 'd':
				if not self.lab[self.coord[1]][self.coord[0]+1] =='X':
					self.coord[1] += 1
					self.place == self.lab[self.coord[1]][self.coord[0]]
				else:
					print('Ce déplacement est impossible !')
			else:
				print('La commande entrée est incorecte')
			self.lab[self.coord[1]][self.coord[0]] =='T'
			self.printLab()
			self.lab[self.coord[1]][self.coord[0]] == self.place
		print("C'est gagné !")

		def printLab(self):
			for tupple in self.lab:
				for x in tupple:
					print(x, end =' ')
				print()




coord = [4,1]
liste = [['X','E','X','X','X','X'],['X','0','0','0','0','X'],['X','0','0','X','0','X'],['X','X','X','X','X','X']]
Labyrinthe(liste, coord)
input()