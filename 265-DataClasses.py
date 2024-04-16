# dataclasses - O que são dataclasses?
# O módulo dataclasses fornece um decorador e funções para criar métodos como
# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo
# usuário.
# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.
# doc: https://docs.python.org/3/library/dataclasses.html

from dataclasses import dataclass


@dataclass # Decorador
# Esta classe já tem um '__rerp__'; 
# Isso significa que minha classe já retorna os valores dela em vez do objeto.
class Pessoa:
    nome: str
    sobrenome: str

    # Post init está fazendo o mesmo que no getter e setter
    def __post_init__(self):
        self.nome_completo = f'POST INIT {self.__class__.__name__}: {self.nome} {self.sobrenome}'


    # @property
    # def nome_completo(self):
    #     return f'{self.nome} {self.sobrenome}'


    # @nome_completo.setter
    # def nome_completo(self, valor):
    #     nome, *sobrenome = valor.split()
    #     self.nome = nome
    #     self.sobrenome = ' '.join(sobrenome)


# (init=False): 
# Eu acabei de definir o __init__ do decorador como False;
# Isso significa que eu terei que criar o __init__ manualmente;
# O método especial "__post_init__" também já não funcionará mais.
@dataclass(init=False)
class Carro:
    nome_do_carro: str
    ano: int

    def __init__(self, nome_do_carro, ano):
        self.nome_do_carro = nome_do_carro
        self.ano = ano

    # Fazendo um print para mostrar que POST INIT não será chamado.
    def __post_init__(self):
        print(f'POST INIT {self.__class__.__name__}')


print()

print('OBJETO 1: ')
p1 = Pessoa('Victor', 'Inácio')
print(p1) # Printando o objeto Pessoa, que agora vai exibir os atributos do objeto
print(p1.nome_completo)
print()


print('OBJETO 2:')
c1 = Carro('Fusca', 1998)
print(c1) # O objeto ainda é exibido de forma 'formatada' pois estamos usando @dataclass
# Pode-se perceber que ele não exibiu POST INIT da classe Carro, pois (init=False)
