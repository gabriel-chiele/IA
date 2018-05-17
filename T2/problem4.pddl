(define (problem teste4)
    (:domain agenteSeguranca)
    (:domain agenteSeguranca)
    ; cria os objetos
    (:objects Corredor             LuzC 
              Sala1 Porta1 Janela1 Luz1
              Sala2 Porta2 Janela2 Luz2
              Sala3 Porta3 Janela3 Luz3)
    ; inicialização
    (:init (Sala Corredor) (Luz LuzC) (Pertence Corredor LuzC) (Aberta LuzC)    ; inicia o corredor
      (Em Corredor)                                                             ; posiciona o zelador
      
      ; inicialização da sala1
      (Sala Sala1)
      (Porta Porta1) (Pertence Sala1 Porta1) (Pertence Corredor Porta1)
      (Janela Janela1) (Pertence Sala1 Janela1)
      (Luz Luz1) (Pertence Sala1 Luz1)
      
      ; inicialização da sala2
      (Sala Sala2)
      (Porta Porta2) (Pertence Sala2 Porta2) (Pertence Corredor Porta2)
      (Janela Janela2) (Pertence Sala2 Janela2)
      (Luz Luz2) (Pertence Sala2 Luz2)
      
      ; inicialização da sala3
      (Sala Sala3)
      (Porta Porta3) (Pertence Sala3 Porta3) (Pertence Sala2 Porta3)
      (Janela Janela3) (Pertence Sala3 Janela3)
      (Luz Luz3) (Pertence Sala3 Luz3)
      
      ; inicializa os estados dos objetos da sala1
      (Aberta Porta1) (Aberta Janela1) (Aberta Luz1)
      ; inicializa os estados dos objetos da sala2
      (Aberta Porta2) (Aberta Janela2) (Aberta Luz2)
      ; inicializa os estados dos objetos da sala3
      (Aberta Porta3) (Aberta Janela3) (Aberta Luz3)
      
      (Conectadas Corredor Sala1) ; conecta as salas [1 - C]
      (Conectadas Corredor Sala2) ; conecta as salas [1 - C - 2]
      (Conectadas Sala2    Sala3) ; conecta as salas [1 - C - 2 - 3]
    )
    (:goal (and (not(Aberta Janela1)) (not(Aberta Porta1)) (not(Aberta Luz1))
                (not(Aberta Janela2)) (not(Aberta Porta2)) (not(Aberta Luz2))
                (not(Aberta Janela3)) (not(Aberta Porta3)) (not(Aberta Luz3))
                (Em Corredor)
            )
    )
)
