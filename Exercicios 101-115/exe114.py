import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não está acessivel no momento!')
else:
    print('Conseugi acessar o site Pudim com sucesso!')