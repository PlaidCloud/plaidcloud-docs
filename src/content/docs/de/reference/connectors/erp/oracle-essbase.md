---
title: Oracle-Essbase-Connector
description: Verbinden Sie PlaidCloud mit einem Servicekonto mit Oracle Essbase 21c oder Oracle Analytics Cloud, um aus einem Workflow Live-MDX-Abfragen gegen Essbase-Cubes auszuführen.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/oracle-essbase.md
---

## API-Dokumentation

Dieser Connector spricht die [REST-API von Oracle Essbase](https://docs.oracle.com/en/database/other-databases/essbase/) an, also dieselben Endpunkte für `grid/mdx`, Anwendungen, Datenbanken und Outlines, die Oracle für Essbase 21c und Oracle Analytics Cloud (OAC) dokumentiert.

## Womit er sich verbindet

Oracle Essbase **21c oder höher** und Essbase in Oracle Analytics Cloud (OAC). Diese Versionen stellen Essbase über eine dokumentierte REST-API bereit, die PlaidCloud aufruft. Lokale Essbase-Versionen vor der REST-API werden **nicht unterstützt**; es gibt keinen Pfad über die alte Java-API oder den Grid-Client.

Sobald die Verbindung besteht, führt der Schritt [Essbase: Cube abfragen](/de/reference/workflow-steps/essbase/essbase-query/) Live-MDX gegen einen Cube aus und legt das Ergebnisraster in einer Tabelle ab; der Schritt [Essbase: Dimension lesen](/de/reference/workflow-steps/essbase/essbase-dimension-read/) lädt eine Dimensions-Outline in eine PlaidCloud-Dimension.

## So funktioniert die Authentifizierung

Die Verbindung authentifiziert sich mit Benutzername und Passwort eines Servicekontos über HTTP Basic. Die Essbase-Bereitstellung dieses Kontos steuert, welche Anwendungen und Cubes es sehen und abfragen kann; gewähren Sie ihm daher Lesezugriff genau auf die Anwendungen, die Sie abfragen möchten, und auf nichts darüber hinaus.

## Konfiguration

| Feld | Typ | Beschreibung |
|---|---|---|
| Name | Text | Anzeigename dieser Verbindung. |
| Basis-URL | Text | Der Ursprung des Essbase-Servers, zum Beispiel `https://your-host:9001`. Geben Sie nur den Ursprung an, ohne nachgestellten Pfad `/essbase/...`. |
| Standardanwendung | Text *(optional)* | Wählt diese Anwendung im Formular des Schritts Essbase: Cube abfragen vor. |
| Username | Text | Servicekonto-Benutzer für die HTTP-Basic-Authentifizierung. |
| Password | Text | Passwort des Servicekontos. Wird verschlüsselt gespeichert. |
| Verify SSL | Schalter | Standardmäßig aktiviert. Deaktivieren Sie die Option nur für einen Host mit selbstsigniertem oder anderweitig nicht überprüfbarem Zertifikat. |

## Verbindung testen

Verwenden Sie **Verbindung testen** im Verbindungseditor. Ein erfolgreicher Test erreicht den Essbase-Server, listet die Anwendungen auf, die das Servicekonto sehen kann, und meldet, wie viele er gefunden hat. So bestätigen Sie sowohl die Basis-URL als auch die Anmeldedaten, bevor Sie eine Abfrage erstellen.

## Verwandte Themen

- [Essbase: Cube abfragen](/de/reference/workflow-steps/essbase/essbase-query/) (Schritt) — führt eine Live-MDX-Abfrage gegen einen Cube aus und legt das Ergebnis in einer Tabelle ab.
- [Essbase: Dimension lesen](/de/reference/workflow-steps/essbase/essbase-dimension-read/) (Schritt) — lädt eine Dimensions-Outline in eine PlaidCloud-Dimension.
- [Oracle-Essbase-Schritte](/de/reference/workflow-steps/essbase/)
- [Verbindung zu Oracle Essbase herstellen (Anleitung)](/de/guides/connections/essbase/)
- [Verbindung erstellen und verwalten](/de/guides/connections/create-connection/)
