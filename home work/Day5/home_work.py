class Basket:
	def __init__(self, area):
		self.area = area
		self.storage = []

	def status(self):
		self.busy = len(self.storage)
		self.free = self.area - self.busy

	def put_in(self, obj):
		self.status()
		if len(obj) <= self.free:
			self.storage += obj
			return True
		else:
			print('Данный объект не влезает в меня')
			return False

class Packet(Basket):

	def print_status(self):
		print('Я уже заполнен на {Now} позиций из {Max}'.format(Now = self.busy, Max = self.area))

	def status(self):
		self.busy = len(self.storage)
		self.free = self.area - self.busy
		self.print_status()

	def put_in(self, obj):
		# self.obj = obj
		put_overload = super().put_in(obj)
		if not put_overload :
			self.storage += obj[:self.free]
		self.status()



litle_basket = Basket(10)
litle_basket.put_in('qwerty')
print(litle_basket.storage)

litle_basket.put_in('123456')
print(litle_basket.storage)

litle_packet = Packet(10)
litle_packet.put_in('qwerty')
print(litle_packet.storage)

litle_packet.put_in('123456')
print(litle_packet.storage)