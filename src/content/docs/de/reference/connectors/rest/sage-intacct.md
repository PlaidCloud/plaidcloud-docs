---
title: Sage-Intacct-REST-Konnektor
description: Richten Sie in PlaidCloud eine Sage-Intacct-REST-API-Verbindung ein, um Finanz- und Buchhaltungsdaten in Ihre Workflows zu integrieren.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/sage-intacct.md
---

## API-Dokumentation

Die Dokumentation der Sage-Intacct-REST-API finden Sie auf der [Sage-Entwicklerseite](https://developer.sage.com/intacct/docs/1/sage-intacct-rest-api/get-started/quick-start).


## Sicherheitsanforderungen

PlaidCloud stellt in der Familie der REST-Verbindungen eine dedizierte **Intacct**-Verbindung bereit (aufgeführt als **REST – Intacct**). Sie authentifiziert sich mit OAuth2 Client Credentials an der Intacct-REST-API: Das Paar aus Sender-ID und Sender-Passwort von Sage Intacct **Web Services** wird als **Client-ID** und **Client-Secret** der Verbindung eingegeben, dazu ein Benutzername des Webservice-Benutzers und eine Unternehmens-ID. Die Sender-Zugangsdaten müssen vom Sage-Support für Ihr Unternehmen aktiviert werden; der Webservice-Benutzer muss Berechtigungen für jedes Intacct-Objekt haben, das der Konnektor liest.

Behandeln Sie Client-ID und Client-Secret als Geheimnisse – speichern Sie sie nur über den Bereich **Credentials** in PlaidCloud und verweisen Sie von der Verbindung darauf.


## Zugangsdaten beschaffen

1. Öffnen Sie den Bereich **Company Setup** in Sage Intacct
2. Aktivieren Sie Web Services für die von Sage bereitgestellte Sender-ID
3. Erstellen oder wählen Sie einen Webservice-Benutzer für PlaidCloud
4. Erteilen Sie dem Benutzer Berechtigungen für jedes Objekt, das Sie abfragen möchten
5. Notieren Sie Unternehmens-ID, Benutzername des Webservice-Benutzers, Sender-ID und Sender-Passwort


## Sage-Intacct-Konnektor erstellen

1. Gehen Sie zu **Tools > Connections** und klicken Sie auf `Add Connection`
2. Wählen Sie unter **REST** den Eintrag **Intacct** (aufgeführt als **REST – Intacct**)
3. Geben Sie ein:
    * **Verbindungsname** – Anzeigename in Workflow-Schritten
    * **Client-ID** – Ihre Intacct-Sender-ID
    * **Client-Secret** – Ihr Intacct-Sender-Passwort
    * **Benutzername des Webservice-Benutzers** – der Login des Webservice-Benutzers
    * **Unternehmens-ID** – das Intacct-Unternehmen, mit dem Sie sich verbinden
4. Klicken Sie auf `Test`, um die Zugangsdaten zu prüfen
5. Klicken Sie auf `Save`


## In Workflow-Schritten verwenden

Dieselbe Verbindung dient sowohl zum Lesen aus Intacct als auch zum Buchen dorthin. Sie ist auswählbar in:

* [Import Sage AP](../../../workflow-steps/sage-intacct/import-sage-ap/) – Kopfdaten von Kreditorenrechnungen
* [Import Sage AP Lines](../../../workflow-steps/sage-intacct/import-sage-ap-lines/) – Positionsdetails von Kreditorenrechnungen
* [Import Sage Intacct Query](../../../workflow-steps/sage-intacct/import-intacct-query/) – generische Abfrage auf jedes Intacct-Objekt
* [Import Intacct Entity](../../../workflow-steps/sage-intacct/import-intacct-entity/) – Hauptbuchdetails, Salden, Buchungen und Dimensionsstammdaten, mit automatischer Paginierung
* [Intacct: Journalbuchung buchen](../../../workflow-steps/sage-intacct/export-to-sage/) – Journalbuchungen buchen
