(define (domain agenteSeguranca)
  (:requirements :strips :negative-preconditions)
  (:predicates (Em ?sala ) (Aberta ?x) (Conectadas ?sala1 ?sala2) (Pertence ?sala ?x) (Sala ?sala) (Porta ?porta) (Janela ?janela))
  
  (:action AbrirPorta :parameters (?sala1 ?porta)
      :precondition (and (Sala ?sala1) (Porta ?porta) (Em ?sala1) (Pertence ?sala1 ?porta) (not (Aberta ?porta)))
      :effect (and (Aberta ?porta))
  )
  
  (:action FecharPorta :parameters (?sala1 ?porta)
      :precondition (and (Sala ?sala1) (Porta ?porta) (Em ?sala1) (Pertence ?sala1 ?porta) (Aberta ?porta))
      :effect (and (not (Aberta ?porta)))
  )
  
  (:action AbrirJanela :parameters (?sala1 ?janela)
      :precondition (and (Sala ?sala1) (Janela ?janela) (Em ?sala1) (Pertence ?sala1 ?janela) (not (Aberta ?janela)))
      :effect (and (Aberta ?janela))
  )
  
  (:action FecharJanela :parameters (?sala1 ?janela)
      :precondition (and (Sala ?sala1) (Janela ?janela) (Em ?sala1) (Pertence ?sala1 ?janela) (Aberta ?janela))
      :effect (and (not (Aberta ?janela)))
  )
  
  (:action Andar :parameters (?sala1 ?sala2 ?porta)
      :precondition (and (Sala ?sala1) (Sala ?sala2) (Porta ?porta) (Em ?sala1) (Pertence ?sala1 ?porta) (Pertence ?sala2 ?porta) (Aberta ?porta))
      :effect (and (not (Em ?sala1)) (Em ?sala2))
  )
)
