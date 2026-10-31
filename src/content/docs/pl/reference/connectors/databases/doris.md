---
title: Apache Doris
description: Skonfiguruj połączenie z bazą danych Apache Doris w PlaidCloud, aby uruchamiać analityczne zapytania w czasie rzeczywistym na dużych zbiorach danych.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/doris.md
---

**Apache Doris** to wydajna analityczna baza danych MPP, z której wyodrębniono StarRocks. Użyj tego konektora, aby wykonywać zapytania do wdrożeń Doris z przepływów pracy PlaidCloud. Połączenie korzysta z protokołu sieciowego MySQL ze standardowym uwierzytelnianiem nazwą użytkownika i hasłem.

## Dokumentacja producenta
[Dokumentacja Apache Doris](https://doris.apache.org/docs/4.x/gettingStarted/what-is-apache-doris).

[Strona główna projektu Apache Doris](https://doris.apache.org/).

## Konfiguracja

Ten konektor korzysta z przepływu uwierzytelniania specyficznego dla dostawcy i jest konfigurowany bezpośrednio na ekranie **Połączenia** w Twoim obszarze roboczym. Wyświetlane pola konfiguracji zależą od poświadczeń udostępnionych na potrzeby integracji przez administratora Twojego tenanta.

Najnowsze szczegóły konfiguracji znajdziesz w oficjalnej [dokumentacji doris](https://doris.apache.org/docs/).

Jeśli potrzebujesz pomocy w skonfigurowaniu tego konektora dla swojego tenanta, skontaktuj się ze swoim zespołem obsługi konta — poświadczenia specyficzne dla konektora, adresy URL środowisk i wszelkie wymagane wstępne przygotowanie zwykle trzeba uzgodnić z pomocą techniczną PlaidCloud.
