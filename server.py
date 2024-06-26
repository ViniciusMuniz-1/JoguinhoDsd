import socket
import random
from pokemon import Pokemon, pokemons  # Importa a classe Pokemon do módulo pokemon



def main():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 12345))
    server_socket.listen(2)  # Aceita até 2 conexões simultâneas
    print("Servidor TCP esperando conexões...")

    players = []  # Lista para manter as conexões dos jogadores
    player_pokemons = []  # Lista para manter os pokémons escolhidos por cada jogador

    # Espera conexões de dois jogadores
    for _ in range(2):
        connection, client_address = server_socket.accept()
        print("Conexão estabelecida com", client_address)
        players.append((connection, client_address))

    # Escolha de Pokémon para cada jogador
    for i, (player, client_address) in enumerate(players):
        # Receba a escolha do jogador e informe o Pokémon escolhido
        pokemon_idx = int(player.recv(1024).decode())
        selected_pokemon = pokemons[pokemon_idx]
        player_pokemons.append(selected_pokemon)
        player.sendall(f"Você escolheu {selected_pokemon.nome}\n".encode())
        
        player.sendall("Aguardando o outro jogador...\n".encode())

    # Inicializa o turno do primeiro jogador
    current_player_index = 0

    while True:
        current_player, _ = players[current_player_index]
        other_player, _ = players[(current_player_index + 1) % 2]

        current_pokemon = player_pokemons[current_player_index]
        other_pokemon = player_pokemons[(current_player_index + 1) % 2]

        # Envie informações de vida e solicite ação para cada jogador
        for player, _ in players:
            if player == current_player:
                player.sendall(f"Vida atual do seu Pokémon ({current_pokemon.nome}): {current_pokemon.vida}\n".encode())
                player.sendall(f"Vida atual do Pokémon adversário ({other_pokemon.nome}): {other_pokemon.vida}\n".encode())
                player.sendall(f"Sua vez de atacar! Role o dado e digite 'ataque' para atacar:\n".encode())
            else:
                player.sendall(f"Vida atual do seu Pokémon ({other_pokemon.nome}): {other_pokemon.vida}\n".encode())
                player.sendall(f"Vida atual do Pokémon adversário ({current_pokemon.nome}): {current_pokemon.vida}\n".encode())
                player.sendall("Aguardando a vez do outro jogador...\n".encode())

        # Receba o comando de ataque do jogador atual
        data = current_player.recv(1024).decode()
        if data.strip().lower() == 'ataque':
            # Simule o ataque
            dado_result = random.randint(1, 20)
            ataque = current_pokemon.ataque + dado_result

            # Envie o resultado do ataque para ambos os jogadores
            for player, _ in players:
                player.sendall(f"Resultado do dado: {dado_result}\n".encode())
                player.sendall(f"Resultado do ataque: {ataque}\n".encode())

            # Verifique se o ataque acertou
            if ataque > other_pokemon.defesa:
                other_pokemon.vida -= current_pokemon.dano
                # Envie mensagem de ataque bem-sucedido e vida atual do oponente
                for player, _ in players:
                    player.sendall(f"Ataque de {current_pokemon.nome} acertou! Causou {current_pokemon.dano} de dano\n".encode())

                # Verifique se o jogo terminou
                if not other_pokemon.esta_vivo():
                    current_player.sendall("Parabéns! Seu Pokémon derrotou o adversário!\n".encode())
                    other_player.sendall("Seu Pokémon foi derrotado pelo adversário!\n".encode())
                    break  # Saia do loop principal do jogo


        # Alternar para o próximo jogador
        current_player_index = (current_player_index + 1) % 2

                        
if __name__ == "__main__":
    main()
