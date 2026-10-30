---
title: Call SAP Master Data Table RFC (Schritt)
description: Ruft einen SAP-ECC- / S/4HANA-Remote-Function-Call (RFC) auf, der auf Stammdatentabellen zugreift, und liefert die Daten in tabellarischer Form.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-master-data-table-rfc.md
---

## Beschreibung


Ruft einen SAP-ECC- / S/4HANA-Remote-Function-Call (RFC) auf, der auf Stammdatentabellen zugreift, und liefert die Daten in tabellarischer Form. Diese Daten stehen anschließend für Transformationsprozesse in PlaidCloud zur Verfügung. Zusätzlich können Sie die Struktur der Stammdatentabelle in eine separate Datei exportieren, die Spaltennamen, Datentypen und die Spaltenreihenfolge enthält.


## Beispiele


### RFC-Parameter


Wählen Sie den **Zu verwendender Agent** aus. Wählen Sie in der Dropdown-Liste das **Zielverzeichnis** aus und navigieren Sie darunter zum passenden untergeordneten Ordner für die Datei. Vergeben Sie anschließend einen passenden Namen für den „Target File Name“. Geben Sie unter „Function Call Information“ die Funktion und den **Rückgabewert-Parameter** ein und wählen Sie die Parameter aus.



Im Abschnitt „Parameters“ können Sie **Zeile einfügen** oder **Zeile anhängen** wählen sowie die Parameter benennen und mit Werten versehen. Legen Sie die Anzahl für **Max. gleichzeitige Anfragen** fest und wählen Sie „Wait for RFC to Complete“. Speichern und führen Sie den Schritt aus.
