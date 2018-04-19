# IA - Inteligência Artificial

Repositório para os trabalhos da disciplina de Inteligência Artificial

PUCRS - 18/1

Lista de tarefas a serem realizadas para concluir o trabalho, organizada
em ordem de prioridades.

OBS: Lista propensa a alteração ao decorrer da implementação

###################################  TODO  ###################################
- verificar se o método LookAround funciona através de paredes
	- se funciona arrumar

- modificar CooseAction para levar em conta a BestPropose

- separar parte gráfica em outra thread

- quando ação for casar:
	- ao receber reposta, se for posistiva ir na direção do outro agente
	- quando agentes se encontrarem, ir ao cartorio

- quando ação for ir ao cartorio
	- homem calcula o cartorio mais proximo e passa a localização para a mulher
	- os dois agentes se direcionam para lá
	- ao chegar no cartorio, se cadastra e espera lá até o namorado chegar
	- quando os dois chegarem, forma casal

- implementar grid de representação do mapa

- implementar verificação de consistencia de entrada
	EX.: mapa pequeno para um numero grande de agentes ou cartorios

- implementar a máquina de estados de movimentação dos agentes

- implementar o sistema de turnos dos agentes

- realizar testes com outros arquivos de input e tamanho de mapa
