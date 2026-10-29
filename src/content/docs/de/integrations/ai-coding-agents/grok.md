---
title: Grok
description: Verbinden Sie Grok von xAI über die Custom Connectors mit dem MCP-Server von PlaidCloud.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/grok.md
---

[Grok](https://grok.com) unterstützt MCP-Server über Custom Connectors, die auf grok.com konfiguriert werden.

## Einrichtung

1. Rufen Sie [grok.com/connectors](https://grok.com/connectors) auf und klicken Sie auf **New Connector → Custom**.
2. Fügen Sie die MCP-Server-URL ein: `https://<your-workspace>.plaid.cloud/mcp`.
3. Schließen Sie die Anmeldung ab, wenn Grok Sie zu PlaidCloud weiterleitet. Es erscheint eine Seite **Application Access Request**, die die anfragende Anwendung und den Redirect-URI nennt, an den die Zugangsdaten gesendet werden – prüfen Sie vor der Bestätigung, dass beide zu Grok passen.

## Unternehmenspläne

Bei Business- und Enterprise-Workspaces läuft die Einrichtung von Connectors über einen Team-Administrator: Ein Workspace-Administrator stellt den Connector auf grok.com/connectors bereit, danach verbinden Mitglieder ihr eigenes Konto damit.

## Zugriff erneuern

Meldet Grok, dass die Verbindung neu autorisiert werden muss, wiederholen Sie den Anmeldeschritt – der Connector behält seine URL, Sie müssen ihn also nicht von Grund auf neu hinzufügen.
