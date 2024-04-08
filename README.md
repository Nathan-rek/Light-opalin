## Préambule
Un espace composé d'objets peut être abordé non pas comme un ensemble de substances uniques et singulières, mais comme un ensemble d'interactions distinctes qui révèlent non pas une totalité, mais des possibilités de relations.

Notre installation tente de comprendre, à travers un équipement technique, les possibilités d'interaction entre les objets qui la composent. Le son et la lumière sont deux dimensions sensibles que nous mettons en rapport particulier, tout en révélant d'autres manières dont ces objets peuvent interagir avec l'espace.

Un son généré se mêle à l'espace, un appareil qui agit comme un supra-écho. Cet appareil sonore enregistre et remodelle les sons de l'espace. Il utilise sa propre cognition pour sélectionner parmi tous les sons entendus ceux qu'il reproduit et ceux qu'il ignore. En jouant en permanence, il devient un écho constant, une mémoire propre au lieu et à sa capacité d'expression.

De cette première interaction sonore naît une interaction lumineuse. Un panneau lumineux se modifie en fonction de ce que le dispositif sonore produit. Il prend en compte des paramètres qui lui sont propres, des propriétés sensibles qu'il transforme en d'autres propriétés sensibles. Le panneau varie en intensité lumineuse, ce qui lui permet d'exprimer une relation changeante avec tous les objets matériels présents dans l'espace, accentuant les ombres portées ou obstruant entièrement l'espace. La lumière dévoile ainsi ses possibilités d'interactions spatiales. Cependant, ces conditions d'interaction sont également orchestrées par un système de relation entre émission et réception. L'installation ne prétend pas être un appareil autonome orchestrant sa propre relation au monde. Elle intensifie des relations déjà présentes, mais dont les possibilités d'interactions se conjuguent. En proposant par le sensible une relation qui n'est pas seulement celle d'un corps avec un objet, mais des objets entre eux.

## Traces -Développement
Dans un premier temps j'ai exploré les relations son-lumière via ruban LED WS. En traduisant avec un FFT les variations d'une musique afin de faire varier les phases d'un gradiant sur l'axe X qui ensuite envoi ses coordonées de couleur au ruban. En passant par le [CHOP Serial](https://derivative.ca/UserGuide/Serial_CHOP) qui permet de rentrer en communication serial avec des composants comme Arduino. J'intègre un code capable de recevoir du serial et de l'envoyer sur une Pin de mon arduino.  Cela me permet d'envoyer en serial la valeur RGB de chaque LED : [touch-designer file: serial-led.toe](https://github.com/Nathan-rek/Light-opalin/tree/master/02_Prod/touchdesigner) | [Arduino File](https://github.com/Nathan-rek/Light-opalin/tree/master/02_Prod/arduino/neopixel). 

<br>
Musique: [*Do While*, Oval](https://oval.bandcamp.com/track/do-while) 
*<video controls src="static/img/light-opalin/ruban-led.mp4"> </video>
<img src="static/img/light-opalin/graphviz-td-ruban.png">*


Ensuite, j'ai cherché comment moduler une tension électrique, notamment sur des panneaux [LEDVANCE PANEL 600 36W | 4000K | 4320 lm | White Aluminuim Housing](https://benelux.ledvance.com/fr/professionnels/produits/luminaires/luminaires-professionnels/luminaires-panel/panel-ip54/panel-ip54-de-forte-puissance--600-x-600-mm-c8598?productId=137324). J'utilise le même FFT qui me permet d'analyser une musique cette fois pour transformer un son en une variation de 0 - 255, ordre de grandeur propre aux variations PWM (modulation de largeur d'impulsion). Cela me permet d'envoyer un signal PWM au Mosfet, qui regule la tension envoyée aux panneaux LED. Transformant la variation musical en variation de tensoin.
<br>
Musique: [*QKThr*, Aphex Twin](https://www.youtube.com/watch?v=9wCfNFmpL1s)
*<video controls src="static/img/light-opalin/LED-num.mp4"> </video>
<img src="static/img/light-opalin/graphviz-td-LEDboard.png">*

Ensuite, j'ai inclus un deuxième panneau au module en superposant simplement les câbles positif et négatif de celui-ci, sans effectuer de modifications réelles.
<br>
Musique: [*Blink*, Hiroshi Yoshimura](https://www.youtube.com/watch?v=0RHmeCjqnfw) 
*<video controls src="static/img/light-opalin/2LED.MP4"> </video>
<img src="static/img/light-opalin/graphviz-td-2LEDboard.png">*


## Documentation
### MaxMPS
Marie...
### Arduino
Musique to LED
- TouchDesigner to Arduino: 

Les panneaux lumineux varient via la variation d'un MOSFET(LR7843 MOSFET) qui régule la tension envoyée aux paneaux. Pour Réguler la tension j'envoie une variation en PWM à un MOSFET.

<img src="static/img/light-opalin/graphviz.png">

