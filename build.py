from sys import argv
import fontforge

font_list = ['ClassWizCWDisplayExt-Regular.sfd', 'ClassWizXDisplayExt-Regular.sfd', 'ClassWizCWMathExt-Regular.sfd', 'ClassWizXMathExt-Regular.sfd']

for file_in in font_list:
    font = fontforge.open(file_in)
    for font_out in ['.otf', '.ttf', '.woff2']:
        font.generate(file_in.split('.')[0] + file_out)
