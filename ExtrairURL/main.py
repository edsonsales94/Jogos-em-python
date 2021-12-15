url = "    htttp://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real    "
##print(url)
#url = '  '

#sanitização de url
url = url.strip()

#validação de url
if url == '':
    raise ValueError("A URL esta vazia")

indice_inter= url.find('?')
url_base  = url[0:indice_inter]
print(url_base)

url_param = url[indice_inter+1:]
print(url_param)



param_buscar = 'moedaDestino'
indice_param = url_param.find(param_buscar)
indice_valor = indice_param + len(param_buscar) + 1
indice_ecomerc = url_param.find('&', indice_valor)

if indice_ecomerc ==-1:
   valor = url_param[indice_valor:]
else:
    valor = url_param[indice_valor:indice_ecomerc]

print(valor)
