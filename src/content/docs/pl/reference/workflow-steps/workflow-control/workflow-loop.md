---
title: Workflow Loop (krok)
description: Tworzy pętlę w kroku przepływu pracy PlaidCloud, aby iterować po zestawie wartości i powtarzać kroki dla każdego elementu kolekcji.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/workflow-control/workflow-loop.md
---

## Opis

Uruchamia docelowy przepływ pracy raz dla każdego wiersza zestawu danych, ustawiając przed każdą iteracją wartości kolumn danego wiersza jako zmienne projektu. Użyj tego kroku, gdy parametryzowany proces ma być uruchamiany wielokrotnie z różnymi danymi wejściowymi — na przykład „uruchom zamknięcie miesiąca dla każdej jednostki biznesowej z tej tabeli” albo „załaduj ten raport dla każdego wymienionego kwartału”.

Każda iteracja pętli widzi zmienne tak, jakby zostały ustawione ręcznie, więc wywoływany przepływ pracy może się do nich odwoływać w wyrażeniach, filtrach, ścieżkach plików i nazwach tabel za pomocą standardowej składni `\{variable_name}`. Pętla jest domyślnie sekwencyjna; iteracje nie działają równolegle.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 690 170" role="img" aria-label="Krok Workflow Loop po zestawie danych z wierszami Q1, Q2 i Q3. Wartości kolumn każdego wiersza stają się zmiennymi projektu, a następnie uruchamiany jest docelowy przepływ pracy — jeden przebieg na wiersz, po kolei, nie równolegle." style="width:100%;max-width:690px;height:auto;">
  <defs><marker id="wl-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="50" width="120" height="74" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="74" y="44" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">zestaw danych</text>
  <text x="74" y="76" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Q1</text>
  <text x="74" y="96" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Q2</text>
  <text x="74" y="116" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Q3</text>
  <path d="M134 87 L178 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="180" y="63" width="140" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="250" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = Q1</text>
  <text x="250" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">przebieg 1</text>
  <path d="M320 87 L360 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="362" y="63" width="140" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="432" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = Q2</text>
  <text x="432" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">przebieg 2</text>
  <path d="M502 87 L542 87" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#wl-arrow)" />
  <rect x="544" y="63" width="138" height="48" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="613" y="83" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">quarter = Q3</text>
  <text x="613" y="99" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">przebieg 3</text>
  <text x="408" y="142" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">sekwencyjnie — jeden przebieg naraz, nie równolegle</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Kolumny każdego wiersza stają się zmiennymi projektu, a następnie uruchamiany jest docelowy przepływ pracy — jeden przebieg na wiersz, po kolei. Aby uzyskać izolowane rozgałęzienie równoległe, użyj <a href="/pl/guides/workflows/create-a-macro/">makra</a>.</figcaption>
</figure>



## Przepływ pracy do zatrzymania


Najpierw wybierz projekt zawierający przepływ pracy, który zostanie uruchomiony w każdej pętli, z menu rozwijanego **Projekt**.



Następnie wybierz konkretny przepływ pracy do uruchomienia z menu rozwijanego **Przepływ pracy**.

## Jeśli iteracja zakończy się niepowodzeniem

Domyślnie pętla zatrzymuje się na pierwszej iteracji, której przepływ pracy zakończy się niepowodzeniem, a krok kończy się niepowodzeniem. W sekcji **Obsługa błędów** wybierz **Kontynuuj po nieudanej iteracji**, aby uruchomić każdą iterację, nawet gdy któraś zakończy się niepowodzeniem. Każde niepowodzenie jest zachowywane w **Stan uruchomienia pętli** razem z wynikiem każdej iteracji, a krok kończy się ostrzeżeniem informującym, ile iteracji zakończyło się niepowodzeniem. Po wyczyszczeniu tej opcji pętla zatrzymuje się na pierwszym niepowodzeniu.

## Przykłady

Przykłady pojawią się wkrótce
