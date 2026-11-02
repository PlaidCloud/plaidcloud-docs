---
title: Call SAP Financial Document Attachment (Schritt)
description: Rufen Sie Anhänge von SAP-Finanzbelegen aus einem PlaidCloud-Workflow-Schritt ab, für die automatisierte Dokumentenextraktion und -verarbeitung.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-financial-document-attachment.md
---

## Beschreibung



Hängt über einen RFC (Remote Function Call) eine Datei an einen bestimmten FI-Beleg (Financial Accounting) in SAP ECC / S/4HANA an. Nützlich, um belegende Unterlagen — gescannte Rechnungen, Genehmigungsabläufe, Vertragskopien — zusammen mit den Finanzbuchungen zu erfassen, die sie stützen.

Erfordert die im SAP-Konnektor konfigurierten SAP-RFC-Anmeldedaten und die Nummer des Ziel-FI-Belegs (Buchungskreis, Belegnummer, Geschäftsjahr).


## Was beim Speichern geprüft wird

Der Schritt liest den Pfad jeder Datei aus einer Spalte `relative_file_path` unter den Ausgabespalten auf seiner Registerkarte **Spalten**, und diese Spalte muss Text sein. Das Speichern wird ohne eine solche Spalte abgelehnt — *Die Ausgabespalten müssen relative_file_path enthalten, den Pfad jeder anzuhängenden Datei.* — oder wenn sie einen anderen Typ hat — *Die Spalte relative_file_path muss Text sein, nicht integer.*

Beim Speichern mit gewählter Quelltabelle, aber ohne Quell- oder Zielspalten wird die leere Seite aus der Quelle gefüllt, so wie es **Beide Zuordnungstabellen füllen** täte.


## Beispiele


### RFC-Parameter


Wählen Sie „Zu verwendender Agent“. Wählen Sie „Zielverzeichnis“ in der Dropdown-Leiste und navigieren Sie darunter zum richtigen untergeordneten Ordner als Ziel für die Datei. Geben Sie als Nächstes den „Target File Name“ passend an. Geben Sie unter „Function Call Information“ die Funktion und den „Rückgabewert-Parameter“ ein und wählen Sie die Parameter aus.



Im Abschnitt „Parameter“ können Sie „Zeile einfügen“ oder „Zeile anhängen“ wählen sowie die Parameter benennen und ihnen Werte geben. Wählen Sie die Zahl für „Max. gleichzeitige Anfragen“ und wählen Sie „Wait for RFC to Complete“. Wählen Sie „Speichern und ausführen“.
