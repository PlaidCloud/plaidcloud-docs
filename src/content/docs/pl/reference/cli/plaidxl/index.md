---
title: PlaidXL
description: Użyj dodatku PlaidXL do Excela, aby zalogować się do swojego obszaru roboczego PlaidCloud, pobierać tabele projektu i hierarchie wymiarów do arkuszy, odświeżać je na żądanie oraz tworzyć aktywne raporty za pomocą funkcji niestandardowych PlaidXL.
sidebar:
  label: PlaidXL
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/index.md
---

PlaidXL to dodatek PlaidCloud do programu Microsoft Excel. Łączy skoroszyt z Twoim obszarem roboczym PlaidCloud, dzięki czemu modele i raporty odczytują dane z autorytatywnych tabel projektu i wymiarów, a nie z kopii, która staje się nieaktualna po kolejnym uruchomieniu przepływu pracy.

Z PlaidXL można pracować na dwa sposoby, a większość skoroszytów korzysta z obu:

- **Okienko zadań** — przeglądaj projekty, wybierz tabelę lub wymiar, wskaż kolumny i filtry i pobierz dane do arkusza. **Refresh All Tables** pobiera bieżące dane dla każdej pobranej tabeli.
- **Funkcje niestandardowe** — formuły takie jak `=PLAIDXL.TABLE.GET_TABLE("Sales")` i `=PLAIDXL.CELL(...)`, które wczytują dane PlaidCloud bezpośrednio do komórek. Użyj ich do wyświetlania listy tabel i wymiarów, rozmieszczania hierarchii oraz obliczania zagregowanych wartości na potrzeby raportu.

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
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Okienko zadań i funkcje niestandardowe odczytują dane z wybranego projektu z Twoimi własnymi uprawnieniami PlaidCloud.</figcaption>
</figure>

PlaidXL odczytuje dane. Niczego nie zapisuje z powrotem w PlaidCloud, więc edycja pobranego arkusza nigdy nie zmienia tabeli projektu.

## Wymagania

- Excel dla Microsoft 365 lub Excel 2021 albo nowszy, w systemie Windows lub Mac. Karta PlaidCloud na wstążce i okienko zadań działają w Excelu na komputery stacjonarne.
- Konto PlaidCloud w co najmniej jednym obszarze roboczym oraz dostęp do projektów, które chcesz odczytywać. PlaidXL pokazuje tylko te projekty, tabele i wymiary, które Twoje konto już widzi w PlaidCloud.

## Tematy

- [Instalacja](/pl/reference/cli/plaidxl/install/) — dodaj PlaidXL do Excela i otwórz okienko zadań
- [Logowanie](/pl/reference/cli/plaidxl/connect/) — połącz się z obszarem roboczym, wyloguj się i przełączaj obszary robocze
- [Praca z tabelami i wymiarami](/pl/reference/cli/plaidxl/retrieve/) — wybierz projekt, przefiltruj tabelę, pobierz ją do arkusza i odśwież
- [Funkcje niestandardowe](/pl/reference/cli/plaidxl/functions/) — każda funkcja `PLAIDXL`, jej argumenty i zwracana wartość
- [Tworzenie raportu za pomocą funkcji niestandardowych](/pl/reference/cli/plaidxl/build-a-report/) — rozmieść hierarchię i wypełnij ją zagregowanymi wartościami
- [Wstążka PlaidCloud](/pl/reference/cli/plaidxl/ribbon/) — polecenia odświeżania, rozwijania i oczyszczania
- [Rozwiązywanie problemów](/pl/reference/cli/plaidxl/troubleshooting/) — rozwiązania najczęstszych problemów

Dopiero zaczynasz z PlaidXL? Samouczek [Praca w Excelu z PlaidXL](/pl/get-started/tutorials/excel-with-plaidxl/) przeprowadzi Cię od instalacji dodatku do pierwszego raportu w około 20 minut.

## Powiązane

- [Projekty](/pl/guides/projects/) — co zawiera projekt i jak go znaleźć
- [Tabele i widoki](/pl/guides/data/tables-views/) — tabele pobierane przez PlaidXL
- [Korzystanie z wymiarów](/pl/guides/dimensions/dimensions/) — hierarchie, które PlaidXL rozmieszcza i agreguje
