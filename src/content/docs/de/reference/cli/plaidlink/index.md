---
title: PlaidLink
description: Installieren und konfigurieren Sie PlaidLink-Agents für den sicheren Zugriff auf Systeme hinter Firewalls und ermöglichen Sie Remote-Abfragen und Dateiübertragungen.
sidebar:
  label: PlaidLink
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidlink/index.md
---

PlaidLink bietet indirekten Zugriff auf Kundensysteme und -prozesse, die durch Firewalls oder andere Einschränkungen geschützt sind und direkte Verbindungen aus PlaidCloud heraus erschweren. Mit einem PlaidCloud-Agent, der im isolierten Bereich installiert ist, kann PlaidCloud den Agent beauftragen, Aktionen auszuführen, etwa Abfragen auszuführen, Dateien herunter- oder hochzuladen, Sensorbedingungen zu prüfen, mit SAP zu interagieren und vieles mehr.

Da der Agent den Kontakt zu PlaidCloud selbst aufbaut und über standardmäßige HTTPS-Netzwerkprotokolle kommuniziert, lässt er sich in der Regel mit minimalem Einrichtungsaufwand betreiben. Zusätzlich kann der Agent als nicht privilegierter Benutzer ausgeführt werden, um die Zugriffsrechte in einer eingeschränkten Umgebung zu steuern.

## Themen

- [Installieren](/de/reference/cli/plaidlink/install/) — PlaidLink unter Windows, Linux, macOS oder in einem Container zum Laufen bringen
- [Konfigurieren](/de/reference/cli/plaidlink/configure/) — Verbindungseinstellungen, Anmeldedaten und Laufzeitoptionen
- [Agents](/de/reference/cli/plaidlink/agents/) — mehrere Agents und ihre Fähigkeiten verwalten
- [Upgrade](/de/reference/cli/plaidlink/upgrade/) — auf einen neueren PlaidLink-Build wechseln
