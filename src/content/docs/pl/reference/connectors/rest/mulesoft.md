---
title: Konektor REST MuleSoft
description: Połącz PlaidCloud z bramą MuleSoft Anypoint i dołącz definicję API, aby kroki przepływu pracy mogły wyświetlać jej punkty końcowe.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/rest/mulesoft.md
---

MuleSoft Anypoint to brama API: stoi przed usługami opublikowanymi przez Twoją organizację, pod adresem specyficznym dla Twojego wdrożenia. Dlatego, w przeciwieństwie do konektora zbudowanego dla jednej usługi, połączenie MuleSoft nie zna własnych punktów końcowych — to Ty wskazujesz, gdzie znajduje się API i jego definicja.

## Dokumentacja API

Dokumentacją API dla tego połączenia jest dokumentacja usług, które udostępnia Twoja brama.

## Konfiguracja

MuleSoft używa tego samego formularza co [ogólne połączenie REST](/pl/reference/connectors/rest/generic-rest/) — te same cztery karty, te same pola i to samo zachowanie. Dwa z nich mają tu największe znaczenie:

- **Host lub adres IP** — adres Twojej bramy Anypoint. Nie ma wartości domyślnej, ponieważ adres MuleSoft jest specyficzny dla Twojego wdrożenia.
- **Typ uwierzytelniania** — dowolny z typów `None`, `Basic`, `API Key`, `Bearer Token` lub `OAuth 2.0`, którego oczekuje Twoja brama. Niczego nie zakładamy za Ciebie.

## Wyświetlanie punktów końcowych w przepływie pracy

Ponieważ brama nie ma wbudowanej listy punktów końcowych, dołącz do połączenia definicję OpenAPI 3.x lub Swagger 2.0 swojego API w sekcji **Definicja API** — albo adres, pod którym jest opublikowana, albo plik `.json` lub `.yaml` przechowywany w Document. Opis pól znajdziesz w sekcji [Definicja API](/pl/reference/connectors/rest/generic-rest/#definicja-api).

[Krok Żądanie REST](/pl/guides/workflows/rest-request-step/) używający tego połączenia może następnie ustawić **Źródło punktów końcowych** na **Z definicji API połączenia** i wybrać **Załaduj katalog**, aby wybrać punkt końcowy z listy API zamiast wpisywać każdą ścieżkę ręcznie.

## Powiązane

- [Ogólne połączenie REST](/pl/reference/connectors/rest/generic-rest/) — pełny opis pól tego formularza.
- [Tworzenie połączenia i zarządzanie nim](/pl/guides/connections/create-connection/)
- [Krok przepływu pracy Żądanie REST](/pl/guides/workflows/rest-request-step/)
