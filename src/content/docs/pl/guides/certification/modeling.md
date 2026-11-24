---
title: Ścieżka nauki Modelowanie
description: Co przeczytać przed laboratoriami Praktyk i Ekspert z modelowania PlaidCloud i czego wymaga każde laboratorium.
sidebar:
  label: Modelowanie
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/certification/modeling.md
---

Ścieżka Modelowanie dotyczy wymiarów i alokacji: budowania hierarchii, rozdzielania kosztów według kluczy alokacji i dowodzenia, że wyniki się zgadzają. Zacznij od ścieżki [Podstawy](/pl/guides/certification/foundations/). Informacje o tym, jak działają laboratoria, znajdziesz w [Certyfikacja PlaidCloud](/pl/guides/certification/).

## Praktyk

### Czytaj w tej kolejności

1. [Wprowadzenie do wymiarów](/pl/guides/dimensions/getting-started/)
2. [Zarządzanie hierarchiami](/pl/guides/projects/managing-hierarchies/)
3. [Zaprojektuj hierarchię wymiaru](/pl/get-started/tutorials/design-a-dimension/)
4. [Szybki start z alokacjami](/pl/guides/allocations/getting-started/allocations-quick-start/)
5. [Allocation Split](/pl/reference/workflow-steps/allocation/allocation-split/)
6. [Zbuduj model alokacji](/pl/get-started/tutorials/build-an-allocation/)
7. [Wyniki alokacji](/pl/guides/allocations/results/allocation-results/)
8. [Wyświetlanie dziennika przepływu pracy](/pl/guides/workflows/viewing-workflow-log/)

### Czego wymaga laboratorium

Laboratorium nosi nazwę *Modelowanie: alokacja wspólnych kosztów IT*.

Tabela zawiera każdy dział i jego element nadrzędny. Budujesz wymiar, którego główna hierarchia jest dokładnie tym drzewem. Następnie w przepływie pracy laboratorium alokujesz pulę kosztów na działy proporcjonalnie do liczby pracowników, z jednym wierszem wyniku na dział. Jest też druga tabela sterująca, która nie jest kluczem dla tej puli.

Laboratorium sprawdza, czy przepływ pracy się uruchamia, czy hierarchia jest prawidłowa, czy zaalokowana suma zgadza się ze źródłem oraz czy każdy dział otrzymuje prawidłową kwotę.

## Ekspert

Laboratorium Ekspert jest na czas: masz 4 godziny od chwili jego rozpoczęcia.

### Czytaj w tej kolejności

1. [Konfigurowanie alokacji](/pl/guides/allocations/setup/configure-an-allocation/)
2. [Rozwiązywanie problemów z alokacjami](/pl/guides/allocations/results/troubleshooting-allocations/)
3. [Śledzenie alokacji za pomocą agenta AI połączonego przez MCP](/pl/integrations/ai-coding-agents/tracing-allocations/)
4. [Wyniki alokacji](/pl/guides/allocations/results/allocation-results/)
5. [Wypróbuj symulację klucza alokacji](/pl/guides/allocations/results/driver-what-if/)
6. [Zarządzanie hierarchiami](/pl/guides/projects/managing-hierarchies/)

### Czego wymaga laboratorium

Laboratorium nosi nazwę *Modelowanie Ekspert: napraw model alokacji*.

Dwuetapowy model alokacji przestał się zgadzać z księgą, a niektóre działy mają wyraźnie błędne wartości. Ustalasz przyczynę i naprawiasz model: każdy etap alokuje dokładnie swoją pulę, sumy działów są prawidłowe i zgadzają się z księgą, a wymiar działów zawiera tylko działy, które istnieją. Nie wolno używać wiersza bilansującego, aby cokolwiek się zgadzało. Następnie dodajesz krok, który pokazuje, ile IT kosztowałoby każdy dział, gdyby alokowano je według powierzchni zamiast liczby pracowników.

Laboratorium sprawdza, czy przepływ pracy się uruchamia, czy hierarchia jest prawidłowa, czy każdy etap i sumy działów zgadzają się z księgą, czy każdy dział otrzymuje prawidłową sumę oraz czy scenariusz powierzchni jest prawidłowy.
