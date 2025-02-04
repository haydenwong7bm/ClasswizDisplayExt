from sys import argv
from os import mkdir
import fontforge

font_list = ['ClassWizCWDisplayExt-Regular.sfd', 'ClassWizXDisplayExt-Regular.sfd', 'ClassWizCWMathExt-Regular.sfd', 'ClassWizXMathExt-Regular.sfd']

mkdir('output')

for file_in in font_list:
    font = fontforge.open(file_in)
    for filetype in ['.otf', '.ttf', '.woff2']:
        font.generate('output/' + file_in.split('.')[0] + filetype)
