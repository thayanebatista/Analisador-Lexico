# Thayane Batista RA159049
# Curso: Engenharia de Computação
# Universidade Católica Dom Bosco
# Disciplina: Compiladores
# 2020B

# Analisador Lexico

class Token:
    def __init__(self, token, tipotoken, linha):
        self.token = token
        self.tipotoken = tipotoken
        self.linha = linha

    def __str__(self):
        return "{}\t\t{}\t\t{}".format(self.token, self.tipotoken, self.linha)


# #


class Analexic:
    def __init__(self, program):
        self.program = program
        self.reservadas = ['if', 'else', 'integer', 'var', 'then', 'while', 'do', 'begin', 'end', 'procedure',
                           'program', 'real', 'var', 'write', 'read', 'readd', 'repeat']
        self.operadores_relacionais = ['=', '<', '>', '>=', '<=', '<>']
        self.operadores_ad = ['+', '-', 'or']
        self.operadores_mult = ['*', '/', 'and']
        self.separadores = [',', '.', ';', ':', ':=', ')', '(']
        self.numeros = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
        self.letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',
                       'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'x', 'y', 'z']
        self.tokens = []
        self.alph = [self.numeros + self.operadores_ad + self.operadores_mult +
                     self.operadores_relacionais + self.separadores + self.letras]

    def parse(self):
        i = 0  # para analisar cada parte
        tam = len(self.program)  # pega o tamanho da entrada
        linha = 1  # para contagem da linha

        # print(self.program)

        while i < tam:
            token = ''
            # erro = []
            aux = 'null'  # valor atual

            # virificações de numeros
            if self.program[i].isdigit():
                aux = '- Numero Inteiro'
                # verifica numeros inteiros
                while i < tam and self.program[i] in self.numeros:
                    token += self.program[i]
                    i += 1

                # verificação de numero real
                if i < tam and self.program[i] == '.' and self.program[i + 1].isdigit():
                    aux = 'Numero Real'
                    token += self.program[i]
                    i += 1
                    while i < tam and self.program[i].isdigit():
                        token += self.program[i]
                        i += 1
                    print(token, aux)
                elif i < tam and (self.program[i + 1] not in self.numeros):
                    # self.erro += self.program[i] + self.program[i + 1]
                    token += self.program[i] + self.program[i + 1]
                    i += 2
                    # print('      - erro aqui' )
                    print('Erro na linha {}: numero incompleto em {}'.format(linha, token))
                # possibilidade de novas verificações de tipos numericos
            # #
            # verificando identificador, palavra reservada e alguns operadores
            elif self.program[i].isalpha():
                aux = 'Identificador'
                while i < tam and (self.program[i].isalpha() or self.program[i].isdigit() or self.program[i] == '_'):
                    token += self.program[i]
                    i += 1
                if token in self.reservadas:
                    aux = '- Palavra Reservada'
                    print(token, '- ', token)
                elif token in self.operadores_mult:
                    aux = '- Operador Mult/Div/And'
                    print(token, '- ', token)
                elif token in self.operadores_ad:
                    aux = 'Operador Add/Sub/Or'
                    print(token, '- ', token)
                else:
                    print(token, '- ', aux)
                # print(token, '- ', token)
            # verificando operadores relacionais
            elif self.program[i] in self.operadores_relacionais:
                aux = '- Operador Relacional'
                if self.program[i] == '<' or self.program[i] == '>':
                    token += self.program[i]
                    i += 1
                    if i < tam and self.program[i] == '=':
                        token += self.program[i]
                        i += 1
                        print(token, '- ', token)
                    elif i < tam and self.program[i - 1] == '<' and self.program[i] == '>':
                        token += self.program[i]
                        i += 1
                        print(token, '- ', token)
                    print(token, '- ', token)
                else:
                    token += self.program[i]
                    i += 1
                    print(token, '- ', token)

            elif self.program[i] in self.operadores_ad:
                aux = '- Operador Aditivo'
                token += self.program[i]
                i += 1
                print(token, '- ', token)
            elif self.program[i] in self.operadores_mult:
                aux = '- Operador Multiplicativo'
                token += self.program[i]
                i += 1
                print(token, '- ', token)
            # verificando separadores
            elif self.program[i] in self.separadores:
                aux = '- Separador'
                if self.program[i] == ':' and i < tam - 1 and self.program[i + 1] == '=':
                    aux = ' - :='
                    token += self.program[i] + self.program[i + 1]
                    i += 2
                    print(token, '- ', token)
                else:
                    token += self.program[i]
                    i += 1
                    print(token, '- ', token)

            # verificando comentarios
            elif self.program[i] == '{':
                coment = linha
                while self.program[i] != '}':
                    i += 1
                    if i >= tam:
                        print("Erro na linha{}: conentario aberto e nao fechado".format(coment))
                        # sys.exit("Erro: feche o comentario aberto na linha {}".format(coment))
                    if self.program[i] == '\n':
                        linha += 1
                i += 1

            # erro no coment
            # elif self.program[i] == '}':
            #    print("Erro: Comentario fechado e não aberto na linha {}".format(linha))
            # sys.exit("Erro: Comentario fechado e não aberto na linha {}".format(linha))

            # contagem das linhas
            elif self.program[i] == '\n':
                i += 1
                linha += 1
            # tratamento de caracteres nao reconhecido pela linguagem
            elif not (self.program[i] in self.alph) and not (self.program[i] in self.reservadas) \
                    and not (self.program[i] == ' '):
                print("Erro na linha {}: caracter nao reconhecido na linguagem".format(self.program[i]))
                i += 1
            else:
                i += 1
            if token:
                self.tokens.append(Token(token, aux, linha))

        return self.tokens


# aberturas


file = open('input.txt', "r").read()
Analexic(file).parse()
