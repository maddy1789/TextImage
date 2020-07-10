from PIL import Image, ImageFont, ImageDraw, ImageEnhance
import string
import collections

font = ImageFont.load_default()


# chars = list(sorted(string.ascii_letters + string.digits + string.punctuation + ' ', reverse=True))
chars = ['#', '?', '%', '.', 'M', '+', '.', '*', ':', ',', '@']

def parse_argument():
    """Argument Parser Function: Get all the argument parsed during runtime"""
    import argparse
    parser = argparse.ArgumentParser(description="Generate Ascii art from an Image File.")
    parser.add_argument("-i", "--image", dest="image", help="Image file path")
    parser.add_argument("-w", "--width", dest="width", type=int, help="Width of Ascii Text. (Default: width of image)")
    args = parser.parse_args()
    
    if not args.image:
        parser.error("Please specify the image file path, use --help for more option")

    return args

def image_to_ascii(img_path, width=None):
    import os
    if os.path.isfile:
        image = None
        try:
            image = Image.open(img_path)
        except Exception as e:
            print("Unable to open Image File {} \n EXCEPTION: \n {}".format(img_path, e))
            return

        if width is not None:
            scale = float(width) / image.size[0]
        else:
            scale = 100

    image_ascii = convert_image(image, width)
    print(image_ascii)

        
def convert_image(image, width):
    image = scale_image(image, width)
    image = convert_to_grayscale(image)

    pixel_to_char = map_pixel(image)
    len_pixel_char = len(pixel_to_char)
    
    image_ascii = [pixel_to_char[index: index + width] for index in range(0, len_pixel_char, width)]
    return "\n".join(image_ascii)


def scale_image(image, width=100):
    (original_width, original_height) = image.size
    aspect_ratio = original_height/float(original_width)
    height  = int(aspect_ratio * width)

    new_image = image.resize((width, height))
    return new_image


def convert_to_grayscale(image):
    return image.convert('L')


def map_pixel(image, range_width=25):
    pixel_in_image = list(image.getdata())
    pixel_to_char = [chars[int(pixel_value/range_width)] for pixel_value in pixel_in_image]
    return "".join(pixel_to_char)

if __name__ == "__main__":
    args = parse_argument()
    image_to_ascii(args.image, 100)

    

