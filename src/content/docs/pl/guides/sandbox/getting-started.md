---
title: Pierwsze kroki z Custom App Sandbox
description: Zacznij tworzyć i wdrażać własne aplikacje w środowisku PlaidCloud Sandbox — kroki konfiguracji i ustawień.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/sandbox/getting-started.md
---

## Czym jest Sandbox
PlaidCloud Sandbox umożliwia wdrażanie własnych aplikacji z natywnym lokalnym dostępem do danych i operacji PlaidCloud.  Środowisko Sandbox zapewnia pełne środowisko obliczeniowe do budowania aplikacji niestandardowych, które rozszerzają korzystanie z PlaidCloud.

Wszystkie aplikacje niestandardowe działają w oparciu o procesy wdrożeniowe Kubernetes, dlatego niezbędna jest podstawowa znajomość obiektów Kubernetes.  Dostępny jest [przykład Hello World](https://github.com/PlaidCloud/custom-app-template), który pokazuje, jak wdrożyć prostą aplikację.

## Dostępne zasoby
Aplikacje Sandbox mają miękki limit zasobów, przy założeniu, że zasoby nie będą nadużywane.  Możemy obsłużyć duże ilości mocy obliczeniowej, jeśli zajdzie taka potrzeba, ale porozmawiajmy o tym przed próbą wdrożenia.  Skontaktuj się z nami, jeśli spodziewasz się potrzeby znacznych zasobów.

Aplikacje działające w sandboxie mają bezpośredni dostęp do Lakehouse i do dowolnej liczby baz danych Postgres, jakie sobie zażyczysz.  Bazy danych Postgres są przeznaczone do obsługi danych o umiarkowanej wielkości, więc doskonale nadają się do przechowywania konfiguracji i innych metadanych.  Do podstawowego przechowywania danych używaj Lakehouse, ponieważ umożliwia przechowywanie dużych ilości danych przy zachowaniu wydajności.

Wszystkie interfejsy API PlaidCloud są również dostępne bezpośrednio z Sandbox bez używania publicznego adresu URL, co pomaga w szybkości przesyłania danych.

## Wymagania dotyczące obrazów

Każdy obraz obsługujący wdrożenie Kubernetes oparte na Dockerze nadaje się do aplikacji niestandardowej.  Obecnie obsługiwane są tylko obrazy oparte na systemach *nix.  Jeśli potrzebujesz uruchomić obraz oparty na systemie Windows, skontaktuj się z nami.

## Integracja z potokiem CI/CD

Wdrożenie aplikacji Sandbox w Kubernetes wykorzystuje procesy GitOps.  Dzięki temu możesz wdrożyć własny proces CI/CD do budowania i wdrażania obrazów.  Repozytorium git Twojej aplikacji niestandardowej jest stale monitorowane pod kątem zmian, więc w miarę wprowadzania aktualizacji Twój sandbox będzie aktualizowany.
