import glob
from os import getcwd
from os.path import basename, join

import cairosvg
import PyPDF2


def rotate(file_path, angle):
    file = PyPDF2.PdfFileReader(open(file_path, 'rb'))
    file_output = PyPDF2.PdfFileWriter()
    for page_num in range(file.numPages):
        page = file.getPage(page_num)
        page.rotateClockwise(angle)
        file_output.addPage(page)
    with open(file_path, 'wb') as f:
        file_output.write(f)


def convert(dir):
    path_list = []
    for ext in ('*.svg'):
        path_list.extend(glob.glob(join(dir, ext)))

    for file in path_list:
        print(file + 'を変換します。')
        converted_file_name = (basename(file).split('.', 1)[0]) + '.pdf'
        cairosvg.svg2pdf(url=file, write_to=converted_file_name)
        print(converted_file_name + 'を出力しました。')
        rotate(converted_file_name, 270)
        print(converted_file_name + 'を回転しました。')
    return


def main():
    image_path = getcwd() + '/images'
    print(image_path + 'のファイルが対象です。')
    convert(image_path)

if __name__ == "__main__":
    main()