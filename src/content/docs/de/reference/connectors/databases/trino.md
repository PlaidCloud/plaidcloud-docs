---
title: Trino
description: Richten Sie in PlaidCloud eine Verbindung zur verteilten Abfrage-Engine Trino ein, um föderierte Abfragen über mehrere Datenquellen auszuführen.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/trino.md
---

**Trino** (früher PrestoSQL) ist die verteilte SQL-Abfrage-Engine, die häufig über Data Lakes eingesetzt wird. Mit diesem Connector fragen Sie Trino-Bereitstellungen aus PlaidCloud-Workflows ab. Die Authentifizierung erfolgt über HTTP Basic Auth oder JWT; der Katalog und das Schema, auf die Sie zielen, bestimmen, welche zugrunde liegende Datenquelle die Abfrage trifft.

## Dokumentation des Herstellers
[Die Trino-Dokumentation](https://trino.io/docs/current/index.html).

## Einrichtung

Dieser Connector verwendet einen herstellerspezifischen Authentifizierungsablauf und wird direkt auf dem Bildschirm **Verbindungen** in Ihrem Workspace konfiguriert. Welche Konfigurationsfelder angezeigt werden, hängt von den Anmeldedaten ab, die Ihr Tenant-Administrator für die Integration bereitgestellt hat.

Die aktuellen Einrichtungsdetails finden Sie in der [Trino-Dokumentation](https://trino.io/docs/current/) des Herstellers.

Wenn Sie Unterstützung bei der Einrichtung dieses Connectors für Ihren Tenant benötigen, wenden Sie sich an Ihr Account-Team. Connectorspezifische Anmeldedaten, Umgebungs-URLs und eine eventuell erforderliche Vorabbereitstellung müssen in der Regel mit dem PlaidCloud-Support abgestimmt werden.
