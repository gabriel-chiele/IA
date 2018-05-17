(define (problem teste3)
    (:domain agenteSeguranca)
    ; cria os objetos
    (:objects Corredor             LuzC 
              Sala1 Porta1 Janela1 Luz1
              Sala2 Porta2 Janela2 Luz2)
    ; inicialização
    (:init (Sala Corredor) (Luz LuzC) (Pertence Corredor LuzC) (Aberta LuzC)    ; inicia o corredor
      (Em Corredor)                                                             ; posiciona o zelador
      
      ; inicialização da sala1
      (Sala Sala1)
      (Porta Porta1) (Pertence Sala1 Porta1) (Pertence Corredor Porta1)
      (Janela Janela1) (Pertence Sala1 Janela1)
      (Luz Luz1) (Pertence Sala1 Luz1)
      
      ; inicialização da sala1
      (Sala Sala2)
      (Porta Porta2) (Pertence Sala2 Porta2) (Pertence Corredor Porta2)
      (Janela Janela2) (Pertence Sala2 Janela2)
      (Luz Luz2) (Pertence Sala2 Luz2)
      
      ; inicializa os estados dos objetos da sala1
      (Aberta Porta1) (Aberta Janela1) (Aberta Luz1)
      ; inicializa os estados dos objetos da sala2
      (Aberta Porta2) (Aberta Janela2) (Aberta Luz2)
      
      (Conectadas Corredor Sala1) ; conecta as salas [1 - C]
      (Conectadas Corredor Sala2) ; conecta as salas [1 - C - 2]
    )
    (:goal (and (not(Aberta Janela1)) (not(Aberta Porta1)) (not(Aberta Luz1))
                (not(Aberta Janela2)) (not(Aberta Porta2)) (not(Aberta Luz2))
                (Em Corredor)
            )
    )
)
