from sys import argv
import fontforge

font_list = [('ClassWizCWDisplay-Regular.ufo', 'ClassWizCWDisplay-Regular.otf'),
('ClassWizCWDisplay-Regular.ufo', 'ClassWizCWDisplay-Regular.ttf'),
('ClassWizCWDisplay-Regular.ufo', 'ClassWizCWDisplay-Regular.woff2'),

('ClassWizXDisplay-Regular.ufo', 'ClassWizXDisplay-Regular.otf'),
('ClassWizXDisplay-Regular.ufo', 'ClassWizXDisplay-Regular.ttf'),
('ClassWizXDisplay-Regular.ufo', 'ClassWizXDisplay-Regular.woff2'),

('ClassWizMathCW-Regular.sfd', 'ClassWizMathCW-Regular.otf'),
('ClassWizMathX-Regular.sfd', 'ClassWizMathX-Regular.otf'),]

for file_in, file_out in font_list:
	fontforge.open(file_in).generate(file_out)
