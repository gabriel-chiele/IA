(define (problem teste1)
    (:domain agenteSeguranca)
    ; cria os objetos
    (:objects Corredor             LuzC 
              Sala1 Porta1 Janela1 Luz1)
    ;inicialização
    (:init (Sala Corredor) (Luz LuzC) (Pertence Corredor LuzC) (Aberta LuzC)    ; inicia o corredor
      (Em Corredor)                                                             ; posiciona o zelador
      
      ;inicialização da sala1
      (Sala Sala1)                                                              
      (Porta Porta1) (Pertence Sala1 Porta1) (Pertence Corredor Porta1)
      (Janela Janela1)  (Pertence Sala1 Janela1)
      (Luz Luz1) (Pertence Sala1 Luz1)
      
      ; inicializa os estados dos objetos da sala1
      (Aberta Porta1) (Aberta Janela1) (Aberta Luz1)
      
      (Conectadas Corredor Sala1) ; conecta as salas [1 - C]
    )
    (:goal (and (not (Aberta Janela1)) (not (Aberta Porta1)) (not (Aberta Luz1))
                (Em Corredor) 
            )
    )
)
