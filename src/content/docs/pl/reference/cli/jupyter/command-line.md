---
title: Wiersz poleceń
description: Użyj interfejsu wiersza poleceń PlaidCloud do automatyzacji zadań, uruchamiania skryptów i pracy z zasobami PlaidCloud z poziomu terminala.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/command-line.md
---

PlaidCloud używa standardowych żądań JSON-RPC i można go stosować z dowolną aplikacją, która potrafi wysyłać takie żądania.


Aby ułatwić pracę, dostępny jest pakiet Pythona, który upraszcza nawiązywanie połączenia i wywoływanie API.


## Wymagana instalacja

W terminalu uruchom następujące polecenie:

```bash
pip install plaidcloud-rpc
```


## Użycie obiektu Simplerpc do wysłania żądania

Aby wysłać żądanie za pomocą pakietu `plaidcloud-rpc`, użyj obiektu `SimpleRPC`.

```python
from plaidcloud.rpc.connection.jsonrpc import SimpleRPC  
  
auth_token = "Your PlaidCloud Auth Token" # See Obtaining Token below  
endpoint_uri = "plaidcloud.com" # or plaidcloud.net  
rpc = SimpleRPC(auth_token, endpoint_uri)
```

Po utworzeniu obiektu `SimpleRPC` możesz wysyłać żądania RPC do PlaidCloud. Ten przykład żąda metadanych tabeli.

```python
table = rpc.analyze.table.table(  
            project_id=project_id,  
            table_id=table_id  
        )
```

## Jakie interfejsy API są dostępne?

Dostępnych jest wiele interfejsów API, które sterują niemal każdym aspektem PlaidCloud. Interaktywna dokumentacja referencyjna API jest udostępniana osobno dla każdej dzierżawy wewnątrz każdego obszaru roboczego PlaidCloud — otwórz swój obszar roboczy i przejdź do menu dokumentacji API, aby zobaczyć aktualny katalog punktów końcowych.


## Uzyskiwanie tokenu OAuth

Więcej informacji o uzyskiwaniu tokenu OAuth i konfigurowaniu systemu do zautomatyzowanego uwierzytelniania znajdziesz w sekcji [Konfiguracja OAuth](/pl/reference/cli/jupyter/oauth-setup/).
