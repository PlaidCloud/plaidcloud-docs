---
title: PlaidLink
description: Zainstaluj i skonfiguruj agentów PlaidLink, aby bezpiecznie uzyskiwać dostęp do systemów za zaporami sieciowymi oraz umożliwić zdalne zapytania i transfer plików.
sidebar:
  label: PlaidLink
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidlink/index.md
---

PlaidLink zapewnia pośredni dostęp do systemów i procesów klienta, które są chronione zaporami sieciowymi lub objęte innymi ograniczeniami utrudniającymi bezpośrednie połączenia z PlaidCloud. Dzięki Agentowi PlaidCloud zainstalowanemu wewnątrz odizolowanego obszaru PlaidCloud może zlecić agentowi wykonywanie takich działań, jak uruchamianie zapytań, pobieranie i przesyłanie plików, sprawdzanie warunków czujników, współpraca z SAP i wiele innych.

Ponieważ agent sam nawiązuje kontakt z PlaidCloud i komunikuje się za pomocą standardowych protokołów sieciowych HTTPS, zwykle wymaga minimalnej konfiguracji. Dodatkowo agent może działać jako nieuprzywilejowany użytkownik, co pozwala kontrolować prawa dostępu w środowisku o ograniczonych uprawnieniach.

## Tematy

- [Instalacja](/pl/reference/cli/plaidlink/install/) — uruchomienie PlaidLink w systemie Windows, Linux, macOS lub w kontenerze
- [Konfiguracja](/pl/reference/cli/plaidlink/configure/) — ustawienia połączenia, poświadczenia i opcje uruchomieniowe
- [Agenci](/pl/reference/cli/plaidlink/agents/) — zarządzanie wieloma agentami i ich możliwościami
- [Uaktualnienie](/pl/reference/cli/plaidlink/upgrade/) — przejście na nowszą wersję PlaidLink
