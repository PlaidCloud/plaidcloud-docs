---
title: Apache Spark
description: Richten Sie in PlaidCloud eine Apache-Spark-Datenbankverbindung ein, um verteilte Abfragen auszuführen und Big Data in Workflows einzubinden.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/spark.md
---

**Apache Spark** ist die verteilte Compute-Engine, die häufig für ETL über große Datensätze eingesetzt wird. Mit diesem Connector lesen und schreiben Sie Daten über Spark-SQL-Endpunkte (typischerweise den Spark Thrift Server). Verwenden Sie für von Databricks verwaltetes Spark vorzugsweise den Connector [Azure Databricks](../azure-databricks/).

## Dokumentation des Herstellers
[Die Apache-Spark-Dokumentation](https://spark.apache.org/documentation.html).

Das [Apache-Projekt](https://spark.apache.org/).

## Einrichtung

Dieser Connector verwendet einen herstellerspezifischen Authentifizierungsablauf und wird direkt auf dem Bildschirm **Verbindungen** in Ihrem Workspace konfiguriert. Welche Konfigurationsfelder angezeigt werden, hängt von den Anmeldedaten ab, die Ihr Tenant-Administrator für die Integration bereitgestellt hat.

Die aktuellen Einrichtungsdetails finden Sie in der [Spark-Dokumentation](https://spark.apache.org/docs/latest/) des Herstellers.

Wenn Sie Unterstützung bei der Einrichtung dieses Connectors für Ihren Tenant benötigen, wenden Sie sich an Ihr Account-Team. Connectorspezifische Anmeldedaten, Umgebungs-URLs und eine eventuell erforderliche Vorabbereitstellung müssen in der Regel mit dem PlaidCloud-Support abgestimmt werden.
