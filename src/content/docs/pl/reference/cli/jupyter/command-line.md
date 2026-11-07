---
title: Wiersz poleceń
description: Użyj interfejsu wiersza poleceń PlaidCloud do automatyzacji zadań, uruchamiania skryptów i pracy z zasobami PlaidCloud z poziomu terminala.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/jupyter/command-line.md
---

PlaidCloud udostępnia REST API, z którego może korzystać każda aplikacja zdolna do wysyłania żądań HTTP. Aby to ułatwić, pakiet Python `plaidcloud-rpc` obsługuje za Ciebie szczegóły połączenia i żądań.

:::caution[JSON-RPC jest przestarzały]
JSON-RPC jest przestarzały i zostanie usunięty w jednym z kolejnych wydań. Używaj `plaidcloud-rpc` 1.25.0 lub nowszego, który wysyła wywołania do REST API, a nowe integracje twórz w oparciu o REST API. Zobacz [JSON-RPC jest przestarzały](#json-rpc-jest-przestarzały).
:::


## Wymagana instalacja

W terminalu uruchom następujące polecenie:

```bash
pip install "plaidcloud-rpc>=1.25.0"
```


## Wysyłanie żądania za pomocą obiektu SimpleRPC

Aby wysłać żądanie za pomocą pakietu `plaidcloud-rpc`, użyj obiektu `SimpleRPC`.

```python
from plaidcloud.rpc.connection.jsonrpc import SimpleRPC

auth_token = "Your PlaidCloud OAuth token"  # See Obtaining an OAuth Token below
endpoint_uri = "https://<your-workspace>.plaid.cloud/json-rpc/"
rpc = SimpleRPC(auth_token, endpoint_uri)
```

Po utworzeniu instancji obiektu `SimpleRPC` możesz wysyłać żądania do PlaidCloud. Ten przykład pobiera metadane tabeli.

```python
table = rpc.analyze.table.table(
            project_id=project_id,
            table_id=table_id
        )
```

`SimpleRPC` wysyła każde wywołanie do REST API pod adresem `/rest/v1/` na hoście obszaru roboczego, z tym samym tokenem. Wywołanie, którego REST API jeszcze nie obsługuje, albo wywołanie do obszaru roboczego działającego jeszcze na starszym wydaniu, korzysta zamiast tego z JSON-RPC, więc ten sam kod działa w obu przypadkach. Nieudane wywołanie w obu przypadkach zgłasza `RPCError`.


## Bezpośrednie wywoływanie REST API

`call_rest` wysyła żądanie do dowolnego punktu końcowego REST API z tym samym tokenem, tymi samymi ustawieniami TLS i tymi samymi ponowieniami co `SimpleRPC`. Podaj metodę HTTP, ścieżkę pod `/rest/v1/` oraz opcjonalnie `params` dla ciągu zapytania i `body` dla treści żądania JSON.

```python
dimensions = rpc.call_rest(
    'GET',
    'analyze/dimension/dimensions',
    params={'project_id': project_id},
)
```

Zwraca zdekodowaną odpowiedź JSON albo `None`, gdy odpowiedź nie ma treści. Każda odpowiedź inna niż pomyślna zgłasza `RPCError` ze statusem HTTP jako `code`.


## JSON-RPC jest przestarzały

JSON-RPC jest przestarzały i zostanie usunięty w jednym z kolejnych wydań. Wersje `plaidcloud-rpc` starsze niż 1.25.0 wysyłają każde wywołanie przez JSON-RPC, więc przestaną działać po jego usunięciu. Zaktualizuj do wersji 1.25.0 lub nowszej; Twój kod `SimpleRPC` nie wymaga zmian. Nowe integracje twórz w oparciu o REST API.


## Jakie interfejsy API są dostępne?

Dostępnych jest wiele interfejsów API, które sterują niemal każdym aspektem PlaidCloud. Interaktywna dokumentacja referencyjna API jest udostępniana osobno dla każdej dzierżawy wewnątrz każdego obszaru roboczego PlaidCloud — otwórz swój obszar roboczy i przejdź do menu dokumentacji API, aby zobaczyć aktualny katalog punktów końcowych.


## Uzyskiwanie tokenu OAuth

Więcej informacji o uzyskiwaniu tokenu OAuth i konfigurowaniu systemu do zautomatyzowanego uwierzytelniania znajdziesz w sekcji [Konfiguracja OAuth](/pl/reference/cli/jupyter/oauth-setup/).
