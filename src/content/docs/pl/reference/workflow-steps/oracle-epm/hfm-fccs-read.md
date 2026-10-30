---
title: "HFM/FCCS: odczytaj dane (ad hoc)"
description: Samodzielnie pobierz wycinek danych z Oracle FCCS, budując punkt widzenia w formularzu kroku — zwrócona siatka trafia automatycznie do tabeli, powtórne pobrania są buforowane, kolumna Entity jest gotowa na zabezpieczenia na poziomie wierszy, a opcjonalny ograniczony cel zamienia krok w zaplanowane cykliczne ładowanie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/oracle-epm/hfm-fccs-read.md
---

## Opis

Odczytuje wycinek danych ad hoc z Oracle **FCCS** (Financial Consolidation and Close, EPM Cloud) przez [połączenie HFM/FCCS](/pl/guides/connections/hfm-fccs/), według **punktu widzenia (POV)**, a nie przez pisanie zapytania. Użytkownik finansowy wybiera aplikację, buduje POV z wymiarów FCCS i uruchamia krok; zwrócona siatka trafia automatycznie do tabeli projektu (schemat przy odczycie — tabela jest tworzona na podstawie kolumn siatki). Działa to jak zapytanie na żywo, ale w rzeczywistości krok przesyła zadanie eksportu do FCCS, **odpytuje** je do zakończenia, a następnie pobiera i ładuje wynik — dzięki temu długo trwający wycinek nie blokuje, a całość nie wymaga zgłoszenia do zespołu HFM.

Ten krok jest dostępny w menu kroków w sekcji **Oracle EPM (HFM/FCCS)**.

:::note[Ogranicz wymiar jednostki]
Utrzymuj ograniczony wybór **Entity** — niezawężone wyodrębnienie może blokować aplikację FCCS przez długi czas, gdy trwa zadanie eksportu.
:::

## Konfiguracja

### Źródło i cel

| Pole | Wymagane | Uwagi |
|---|---|---|
| Połączenie HFM/FCCS | Tak | [Połączenie HFM/FCCS](/pl/guides/connections/hfm-fccs/), przez które odbywa się odczyt. |
| Środowisko | Tak | Środowisko połączenia. |
| Aplikacja | Tak | Aplikacja FCCS, z której odbywa się odczyt. Domyślnie jest to Aplikacja domyślna połączenia, jeśli została ustawiona. Wybór aplikacji uruchamia odkrywanie członków POV na żywo. |
| Tabela docelowa | Tak | Tabela projektu, do której trafia zwrócona siatka. |

### Punkt widzenia

Zbuduj wycinek z wymiarów FCCS. Na obsługiwanych instancjach listy członków wypełniają się automatycznie z odkrywania metadanych na żywo po wybraniu połączenia i aplikacji; na starszych instancjach nazwy członków wpisujesz ręcznie.

| Wymiar | Wymagane | Uwagi |
|---|---|---|
| Scenariusz | Tak | |
| Rok | Tak | |
| Okres | Tak | |
| Jednostka | Ograniczony | Musi wskazywać ograniczony wycinek — formularz odrzuca pusty wybór, „all" lub wybór szerszy niż 500 członków. Utrzymuj wybór zawężony, aby eksport nie blokował aplikacji. |
| Konto | Nie | |
| Custom1–Custom4 | Nie | Wymiary niestandardowe aplikacji. |
| ICP | Nie | Transakcje wewnątrzgrupowe. |
| Widok | Nie | |
| Wartość | Nie | |

Nieustawiony opcjonalny wymiar nie stosuje filtra na tej osi (używany jest domyślny członek FCCS).

### Ogranicz cel

Domyślnie wyłączone — każde uruchomienie ładuje wycinek ad hoc, który nadpisuje tabelę docelową.

| Pole | Uwagi |
|---|---|
| Ograniczony cel (zaplanowane cykliczne ładowanie) | Po zaznaczeniu cel staje się **trwałą** tabelą: krok scala dane do niej za pomocą upsertu opartego na kluczu zamiast nadpisywać, a schemat rośnie addytywnie, gdy późniejsza siatka wnosi nowe kolumny (nowa kolumna wywołuje ostrzeżenie, nigdy niepowodzenie). Umieszczenie kroku w zaplanowanym przepływie pracy daje cykliczne ładowanie, które gromadzi dane zamiast je kasować. |
| Kolumny kluczowe | Włączone tylko przy włączonym Ograniczonym celu. Kolumny oddzielone przecinkami, które tworzą klucz scalania (na przykład `Entity, Account`). **Pozostaw puste**, aby jako klucz scalania użyć kolumn wymiarów POV obecnych w załadowanej siatce. |

## Jak to działa

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 720 130" role="img" aria-label="Krok przesyła zadanie eksportu do FCCS, odpytuje je do zakończenia, pobiera siatkę i ładuje ją jako tabelę; powtórzony punkt widzenia jest obsługiwany z tabeli w pamięci podręcznej." style="width:100%;max-width:720px;height:auto;">
<defs><marker id="hf-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
<rect x="10" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="58" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Prześlij zadanie</text>
<rect x="150" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="198" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Odpytuj</text>
<rect x="290" y="46" width="96" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="338" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Pobierz siatkę</text>
<rect x="430" y="46" width="120" height="40" rx="7" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" /><text x="490" y="70" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Załaduj tabelę</text>
<path d="M106 66 L150 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<path d="M246 66 L290 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<path d="M386 66 L430 66" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#hf-arrow)" />
<text x="198" y="34" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">w trakcie działania…</text>
<rect x="590" y="46" width="120" height="40" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" /><text x="650" y="64" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">Powtórzony POV</text><text x="650" y="78" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">z pamięci podręcznej</text>
<path d="M550 82 C570 100 630 100 650 88" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" stroke-dasharray="4 3" marker-end="url(#hf-arrow)" />
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Uruchomienie przesyła zadanie eksportu, odpytuje je, pobiera siatkę i ładuje tabelę. Ten sam punkt widzenia zażądany ponownie jest obsługiwany z już załadowanej kopii.</figcaption>
</figure>

Podczas działania zadania krok pokazuje status odpytywania. Po załadowaniu tabela jest tworzona na podstawie kolumn siatki — nie trzeba z góry definiować schematu.

## Buforowanie

Ten sam POV zażądany ponownie jest **obsługiwany z już załadowanej tabeli**, natychmiast, zamiast ponownego przesyłania eksportu do FCCS. Uruchomienie jest identyfikowane kluczem złożonym z aplikacji, tabeli docelowej, punktu widzenia i znacznika **as-of** (domyślnie `latest`); powtórzenie, które trafia na już załadowany wycinek, zgłasza, że tabela została pozostawiona bez zmian, zamiast ją ponownie zapisywać. Zmień znacznik as-of, gdy chcesz wymusić świeże wyodrębnienie tego samego POV.

## Zabezpieczenia na poziomie wierszy

Oś jednostek załadowanej siatki jest normalizowana do kolumny o nazwie dokładnie **`Entity`**, dzięki czemu tabela jest **gotowa na zabezpieczenia na poziomie wierszy** — administrator może nią zarządzać za pomocą [Dostępu do wierszy](/pl/administration/access/managing-security-groups-and-assignments/), aby użytkownicy samoobsługowi widzieli tylko jednostki, do których mają uprawnienia.

To jest **zarządzane pod kontrolą administratora, nie automatycznie**. Ponieważ wyodrębnianie działa na koncie usługi połączenia, PlaidCloud nie pozwoli, aby krok sam deklarował swoje zabezpieczenia. Administrator wykonuje standardowy proces Dostępu do wierszy:

1. **Opublikuj** załadowaną tabelę na potrzeby raportowania.
2. **Zadeklaruj** kolumnę `Entity` jako atrybut zarządzający (domyślnie odmowa).
3. **Zatwierdź** pierwszy zarządzany zapis.
4. **Uzgodnij**, aby uprawnienia zaczęły obowiązywać.

Dopóki administrator tego nie zrobi, tabela nie jest filtrowana. Zobacz [Zarządzanie grupami zabezpieczeń i przypisaniami](/pl/administration/access/managing-security-groups-and-assignments/).

## Ograniczenia możliwości

| Ograniczenie | Co oznacza |
|---|---|
| Tylko do odczytu | Wyodrębnia wycinek z FCCS. Nie zapisuje danych konsolidacji, nie uruchamia konsolidacji ani nie księguje z powrotem. |
| Wymagana ograniczona jednostka | Formularz odrzuca pusty wybór jednostki, „all" lub szerszy niż 500 członków, a pojedynczy człon agregujący nadal może rozwinąć się po stronie serwera — utrzymuj wycinek zawężony. |
| Ręczni członkowie na starszych instancjach | Tam, gdzie instancja nie udostępnia punktu końcowego metadanych, listy członków nie wypełniają się automatycznie; wpisz nazwy członków ręcznie. |
| Zabezpieczenia na poziomie wierszy zarządzane przez administratora | Kolumna `Entity` jest gotowa na zabezpieczenia na poziomie wierszy, ale administrator musi opublikować, zadeklarować, zatwierdzić pierwszy zapis i uzgodnić, zanim tabela zostanie przefiltrowana. |

## Powiązane

- [Wyodrębnianie z HFM / FCCS (przewodnik)](/pl/guides/connections/hfm-fccs/) — pełny opis krok po kroku.
- [Konektor HFM / FCCS](/pl/reference/connectors/rest/hfm-fccs/) — opis pól połączenia.
- [Kroki Oracle EPM (HFM / FCCS)](/pl/reference/workflow-steps/oracle-epm/)
- [Zarządzanie grupami zabezpieczeń i przypisaniami](/pl/administration/access/managing-security-groups-and-assignments/)
