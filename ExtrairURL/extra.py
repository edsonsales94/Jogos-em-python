class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)

    def sanitiza_url(self,  url):
        return url.strip()

    def valida_url(self):
        if self.url == "":
            raise ValueError("A URL esta vazia")

    def get_url_base(self):
        indice_inter = self.url.find('?')
        url_base = self.url[ :indice_inter]
        return url_base

    def get_url_parametro(self):
        indice_inter = self.url.find('?')
        url_param = self.url[indice_inter + 1:]
        return url_param

    def get_valor_parametro(self, param_buscar):

        indice_param = self.get_url_parametro().find(param_buscar)
        indice_valor = indice_param + len(param_buscar) + 1
        indice_ecomerc = self.get_url_parametro().find('&', indice_valor)

        if indice_ecomerc == -1:
            valor = self.get_url_parametro()[indice_valor:]
        else:
            valor = self.get_url_parametro()[indice_valor:indice_ecomerc]
        return valor


extrator_url = ExtratorURL("htttp://bytebank.com/cambio?moedaDestino=dolar&quantidade=100&moedaOrigem=real")
valor_quantidade = extrator_url.get_valor_parametro("quantidade")
print(valor_quantidade)