---
title: Call SAP RFC (Schritt)
description: Rufen Sie SAP-RFC-Funktionsbausteine aus einem PlaidCloud-Workflow-Schritt auf, um SAP-ECC- und S/4HANA-Systeme direkt anzubinden.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-rfc.md
---

## Beschreibung


Ruft einen SAP-ECC- / S/4HANA-Remote-Function-Call (RFC) auf und liefert die Daten in tabellarischer Form. Diese Daten stehen anschließend für Transformationsprozesse in PlaidCloud zur Verfügung.


## Datenziel

Legen Sie das RFC-Ergebnis als Datei oder in einer Tabelle ab.

Bei **Datei** wird das Ergebnis als **JSON**, **Durch Komma getrennt**, **Durch Tabulator getrennt**, **Durch senkrechten Strich getrennt** oder **Parquet** geschrieben. Eine Parquet-Datei enthält dieselben Spaltentypen wie eine Tabelle.

Bei **Tabelle** wird das Ergebnis in einer **Zieltabelle** abgelegt, typisiert anhand der eigenen Felddefinitionen des RFC-Funktionsbausteins:

| SAP-Feldtyp | Wird abgelegt als |
|---|---|
| Datum | Datum. Ein leeres oder initiales Datum wird leer abgelegt. Ein ungültiges Datum wird leer abgelegt, und der Schritt endet mit einer Warnung, die die Spalte nennt. |
| Gepackte Dezimalzahl | Exakte Dezimalzahl. Bei mehr als 10 Nachkommastellen oder 28 Ganzzahlstellen wird stattdessen Text abgelegt, und der Schritt endet mit einer Warnung, die die Spalte nennt. |
| Ganzzahl | Ganzzahl. |
| `FLOAT` | Double. |
| Dezimale Gleitkommazahl | Exakter Text. |
| `NUMC`, `CHAR` | Text, führende Nullen bleiben erhalten. |
| Uhrzeit | Text, als `HH:MM:SS`. |
| Rohbytes | Hex-Text. |
| `UTCLONG` | Text. |

Wenn SAP die Felder des Funktionsbausteins nicht beschreiben kann, werden Dezimalzahlen stattdessen als exakter Text abgelegt.

Wenn SAP den Funktionsbaustein beschreibt, wird jeder Parameter in den erwarteten Typ umgewandelt: Datumswerte in `YYYYMMDD`, Uhrzeiten in `HHMMSS`, Ganzzahlen und Dezimalzahlen in Zahlen, Textfelder in Text sowie Struktur- und Tabellenparameter feldweise. Ein Wert, der sich nicht in einen Ganzzahl- oder Dezimalparameter umwandeln lässt, lässt den Schritt fehlschlagen.

## Beispiele


### RFC-Parameter


Wählen Sie den **Zu verwendender Agent** aus. Wählen Sie in der Dropdown-Liste das **Zielverzeichnis** aus und navigieren Sie darunter zum passenden untergeordneten Ordner für die Datei. Vergeben Sie anschließend einen passenden Namen für den 
„Target File Name“. Geben Sie unter „Function Call Information“ die Funktion und den **Rückgabewert-Parameter** ein und wählen Sie die Parameter aus.

Im Abschnitt „Parameters“ können Sie **Zeile einfügen** oder **Zeile anhängen** wählen sowie die Parameter benennen und mit Werten versehen. Legen Sie die Anzahl für **Max. gleichzeitige Anfragen** fest 
und wählen Sie „Wait for RFC to Complete“. Speichern und führen Sie den Schritt aus.



### Erweiterte Werteiteration


Sie können oben auf dieser Registerkarte „No Iterators“ wählen und dann den Schritt speichern und ausführen, oder Sie legen Iteratoren fest.


Hier können Sie unter **Iterieren über** die Option „Specify Argument Values“ wählen und Argumente anlegen, die anschließend zum **Iterationswert** führen.


Neben **Iteratorargument zum Bearbeiten der Werte auswählen** stehen die Optionen „Insert Row“, **Zeile anhängen**, **Zeile löschen**, **Nach unten** und **An das Ende verschieben** zur Verfügung. 
Darunter können Sie mit demselben Dropdown-Menü **Bereichsiteratoren** wählen. Der letzte Abschnitt heißt „Exclusions for Selected Range Iteration“ 
und bietet pro Zeile dieselben Optionen zum Hinzufügen, Löschen usw. Die auszuschließenden Werte können Sie darunter eingeben. Speichern und führen Sie den Schritt aus.
