---
title: "TM1: Cube abfragen (Agent)"
description: "Lesen Sie einen Cube-Ausschnitt von einem lokalen IBM-TM1-/Planning-Analytics-Server, den die Cloud nicht direkt erreichen kann — dieselbe Ansichts-/MDX-/Betrachtungspunkt-Abfrage wie TM1: Cube abfragen, über einen installierten PlaidLink-Agent ausgeführt."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote.md
---

## Beschreibung

Das lokale Gegenstück zu [TM1: Cube abfragen](/de/reference/workflow-steps/ibm-planning-analytics/tm1-query/): dasselbe Lesen — eine gespeicherte **Ansicht** oder eine **MDX**-Abfrage gegen einen TM1-Cube, mit optionalem Betrachtungspunkt-Ausschnitt (POV), abgelegt als Projekttabelle —, jedoch über einen installierten [PlaidLink-Agent](/de/reference/cli/plaidlink/) in Ihrem Netzwerk ausgeführt statt direkt aus der Cloud aufgerufen. Verwenden Sie diesen Schritt anstelle von TM1: Cube abfragen, wenn der TM1-Server nur aus Ihrem eigenen Netzwerk erreichbar ist.

Dieser Schritt erscheint im Schrittmenü unter **IBM TM1 / Planning Analytics**.

## Unterschiede zu TM1: Cube abfragen

| | TM1: Cube abfragen | TM1: Cube abfragen (Agent) |
|---|---|---|
| Transport | Direkt aus der Cloud über REST | An einen PlaidLink-Agent in Ihrem Netzwerk gesendet |
| Konfigurationsfelder | — | Identisch, plus ein erforderlicher **Agent** |
| Ermittlung von Cube/Ansicht | Live, aus der verbundenen Datenbank | Nicht verfügbar — geben Sie die Namen von Hand ein |
| Vorschau vor dem Speichern | Ja | Nicht verfügbar |

Alles Übrige — die Verbindung, die Datenbank, die Wahl zwischen Ansicht und MDX, der Betrachtungspunkt-Ausschnitt, Null-/Leerzellen unterdrücken, Zeilenlimit und das Muster des inkrementellen Extrakts nach Periode — funktioniert genau wie auf der Seite [TM1: Cube abfragen](/de/reference/workflow-steps/ibm-planning-analytics/tm1-query/) beschrieben. Nur die folgenden Unterschiede sind für diesen Schritt spezifisch.

## Konfiguration

### Quelle und Ziel

| Feld | Erforderlich | Hinweise |
|---|---|---|
| Agent | Ja | Der PlaidLink-Agent, an den dieses Lesen gesendet wird. Sein Build muss den TM1-Handler enthalten (siehe [Anforderungen](#anforderungen) unten). |
| TM1-Verbindung | Ja | Die [TM1-Verbindung](/de/guides/connections/tm1/), über die gelesen wird. Die Verbindungsauswahl wird nicht nach dem gewählten Agent gefiltert — geben Sie die Verbindung separat für den Agent frei (siehe unten). |
| Umgebung | Ja | Die Umgebung der Verbindung. |
| Datenbank | Ja | Die abzufragende TM1-Datenbank (Instanz). |
| Cube | Ja | Der abzufragende TM1-Cube. Wird von Hand eingegeben — bei diesem Schritt gibt es keine Live-Ermittlung. |
| Zieltabelle | Ja | Die Projekttabelle, in der das zurückgegebene Cellset landet. |

### Ausschnitt und Optionen

Dieselben Felder wie bei [TM1: Cube abfragen](/de/reference/workflow-steps/ibm-planning-analytics/tm1-query/#ausschnitt) — Quellmodus (Nach Ansicht / Nach MDX), Ansicht, MDX, Betrachtungspunkt, Null-/Leerzellen unterdrücken und Zeilenlimit —, alle per Eingabe statt per Ermittlung und alle bei der Ausführung des Schritts validiert statt in einer Vorschau.

## Keine vom Agent vermittelte Ermittlung

Die Auswahlfelder für Cube, Ansicht und Dimension bei TM1: Cube abfragen fragen den verbundenen Server live ab, während Sie den Schritt bearbeiten. Diese Live-Ermittlung gibt es für diesen Schritt nicht: Ein Agent ist nur während einer Ausführung erreichbar, nicht, solange ein Formular in Ihrem Browser geöffnet ist. Cube, Ansicht und MDX werden eingegeben, und ein nicht erkannter Name lässt die Ausführung mit einem klaren Fehler fehlschlagen, statt stillschweigend zu scheitern. Aus demselben Grund gibt es keine Schaltfläche **Vorschau** — eine Vorschau müsste TM1 erreichen, was nur der Agent kann.

## Anforderungen

Zum Lesen eines lokalen TM1-Servers benötigen Sie:

- **Einen installierten PlaidLink-Agent** auf einem Rechner mit Netzwerkzugriff auf den TM1-Server. Siehe [PlaidLink installieren](/de/reference/cli/plaidlink/install/).
- **Einen Build dieses Agent, der den TM1-Handler enthält.** PlaidCloud prüft vor dem Senden die vom Agent gemeldeten Fähigkeiten. Ein Agent, dessen Build älter als diese Fähigkeit ist, kann die Anfrage nicht bedienen. **PlaidLink aktualisiert sich nicht automatisch** — ein vorhandener Agent muss manuell neu gebaut bzw. neu installiert werden, um TM1-Unterstützung zu erhalten. Siehe [PlaidLink aktualisieren](/de/reference/cli/plaidlink/upgrade/).
- **Die TM1-Verbindung, die für diesen Agent freigegeben ist**, zusätzlich zu allen Mitglieds- oder Gruppenzugriffen, die sie bereits hat — erteilen Sie die Freigabe über die Liste `Actions > Agents` der Verbindung. Siehe [Sicherheitsmodell](/de/guides/connections/create-connection/#sicherheitsmodell).

## Verwandte Themen

- [TM1: Cube abfragen](/de/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — das Cloud-direkte Gegenstück, das dieser Schritt spiegelt.
- [TM1: Dimension lesen](/de/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) — lädt eine TM1-Hierarchie in eine PlaidCloud-Dimension, direkt aus der Cloud.
- [Mit TM1 verbinden (Leitfaden)](/de/guides/connections/tm1/) — die Verbindung erstellen.
- [TM1-Connector](/de/reference/connectors/rest/tm1/) — Referenz der Verbindungsfelder, einschließlich des lokalen Agent-Wegs.
- [PlaidLink](/de/reference/cli/plaidlink/) — Agents installieren und aktualisieren.
- [Schritte für IBM TM1 / Planning Analytics](/de/reference/workflow-steps/ibm-planning-analytics/)
