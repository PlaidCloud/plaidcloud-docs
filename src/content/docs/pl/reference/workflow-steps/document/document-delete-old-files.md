---
title: Delete Old Files (krok)
description: Usuń pliki na koncie dokumentów starsze lub nowsze niż wybrany wiek, z listą podglądową przed usunięciem czegokolwiek.
sidebar:
  order: 23
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/document-delete-old-files.md
---

import { Aside } from '@astrojs/starlight/components';

## Opis

Usuwa pliki na koncie dokumentów na podstawie wieku. Użyj go, aby folder eksportu lub folder wejściowy nie rósł bez końca — usuń wczorajsze wyodrębnienia lub wyczyść archiwa starsze niż rok.

## Konfiguracja

### Pliki do usunięcia

- **Ścieżka pliku** — konto dokumentów i folder, w którym krok działa.
- **Wiek** — liczba oraz jednostka: minuty, godziny, dni, miesiące lub lata.
- **Przed lub po** — usuń pliki zmodyfikowane ostatnio **przed** datą graniczną (zwykły kierunek czyszczenia) lub **po** niej.
- **Rekurencyjnie** — domyślnie wyłączone. Włącz, aby objąć podfoldery.
- **Tabela wyników testu** — tabela, do której przycisk **Testuj** w edytorze kroku zapisuje
  podgląd pasujących plików.

<Aside type="caution" title="Podgląd przez Testuj, a nie przez uruchomienie kroku">
  Podgląd pochodzi z przycisku **Testuj** podczas edycji kroku.
  Uruchomienie kroku w przepływie pracy zawsze usuwa pliki — nie ma trybu próbnego,
  a tabela wyników testu nie zmienia tego zachowania. Usunięcia nie można cofnąć,
  a błędna ścieżka przy włączonej opcji **Rekurencyjnie** sięga dalej, niż się spodziewasz, więc sprawdź
  podgląd, zanim ustawisz harmonogram.
</Aside>

## Powiązane

- [Kroki dokumentów](/pl/reference/workflow-steps/document/)
- [Delete Document File (krok)](/pl/reference/workflow-steps/document/delete-document-file/)
- [Lista katalogu](/pl/reference/workflow-steps/document/directory-listing/)
