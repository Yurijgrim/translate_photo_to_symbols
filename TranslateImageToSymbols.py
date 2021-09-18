
from PIL import Image
from os import system
from time import sleep

class Transform():
	def __init__(self):
		pass

	def five_parser(self, x):
		if 0 <= x <= 51:
			return 0
		elif 51 < x <= 102:
			return 1
		elif 102 < x <= 153:
			return 2
		elif 153 < x <= 204:
			return 3
		elif 204 < x <= 255:
			return 4

	def write_array_color(self, image):
		image = Image.open(image)
		gray = image.convert('L')
		data = list(gray.getdata())
		new_array_pxl = []
		for pxl in data:
			p = self.five_parser(pxl)
			new_array_pxl.append(p)
		return new_array_pxl

	# symbol_0 = '#', symbol_1 = '.'
	def create_console_color(self, image = None, width = 200,
						 symbol_0 = " ", symbol_1 = ' ',
						 symbol_2 = '.', symbol_3 = 'o', symbol_4 = '#'):
		line = ''
		count = 0
		self.line = width
		self.new = self.write_array_color(image)
		for pxl in self.new:
			if pxl == 0:
				line += symbol_0
			elif pxl == 1:
				line += symbol_1
			elif pxl == 2:
				line += symbol_2
			elif pxl == 3:
				line += symbol_3
			elif pxl == 4:
				line += symbol_4
			count += 1
			if count == self.line:
				count = 0

				line += '\n'
		print(line)


	def create_console_invert(self, image = None, width = 200,
						 symbol_0 = "#", symbol_1 = 'o',
						 symbol_2 = '.', symbol_3 = ' ', symbol_4 = ' '):
		line = ''
		count = 0
		self.line = width
		self.new = self.write_array_color(image)
		for pxl in self.new:
			if pxl == 0:
				line += symbol_0
			elif pxl == 1:
				line += symbol_1
			elif pxl == 2:
				line += symbol_2
			elif pxl == 3:
				line += symbol_3
			elif pxl == 4:
				line += symbol_4
			count += 1
			if count == self.line:
				count = 0

				line += '\n'
		print(line)


	def write_array(self, image):
		image = Image.open(image)
		gray = image.convert('L')
		bw = gray.point(lambda x: 1 if x < 128 else 0)
		data = list(bw.getdata())
		# gray.show()
		return data


	def create_console(self, image = None, width = 200, symbol_0 = '#', symbol_1 = '.'):
		line = ''
		count = 0
		self.line = width
		self.new = self.write_array(image)
		for pxl in self.new:
			if pxl == 0:
				line += symbol_0
			elif pxl == 1:
				line += symbol_1
			count += 1
			if count == self.line:
				count = 0
				print(line)
				line = ''

	def clear_console(self):
		system('cls')

	def animation_console(self, array_images = None, width = 200, fps = 10, loop_count = 10):
		self.imgs = []
		for im in array_images:
			self.imgs.append(im)
		print(self.imgs)
		count = 0
		if loop_count == -1 or loop_count == 0:
			while True:
				for im in self.imgs:
					self.create_console(image=im, width=width)
					sleep(fps)
					self.clear_console()

		elif count < loop_count:
			while count <= loop_count:
				for im in self.imgs:
					self.create_console(image=im, width=width)
					sleep(fps)
					self.clear_console()
					count += 1
					if count == loop_count:
						return 0

if __name__ == '__main__':

	t = Transform()
	from time import sleep

	nf = input('NAME FILE PNG or JPG or GIF:   ')
	w = int(input('HIS WIDTH :   '))


	t.create_console_invert(nf, w)
	sleep(5)
	t.create_console(nf, w)
	sleep(10)
	t.create_console_color(nf, w)


# t.create_console('test00.png', width=1200)
# t.create_console_color('test00.png', width=1200)
# # sleep(10)
# t.create_console('test3.png', width=1080)
# t.create_console_color('test3.png', width=1080)
# # sleep(10)
# t.create_console('test4.png', width=1200)
# t.create_console_color('test4.png', width=1200)
# # sleep(10)
# t.create_console('test5.png', width=900)
# t.create_console_color('test5.png', width=900)
# # sleep(10)


#
# name_file = input('Name file Image:  ')
# size_width = int(input('width image:  '))
# t.create_console(image=name_file, width=size_width, symbol_0='.',symbol_1='0')

# list_img = ['im1.png','im2.png','im3.png','im4.png', 'im5.png']
# t = Transform()
# t.animation_console(list_img, fps=0.5, loop_count=0, width=200)
#

input()
input('EXIT ....')


