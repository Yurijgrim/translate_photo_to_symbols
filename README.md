# translate_photo_to_symbols
Конвертирование изображения в символы

Пример использования:
_____________________________________
 
	t = Transform()
	from time import sleep

	name_image = "image.png" //.jpeg // .jpg // ..
	width_image_in_px = 600


	t.create_console_invert(name_image, width_image_in_px)
	t.create_console(name_image, width_image_in_px)
	t.create_console_color(name_image, width_image_in_px)


__________________________________________

Также есть возможность доработать или изменить на своё усмотрение.
Вы можете запустить анимацию из набора данных.

__________________________________________


list_image = ['im1.png','im2.png','im3.png','im4.png', 'im5.png']
t = Transform()
t.animation_console(list_imgage, fps=0.5, loop_count=0, width=200)

____________________________________________

Но необходимо знать что изображения должны быть одинаковые по ширине в пикселях.
