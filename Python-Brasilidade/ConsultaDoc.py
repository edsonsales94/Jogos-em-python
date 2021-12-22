from Cpf_cnpj import Documentos
from validate_docbr import CNPJ

#cpf = Cpf('01491787279')
#print(cpf)

doc = input("Informe um Cpf/Cnpj ")

documento = Documentos.cria_documento(doc)

print(documento)