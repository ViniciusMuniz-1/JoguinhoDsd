                for player, _ in players:
                    player.sendall(f"Resultado do dado: {dado_result}\n".encode())
                    player.sendall(f"Resultado do ataque: {ataque}\n".encode())