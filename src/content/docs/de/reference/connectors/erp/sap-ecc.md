---
title: SAP-ECC- und S/4HANA-Connector
description: Konfigurieren Sie in PlaidCloud die Verbindung SAP ECC / S/4HANA, um Finanz-, Logistik- und Betriebsdaten aus SAP über RFC in Ihre Workflows zu integrieren.
sidebar:
  order: 1
  label: SAP ECC / S/4HANA
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/sap-ecc.md
---

Ein Verbindungstyp deckt sowohl SAP ECC als auch SAP S/4HANA ab. Beide werden auf dieselbe Weise erreicht, nämlich über Remote Function Calls gegen den Anwendungsserver; PlaidCloud fragt Sie daher nicht, welche Generation Sie einsetzen. Wählen Sie auf dem Bildschirm **Verbindungen** **Neu → SAP-ECC-/S/4HANA-Instanz**.

Alle [SAP-Workflow-Schritte](/de/reference/workflow-steps/sap/) laufen gegen eine Verbindung dieses Typs. Wie Sie SAP durchsuchen und Tabellen, Transaktionen, Berichte und gespeicherte SAP-Queries extrahieren, lesen Sie unter [Ad-hoc-Extrakte aus SAP ECC / S/4HANA](/de/guides/connections/sap-adhoc-extract/).

## Dokumentation des Herstellers

SAP hat die gesamte ECC-Dokumentation entfernt und stellt derzeit nur Dokumentation für [S/4HANA](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE) bereit. Die RFC-Schnittstellen, die PlaidCloud verwendet, sind beiden gemeinsam.

## Konfiguration

Diese Felder werden beim Erstellen oder Bearbeiten der Verbindung angezeigt.

### Kontobeschreibung

| Feld | Typ | Beschreibung |
|---|---|---|
| Kontoname | Text | Anzeigename dieser Verbindung, der überall angezeigt wird, wo ein Schritt eine Verbindung auswählt. Erforderlich. |
| Memo | Text (mehrzeilig) | Optionale Notizen zur Verbindung, etwa auf welches System sie zeigt und wer sie verantwortet. |

### SAP-Umgebung

| Feld | Typ | Beschreibung |
|---|---|---|
| Client | Text | SAP-Mandantennummer, z. B. `100`. Erforderlich. |
| Language | Auswahl | Anmeldesprache als zweistelliger SAP-Code. Standardmäßig `EN`. Erforderlich. |
| Trace-Stufe | Auswahl | Ausführlichkeit des RFC-Traces: Off, Brief, Verbose oder Full. Belassen Sie sie auf Off, sofern Sie kein Verbindungsproblem diagnostizieren. Erforderlich. |
| Connection type | Optionsfeld | **Einzelne direkte Verbindung verwenden**, um einen Anwendungsserver zu erreichen, oder **Lastverteilte Mehrsystemverbindung verwenden**, um über einen Message-Server zu gehen. Die folgenden Felder werden entsprechend dieser Auswahl aktiviert. |

Die Auswahl von **Einzelne direkte Verbindung verwenden** aktiviert:

| Feld | Typ | Beschreibung |
|---|---|---|
| Host | Text | Hostname oder IP-Adresse des Anwendungsservers. |
| Systemnummer | Text | Zweistellige SAP-Systemnummer, z. B. `00`. |

Die Auswahl von **Lastverteilte Mehrsystemverbindung verwenden** aktiviert:

| Feld | Typ | Beschreibung |
|---|---|---|
| MS-Host | Text | Hostname oder IP-Adresse des Message-Servers. |
| MS-Server | Text | Port oder Dienstname des Message-Servers. |
| System-ID | Text | Dreistellige SAP-System-ID, z. B. `PRD`. |
| Group | Text | Anmeldegruppe, auf die verteilt wird, z. B. `PUBLIC`. |

### Authentifizierungsdaten

| Feld | Typ | Beschreibung |
|---|---|---|
| User | Text | SAP-Anmeldebenutzer für die RFC-Aufrufe. Erforderlich. |
| Password | Passwort | Passwort dieses Benutzers. Nur schreibbar: Lassen Sie das Feld beim Bearbeiten leer, um das gespeicherte Passwort beizubehalten. |

### Nutzung

| Feld | Typ | Beschreibung |
|---|---|---|
| Active (Allow Access) | Schalter | Gibt an, ob die Verbindung verwendet werden kann. Deaktivieren Sie sie, um die Verbindung zu pausieren, ohne sie zu löschen. |
| Schreibgeschützt | Schalter | Beschränkt die Verbindung auf Lesevorgänge. |

### Sicherheitsmodell

| Feld | Typ | Beschreibung |
|---|---|---|
| Sicherheitsmodell | Auswahl | Wer diese Verbindung verwenden darf: Private (Only Owners), Nur bestimmte Mitglieder, Nur bestimmte Sicherheitsgruppen oder Alle Arbeitsbereichsmitglieder. |

## Verbindung testen

**Verbindung testen** im Verbindungsfenster meldet sich mit den obigen Angaben an und meldet das Ergebnis zurück. Wenn Sie eine bestehende Verbindung bearbeiten und eine Einstellung ändern, geben Sie das Passwort vor dem Testen erneut ein, da das gespeicherte nicht zusammen mit den geänderten Werten gesendet wird.
