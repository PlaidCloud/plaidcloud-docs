---
title: MuleSoft-REST-Konnektor
description: Verbinden Sie PlaidCloud mit einem MuleSoft-Anypoint-Gateway und hängen Sie die API-Definition an, damit Workflow-Schritte ihre Endpunkte auflisten können.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/mulesoft.md
---

MuleSoft Anypoint ist ein API-Gateway: Es steht vor allen Diensten, die Ihre Organisation dahinter veröffentlicht hat, unter einer für Ihr Deployment spezifischen Adresse. Anders als ein Konnektor für einen einzelnen Dienst kennt eine MuleSoft-Verbindung daher ihre eigenen Endpunkte nicht – Sie geben an, wo die API und ihre Definition liegen.

## API-Dokumentation

Die API-Dokumentation für diese Verbindung ist die Dokumentation der Dienste, die Ihr Gateway bereitstellt.

## Konfiguration

MuleSoft verwendet dasselbe Formular wie die [generische REST-Verbindung](/de/reference/connectors/rest/generic-rest/) – dieselben vier Registerkarten, dieselben Felder, dasselbe Verhalten. Zwei Felder sind hier besonders wichtig:

- **Host oder IP-Adresse** – die Adresse Ihres Anypoint-Gateways. Es gibt keinen Standardwert, da eine MuleSoft-Adresse spezifisch für Ihr Deployment ist.
- **Authentifizierungstyp** – je nachdem, was Ihr Gateway erwartet: `None`, `Basic`, `API Key`, `Bearer Token` oder `OAuth 2.0`. Es wird nichts vorausgesetzt.

## Endpunkte in einem Workflow auflisten

Da das Gateway keine integrierte Endpunktliste hat, hängen Sie die OpenAPI-3.x- oder Swagger-2.0-Definition Ihrer API unter **API-Definition** an die Verbindung an – entweder die Adresse, unter der sie veröffentlicht ist, oder eine in Document gespeicherte `.json`- oder `.yaml`-Datei. Die Felder finden Sie unter [API-Definition](/de/reference/connectors/rest/generic-rest/#api-definition).

Ein [Schritt REST-Anfrage](/de/guides/workflows/rest-request-step/), der diese Verbindung verwendet, kann dann **Endpunktquelle** auf **Aus der API-Definition der Verbindung** setzen und **Katalog laden** wählen, um Endpunkte der API auszuwählen, statt jeden Pfad von Hand einzugeben.

## Verwandte Themen

- [Generische REST-Verbindung](/de/reference/connectors/rest/generic-rest/) – die vollständige Feldreferenz für dieses Formular.
- [Verbindung erstellen und verwalten](/de/guides/connections/create-connection/)
- [Workflow-Schritt REST-Anfrage](/de/guides/workflows/rest-request-step/)
