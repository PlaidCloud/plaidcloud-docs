---
title: Zarządzanie edytorami danych
description: Zarządzaj przypisaniami edytorów danych w projektach PlaidCloud, aby kontrolować, kto może modyfikować dane tabel bezpośrednio przez interfejs danych.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/managing-data-editors.md
---

PlaidCloud umożliwia porządkowanie edytorów danych i zarządzanie nimi, w tym etykietami. Edytory danych pozwalają edytować dane tabel lub tworzyć dane poprzez interakcję użytkownika.



PlaidCloud wykorzystuje system oparty na ścieżkach do porządkowania edytorów danych, podobny do nawigowania po szeregu folderów, co pozwala na elastyczniejszą i bardziej logiczną organizację (hierarchia sterująca) edytorów danych. Dzięki temu systemowi edytory danych można przenosić w obrębie hierarchii sterującej. Można tworzyć wiele odwołań do jednego edytora danych z różnych miejsc hierarchii sterującej (hierarchie alternatywne). Zarządzanie edytorami danych tą metodą pozwala, aby struktura odzwierciedlała potrzeby operacyjne, raportowanie i kontrolę.




## Tworzenie edytora danych z tabeli


Gotowy do użycia edytor danych możesz zbudować bezpośrednio z istniejącej tabeli. PlaidCloud analizuje kolumny tabeli i wstępnie konfiguruje edytor — wybierając kontrolkę wejściową dla każdej kolumny i zamieniając kolumny zawierające niewielki zbiór powtarzających się wartości na rozwijane listy wyboru.


Aby utworzyć edytor danych z tabeli:


1. Otwórz widok **Tabele** projektu i wybierz pojedynczą tabelę
2. Otwórz **Utwórz edytor danych z tabeli** — z menu **Nowy** na pasku narzędzi lub klikając tabelę prawym przyciskiem myszy
3. PlaidCloud profiluje tabelę i otwiera okno **Konfiguracja edytora danych** ze wszystkim wstępnie wypełnionym: ustawia zarówno źródło, jak i cel na wybraną tabelę, więc Twoje zmiany zapisują się bezpośrednio w niej, i nadaje każdej kolumnie na karcie **Kolumny formularza** kontrolkę odpowiadającą jej typowi danych i wartościom
4. Przejrzyj kolumny i w razie potrzeby dostosuj kontrolki
5. Kliknij **Zapisz** lub **Zapisz i zamknij**

Zapisanie tworzy edytor — kliknięcie **Anuluj** niczego nie dodaje.

Gdy kolumna odpowiada wymiarowi, przed zapisaniem wybierz dla niej hierarchię na karcie Kolumny formularza. PlaidCloud blokuje zapis, dopóki kolumna wymiaru nie ma hierarchii.


## Jak PlaidCloud konfiguruje kolumny


Gdy tworzysz edytor z tabeli — lub używasz **Wypełnij ze źródła** — PlaidCloud automatycznie konfiguruje każdą kolumnę:


- Kolumny **Boolean** stają się polem wyboru albo listą Prawda/Fałsz, gdy kolumna dopuszcza wartości puste
- Kolumny **Data** stają się selektorem daty
- Kolumny **Liczbowy** stają się polem liczbowym
- Kolumny odpowiadające **wymiarowi** stają się selektorem wymiaru, w którym wybierasz hierarchię — edycja komórki otwiera to samo drzewo wyboru członków opisane w [Właściwości typu wymiaru i selektor członków](/pl/guides/dimensions/dimensions/#właściwości-typu-wymiar-i-selektor-członków), z opcjami **Rozwiń wszystko**, **Zwiń wszystko**, **Zastosuj**, **Wyczyść** i **Anuluj**
- Kolumny, których wartości powtarzają się w niewielkim zbiorze — na przykład kod stanu lub regionu — stają się **listą rozwijaną** z wartościami znalezionymi w kolumnie
- Pozostałe kolumny **tekstowe** stają się polem tekstowym albo obszarem tekstowym dla długich wartości
- PlaidCloud uwzględnia kolumny przypominające klucze, takie jak automatycznie generowane identyfikatory, ale oznacza je jako tylko do odczytu

W przypadku bardzo dużych tabel PlaidCloud szacuje listę wartości na podstawie próbki wierszy. Kontrolkę dowolnej kolumny możesz później zmienić.

Na karcie **Kolumny formularza** wybierz kolumnę, aby zobaczyć krótkie wyjaśnienie, dlaczego PlaidCloud wybrał jej kontrolkę.


## Dostosowywanie progu listy wyboru


PlaidCloud zamienia kolumnę w listę rozwijaną tylko wtedy, gdy jej wartości powtarzają się w niewielkim zbiorze. Możesz zmienić ten próg i ponownie wyznaczyć kolumny:


1. Na karcie **Kolumny formularza** ustaw **Maks. liczba wartości listy wyboru** na największą liczbę różnych wartości, jaką kolumna może mieć, aby nadal stać się listą rozwijaną
2. Kliknij **Ponownie profiluj**

PlaidCloud ponownie analizuje tabelę źródłową z nowym ustawieniem i odbudowuje kolumny. Jeśli edytor ma już kolumny, ponowne profilowanie je zastępuje, więc PlaidCloud prosi o potwierdzenie.


## Wypełnianie istniejącego edytora z tabeli


To samo automatyczne konfigurowanie możesz zastosować do edytora, który już edytujesz:


1. Otwórz konfigurację edytora danych i przejdź do karty **Źródło i cel**
2. Ustaw źródło na tabelę
3. Na karcie **Kolumny formularza** kliknij **Wypełnij ze źródła**

PlaidCloud dodaje skonfigurowaną kolumnę dla każdej kolumny tabeli źródłowej. Zachowuje kolumny, które już dostosowałeś, i prosi o usunięcie kolumn, których nie ma już w źródle.


## Wyszukiwanie


Aby wyszukać edytory danych:


1. Użyj pola filtru w lewym dolnym rogu hierarchii sterującej

Filtr wyszukiwania przeszukuje nazwy i etykiety edytorów danych pod kątem dopasowań i pokazuje wyniki w hierarchii sterującej powyżej.




## Przenoszenie


Aby przenieść edytor danych w obrębie hierarchii sterującej:


1. Przeciągnij go do folderu, w którym chcesz go umieścić

## Zmiana nazwy


Aby zmienić nazwę edytora danych:


1. Kliknij edytor danych prawym przyciskiem myszy
2. Wybierz opcję zmiany nazwy
3. Wpisz nową nazwę i zapisz ją

Edytor danych będzie miał nową nazwę, ale zachowa swój pierwotny unikatowy identyfikator.




## Usuwanie


Możesz usunąć jeden edytor danych lub wiele edytorów danych.


Aby usunąć edytor danych:


1. Zaznacz edytory danych w hierarchii sterującej
2. Kliknij przycisk usuwania na górnym pasku narzędzi


## Tworzenie nowej struktury katalogów


Aby dodać nowy folder do hierarchii sterującej:


1. Kliknij przycisk Nowy folder na pasku narzędzi

Aby dodać folder do istniejącego folderu:


1. Kliknij folder prawym przyciskiem myszy
2. Wybierz Nowy folder


## Oznaczanie hierarchii dla ról przeglądających


Wyświetlanie edytorów danych przez różne role:


1. Zaznacz pola wyboru Eksplorator lub Menedżer

Aby zaktualizować wiele edytorów danych:


1. Zaznacz edytory danych w hierarchii sterującej
2. Wybierz żądaną rolę przeglądającą z menu Akcje na górnym pasku narzędzi


## Notatki opisujące zawartość tabeli


Aby dodać notatkę do edytora danych:


1. Zaznacz edytor danych
2. Zaktualizuj notatkę w formularzu kontekstowym po prawej stronie


## Wyświetlanie dodatkowych atrybutów hierarchii


Aby wyświetlić i edytować dodatkowe atrybuty edytora danych:


1. Zaznacz edytor danych i wyświetl formularz kontekstowy edytora danych po prawej stronie


## Duplikowanie edytora danych


Aby zduplikować edytor danych:


1. Zaznacz edytor danych
2. Kliknij przycisk Duplikuj na górnym pasku narzędzi


## Zapis przez asystenta AI lub MCP

Poza ekranami konfiguracji `editor_upsert` może ustawić źródło, cel i kontrolki edytora danych oraz zapisywać do niego wiersze bezpośrednio — `data` to lista obiektów wierszy kluczowanych identyfikatorem każdej kontrolki. Nieprawidłowa data jest odrzucana, zanim cokolwiek dotknie tabeli docelowej, więc błędny zapis nigdy nie ląduje częściowo.
