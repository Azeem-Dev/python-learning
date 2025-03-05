from PIL import Image, ImageEnhance, ImageFilter
import os

photos_in = os.path.join(os.getcwd(), 'images_to_edit')
photos_out = os.path.join(os.getcwd(), 'edited_images')

if not os.path.exists(photos_out):
    os.makedirs(photos_out)

for filename in os.listdir(photos_in):
    img = Image.open(f'{photos_in}/{filename}')

    edit = img.filter(ImageFilter.SHARPEN).convert("L")
    # .rotate(-90)

    factor = 1.5

    enhacer = ImageEnhance.Contrast(edit)

    edit = enhacer.enhance(factor)

    clean_name = os.path.splitext(filename)[0]

    edit.save(os.path.join(photos_out, f"{clean_name}_edited.jpg"))
