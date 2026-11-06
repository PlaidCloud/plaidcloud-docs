---
title: PlaidXL
description: Używaj dodatku PlaidXL do Excela, aby logować się do obszaru roboczego PlaidCloud, pobierać tabele projektu i hierarchie wymiarów do arkuszy, tworzyć aktywne raporty, drążyć i wyjaśniać liczby, odczytywać zarządzane metryki, planować przez wpisywanie wartości z powrotem do PlaidCloud oraz zadawać pytania Weave.
sidebar:
  label: PlaidXL
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/index.md
---

PlaidXL to dodatek PlaidCloud do programu Microsoft Excel. Łączy skoroszyt z Twoim obszarem roboczym PlaidCloud, dzięki czemu modele i raporty korzystają z wiarygodnych tabel projektu i wymiarów, a nie z kopii, która traci aktualność przy kolejnym uruchomieniu przepływu pracy.

Z PlaidXL możesz pracować na trzy sposoby, a większość skoroszytów korzysta ze wszystkich:

- **Okienko zadań** — przeglądaj projekty, wybierz tabelę lub wymiar, wskaż kolumny i filtry oraz pobierz dane do arkusza. Odświeżanie utrzymuje je aktualne, a **Save to PlaidCloud** zapisuje edytowaną tabelę z powrotem. Pozostałe karty budują za Ciebie formułę lub cały raport, wyjaśniają, skąd pochodzi liczba, i pozwalają zadać pytanie Weave zwykłymi słowami.
- **Funkcje niestandardowe** — formuły takie jak `=PLAIDXL.TABLE.GET_TABLE("Sales")`, `=PLAIDXL.CELL(...)` i `=PLAIDXL.METRIC("Net Revenue")` odczytują dane PlaidCloud bezpośrednio do komórek. Używaj ich do wyświetlania list tabel i wymiarów, układania hierarchii, obliczania zagregowanych wartości do raportu i odczytywania zarządzanych metryk.
- **Wstążka i menu prawego przycisku myszy** — drąż wymiar z dowolnej komórki, wybieraj elementy, odświeżaj, wyjaśniaj liczbę lub pokaż wiersze, na których się opiera, ze skrótem klawiszowym dla każdej z tych czynności.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 660 230" role="img" aria-label="Excel zawiera okienko zadań PlaidXL i funkcje niestandardowe PlaidXL. Oba wysyłają żądania, zalogowane jako Ty, do projektu w Twoim obszarze roboczym PlaidCloud, który zwraca wiersze tabel, hierarchie wymiarów i zagregowane wartości do komórek arkusza." style="width:100%;max-width:660px;height:auto;">
  <defs>
    <marker id="px-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker>
  </defs>
  <rect x="20" y="20" width="250" height="190" rx="10" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="145" y="44" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Skoroszyt Excela</text>
  <rect x="40" y="62" width="210" height="52" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="145" y="84" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Okienko zadań PlaidXL</text>
  <text x="145" y="102" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">przeglądanie, filtrowanie, pobieranie, odświeżanie</text>
  <rect x="40" y="130" width="210" height="52" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="145" y="152" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Funkcje PLAIDXL.*</text>
  <text x="145" y="170" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">tabele, hierarchie, wartości w komórkach</text>
  <rect x="410" y="40" width="230" height="150" rx="10" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="525" y="66" text-anchor="middle" font-size="13" font-weight="700" fill="var(--sl-color-text)">Obszar roboczy PlaidCloud</text>
  <rect x="430" y="80" width="190" height="94" rx="8" fill="none" stroke="var(--sl-color-gray-5)" />
  <text x="525" y="102" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Projekt</text>
  <text x="525" y="124" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">tabele</text>
  <text x="525" y="142" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">wymiary i hierarchie</text>
  <path d="M252 98 L405 98" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#px-arrow)" />
  <text x="330" y="90" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">zalogowany jako Ty</text>
  <path d="M405 150 L254 150" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#px-arrow)" />
  <text x="330" y="168" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">wiersze, węzły, wartości</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Okienko zadań i funkcje niestandardowe odczytują dane z wybranego projektu z Twoimi własnymi uprawnieniami w PlaidCloud.</figcaption>
</figure>

PlaidXL odczytuje dane z PlaidCloud i zmienia tabelę projektu tylko wtedy, gdy sam do niej zapisujesz: wpisz liczbę nad wartością `CELL` albo zapisz pobrany arkusz za pomocą **Save to PlaidCloud**. Oba zapisy następują natychmiast, a **Undo last write** je cofa. Zobacz [Wpisywanie wartości do PlaidCloud](/pl/reference/cli/plaidxl/write-values/).

## Wymagania

- Excel dla Microsoft 365 albo Excel 2021 lub nowszy, w systemie Windows lub Mac. Karta PlaidCloud na wstążce, menu prawego przycisku myszy i okienko zadań działają w Excelu na komputerze.
- Konto PlaidCloud w co najmniej jednym obszarze roboczym oraz dostęp do projektów, które chcesz odczytywać. PlaidXL pokazuje tylko projekty, tabele i wymiary, które Twoje konto już widzi w PlaidCloud.

## Tematy

- [Instalacja](/pl/reference/cli/plaidxl/install/) — dodaj PlaidXL do Excela i otwórz okienko zadań
- [Logowanie](/pl/reference/cli/plaidxl/connect/) — połącz się z obszarem roboczym, wyloguj się i przełączaj obszary robocze
- [Praca z tabelami i wymiarami](/pl/reference/cli/plaidxl/retrieve/) — wybierz projekt, przefiltruj tabelę, pobierz ją do arkusza, odśwież i zapisz z powrotem
- [Funkcje niestandardowe](/pl/reference/cli/plaidxl/functions/) — każda funkcja `PLAIDXL`, jej argumenty i to, co zwraca
- [Tworzenie raportu](/pl/reference/cli/plaidxl/build-a-report/) — ułóż aktywny raport z okienka zadań lub za pomocą formuł
- [Drążenie, wybór elementów i wyjaśnianie liczb](/pl/reference/cli/plaidxl/drill/) — drąż z komórki, wybieraj elementy, wyjaśniaj liczbę i pokazuj jej wiersze szczegółowe
- [Wpisywanie wartości do PlaidCloud](/pl/reference/cli/plaidxl/write-values/) — planuj, nadpisując wartości raportu, i cofaj dowolny zapis
- [Zapytaj Weave w Excelu](/pl/reference/cli/plaidxl/weave/) — twórz, drąż i naprawiaj na podstawie próśb zapisanych zwykłym językiem
- [Wstążka PlaidCloud](/pl/reference/cli/plaidxl/ribbon/) — każde polecenie, menu prawego przycisku myszy i skróty klawiszowe
- [Rozwiązywanie problemów](/pl/reference/cli/plaidxl/troubleshooting/) — rozwiązania najczęstszych problemów

Zaczynasz pracę z PlaidXL? Samouczek [Praca w Excelu z PlaidXL](/pl/get-started/tutorials/excel-with-plaidxl/) prowadzi od instalacji dodatku do pierwszego raportu w około 20 minut.

## Powiązane

- [Projekty](/pl/guides/projects/) — co zawiera projekt i jak go znaleźć
- [Tabele i widoki](/pl/guides/data/tables-views/) — tabele, które pobiera PlaidXL
- [Korzystanie z wymiarów](/pl/guides/dimensions/dimensions/) — hierarchie, które PlaidXL układa i agreguje
