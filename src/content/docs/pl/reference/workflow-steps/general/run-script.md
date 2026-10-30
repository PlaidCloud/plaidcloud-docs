---
title: Uruchom operację aplikacji
description: Wywołaj zarejestrowaną operację aplikacji z przepływu pracy, opcjonalnie przekazując ścieżkę dokumentu i parametry.
sidebar:
  order: 10
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/run-script.md
---

## Opis

Wywołuje zarejestrowaną operację aplikacji z poziomu przepływu pracy. Używaj go do uruchamiania prac platformy, które nie są transformacją danych — operacji udostępnianych przez aplikację do automatyzacji.

## Konfiguracja

### Operacja aplikacji do wykonania

Operacja do wywołania.

### Ścieżka pliku

Dla operacji przyjmujących plik:

- **Katalog dokumentów** — konto dokumentów i ścieżka do przekazania.
- **Nazwa parametru pliku** — parametr, pod którym operacja oczekuje ścieżki. Domyślnie `document_path`; zmień tylko wtedy, gdy operacja nazywa go inaczej.

### Parametry opcjonalne

Pary nazwa/wartość przekazywane do operacji obok ścieżki pliku.

## Powiązane

- [Kroki ogólne](/pl/reference/workflow-steps/general/)
- [User Defined Transform](/pl/reference/workflow-steps/general/user-defined-transform/)
- [Run Remote Python](/pl/reference/workflow-steps/general/run-remote-python/)
