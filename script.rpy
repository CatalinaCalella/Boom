define e = Character("Bauti")
define i = Character("Luis")
define a = Character("Sol")
define player = Character("Tú")
define bombita = Character("Bombita")
define s = Character("Santi del Morbo")

label start:
    scene apartment a living room day
    "Estábamos encerrados con 3 de mis amigos en mi casa. No sé cómo apareció una bomba con una cuenta regresiva de 10 minutos."
    "Ya intentamos romper ventanas y puertas, pero parecen de acero, intentemos llamar a la policías, pero no hay señal ni internet…"
    show bauti at left
    e "¡Relax gente, esto es una cámara oculta para Showmatch!"
    hide bauti 
    show luis at right
    i "¡No creo que sea una broma! Cuando esa contador llegue a cero..."
    i "TODOS VAMOS A MORIR."
    hide luis
    show bauti at center
    e "Capaz en 10 minutos va a saltar papelitos de colores, tipo revelación de género."
    hide bauti
    show sol at center
    a "Esto es ridículo... Si va a explotar, que explote ya, ¿Para que nos hace esperar 10 minutos?"
    hide sol
    player "Tal vez porque debe haber una manera de detener la bomba antes de que el tiempo acabe."
    player "¡Espera! Hay algo como un juego de trivia atras de la bomba"
    show bauti at center
    e "O sea, what?"
    show luis at right
    i "Tal vez si las respondemos, la bomba no explote."
    hide bauti
    hide luis
    show sol at center
    a "Medio que es una pelotudez, si va a ser un juego mortal que mínimo sea interesante."
    a "Como una pistola no se."
    hide sol
    show bauti at center
    e "Si lo contestamos bien, capaz nos ganemos 5 lucas, anasheeeee."
    hide bauti

    menu:
        "Responder las preguntas":
            jump pregunta_bomba_1
        "Buscar otra salida":
            jump final_malo
        "No hacer nada":
            jump final_muy_malo

label pregunta_bomba_1: #primera pregunta
    bombita "Primera prengunta: ¿Qué tiene llaves pero no abre puertas?"
    menu:
         "Un piano":
              "Correcto. Pasas a la siguiente ronda."
              jump siguiente_paso
         "Un cofre":
              "Incorrecto. Perdieron el juego..."
              jump casa_explota
         "Un cajon":
              "Incorrecto. Perdieron el juego..."
              jump casa_explota

label siguiente_paso: #introduccion a la pregunta 2
    "Todos nos relagamos un poco"
    show bauti at center
    e "Let's gooo"
    hide bauti
    show luis at center
    i "¿Cuantas preguntas hay que responder?"
    player "Aqui dice que quedan 4 mas"
    "Luis suspira aliviado"
    i "Bien, si son como la primera son preguntas faciles, si trabajamos juntos lo lograremos"
    player "¡Si!"
    hide luis
    show sol at center
    a "Entonces el premio es solo...vivir?"
    player "¿Te parece poco?"
    a "Si, minimo si voy a pasar por esto que me paguen"
    hide sol
    jump siguente_pregunta

label final_malo: #buscan otra salida
    player "Talvez sea una trampa."
    show luis at right
    show bauti at left
    show sol at center
    player "Nadie nos garantiza que respondiendo las preguntas se desactive"
    hide bauti
    hide luis
    a "Si, talvez solo gastemos tiempo valioso."
    hide sol
    show bauti at left
    e "Yo opino que respondamos las preguntas."
    hide bauti
    show sol at center
    a "Yo opino que sos un boludo."
    hide sol
    player "Wooooo"
    show luis at center
    i "Woooooo"
    hide luis
    show bauti at center
    e "Woooo"
    e "Estuvo buena esa ea"
    hide bauti
    scene boom
    "Buscas una salida, pero las puertas están selladas. La bomba explota."
    return
label final_muy_malo: #el tiempo pasa
    player "Bueno... esperemos a que el tiempo pase, tal vez si es una broma como dice Bauti"
    show bauti at center
    e "Bueno pero tampoco quiero estar 10 minutos mirando la pared"
    player "¿Tenes alguna sugerencia Bauti?"
    e "..."
    player "..."
    e "Veo veo"
    hide bauti
    scene boom
    "La bomba explota."
    return

label final_bueno: #alargar el final  #ninguna eleccion lleva a este final
    "Logramos desactivar la bomba y todos se salvan."
    scene apartment a exterior day
    "Salimos afuera a respierar un poco de aire. Podia ver la felicidad en el rostro de todos"
    show luis at right
    i "¿En serio termino?"
    show bauti at left
    e "Fue re facil al final"
    player "Si... Por lo menos siento que esta experiencia nos unio a todos a pesar de nuestras diferencias"
    show sol
    a "No se si para tanto"
    a "Pero me alegra que estemos vivos"
    hide sol
    hide bauti
    hide luis
    scene apartment a living room day
    "Volvi a dentro para verificar la bomba"
    "Pero ya no estaba"
    return

label casa_explota: #respondes mal
    "3..."
    "2..."
    "1..."
    "..."
    show bauti at center
    e "..?"
    e "Medio una estaf-"
    hide bauti
    scene boom
    "BOOM"
    return
label siguente_pregunta: #pregunta 2
    "Bien pasemos a la siguentes pregunta"
    bombita "Segunda prengunta: ¿Quién es el hijo de mi madre que no es mi hermano?"
    menu:
         "Yo":
            "Correcto. Pasas a la siguiente ronda."
            jump parte_3
         "Mi hermano":
            "Incorrecto. Perdieron el juego..."
            jump casa_explota
label parte_3: #charla para elegir con quien pasas rato
    "Bueno solo faltan dos"
    player "Talvez debamos tomarnos un descanso, para relajar la mente"
    show luis
    i "Si eso quieren, todavia tenemos tiempo"
    hide luis
    menu:
          "Vamos a la siguiente pregunta":
             jump pregunta_3
          "Descansemos un poco":
             jump tiempo_libre

label tiempo_libre: #elegis con quien pasar tiempo
    show luis at left
    show bauti at center
    show sol at right
    player "Creo que seria mejor descansa, asi pensamos mejor las siguientes respuestas"
    player "Solo seran uno o dos minutos ¿De acuerdo?"
    hide sol
    hide luis
    e "Oka, me voy a las piezas a ver si hay algo para entretenerme"
    hide bauti
    show sol
    a "Yo voy a la concina a ver si hay algo para tomar"
    hide sol
    show luis
    i "Yo voy al sotano a estar tranquilo un rato"
    hide luis
    show bauti
    e "¿Hay sotano? ¿Desde cuando?"
    hide bauti
    "Bien, ¿yo que hare?"
    menu:
     "Ir con Bauti":
        jump bauti_ruta
     "Ir con Luis":
        jump luis_ruta
     "Ir con Sol":
        jump sol_ruta

label bauti_ruta:
 show bauti
 player "Bauti yo voy con vos"
 e "Joyon vamos arriba, capaz encontremos algun juego"
 scene pieza
 show bauti
 "Subimos arriba con Bauti a mi habitacion"
 player "Creo que tengo algunos juegos de mesa por aqui"
 player "..eh"
 player "Che Bauti..."
 e "¿Que paso?"
 player "¿Vos de verdad pensas que es joda que la bomba va a explotar?"
 e "La verdad intento no pensar mucho en eso"
 e "Si me lo tomo en serio o no, no cambia la situacion en la que estamos...Si entro en panico como Luis o me frustro como Sol talvez sea mas dificil sobrellevar la situacion"
 e "Con calma podemos solucionar la situacion, solo quedan tres preguntas. Yo se que entre todos lo vamso a solucionar"
 player "Me gustaria tener tu calma en este momento..."
 e "Bueno pero subimos aca a relajarnos, no a estresarnos mas"
 e "¿Que queres hacer?"
 hide bauti
menu: 
    "Juguemos a un rompe cabezas": #juegan nomal
        jump pregunta_3 
    "Creo que abajo de la cama vi una consola vieja": #final secreto boffe
         jump bauti_secre 

label bauti_secre: #Final secreto boffe
 show bauti
 e "¿Como abajo de la cama? Ratas tenes abajo de tu cama, es un desastre"
 player "Bueno ayudame a mover la cama ya que estas tirando hate"
 "Movimos la cama con bauti hasta que lo sacamos completamente"
 "Entre toda la ropa que tenia abajo de la cama, habia una compuerta pequeña en el piso"
 scene agujero
 e "Eeeh... ¿Eso siempre estuvo ahi?"
 player "...No?"
 "Junto a Bauti la abrimos completamente. Daba a un tunel subterráneo"
 player "¿Crees que deberiamos avisarle a los demas primero?"
 show bauti
 e "Primero investiguemos bien que hay aca, talvez no sea una salida como tal"
 "Bauti estaba muy serio, asi que decidi no contradecirlo"
 scene camino
 "Este lugar...¿En serio estuvo todo este tiempo abajo de mi casa?" 
 show bauti
 "Bauti tambien estaba inquieto"
 e "Tal vez si deberiamos irnos..."
 player "¡Espera! Creo que estoy escuchando musica"
 e "¿Musica?"
 player "Si, tal vez si de a una salida"
 "Corri en direccion al lugar de la musica. Bauti me segui"
 scene black
 e "¿Q-que? ¿Que paso?"
 "Siguimos caminando aun sin ver nada"
 player "No lo se..."
 "Otra vez comenzamos a escuhcar una musica, pero esta vez mucho mas fuerte"
 player "Espera..."
 scene gh with fade 
 player "???"
 show bauti
 e "No lo puedo creer..."
 player "¿Porque parece que conocieras este lugar?"
 e "Porque lo hago..."
 e "Se que me encuentras un enorme parecido con un famoso que esta relacionado con este programa..."
 player "Si, la verdad es que eres identico a el"
 e "Porque en realidad no me llamo Bauti... Yo soy..."
 hide bauti
 show bautidelmoro
 e "Santiago del Morbo..."
 player "¡Nos mentiste todo este tiempo! ¡¿Todo esto fue tu plan!?"
 s "Asi es"
 return
label sol_ruta:
 jump pregunta_3 
label luis_ruta:
 jump pregunta_3
label pregunta_3: #pregunta 3
        scene apartment a living room day
        bombita "Tercera prengunta: ¿Cómo podemos hacer que cuatro nueves den como resultado cien?"
        show sol at right
        a "¿Quien es bueno en matematicas?"
        show luis at left
        i "¿No hay calculadoras por aca? o ¿algun papel para anotar?"
        a "Tal vez sea 9/9+99=100"
        i "Yo creo que es 9+9+9+9x9=100"
        hide luis
        hide sol
        menu:
            "9+9+9+9x9=100":
              "Incorrecto. Perdieron el juego..."
              jump casa_explota
            "(9x9)+(9/9)=100":
              "Incorrecto. Perdieron el juego..."
              jump casa_explota
            "9/9+99=100":
              "Correcto. Pasas a la siguiente ronda."
              jump pregunta_4
label pregunta_4:
    scene apartment a living room day
    bombita "Cuarta pregunta: ¿Cómo se llama en la mesa al cloruro de sodio: azúcar, sal o vinagre?"
    menu:
        "Vinagre":
         "Incorrecto. Perdieron el juego..."
         jump casa_explota
        "Azucar":
         "Incorrecto. Perdieron el juego..."
         jump casa_explota
        "Sal":
         "Correcto. Pasas a la siguiente ronda."
         jump pregunta_5
label pregunta_5:
    bombita "Ultima pregunta:¿Que decia Aristóteles que era el objetivo de la vida?"
    menu:
        "Reproducirte":
         "Incorrecto. Perdieron el juego..."
         jump casa_explota
        "La felicidad":
         "Correcto. Felicidades han pasado el juego"
         jump final_bueno
        "El estatus social":
         "Incorrecto. Perdieron el juego..."
         jump casa_explota