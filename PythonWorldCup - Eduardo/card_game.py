players_dic = {}

import random
class deck(list):
	def __init__(self):
		super(deck, self).__init__()

	def shuffle(self):
		random.shuffle(self)

	def distribute(self, *players):
		i = 0
		while len(self) > 0:
			for player in players:
				try:
					player.deck.append(self.pop(0))
				except:
					break

	def pop_card(self, *, drawFrom = 'top'):
		if drawFrom.lower() == 'top':
			n = 0
		elif drawFrom.lower() == 'bottom':
			n = -1
		else:
			n = int(drawFrom%len(self))
		return self.pop(n)

	def insert(self, position, *cards):
		if position.lower() == "top":
			n = 0
		elif position.lower() == "bottom":
			n = len(self)
		else:
			n = int(drawFrom%len(self))
		for card in cards[-1::-1]:
			super(deck,self).insert(n,card)

class player():
	def __init__(self, name = 'player'):
		self.name = name
		i = 2
		while self.name in players_dic:
			self.name = "{} {}".format(name, i)
			i += 1
		self.deck = deck()
		players_dic[self.name] = self

class card():
	def __init__(self, *properties, line = '', name = 'card', image = None, delimiter = ',', **dic_properties):
		if line == '':
			self.name = name
			self.image = image
			self.properties = dic_properties
		else:
			self.properties = {}
			line = line.split(delimiter)
			for i in range(len(properties)):
				if properties[i] == 'name':
					self.name = line[i]
				elif properties[i] == 'image':
					self.image = line[i]
				else:
					self.properties[properties[i]] = line[i]

	def __repr__(self):
		return self.name + ' ' + str(self.properties)

	def max_prop(self):
		stats = {}
		for key in self.properties:
			try: 
				stats[key] = float(self.properties[key])
			except:
				pass
		return max(stats, key=lambda k: stats[k])

