# Minecraft Hacking Raspberry Pi Grundlagen von erfindergarden 


Stand 14. April 2017


---

##Kursinhalt

###SD Karte brennen

Es kann passieren, dass deine Karte plötzlich nicht mehr funktioniert, mit folgenden Schritten kannst du dir eine neue machen:

* besorge dir eine neue SD Karte (mind. 8GB Class 10)
* [Downloade] (http://www2.kano.me/downloads) das kano image oder ein anderes Raspberry Pi OS Image
* Mac -> [ApplePiBaker] (http://www.tweaking4all.com/hardware/raspberry-pi/macosx-apple-pi-baker/I), Anleitung [hier](./imagebrennenmac.md)
* Windows und Linux --> Etcher



### Einkaufsliste

Alles was du brauchst um nach dem Kurs weiterzumachen findest du in der [Einkaufsliste](./einkaufsliste.md).


### Lapdock mit dem Pi verbinden

Schaue dir die [Anleitung](./lapdockpi) an. 

### Projekt Beispiele

*

### Pi Einführung

### Pong Hacking


### Minecraft Hacking 

Folgende Aufgaben hast du im Kurs gemacht:

* Minecraft - Challenge 1: Load up Minecraft
* Minecraft - Challenge 2: Hello World
* Minecraft - Challenge 3: Teleport
* Minecraft - Challenge 4: Make a Lake
* Minecraft - Challenge 5: Build a Mega Block
* Minecraft - Challenge 6: All Along the Watchtower
* Minecraft - Challenge 7: Shady Tunnels
* Minecraft - Challenge 8: Volcano
* Minecraft - Challenge 9: Build a Tall Tower
* Minecraft - Challenge 10: Stairway to Heaven
* Minecraft - Challenge 11: Castle Wall
* Minecraft - Challenge 12: Lava Trail
* Minecraft - Challenge 13: Freeze

Solltest du noch nicht fertig geworden sein kannst du zu Hause die Aufgaben fertig machen. Im Playground kannst du dann deine eigenen Programme schreiben und dir auch anzeigen wie der Code in Python aussehen würde. 

### Musik Coden

Im Kurs hast du gelernt Töne zu programmieren und man Töne endlos abspielen lassen kann.

Als Hausaufgabe schreibe ein eigenes Musikstück mit Code. Solltest du noch keinen Pi haben kannst du auch Sonic Pi auf dem Mac oder deinem Windows Computer programmieren. 


### Scratch und GPIOS

Das Aufsteckboard das wir im Kurs verwendet haben findest du bei [Ryanteck](https://ryanteck.uk/). Normalerweise verwenden wir dazu unseren TNT Button. 
  

#### TNT Circle 

Am Endes des Kurses habe ich dir noch kurz gezeigt wir mit dem Drücken eines Buttons einen TNT Circle erstellt. 

Den Code dazu findest du unter [Code](./code) 

Öffne das Terminal und tippe. 

```
sudo geany 

```

Das passwort ist kano. 

Dann öffnet sich der Editor. Mit dem kleinen Rädchen kannst du den Code ausführen und mit ```Ctrl + C``` kannst du in stoppen.

Wichtig ist, dass du deinen Code immer unter dem Ordner MyAdventures abspeicherst mit der Endung .py und Minecraft offen hast, wenn du den Code ausführst. 

Mehr Code findest du [hier](http://eu.wiley.com/WileyCDA/Section/id-823690.html).

## More Minecraft Worlds

Die Pi Minecraft Edition nutzt das gleiche Level Format wie die Minecraft Pocket Edition [here](https://drive.google.com/open?id=0B3iYmii-HJ7TeE5MS3BqM2hwaFE) kannst du mehr Welten finden wie Hogwarts, Avatar Hometree, Circular Town, Farm Village, Spleef Arena und mehr. Weitere Welten im [Minecraft Forum](http://www.minecraftforum.net/forums/minecraft-pocket-edition/mcpe-maps/mcpe-wip-maps).

Lade die Welten herunter und kopiere sie in den Ordner ```minecraftWorlds```. Um diesen Ordner zu sehen musst du erst versteckete Dateien (Show Hidden) anzeigen dann findest du ihn under .minecraft > games > com.mojang > minecraftWorlds. 

## Spiele deine programmierte Welt auf den i-phone/i-pad

Du kannst deine mit dem Pi programmierten Welten dann in deiner Pocket Edition auf dein i-pad oder i-phone kopieren. In [diesem Video](https://www.youtube.com/watch?v=muB7SDl6158) wird die gezeigt wie das geht. Für Mac empfehle ich dir den i-explorer. 


## LINKS und Bücher

Es gibt mittlerweile viele Zeitschriften, Bücher und Internetseiten die die helfen weiter mit dem Pi zu arbeiten. Ich empfehle dir erstmal, mit dem weiterzuarbeiten was wir im Kurs gemacht haben und dann auf der Raspberry Pi Seite eine Tutorial durch zu machen. Sehr gut finde ich auch ein Magazin zu abonnieren und jeden Monat durch interessante Projekte inspiriert zu werden.  

* [Ressources in Englisch auf der Raspberry Pi Webseite] (https://www.raspberrypi.org/resources/)
* das MagPi Magazin (Englisch)

## Quellen

Aufsteckboards und Zubehör kannst du bei folgenden Händlern erwerben. Ich würde dir als Einstieg den Traffichat empfehlen oder den Explorer Hat und dann einen Sense Hat oder eine Kamera. Leider scheint es da ein paar Produktionsenpässe zu geben und das einzige Board was zur Zeit zur Verfügung steht ist der Traffic Hat. 

* [Ryanteck](https://ryanteck.uk/)  
	-> [Traffic Hat](https://ryanteck.uk/hats/1-traffichat-0635648607122.html) (9,30 €)
* [seedstudio ](http://www.seeedstudio.com/depot/category_products?themes_id=1413)  
* Adafruit 
* [Pi Hut](http://thepihut.com/)
* [Pimoroni](http://www.pimoroni.com/)

##FAQ

**Wie schließe ich meinen Lapdock an?**

Siehe oben

**Wie wird der Pi mit Strom versorgt?**

Der Pi wird über das USB Kabel im Lapdock mit Strom versorgt. Bei meinem Setup ist es das Kabel mit dem Lila Tape drauf. 

**Ich sehe nichts auf meinem Bilschirm?**

Checke ob du die SD Karte eingesteckt hast und alle Kabel verbunden hast und ob sie fest in ihren Plätzen stecken. 


**Was ist das Password beim einloggen in Kano**

kano 

**Die Zeichen auf den Tasten stimmen nicht mit meinem Keyboard Layout überein, was kann ich machen?**

Unter Settings in kano kannst du deine Tastaturbelegungen auf Deutsch ändern. 

Und mit einem [Tastatursticker ](http://www.amazon.de/Selbstkleben-Deutsche-Tastatur-Aufkleber-TastaturAufkleber/dp/B0050O4K5C/ref=pd_sim_sbs_201_4?ie=UTF8&dpID=31ijYeQClxL&dpSrc=sims&preST=_AC_UL160_SR160%2C160_&refRID=1J1A4ZD3M4SX3HV9JPDT)kannst du dir eine Deutsche Tastatur auf die Tasten kleben.

## Download

* Entweder über "Download ZIP" rechts oben
* Oder direkt über git, ein gutes Tutorial dazu findest du hier: [try.github.io](https://try.github.io)

##Lizenz
Dieses Repository ist unter der Creative Commons Lizenz [CC-BY-SA] (http://creativecommons.org/licenses/by-sa/4.0/) lizensiert. 


## Kontakt

Schreibe uns jeder Zeit eine e-mail wenn du Fragen hast die in diesem Repository nicht benantwortet wuden. 

* Web: [www.erfindergarden.de](http://www.erfindergarden.de)
* Email: [play@erfindergarden.de](mailto:play@erfindergarden.de)
* Twitter: [@andreaskopp](https://twitter.com/andreaskopp) und [@jsphpl](https://twitter.com/jsphpl)