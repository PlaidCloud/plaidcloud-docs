---
title: Call SAP General Ledger Posting (Schritt)
description: Ruft einen SAP-ECC- / S/4HANA-Remote-Function-Call (RFC) auf, der eine Journalbuchung einschließlich anfallender Umsatz- und Quellensteuern bucht.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/sap/call-sap-general-ledger-posting.md
---

## Beschreibung


Ruft einen SAP-ECC- / S/4HANA-Remote-Function-Call (RFC) auf, der eine Journalbuchung einschließlich anfallender Umsatz- und Quellensteuern bucht. Der Aufruf kann auch im Testmodus laufen; dabei wird der Buchungsvorgang durchgeführt, die Buchung aber nicht abgeschlossen. So lassen sich erkennbare Fehler sammeln, etwa ein geschlossenes Konto oder ein Kunde, der im angegebenen Buchungskreis nicht existiert. Die Fehlerprüfung ist gründlich und kann mehrere erkannte Fehler in einem einzigen Test zurückgeben.


## Beispiele


### RFC-Parameter


Wählen Sie den **Zu verwendender Agent** aus. Wählen Sie in der Dropdown-Liste das **Zielverzeichnis** aus und navigieren Sie darunter zum passenden untergeordneten Ordner für die Datei. Vergeben Sie anschließend einen passenden Namen für den „Target File Name“. Geben Sie unter „Function Call Information“ die Funktion und den **Rückgabewert-Parameter** ein und wählen Sie die Parameter aus. 



Im Abschnitt „Parameters“ können Sie **Zeile einfügen** oder **Zeile anhängen** wählen sowie die Parameter benennen und mit Werten versehen. Legen Sie die Anzahl für **Max. gleichzeitige Anfragen** fest und wählen Sie „Wait for RFC to Complete“. Speichern und führen Sie den Schritt aus.


## In „Belege buchen“ konvertieren

Ein gespeicherter Schritt hat eine Schaltfläche **In Beleg-Buchung konvertieren…**. Sie zeigt zuerst, was konvertiert würde – wie viele Spalten Belegfeldern zugeordnet sind und wie viele Entitäten ihren Systemen zugeordnet sind – und verwandelt den Schritt nach Ihrer Bestätigung in einen Schritt **Belege buchen** (siehe [Belege in ERP-Systemen buchen](/de/guides/connections/post-documents/)). Die alten Einstellungen bleiben in den Versionen des Schritts.
