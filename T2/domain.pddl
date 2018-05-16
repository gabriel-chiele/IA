(define (domain agenteSeguranca)
    (:requirements :strips )
    (:predicates (Em ?loc ) (Sala ?loc) (PortaAberta ?loc ) (PortaFechada ?loc) (JanelaAberta ?loc ) (JanelaFechada ?loc))
    
    (:action mover  :parameters (?loc1 ?loc2)
                    :precondition (and (Em ?loc1) (Sala ?loc1) (Sala ?loc2))
                    :effect (and (Em ?loc2) (not (Em ?loc1)) )
    )

    (:action abrirPorta :parameters (?loc1)
                    :precondition (and (Em ?loc1) (Sala ?loc1) (PortaFechada ?loc1))
                    :effect (and (PortaAberta ?loc1) (not (PortaFechada ?loc1)) )
    )

    (:action fecharPorta :parameters (?loc1)
                    :precondition (and (Em ?loc1) (Sala ?loc1) (PortaAberta ?loc1))
                    :effect (and (PortaFechada ?loc1) (not (PortaAberta ?loc1)) )
    )

    (:action abrirJanela :parameters (?loc1)
                    :precondition (and (Em ?loc1) (Sala ?loc1) (JanelaFechada ?loc1))
                    :effect (and (JanelaAberta ?loc1) (not (JanelaFechada ?loc1)) )
    )

    (:action fecharJanela :parameters (?loc1)
                    :precondition (and (Em ?loc1) (Sala ?loc1) (JanelaAberta ?loc1))
                    :effect (and (JanelaFechada ?loc1) (not (JanelaAberta ?loc1)) )
    )
)