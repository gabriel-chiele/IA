(define (domain agenteSeguranca)
  (:requirements :strips )
  (:predicates (Em ?sala ) (Aberta ?x) (Fechada ?x) (Conectadas ?sala1 ?sala2) (Pertence ?sala ?x) (Sala ?sala) (Porta ?porta) (Janela ?janela))
  
  (:action abrirJanela :parameters (?sala ?janela)
      :precondition (and (Em ?sala) (Sala ?sala) (Janela ?janela) (Pertence ?sala ?janela) (Fechada ?janela))
      :effect (and (not Fechada ?janela) (Aberta ?janela))
  )

  (:action fecharJanela :parameters (?sala ?janela)
      :precondition (and (Em ?sala) (Sala ?sala) (Janela ?janela) (Pertence ?sala ?janela) (Aberta ?janela))
      :effect (and (not Aberta ?janela) (Fechada ?janela))
  )

  (:action abrirPorta :parameters (?sala1 ?sala2 ?porta)
      :precondition (and (Em ?sala1) (Sala ?sala1) (Sala ?sala2) (Porta ?porta) (Pertence ?sala2 ?porta) (Fechada ?porta) (Conectadas ?sala1 ?sala2))
      :effect (and (not Fechada ?porta) (Aberta ?porta))
  )

  (:action fecharPorta :parameters (?sala1 ?sala2 ?porta)
      :precondition (and (Em ?sala1) (Sala ?sala1) (Sala ?sala2) (Porta ?porta) (Pertence ?sala2 ?porta) (Aberta ?porta) (Conectadas ?sala1 ?sala2))
      :effect (and (not Aberta ?porta) (not Fechada ?porta))
  )

  (:action Entrar  :parameters (?sala1 ?sala2 ?porta)
      :precondition (and (Em ?sala1) (Sala ?sala1) (Sala ?sala2) (Porta ?porta) (Pertence ?sala2 ?porta) (Aberta ?porta) (Conectadas ?sala1 ?sala2))
      :effect (and (not Em ?sala1) (Em ?sala2) )
  )

  (:action Sair  :parameters (?sala1 ?sala2 ?porta)
      :precondition (and (Em ?sala1) (Sala ?sala1) (Sala ?sala2) (Porta ?porta) (Pertence ?sala1 ?porta) (Aberta ?porta) (Conectadas ?sala1 ?sala2))
      :effect (and (not Em ?sala1) (Em ?sala2) )
  )

)
