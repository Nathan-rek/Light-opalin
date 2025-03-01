## Préambule

Notre installation tente de comprendre, à travers un équipement technique, les possibilités d'interaction entre les objets qui composent un espace. Le son et la lumière sont deux dimensions sensibles que nous mettons en rapport particulier afin de soulever un ensemble d'interactions distinctes qui révèlent non pas une totalité, mais des possibilités de relations.
<br>

Un microphone enregistre en permanence les sons de l'espace et utilise ses enregistrements pour générer un son. L'appareil sonore agit comme un supra-écho non linéaire en enregistrant et en émettant en même temps. Il utilise sa propre cognition pour sélectionner parmi tous les sons entendus ceux qu'il reproduit et ceux qu'il ignore. En jouant en permanence, il devient un écho constant et irrégulier, doté d'une mémoire et d'une manière d'expression propres. Cet écho sonore déclenche une réaction lumineuse. Un panneau lumineux se modifie en fonction de ce que le dispositif sonore produit. Il prend en compte des paramètres qui lui sont propres, des propriétés sensibles qu'il transforme en d'autres propriétés sensibles. Le panneau varie en intensité lumineuse, ce qui lui permet d'exprimer une relation changeante avec tous les objets matériels présents dans l'espace, accentuant les ombres portées ou obstruant entièrement l'espace. La lumière dévoile ainsi ses possibilités d'interactions spatiales. Cependant, ces conditions d'interactions [^1] sont également orchestrées par un système de relation entre émission et réception. L'installation ne prétend pas être un appareil autonome orchestrant sa propre relation au monde. Elle amplifie des relations déjà présentes, mais dont les possibilités d'interactions se croisent grâce au dispositif. Le dispositif émane du lieu et ne le dépasse pas mais il le réinvente par ses nouvelles possibilités techniques. 
<br>


↱ [Jury B2](jury-b2)

<hr>

## Traces -Développement
#### TouchDesigner -> Ruban Led

Dans un premier temps, j'ai exploré les relations entre le son et la lumière à l'aide d'un ruban LED WS. J'ai utilisé un FFT dans TouchDesigner [serial-led.toe](https://github.com/Nathan-rek/Light-opalin/tree/master/02_Prod/touchdesigner) pour convertir les variations sonores en phases d'un dégradé, qui envoie ensuite ses coordonnées de couleur au ruban. 
Pour transmettre les données, j'ai utilisé le [CHOP Serial](https://derivative.ca/UserGuide/Serial_CHOP), qui permet une communication série avec des composants  Arduino. Cela me permet d'envoyer en série les valeurs RGB de chaque LED.

 [touch-designer file: serial-led.toe](https://github.com/Nathan-rek/Light-opalin/tree/master/02_Prod/touchdesigner) | [Arduino File](https://github.com/Nathan-rek/Light-opalin/tree/master/02_Prod/arduino/neopixel). 

<br>

Musique: [*Do While*, Oval](https://oval.bandcamp.com/track/do-while) | 9 ‎Février ‎2024
*<video controls>
    <source src="static/img/light-opalin/ruban-led.mp4" type="video/mp4">
</video>
<img src="static/img/light-opalin/graphviz-td-ruban.png" alt="Titre de l'image" >*
#### TouchDesigner -> LEDBoard

Ensuite, j'ai cherché comment moduler une tension électrique, notamment sur des panneaux [LEDVANCE PANEL 600 36W | 4000K | 4320 lm | White Aluminuim Housing](https://benelux.ledvance.com/fr/professionnels/produits/luminaires/luminaires-professionnels/luminaires-panel/panel-ip54/panel-ip54-de-forte-puissance--600-x-600-mm-c8598?productId=137324). J'utilise le même FFT qui me permet d'analyser une musique cette fois pour transformer un son en une variation de 0 - 255, ordre de grandeur propre aux variations PWM (modulation de largeur d'impulsion) [touchdesigner file:touch-to-mosfet](https://github.com/Nathan-rek/Light-opalin/blob/master/02_Prod/touchdesigner/touch-to-mosfet.toe). Cela me permet d'envoyer un signal PWM au [Mosfet](https://protosupplies.com/product/lr7843-mosfet-control-module/), qui régule la tension envoyée aux panneaux LED. Transformant la variation musical en variation de tension.

<br>
[Arduino file:pwm-touchtouno-1.ino](https://github.com/Nathan-rek/Light-opalin/blob/master/02_Prod/arduino/pwm_touchtouno-1.ino/pwm_touchtouno-1.ino.ino)

<br>

Musique: [*QKThr*, Aphex Twin](https://www.youtube.com/watch?v=9wCfNFmpL1s) | 15 ‎Février ‎2024
*<video controls src="static/img/light-opalin/LED-num.mp4"> </video>
<img src="static/img/light-opalin/graphviz-td-LEDboard.png">*


Ensuite, j'ai ajouté un deuxième panneau au module en superposant simplement les câbles positif et négatif du second, sans apporter de modifications dans le code.
<br>

Musique: [*Blink*, Hiroshi Yoshimura](https://www.youtube.com/watch?v=0RHmeCjqnfw) | 12 ‎Mars ‎2024
*<video controls src="static/img/light-opalin/2LED.MP4"> </video>
<img src="static/img/light-opalin/graphviz-td-2LEDboard.png">*

#### Test In Situ: TouchDesigner -> LEDBoard
‎Musique: [*Aluminaut Rescues Alvin*, Episodes in Oceanography ](https://www.youtube.com/watch?v=Gv41yzQal7c&t=121s)  | 27 ‎Février ‎2024

*<video controls src="static/img/light-opalin/iphone-Decarli-(4).mp4"> </video>*


#### Test In Situ: MaxMSP -> LEDBoard

17 Avril ‎2024

*<video controls src="static/img/light-opalin/marie-vid.mp4"> </video>*

<hr>

*<img src="static/img/light-opalin/graphviz.png">*

## Bucket List

- Lot de câbles Dupont
- 1 [Carte Arduino Uno](https://store.arduino.cc/products/arduino-uno-rev3)
- 1 [USB 2.0 Cable Type A/B](https://store.arduino.cc/products/usb-2-0-cable-type-a-b)
- 1 [LR7843 MOSFET Control Module](https://protosupplies.com/product/lr7843-mosfet-control-module/)
- 2 [LEDVANCE PANEL 600 36W | 4000K | 4320 lm | White Aluminuim Housing](https://benelux.ledvance.com/fr/professionnels/produits/luminaires/luminaires-professionnels/luminaires-panel/panel-ip54/panel-ip54-de-forte-puissance--600-x-600-mm-c8598?productId=137324)
- 1 Alimentation 30V
- 2 Câble de charge Croco clips
- 10 Câbles basiques

## Footnotes
  
[^1]: Longo, Anna, « *Une esthétique spéculative est-elle possible ?* »:, Cahiers critiques de philosophie, no. 1, janvier 2018, pp. 91‑112., " *les objets n’interagissent pas directement, mais au moyen de certaines propriétés sensibles se manifestant dans le cadre d’un rapport particulier* "