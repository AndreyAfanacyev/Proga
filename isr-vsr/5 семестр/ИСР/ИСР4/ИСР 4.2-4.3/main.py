import random
import os
import segno

def create_qrcode(text: str):
    qrcode = segno.make(text, version=2, error='h')
    qrcode.show()

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = '#%02x%02x%02x' % (r, g, b)
    return color

def create_colored_qrcode(text: str):
    qrcode = segno.make(text, version=2, error='h')
    qrcode.save('qrcode.png', scale=10, dark=random_color(), data_dark=random_color())
    os.system('qrcode.png')

if __name__ == '__main__':
    create_qrcode('Hello!')
    create_colored_qrcode('Hello!')
