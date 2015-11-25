from PIL import Image
from time import strftime

max_iteration = 1000
size = 300

def make_grid(size):
    """Iterates over all the points in a grid"""
    for x in range(size):
        for y in range(size):
            yield x, y

def mandelbrot(x, y):
    """Translates x y coordinates to an RGB value"""
    a, b = (0.0, 0.0)
    iteration = 0

    x_re = float(x - size/2.0) * 4.0/size
    x_im = float(y - size/2.0) * 4.0/size

    #complex_number = (x_re, x_im)

    while iteration < max_iteration and (a**2 + b**2) <= 4.0:
        a, b = ((a**2) - (b**2) + x_re, (2 * a * b) + x_im)
        iteration += 1

    if iteration < max_iteration:
        r_val = iteration % 255
        g_val = iteration % 255
        b_val = iteration % 255

        return (r_val, g_val, b_val)
    else:
        return (0,0,0)


def generate_filename():
    """Creates a filename with a timestamp"""
    stamp = strftime("%Y-%m-%d-%H-%M-%S")
    return "images/mandelbrot-{0}.png".format(stamp)

im = Image.new("RGB", (size, size))

for x, y in make_grid(size):
    red, green, blue = mandelbrot(x, y)
    im.putpixel((x, y), (red, green, blue))

filename = generate_filename()

im.save(filename, "PNG")

im.show()


