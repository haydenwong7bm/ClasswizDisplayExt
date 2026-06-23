from sys import argv
from os import makedirs
import itertools, fontforge

font_types = ['Display', 'Math']
font_styles = ['X', 'CW']
font_sizes = [''] # ['', 'Small', 'Tiny']

font_list_display = [f'ClassWiz{font_style}DisplayExt{font_size}.sfd' for font_style, font_size in itertools.product(font_styles, font_sizes)]
font_list_math = [f'ClassWiz{font_style}DisplayExt.sfd' for font_style in font_styles]

makedirs('output', exist_ok=True)

for file_in in font_list_display:
    font = fontforge.open(file_in)
    for filetype in ['.otf', '.ttf', '.woff2']:
        font.generate('output/' + file_in.split('.')[0] + filetype)

for file_in in font_list_math:
    font = fontforge.open(file_in)
    font.generate('output/' + file_in.split('.')[0] + '.otf')