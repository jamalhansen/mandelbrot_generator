#! /usr/bin/env python3

"""This script will generate a PNG image of the Mandelbrot set"""

from PIL import Image
import time
import random
import math

max_iteration = 1000
size = 500

def make_grid(size):
    """Iterates over all the points in a grid"""
    for x in range(size):
        for y in range(size):
            yield x, y

def euclidean(x, y):
    return int(math.sqrt(x**2 + y**2))

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

    if iteration == max_iteration:
        return (255,255,255)
    else:
        dist = euclidean(x,y)
        color_val = (iteration * 10) % 255

        r_val = color_val
        g_val = color_val
        b_val = color_val

        return (r_val, g_val, b_val)

def generate_filename():
    """Creates a filename with a timestamp"""
    stamp = time.strftime("%Y-%m-%d-%H-%M-%S")
    return "images/mandelbrot-{0}.png".format(stamp)

im = Image.new("RGB", (size, size))

for x, y in make_grid(size):
    red, green, blue = mandelbrot(x, y)
    im.putpixel((x, y), (red, green, blue))

filename = generate_filename()

im.save(filename, "PNG")

