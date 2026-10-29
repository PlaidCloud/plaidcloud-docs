---
title: Apache Spark
description: Skonfiguruj w PlaidCloud połączenie z bazą danych Apache Spark, aby uruchamiać zapytania rozproszone i włączać big data do przepływów pracy.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/databases/spark.md
---

**Apache Spark** to rozproszony silnik obliczeniowy, powszechnie używany do ETL na dużych zbiorach danych. Użyj tego konektora do odczytu i zapisu danych przez punkty końcowe Spark SQL (zwykle Spark Thrift Server). Dla Sparka zarządzanego przez Databricks wybierz raczej konektor [Azure Databricks](../azure-databricks/).

## Dokumentacja producenta
[Dokumentacja Apache Spark](https://spark.apache.org/documentation.html).

[Projekt Apache](https://spark.apache.org/).

## Konfiguracja wstępna

Ten konektor używa przepływu uwierzytelniania specyficznego dla dostawcy i jest konfigurowany bezpośrednio na ekranie **Połączenia** w Twoim obszarze roboczym. Wyświetlane pola konfiguracji zależą od danych uwierzytelniających, które administrator tenanta udostępnił na potrzeby integracji.

Najnowsze szczegóły konfiguracji znajdziesz w [dokumentacji spark](https://spark.apache.org/docs/latest/) producenta.

Jeśli potrzebujesz pomocy w skonfigurowaniu tego konektora dla swojego tenanta, skontaktuj się ze swoim zespołem opiekującym się kontem — dane uwierzytelniające specyficzne dla konektora, adresy URL środowisk i wszelkie wymagane wstępne udostępnienie zasobów zwykle trzeba uzgodnić z pomocą techniczną PlaidCloud.
