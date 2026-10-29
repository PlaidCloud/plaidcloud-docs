---
title: "TM1: Dimension lesen"
description: Lesen Sie eine IBM-TM1-/Planning-Analytics-Hierarchie — Elemente, Eltern-Kind-Kanten und Elementattribute — direkt aus der Cloud über REST in eine PlaidCloud-Dimension.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read.md
---

## Beschreibung

Liest eine Hierarchie aus einer IBM-**TM1-/Planning-Analytics**-Dimension über Ihre [TM1-Verbindung](/de/guides/connections/tm1/) und lädt sie in eine PlaidCloud-Dimension. Die Elemente, Eltern-Kind-Kanten und Elementattribute der TM1-Hierarchie werden zunächst als Eltern-Kind-Zeilen in einer Tabelle bereitgestellt, und die PlaidCloud-Dimension wird aus dieser Staging-Tabelle aufgebaut — mit demselben Ladevorgang, den der PlaidCloud-eigene Schritt Dimension Load ausführt, sodass eine TM1-Hierarchie genauso landet wie eine von Hand erstellte oder jede andere extern bezogene.

Dieser Schritt erscheint im Schrittmenü unter **IBM TM1 / Planning Analytics**.

Der Schritt erreicht TM1 **direkt aus der Cloud** über dessen REST-API — es ist kein lokaler Agent beteiligt. Den lokalen Weg finden Sie unter [TM1: Cube abfragen (Agent)](/de/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/).

## Konfiguration

### TM1-Quelle

| Feld | Erforderlich | Hinweise |
|---|---|---|
| TM1-Verbindung | Ja | Die [TM1-Verbindung](/de/guides/connections/tm1/), über die gelesen wird. |
| Umgebung | Ja | Die Umgebung der Verbindung. |
| Datenbank | Ja | Die TM1-Datenbank (Instanz), aus der gelesen wird. Standardmäßig die Standarddatenbank der Verbindung, falls eine festgelegt ist. |
| TM1-Dimension | Ja | Die zu lesende TM1-Dimension. Wird live aus der verbundenen Datenbank ermittelt oder von Hand eingegeben. |
| TM1-Hierarchie | Nein | Die Hierarchie innerhalb der Dimension. Wird live ermittelt, sobald eine Dimension gewählt ist, oder von Hand eingegeben. Lassen Sie das Feld leer, um die eigene (implizite) Hierarchie der Dimension zu lesen, die TM1 nach der Dimension benennt. |
| Staging-Tabelle | Ja | Die Tabelle, in der die rohen Eltern-/Kind-/Attributzeilen landen, bevor die PlaidCloud-Dimension daraus aufgebaut wird. |

Sobald eine Dimension und eine Hierarchie gewählt sind, zeigt das Formular, welche TM1-Elementattribute als PlaidCloud-**Aliase** und welche als **Eigenschaften** landen — gesteuert vom TM1-eigenen Attributtyp (`Alias` gegenüber `Numeric`/`String`). Auch der eigene TM1-Typ jedes Elements (Numeric, String oder Consolidated) landet als Eigenschaft mit dem Namen `tm1_element_type`.

### PlaidCloud-Zieldimension

| Feld | Erforderlich | Hinweise |
|---|---|---|
| Dimension dynamisch angeben | Eines von beiden | Name der Zieldimension, der `{variable}`-Token enthalten darf, die zur Laufzeit aufgelöst werden. Standardmäßig ausgewählt. |
| Bestimmte Dimension verwenden | Eines von beiden | Wählen Sie stattdessen eine bereits vorhandene PlaidCloud-Dimension aus der Struktur. |
| Alternativhierarchie | Nein | Ein Schlüssel einer PlaidCloud-Alternativhierarchie, in die geladen wird. Lassen Sie das Feld leer, um die Haupthierarchie zu laden. |

Das Laden in eine Alternativhierarchie wird validiert, bevor etwas geschrieben wird: Eine PlaidCloud-Alternativhierarchie darf keinen Knoten umhängen, der bereits in der Haupthierarchie der Dimension existiert, und eine TM1-Alternativhierarchie teilt ihre Elemente per Definition mit der TM1-eigenen Haupthierarchie, sodass dies die normale Form für diese Option ist und kein Randfall. Wenn der Elternknoten einer geparsten Zeile bereits in der Haupthierarchie der Zieldimension existiert, schlägt der Schritt gleich zu Beginn fehl, bevor die Staging-Tabelle angetastet wird, und nennt die kollidierenden Elternknoten.

## Was dieser Schritt nicht abbilden kann

| Einschränkung | Bedeutung |
|---|---|
| Elemente mit mehreren Elternknoten werden abgelehnt | Ein PlaidCloud-Dimensionsknoten hat genau einen Elternknoten pro Hierarchie. Ein TM1-Element, das in derselben Hierarchie unter zwei Konsolidierungen steht, kann nicht geladen werden — der Schritt schlägt mit einem benannten Fehler fehl, der jedes betroffene Element und seine Elternknoten auflistet, statt das Element stillschweigend aus der ersten Konsolidierung zu entfernen. Lesen Sie die alternative Aggregation als eigene PlaidCloud-Dimension ein oder beheben Sie die doppelte Elternschaft zuerst in TM1. |
| Konsolidierungsgewichte tragen nur ein Vorzeichen | Eine PlaidCloud-Kante trägt ein Konsolidierungskennzeichen (`+`, `-` oder `~`), keinen Koeffizienten. Das TM1-Gewicht `0` wird zu `~` (das Mitglied wird nicht in seinen Elternknoten aggregiert), ein negatives Gewicht wird zu `-`, ein positives Gewicht wird zu `+`, und ein fehlendes Gewicht (der TM1-eigene Standard) wird als `+` behandelt. Ein **gebrochenes oder multiplikatives Gewicht — 0.5, 2.0 — kann nicht abgebildet werden**: Es landet als einfaches `+`, und der Multiplikator geht verloren. Dies wird gezählt und benannt, nicht verschluckt — die Schrittwarnung der Ausführung meldet, wie viele Kanten betroffen waren, und listet sie als `parent -> child (weight)` auf, zum Beispiel `Total Revenue -> Product A (0.5)`, begrenzt auf 10 mit „(and N more)" darüber hinaus. Eine Wurzelkante (ohne Elternknoten) heißt `(root)` und bleibt nicht leer. Ein vorhandenes, aber nicht numerisches Gewicht wird ausdrücklich abgelehnt, statt geraten zu werden. |
| Keine vom Agent vermittelte Ermittlung | Dieser Schritt arbeitet nur direkt aus der Cloud — unter [TM1: Cube abfragen (Agent)](/de/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) erfahren Sie, wie Sie einen TM1-Server lesen, den die Cloud nicht erreichen kann. |

## Verwandte Themen

- [Mit TM1 verbinden (Leitfaden)](/de/guides/connections/tm1/) — die Verbindung erstellen.
- [TM1-Connector](/de/reference/connectors/rest/tm1/) — Referenz der Verbindungsfelder, einschließlich des lokalen Agent-Wegs.
- [TM1: Cube abfragen](/de/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — Cube-Daten lesen, direkt aus der Cloud.
- [TM1: Cube abfragen (Agent)](/de/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote/) — Cube-Daten über einen lokalen PlaidLink-Agent lesen.
- [Dimension Load](/de/reference/workflow-steps/dimensions/dimension-load/) — derselbe Dimensionsladevorgang, auf dem dieser Schritt aufbaut.
- [Schritte für IBM TM1 / Planning Analytics](/de/reference/workflow-steps/ibm-planning-analytics/)
