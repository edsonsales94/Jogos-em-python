
from modelo import Filme, Serie, Playlist



vingadores = Filme("vingadores Guerra infinita", 2018, 160)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor = Serie('Demolidor', 2016, 2)
atlanta = Serie("atlanta", 2017, 2)
vingadores.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
tmep.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

filme_e_series = [vingadores , atlanta, demolidor, tmep]
playlist_fim_de_Semana = Playlist('fim de semana', filme_e_series)

print(f'playList {len(playlist_fim_de_Semana.listagem)}')

for programa in playlist_fim_de_Semana:
    print(programa)
    print(d)

