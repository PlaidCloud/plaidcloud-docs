---
title: Call SAP Financial Document Attachment (Schritt)
description: Rufen Sie SAP-Anhänge zu Finanzbelegen aus einem PlaidCloud-Workflow-Schritt ab, um Dokumente automatisiert zu extrahieren und zu verarbeiten.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-financial-document-attachment.md
---

## Beschreibung



Hängt über einen RFC (Remote Function Call) eine Datei an einen bestimmten FI-Beleg (Financial Accounting) in SAP ECC / S/4HANA an. Nützlich, um Belege wie gescannte Rechnungen, Genehmigungs-Workflows und Vertragskopien zusammen mit den Finanzbuchungen zu hinterlegen, die sie belegen.

Erfordert die am SAP-Connector konfigurierten SAP-RFC-Zugangsdaten sowie die Nummer des Ziel-FI-Belegs (Buchungskreis, Belegnummer, Geschäftsjahr).


## Was beim Speichern geprüft wird

Der Schritt liest den Pfad jeder Datei aus einer Spalte `relative_file_path` unter den Ausgabespalten auf der Registerkarte **Tabellendatenauswahl**; diese Spalte muss vom Typ Text sein. Das Speichern wird verweigert, wenn sie fehlt — *The output columns must include relative_file_path, the path of each file to attach.* — oder wenn sie einen anderen Typ hat — *The relative_file_path column must be text, not integer.*

Wenn Sie beim Speichern eine Quelltabelle gewählt haben, aber keine Quell- oder Zielspalten, wird die leere Seite aus der Quelle befüllt, so als hätten Sie **Beide Zuordnungstabellen füllen** gewählt.


## Beispiele


### RFC-Parameter


Wählen Sie den **Zu verwendender Agent** aus. Wählen Sie in der Dropdown-Liste das **Zielverzeichnis** aus und navigieren Sie darunter zum passenden untergeordneten Ordner für die Datei. Vergeben Sie anschließend einen passenden Namen für den „Target File Name“. Geben Sie unter „Function Call Information“ die Funktion und den **Rückgabewert-Parameter** ein und wählen Sie die Parameter aus.



Im Abschnitt „Parameters“ können Sie **Zeile einfügen** oder **Zeile anhängen** wählen sowie die Parameter benennen und mit Werten versehen. Legen Sie die Anzahl für **Max. gleichzeitige Anfragen** fest und wählen Sie „Wait for RFC to Complete“. Speichern und führen Sie den Schritt aus.
