---
title: "Essbase: Dimension lesen"
description: Lesen Sie eine Oracle-Essbase-Dimensionsgliederung cloud-direkt in die Haupthierarchie einer PlaidCloud-Dimension – gemeinsame, reine Label-, Dynamic-Calc- und Attributmitglieder sowie alles andere, was die Gliederung nicht abbilden kann, werden namentlich abgelehnt.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/essbase/essbase-dimension-read.md
---

## Beschreibung

Liest eine Dimensionsgliederung aus einem Oracle-**Essbase**-Cube über Ihre [Oracle-Essbase-Verbindung](/de/guides/connections/essbase/) und lädt sie in die **Haupthierarchie** einer PlaidCloud-Dimension.

Dieser Schritt erscheint im Schrittmenü unter **Oracle Essbase**.

Der Schritt erreicht Essbase **cloud-direkt** über dessen REST-API – für diesen Schritt gibt es keinen lokalen Agent-Pfad und keine Remote-Variante.

## Konfiguration

### Essbase-Quelle

| Feld | Erforderlich | Hinweise |
|---|---|---|
| Verbindung | Ja | Die [Oracle-Essbase-Verbindung](/de/guides/connections/essbase/), über die gelesen wird. |
| Anwendung | Ja | Die Essbase-Anwendung, aus der gelesen wird. Die Auswahl listet die Anwendungen auf, die das Servicekonto der Verbindung sehen kann; legt die Verbindung eine Standardanwendung fest, ist sie vorausgewählt. |
| Cube (Datenbank) | Ja | Der Cube innerhalb der gewählten Anwendung, aus dem die Gliederung gelesen wird. |
| Dimension | Ja | Die Essbase-Dimension, deren Gliederung gelesen wird. |

### PlaidCloud-Zieldimension

| Feld | Erforderlich | Hinweise |
|---|---|---|
| Zieldimension | Ja | Die PlaidCloud-Dimension, in die die Gliederung geladen wird. |

## Was dieser Schritt nicht abbilden kann

| Einschränkung | Bedeutung |
|---|---|
| Gemeinsame Mitglieder | Ein gemeinsames Mitglied (Shared Member) verwendet die Daten eines anderen Mitglieds unter einem zweiten übergeordneten Knoten erneut. Ein Dimensionsknoten in PlaidCloud hat genau einen übergeordneten Knoten, daher wird ein gemeinsames Mitglied namentlich abgelehnt, statt als Duplikat geladen oder stillschweigend verworfen zu werden. Lesen Sie die primäre Aggregation als eigene PlaidCloud-Dimension – der zweite übergeordnete Knoten eines gemeinsamen Mitglieds lässt sich hier nicht abbilden. |
| Reine Label-Mitglieder | Ein reines Label-Mitglied (Label Only) dient der Navigation und enthält nie eigene Daten. Es wird namentlich abgelehnt, statt als gewöhnliches Mitglied geladen zu werden, von dem nachgelagert niemand erwartet, dass es leer ist. |
| Dynamic-Calc-Mitglieder | Der Wert eines Dynamic-Calc-Mitglieds wird von Essbase bei Bedarf berechnet und nie gespeichert. Dieser Schritt liest die Struktur der Gliederung, keine berechneten Daten; daher wird ein Dynamic-Calc-Mitglied namentlich abgelehnt, statt wie ein gespeichertes Mitglied geladen zu werden. |
| Attributdimensionen | Eine Attributdimension klassifiziert Mitglieder einer Basisdimension – sie ist keine eigenständige Hierarchie von Fakten. Das Lesen einer solchen wird grundsätzlich abgelehnt; lesen Sie stattdessen die Basisdimension. |
| Nicht abbildbare Konsolidierungsoperatoren | Eine PlaidCloud-Kante trägt ein Konsolidierungskennzeichen (`+`, `-` oder `~`). Die Essbase-Operatoren `+` und `-` werden direkt zugeordnet. `*`, `/` und `%` lassen sich nicht als einfaches Aggregationsvorzeichen darstellen – ein Mitglied, das einen davon verwendet, wird namentlich abgelehnt, statt mit dem falschen Vorzeichen geladen zu werden. |
| Gliederungen über der Mitgliedergrenze | Eine Dimensionsgliederung mit mehr als **5.000 Gliederungsmitgliedern insgesamt** wird abgelehnt, statt teilweise geladen zu werden; der Fehler nennt sowohl die beobachtete Anzahl als auch die Obergrenze. Lesen Sie eine flachere Ebene der Hierarchie oder einen kleineren Teilbaum, um unter die Grenze zu kommen. |

## Verwandte Themen

- [Mit Oracle Essbase verbinden (Leitfaden)](/de/guides/connections/essbase/) – die Verbindung erstellen.
- [Oracle Essbase Connector](/de/reference/connectors/erp/oracle-essbase/) – Referenz der Verbindungsfelder.
- [Essbase: Cube abfragen](/de/reference/workflow-steps/essbase/essbase-query/) – führt cloud-direkt eine Live-MDX-Abfrage gegen einen Cube aus.
- [Oracle-Essbase-Schritte](/de/reference/workflow-steps/essbase/)
