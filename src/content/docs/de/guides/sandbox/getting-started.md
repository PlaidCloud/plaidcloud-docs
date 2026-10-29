---
title: Erste Schritte mit der Custom-App-Sandbox
description: Beginnen Sie mit der Entwicklung und Bereitstellung benutzerdefinierter Anwendungen in der PlaidCloud-Sandbox-Umgebung, mit Einrichtungs- und Konfigurationsschritten.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/sandbox/getting-started.md
---

## Was ist die Sandbox
Die PlaidCloud-Sandbox ermöglicht die Bereitstellung Ihrer eigenen benutzerdefinierten Apps mit nativem lokalem Zugriff auf Daten und PlaidCloud-Operationen.  Die Sandbox-Umgebung bietet eine vollständige Rechenumgebung zum Erstellen benutzerdefinierter Anwendungen, die Ihre Nutzung von PlaidCloud erweitern.

Alle benutzerdefinierten Apps laufen über Kubernetes-Bereitstellungsprozesse, daher sind Grundkenntnisse über Kubernetes-Objekte erforderlich.  Ein [Hello-World-Beispiel](https://github.com/PlaidCloud/custom-app-template) zeigt Ihnen, wie Sie eine einfache Anwendung bereitstellen.

## Verfügbare Ressourcen
Für Sandbox-Apps gilt ein weiches Ressourcenlimit in der Erwartung, dass die Ressourcennutzung nicht missbraucht wird.  Wir können bei Bedarf große Mengen an Rechenleistung bereitstellen, sprechen Sie uns aber vor einer Bereitstellung darauf an.  Kontaktieren Sie uns, wenn Sie erhebliche Ressourcen benötigen.

Die in der Sandbox laufenden Anwendungen haben direkten Zugriff auf das Lakehouse und auf beliebig viele Postgres-Datenbanken.  Postgres-Datenbanken sind für mittelgroße Datenmengen ausgelegt und eignen sich daher bestens zum Speichern von Konfigurationen und anderen Metadaten.  Verwenden Sie für die primäre Datenspeicherung das Lakehouse, da es große Datenmengen speichern kann und dabei leistungsfähig bleibt.

Alle PlaidCloud-APIs sind außerdem direkt aus der Sandbox verfügbar, ohne eine öffentliche URL zu verwenden, was die Datenübertragungsgeschwindigkeit verbessert.

## Image-Anforderungen

Jedes Image, das eine Docker-basierte Kubernetes-Bereitstellung unterstützt, eignet sich für eine benutzerdefinierte App.  Derzeit werden nur *nix-basierte Images unterstützt.  Wenn Sie ein Windows-basiertes Image ausführen müssen, kontaktieren Sie uns bitte.

## In Ihre CI/CD-Pipeline integrieren

Die Kubernetes-Bereitstellung der Sandbox-App nutzt GitOps-Prozesse.  So können Sie Ihren eigenen CI/CD-Prozess für Image-Builds und Bereitstellungen umsetzen.  Das Git-Repository Ihrer benutzerdefinierten App wird ständig auf Änderungen überwacht, sodass Ihre Sandbox aktualisiert wird, sobald Änderungen vorgenommen werden.
