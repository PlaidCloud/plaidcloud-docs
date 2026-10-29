---
title: Czekaj
description: Dodaj opóźnienie czasowe w kroku przepływu pracy PlaidCloud, aby wstrzymać wykonanie na określony czas przed przejściem do następnego kroku.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/wait.md
---

## Opis


Transformacja Czekaj służy do wstrzymania przetwarzania na określony czas. Może to być szczególnie przydatne podczas oczekiwania na operacje wejścia/wyjścia z innych systemów lub przy debugowaniu przepływów pracy w trakcie tworzenia.



## Parametry czasu trwania


Podaj nieujemną liczbę całkowitą za pomocą pokrętła **Czas trwania**.



Następnie wybierz jednostkę czasu z listy rozwijanej. Dostępne są następujące jednostki:


* Sekundy
* Minuty
* Godziny

## Oczekiwanie na czas lub plik

Sekcja **Inne oczekiwania** zawiera te pola. Krok czeka na nie w tej kolejności, po upływie czasu trwania:

* **Milisekundy** (`milliseconds`) — milisekundy odczekane dodatkowo do czasu trwania.
* **Do godziny** (`until_time`) — następnie czeka, aż zegar następnie wskaże tę godzinę, w UTC, w formacie `HH:MM:SS`.
* **Czekaj na plik** (`file`) — następnie czeka, aż ten plik Document, `{account, path}`, zostanie zmieniony. **Zmiana pliku** (`file_event`) to zmiana, na którą należy czekać: `modified` (domyślnie), `created` lub `deleted`. Krok sprawdza plik co **Sprawdzaj plik co (sekundy)** (`poll_seconds`, domyślnie 5) przez najwyżej **Najdłuższe oczekiwanie na plik (sekundy)** (`max_wait_seconds`, domyślnie 3600, najwyżej doba), a następnie kończy się z ostrzeżeniem i przepływ pracy jest kontynuowany. Plik, który już istnieje, gdy czekasz na `created`, od razu kończy oczekiwanie, a brakujący plik przy oczekiwaniu na `modified` lub `deleted` kończy się ostrzeżeniem z podaniem ścieżki, bez czekania.
