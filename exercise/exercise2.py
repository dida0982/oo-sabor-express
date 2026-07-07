import os
'''
Mão na massa: refatorando uma função

No Python, a criação de classes é uma parte essencial da programação orientada a objetos. Abaixo, temos um exemplo de uma classe chamada Musica que representa informações sobre uma música, como nome, artista e duração:

Agora é sua vez! Refaça essa classe Musica utilizando uma forma mais concisa e expressiva, aproveitando a sintaxe simplificada do Python.
'''


class Musica:
    def __init__(self, nome='', artista='', duracao=0):
        self.nome = nome
        self.artista = artista
        self.duracao = duracao

musica1 = Musica(nome='Under Pressure', artista='Queen & David Bowie', duracao=248)
musica2 = Musica(nome='The Trooper', artista='Iron Maiden', duracao=245)
musica3 = Musica(nome='Hotel California', artista='Eagles', duracao=390)

os.system('cls')
print(f'Música: {musica1.nome} | Artista: {musica1.artista} | Duração: {musica1.duracao}s')
print(f'Música: {musica2.nome} | Artista: {musica2.artista} | Duração: {musica2.duracao}s')
print(f'Música: {musica3.nome} | Artista: {musica3.artista} | Duração: {musica3.duracao}s')
