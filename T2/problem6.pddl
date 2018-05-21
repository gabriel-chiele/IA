(define (problem teste4)
    (:domain agenteSeguranca)
    ; cria os objetos
    (:objects Corredor             LuzC 
              Sala1 Porta1 Janela1 Luz1
              Sala2 Porta2 Janela2 Luz2
              Sala3 Porta3 Janela3 Luz3
              Sala4 Porta4 Janela4 Luz4
              Sala5 Porta5 Janela5 Luz5
              Sala6 Porta6 Janela6 Luz6)
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
      (Porta Porta2) (Pertence Sala2 Porta2) (Pertence Sala1 Porta2)
      (Janela Janela2) (Pertence Sala2 Janela2)
      (Luz Luz2) (Pertence Sala2 Luz2)
      
      ; inicialização da sala3
      (Sala Sala3)
      (Porta Porta3) (Pertence Sala3 Porta3) (Pertence Sala2 Porta3)
      (Janela Janela3) (Pertence Sala3 Janela3)
      (Luz Luz3) (Pertence Sala3 Luz3)
      
      ; inicialização da sala4
      (Sala Sala4)
      (Porta Porta4) (Pertence Sala4 Porta4) (Pertence Corredor Porta4)
      (Janela Janela4) (Pertence Sala4 Janela4)
      (Luz Luz4) (Pertence Sala4 Luz4)
      
      ; inicialização da sala5
      (Sala Sala5)
      (Porta Porta5) (Pertence Sala5 Porta5) (Pertence Sala4 Porta5)
      (Janela Janela5) (Pertence Sala5 Janela5)
      (Luz Luz5) (Pertence Sala5 Luz5)
      
      ; inicialização da sala6
      (Sala Sala6)
      (Porta Porta6) (Pertence Sala6 Porta6) (Pertence Sala5 Porta6)
      (Janela Janela6) (Pertence Sala6 Janela6)
      (Luz Luz6) (Pertence Sala6 Luz6)
      
      ; inicializa os estados dos objetos da sala1
      (not (Aberta Porta1)) (Aberta Janela1) (Aberta Luz1)
      ; inicializa os estados dos objetos da sala2
      (Aberta Porta2) (Aberta Janela2) (Aberta Luz2)
      ; inicializa os estados dos objetos da sala3
      (not (Aberta Porta3)) (Aberta Janela3) (Aberta Luz3)
      ; inicializa os estados dos objetos da sala4
      (Aberta Porta4) (not (Aberta Janela4)) (not (Aberta Luz4))
      ; inicializa os estados dos objetos da sala5
      (Aberta Porta5) (Aberta Janela5) (Aberta Luz5)
      ; inicializa os estados dos objetos da sala6
      (not (Aberta Porta6)) (Aberta Janela6) (not (Aberta Luz6))
      
      (Conectadas Corredor Sala1) ; conecta as salas [1 - C]
      (Conectadas Sala1    Sala2) ; conecta as salas [2 - 1 - C]
      (Conectadas Sala2    Sala3) ; conecta as salas [3 - 2 - 1 - C]
      (Conectadas Corredor Sala4) ; conecta as salas [3 - 2 - 1 - C - 4]
      (Conectadas Sala4    Sala5) ; conecta as salas [3 - 2 - 1 - C - 4 - 5]
      (Conectadas Sala5    Sala6) ; conecta as salas [3 - 2 - 1 - C - 4 - 5 - 6]
    )
    (:goal (and (not(Aberta Janela1)) (not(Aberta Porta1)) (not(Aberta Luz1))
                (not(Aberta Janela2)) (not(Aberta Porta2)) (not(Aberta Luz2))
                (not(Aberta Janela3)) (not(Aberta Porta3)) (not(Aberta Luz3))
                (not(Aberta Janela4)) (not(Aberta Porta4)) (not(Aberta Luz4))
                (not(Aberta Janela5)) (not(Aberta Porta5)) (not(Aberta Luz5))
                (not(Aberta Janela6)) (not(Aberta Porta6)) (not(Aberta Luz6))
                (Em Corredor)
            )
    )
)