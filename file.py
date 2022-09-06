# Mode: 'w': write, 't': mean text, 'a' : appending, 'r': read
# Selector: 'b': binary mode, 't': text mode
#'wb': open for writing in binary mode, 'at': open for appending in text mode.
from webbrowser import open_new


f = open('text.txt', mode='wt', encoding='utf-8')
f.write('I love cheese cake\n')
f.write('conclusion\n')
f.close()
#reading text
g= open('text.txt', mode = 'rt', encoding='utf-8')
g.read(32)
g.read()
g.seek(0)
g.readline()