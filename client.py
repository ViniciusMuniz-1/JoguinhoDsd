import socket
import random
from pokemon import pokemons  # Importa a lista de Pokémons do módulo pokemon

def main():
    server_address_tcp = ('localhost', 12345)

    # Estabelecendo conexão TCP
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address_tcp)

    # Escolha de Pokémon
    print("Escolha seu Pokémon:")
    for i, pokemon in enumerate(pokemons):
        print(f"{i}: {pokemon.nome}")

    pokemon_idx = int(input("Selecione um Pokémon: "))
    client_socket.sendall(str(pokemon_idx).encode())

    # Recebendo confirmação do Pokémon escolhido
    response = client_socket.recv(1024).decode()
    print(response)

    while True:
        # Receba a mensagem do servidor
        message = client_socket.recv(1024).decode()
        print(message)

        # Verifique se é o turno do jogador
        if "Sua vez de atacar" in message:
            comando = input("Digite 'ataque' para atacar: ")
            client_socket.sendall(comando.encode())

            if comando.strip().lower() == 'ataque':
                dado_result = client_socket.recv(1024).decode()
                print(f"Resultado do dado: {dado_result}")

                # Recebendo resultado do ataque
                response = client_socket.recv(1024).decode()
                print(response)

                # Verificar se o jogo terminou
                if "venceu" in response or "perdeu" in response:
                    break
        else:
            # Se não for o turno do jogador, continue aguardando mensagens do servidor
            continue

    client_socket.close()

if __name__ == "__main__":
    main()
