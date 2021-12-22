from validate_docbr import CPF, CNPJ

class Documentos:
    @staticmethod
    def cria_documento(documentos):
        if len(documentos) == 11:
            return DocCpf(documentos)
        elif len(documentos) == 14:
            return DocCnpj(documentos)
        else:
            raise ValueError("Quantidade de digitos incorreta!!")

class DocCpf:
    def __init__(self, documentos):
        if self.valida(documentos):
            self.cpf = documentos
        else:
            raise ValueError("Cpf invalido")

    def __str__(self):
        return self.format()

    def valida(self, documentos):
        validador = CPF()
        return validador.validate(documentos)

    def format(self):
        mascara = CPF()
        return mascara.mask(self.cpf)

class DocCnpj:
    def __init__(self, documentos):
        if self.valida(documentos):
            self.cnpj = documentos
        else:
            raise ValueError("Cnpj invalido")

    def __str__(self):
        return self.format()

    def valida(self, documentos):
        validador = CNPJ()
        return validador.validate(documentos)

    def format(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)


'''
    def __init__(self, documento, tipo_doc):
        self.tipo_doc = tipo_doc
        documento = str(documento)
        if tipo_doc =="cpf":
            if self.cpf_eh_Valido(documento):
                self.cpf = documento
            else:
                raise ValueError("CPF Invalido!")
        elif self.tipo_doc == "cnpj":
            if self.cnpj_e_valido(documento):
                self.cnpj = documento
            else:
                raise ValueError("CNPJ Invalido!")
        else:
            raise ValueError("Documento Invalido!!")

    def __str__(self):
        if self.tipo_doc == "cpf":
            return self.format_cpf()
        elif self.tipo_doc == "cnpj":
            return self.format_cnpj()

    def cpf_eh_Valido(self, cpf):
        if len(cpf) == 11:
            validador = CPF()
            return validador.validate(cpf)
        else:
             raise ValueError("Quantidade de digitos incorreta!!")

    def format_cpf(self):
        mascara = CPF()
        return mascara.mask(self.cpf)
    def format_cnpj(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def cnpj_e_valido(self, cnpj):
        if len(cnpj)==14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError("Quantidade de digitos incorreta!!")
'''