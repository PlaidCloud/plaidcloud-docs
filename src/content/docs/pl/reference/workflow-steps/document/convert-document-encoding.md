---
title: Krok Convert Document Encoding
description: Konwertuj kodowanie pliku dokumentu między zestawami znaków w kroku przepływu pracy PlaidCloud, aby rozwiązać problemy ze zgodnością kodowania.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/convert-document-encoding.md
---

## Opis



Zmienia kodowanie znaków pliku tekstowego z jednego na inne. Przydatne, gdy pliki źródłowe docierają w starszych kodowaniach (Windows-1252, ISO-8859-1), a narzędzia docelowe potrzebują UTF-8, lub odwrotnie.

Gdy plik źródłowy nie jest w UTF-8, jego kodowanie jest ustalane na podstawie zawartości pliku. Bardzo krótki lub silnie powtarzalny plik dostarcza zbyt mało informacji i może zostać odczytany błędnie, więc sprawdź przekonwertowane dane wyjściowe takiego pliku.

Znak, którego kodowanie docelowe nie może przechować, domyślnie powoduje niepowodzenie kroku. Zaznacz **Zastąp znakiem ? znaki, których kodowanie docelowe nie obsługuje**, aby zamiast tego zapisać w ich miejscu `?`, tak jak robi to moduł zapisu Javy, a krok zakończy się powodzeniem.

Wybierz kodowanie docelowe w konfiguracji kroku. Skróty dla konkretnych kodowań znajdziesz w wariantach [UTF-8](/pl/reference/workflow-steps/document/convert-document-encoding-to-utf-8/), [UTF-16](/pl/reference/workflow-steps/document/convert-document-encoding-to-utf-16/) i [ASCII](/pl/reference/workflow-steps/document/convert-document-encoding-to-ascii/).


## Przykłady


Utwórz dane źródłowe, wybierz plik wejściowy i wskaż plik w tej lokalizacji. Wybierz żądaną lokalizację wyjściową i wskaż w niej miejsce dla pliku. Zapisz i uruchom.
