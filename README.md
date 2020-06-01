# Tina's Tree

## Eindopdracht programmeren
Wij gaan door middel van een _recursieve_ functie Tina een fractal laten tekenen.

1. Maandagochtend is er een algemene inleiding waarin we een eerste versie van de code zullen maken en beschikbaar stellen.
2. Je gaat vervolgens zelf met de code aan de slag om hier een verbetering is aan te brengen. Denk bijvoorbeeld aan het gebruik van _kleur_, andere regels voor het tekenen van takken, een ander aantal takken per generatie, het tekenen van bladeren, etc.
3. Woensdagochtend lever je de tussenstand in via moodle:
 * Een korte beschrijving met wat je probeert aan te passen.
 * De huidige (beste) versie van je code.
 * Een screenshot van deze uitvoering.
4. Woensdag is er een lesmoment moment om vragen te stellen. Als je tegen problemen aan loopt vul je deze _voor aanvang van de les_ in via moodle.

## Hints
* Sla je code vaak op _met een nieuwe bestandsnaam_. Zo raak je geen werk kwijt.
* Je kunt hiervoor het beste werken met Thonny. Als dit echt niet lukt is het technisch gezien mogelijk te werken met de in-browser versie van python maar omdat Tina er vaak lang over doet zal dit niet altijd goed werken. Ook als je (per ongeluk) de pagina herlaadt ben je je werk kwijt. Download je code dus vaak.
* Het uitvoeren van code zoals deze kan met de verkeerde instellingen _heel erg lang_ duren. Test de snelheid van je code.

## Nuttige functies

### Window-functies
* `tina.getscreen().exitonclick()` - Als Tina klaar is met tekenen sluit het venster. Als je dit toevoegt als laatste regel van je programma blijft het scherm open staan tot je ergens erin klikt. Zo kun je een screenshot ervan maken.

### Kleurfuncties
De `kleur` die je hier invult kan de naam van de kleur zijn "white", "green", "purple" etc. maar ook een _RGB-tuple_: Dit is een lijst van 3 getallen tussen 0.0 en 1.0 die de kleurwaarde in rood, groen en blauw voorstellen. `(1.0, 0.0, 1.0)` is bijvoorbeeld paars.
* `pencolor(kleur)` - Stelt de penkleur van tina in.
* `tina.getscreen().bgcolor(kleur)` - Past de achtergrondkleur aan.
