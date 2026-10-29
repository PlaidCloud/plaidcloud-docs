---
title: Trino
description: Skonfiguruj w PlaidCloud połączenie z rozproszonym silnikiem zapytań Trino, aby uruchamiać zapytania federacyjne na wielu źródłach danych.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/trino.md
---

**Trino** (dawniej PrestoSQL) to rozproszony silnik zapytań SQL, powszechnie używany na jeziorach danych. Użyj tego konektora do wykonywania zapytań do wdrożeń Trino z przepływów pracy PlaidCloud. Uwierzytelnianie korzysta z HTTP Basic Auth lub JWT; wybrany katalog i schemat określają, do którego źródła danych trafi zapytanie.

## Dokumentacja producenta
[Dokumentacja Trino](https://trino.io/docs/current/index.html).

## Konfiguracja wstępna

Ten konektor używa przepływu uwierzytelniania specyficznego dla dostawcy i jest konfigurowany bezpośrednio na ekranie **Połączenia** w Twoim obszarze roboczym. Wyświetlane pola konfiguracji zależą od danych uwierzytelniających, które administrator tenanta udostępnił na potrzeby integracji.

Najnowsze szczegóły konfiguracji znajdziesz w [dokumentacji trino](https://trino.io/docs/current/) producenta.

Jeśli potrzebujesz pomocy w skonfigurowaniu tego konektora dla swojego tenanta, skontaktuj się ze swoim zespołem opiekującym się kontem — dane uwierzytelniające specyficzne dla konektora, adresy URL środowisk i wszelkie wymagane wstępne udostępnienie zasobów zwykle trzeba uzgodnić z pomocą techniczną PlaidCloud.
