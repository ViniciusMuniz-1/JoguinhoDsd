import random

#CRIAÇÃO DA CLASSE POKEMON:
#CADA POKÉMON TEM NOME, VIDA, ATAQUE, DEFESA E UM DANO.
#O MÉTODO ATACAR RETORNA UM VALOR ALEATÓRIO ENTRE 1 E 20 SOMADO AO ATAQUE DO POKÉMON.
#O MÉTODO SOFRER_DANO RECEBE UM DANO E SUBTRAI A DEFESA DO POKÉMON DO DANO RECEBIDO.
#SE O DANO FOR MAIOR QUE 0, O POKÉMON PERDE VIDA.

class Pokemon:
    def __init__(self, nome, vida, ataque, defesa, dano):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.dano = dano

    def atacar(self):
        return random.randint(1, 20) + self.ataque

    def sofrer_dano(self, dano):
        dano -= self.defesa
        if dano > 0:
            self.vida -= dano

    def esta_vivo(self):
        return self.vida > 0

# Lista de Pokémons disponíveis
pokemons = [
    Pokemon("Charmander", vida=100, ataque=20, defesa=10, dano=25),
    Pokemon("Bulbasaur", vida=110, ataque=18, defesa=12, dano=23),
    Pokemon("Squirtle", vida=120, ataque=16, defesa=14, dano=21),
    Pokemon("Pikachu", vida=90, ataque=25, defesa=8, dano=30),
    Pokemon("Jigglypuff", vida=130, ataque=15, defesa=16, dano=20)
]