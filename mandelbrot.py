from PIL import Image
from time import strftime

max_iteration = 1000
x_center = -1.0
y_center = 0.0
size = 300

def make_grid(size):
    for x in range(0, size):
        for y in range(0, size):
            yield x, y

def mandelbrot(x, y):
    return (300 - x, 300 - y, 0)

def generate_filename():
    stamp = strftime("%Y-%m-%d-%H-%M-%S")
    return "images/mandelbrot-{0}.png".format(stamp)

im = Image.new("RGB", (size, size))

for x, y in make_grid(size):
    red, green, blue = mandelbrot(x, y)
    im.putpixel( (x, y), (red, green, blue))

filename = generate_filename()

im.save(filename, "PNG")



