﻿(define (problem teste1)
    (:domain agenteSeguranca)
    (:objects Corredor Sala1 Porta1 Janela1)
    (:init (Sala Corredor) (Em Corredor)
      (Sala Sala1) (Porta Porta1) (Janela Janela1) (Pertence Sala1 Porta1) (Pertence Sala1 Janela1)
      (Aberta Porta1) (Aberta Janela1)
      (Conectadas Corredor Sala1)
    )
    (:goal (and(Fechada Janela1) (Fechada Porta1)))
)
