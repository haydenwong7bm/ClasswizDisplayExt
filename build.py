from sys import argv
from os import makedirs
import fontforge

font_list_display = ['ClassWizCWDisplayExt-Regular.sfd', 'ClassWizXDisplayExt-Regular.sfd']
font_list_math = ['ClassWizCWMathExt-Regular.sfd', 'ClassWizXMathExt-Regular.sfd']

makedirs('output', exist_ok=True)

for file_in in font_list_display:
    font = fontforge.open(file_in)
    for filetype in ['.otf', '.ttf', '.woff2']:
        font.generate('output/' + file_in.split('.')[0] + filetype)

for file_in in font_list_math:
    font = fontforge.open(file_in)
    font.generate('output/' + file_in.split('.')[0] + '.otf')
