import codecs
import glob
from os import getcwd
from os.path import basename, join, splitext

import svgutils
from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF


def rotate(path):
    with codecs.open(path, 'r', 'utf-8', 'ignore') as f:
        svg_text = f.read()
    print(svg_text)
    svg = svgutils.transform.fromstring(svg_text)
    svg.rotate(-90)
    figure = svgutils.compose.Figure(svg.height, svg.width, svg)
    figure.save(path)
    return


def convert_pdf(path):
    filename = path
    filename_without_ext = splitext(basename(path))[0]
    drawing = svg2rlg(filename)
    renderPDF.drawToFile(drawing, filename_without_ext + '.pdf')
    return


def convert(dir):
    path_list = []
    for ext in ('*.svg'):
        path_list.extend(glob.glob(join(dir, ext)))

    for i in path_list:
        print(i)
        rotate(i)
        convert(i)
    return


image_path = getcwd() + '/images'
print(image_path)
convert(image_path)
