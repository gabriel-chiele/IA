(define (domain agenteSeguranca)
  (:requirements :strips :negative-preconditions)
  (:predicates (Em ?sala ) (Aberta ?x) (Conectadas ?sala1 ?sala2) (Pertence ?sala ?x) (Sala ?sala) (Porta ?porta) (Janela ?janela) (Luz ?luz))
  
  (:action AbrirPorta :parameters (?sala1 ?porta)
      :precondition (and (Sala ?sala1) (Porta ?porta) (Em ?sala1) (Pertence ?sala1 ?porta) (not (Aberta ?porta)))
      :effect (and (Aberta ?porta))
  )
  
  (:action FecharPorta :parameters (?sala1 ?porta)
      :precondition (and (Sala ?sala1) (Porta ?porta) (Em ?sala1) (Pertence ?sala1 ?porta) (Aberta ?porta))
      :effect (and (not (Aberta ?porta)))
  )
  
  (:action AbrirJanela :parameters (?sala1 ?janela ?luz)
      :precondition (and (Sala ?sala1) (Janela ?janela) (Luz ?luz) (Em ?sala1) (Pertence ?sala1 ?janela) (Pertence ?sala1 ?luz) (not (Aberta ?janela)) (Aberta ?luz))
      :effect (and (Aberta ?janela))
  )
  
  (:action FecharJanela :parameters (?sala1 ?janela ?luz)
      :precondition (and (Sala ?sala1) (Janela ?janela) (Luz ?luz) (Em ?sala1) (Pertence ?sala1 ?janela) (Pertence ?sala1 ?luz) (Aberta ?janela) (Aberta ?luz))
      :effect (and (not (Aberta ?janela)))
  )
  
  (:action AbrirLuz :parameters (?sala1 ?luz)
      :precondition (and (Sala ?sala1) (Luz ?luz) (Em ?sala1) (Pertence ?sala1 ?luz) (not (Aberta ?luz)))
      :effect (and (Aberta ?luz))
  )
  
  (:action FecharLuz :parameters (?sala1 ?luz)
      :precondition (and (Sala ?sala1) (Luz ?luz) (Em ?sala1) (Pertence ?sala1 ?luz) (Aberta ?luz))
      :effect (and (not (Aberta ?luz)))
  )
  
  (:action Andar :parameters (?sala1 ?sala2 ?porta ?luz)
      :precondition (and (Sala ?sala1) (Sala ?sala2) (Porta ?porta) (Luz ?luz) (Em ?sala1) (Pertence ?sala1 ?porta) (Pertence ?sala1 ?luz) (Pertence ?sala2 ?porta) (Aberta ?porta))
      :effect (and (not (Em ?sala1)) (Em ?sala2))
  )
)