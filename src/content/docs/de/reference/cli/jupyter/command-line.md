---
title: Befehlszeile
description: Verwenden Sie die PlaidCloud-Befehlszeilenschnittstelle, um Aufgaben zu automatisieren, Skripte auszuführen und über das Terminal mit PlaidCloud-Ressourcen zu arbeiten.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/command-line.md
---

PlaidCloud verwendet standardmäßige JSON-RPC-Anfragen und lässt sich mit jeder Anwendung nutzen, die solche Anfragen senden kann.


Zur Vereinfachung steht ein Python-Paket bereit, das den Verbindungsaufbau und die Ausführung von API-Aufrufen erleichtert.


## Erforderliche Installation

Führen Sie in einem Terminal den folgenden Befehl aus:

```bash
pip install plaidcloud-rpc
```


## Eine Anfrage mit dem Simplerpc-Objekt senden

Um mit dem Paket `plaidcloud-rpc` eine Anfrage zu senden, verwenden Sie das Objekt `SimpleRPC`.

```python
from plaidcloud.rpc.connection.jsonrpc import SimpleRPC  
  
auth_token = "Your PlaidCloud Auth Token" # See Obtaining Token below  
endpoint_uri = "plaidcloud.com" # or plaidcloud.net  
rpc = SimpleRPC(auth_token, endpoint_uri)
```

Sobald das Objekt `SimpleRPC` instanziiert ist, können Sie RPC-Anfragen an PlaidCloud senden. Dieses Beispiel fragt die Metadaten einer Tabelle ab.

```python
table = rpc.analyze.table.table(  
            project_id=project_id,  
            table_id=table_id  
        )
```

## Welche APIs stehen zur Verfügung?

Es stehen viele APIs zur Verfügung, die nahezu jeden Aspekt von PlaidCloud steuern. Die interaktive API-Referenz wird pro Mandant in jedem PlaidCloud-Workspace bereitgestellt. Öffnen Sie Ihren Workspace und rufen Sie das Menü der API-Dokumentation auf, um den aktuellen Endpunktkatalog einzusehen.


## OAuth-Token abrufen

Weitere Informationen zum Abrufen eines OAuth-Tokens und zur Konfiguration des Systems für die automatisierte Authentifizierung finden Sie unter [OAuth-Einrichtung](/de/reference/cli/jupyter/oauth-setup/).
