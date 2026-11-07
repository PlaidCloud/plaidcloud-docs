---
title: Befehlszeile
description: Verwenden Sie die PlaidCloud-Befehlszeilenschnittstelle, um Aufgaben zu automatisieren, Skripte auszuführen und über das Terminal mit PlaidCloud-Ressourcen zu arbeiten.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/command-line.md
---

PlaidCloud bietet eine REST-API, die jede Anwendung verwenden kann, die HTTP-Anfragen senden kann. Zur Vereinfachung übernimmt das Python-Paket `plaidcloud-rpc` die Verbindungs- und Anfragedetails für Sie.

:::caution[JSON-RPC ist veraltet]
JSON-RPC ist veraltet und wird in einem späteren Release entfernt. Verwenden Sie `plaidcloud-rpc` 1.25.0 oder höher, das Ihre Aufrufe an die REST-API sendet, und schreiben Sie neue Integrationen gegen die REST-API. Siehe [JSON-RPC ist veraltet](#json-rpc-ist-veraltet).
:::


## Erforderliche Installation

Führen Sie in einem Terminal den folgenden Befehl aus:

```bash
pip install "plaidcloud-rpc>=1.25.0"
```


## Anfragen mit dem SimpleRPC-Objekt senden

Um mit dem Paket `plaidcloud-rpc` eine Anfrage zu senden, verwenden Sie das Objekt `SimpleRPC`.

```python
from plaidcloud.rpc.connection.jsonrpc import SimpleRPC

auth_token = "Your PlaidCloud OAuth token"  # See Obtaining an OAuth Token below
endpoint_uri = "https://<your-workspace>.plaid.cloud/json-rpc/"
rpc = SimpleRPC(auth_token, endpoint_uri)
```

Sobald Sie das `SimpleRPC`-Objekt instanziiert haben, können Sie Anfragen an PlaidCloud senden. Dieses Beispiel fragt die Metadaten einer Tabelle ab.

```python
table = rpc.analyze.table.table(
            project_id=project_id,
            table_id=table_id
        )
```

`SimpleRPC` sendet jeden Aufruf mit demselben Token an die REST-API unter `/rest/v1/` auf dem Host Ihres Workspace. Ein Aufruf, den die REST-API noch nicht abdeckt, oder ein Aufruf an einen Workspace, der noch auf einem älteren Release läuft, verwendet stattdessen JSON-RPC, sodass derselbe Code in beiden Fällen funktioniert. Ein fehlgeschlagener Aufruf löst in beiden Fällen `RPCError` aus.


## Die REST-API direkt aufrufen

`call_rest` sendet eine Anfrage an einen beliebigen Endpunkt der REST-API, mit demselben Token, denselben TLS-Einstellungen und denselben Wiederholungsversuchen wie `SimpleRPC`. Übergeben Sie die HTTP-Methode, den Pfad unter `/rest/v1/` und optional `params` für die Abfragezeichenfolge und `body` für einen JSON-Anfragetext.

```python
dimensions = rpc.call_rest(
    'GET',
    'analyze/dimension/dimensions',
    params={'project_id': project_id},
)
```

Die Methode gibt die decodierte JSON-Antwort zurück oder `None`, wenn die Antwort keinen Inhalt hat. Jede Antwort, die keinen Erfolg meldet, löst `RPCError` aus, mit dem HTTP-Status als `code`.


## JSON-RPC ist veraltet

JSON-RPC ist veraltet und wird in einem späteren Release entfernt. Versionen von `plaidcloud-rpc` vor 1.25.0 senden jeden Aufruf über JSON-RPC und funktionieren daher nicht mehr, sobald es entfernt ist. Aktualisieren Sie auf 1.25.0 oder höher; Ihr `SimpleRPC`-Code muss nicht geändert werden. Schreiben Sie neue Integrationen gegen die REST-API.


## Welche APIs stehen zur Verfügung?

Es stehen viele APIs zur Verfügung, die nahezu jeden Aspekt von PlaidCloud steuern. Die interaktive API-Referenz wird pro Mandant in jedem PlaidCloud-Workspace bereitgestellt. Öffnen Sie Ihren Workspace und rufen Sie das Menü der API-Dokumentation auf, um den aktuellen Endpunktkatalog einzusehen.


## OAuth-Token abrufen

Weitere Informationen zum Abrufen eines OAuth-Tokens und zur Konfiguration des Systems für die automatisierte Authentifizierung finden Sie unter [OAuth-Einrichtung](/de/reference/cli/jupyter/oauth-setup/).
