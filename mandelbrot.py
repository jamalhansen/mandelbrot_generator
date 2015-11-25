from PIL import Image

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

im = Image.new("RGB", (size, size))

for x, y in make_grid(size):
    red, green, blue = mandelbrot(x, y)
    im.putpixel( (x, y), (red, green, blue))

im.save("mandelbrot.png", "PNG")



