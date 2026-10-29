---
title: StarRocks
description: Skonfiguruj w PlaidCloud połączenie z bazą danych StarRocks, aby uruchamiać wydajne zapytania analityczne na dużych zbiorach danych.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/starrocks.md
---

**StarRocks** to wydajna analityczna baza danych, na której działa PlaidCloud Lakehouse v2 (zgodny ze StarRocks 4.1). Użyj tego konektora do zapytań do samodzielnych wdrożeń StarRocks — dla lakehouse wbudowanego w produkt ten konektor nie jest potrzebny.

## Dokumentacja producenta
[Dokumentacja StarRocks](https://docs.starrocks.io/docs/introduction/StarRocks_intro/).

## Konfiguracja wstępna

Ten konektor używa przepływu uwierzytelniania specyficznego dla dostawcy i jest konfigurowany bezpośrednio na ekranie **Połączenia** w Twoim obszarze roboczym. Wyświetlane pola konfiguracji zależą od danych uwierzytelniających, które administrator tenanta udostępnił na potrzeby integracji.

Najnowsze szczegóły konfiguracji znajdziesz w [dokumentacji starrocks](https://docs.starrocks.io/) producenta.

Jeśli potrzebujesz pomocy w skonfigurowaniu tego konektora dla swojego tenanta, skontaktuj się ze swoim zespołem opiekującym się kontem — dane uwierzytelniające specyficzne dla konektora, adresy URL środowisk i wszelkie wymagane wstępne udostępnienie zasobów zwykle trzeba uzgodnić z pomocą techniczną PlaidCloud.
