---
title: Convert Dashboard to PDF (krok)
description: Renderuje pulpit PlaidCloud do plików PDF na koncie dokumentów, po jednym dla każdego wiersza zbioru danych filtrów, ze stosowaniem wartości z wiersza jako filtrów pulpitu.
sidebar:
  order: 22
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/dashboard-to-pdf.md
---

## Opis

Renderuje pulpit do plików PDF i zapisuje je na koncie dokumentów. Użyj go, aby uruchamiać pulpit według harmonogramu — jako pakiet na koniec miesiąca, wysyłkę do osób, które się nie logują, lub zarchiwizowaną migawkę liczb z danego dnia.

Krok renderuje pulpit raz dla każdego wiersza zbioru danych filtrów, stosując wartości z tego wiersza jako filtry pulpitu, dzięki czemu jeden krok może w jednym uruchomieniu wytworzyć zestaw plików PDF dla każdego regionu lub każdej jednostki.

## Konfiguracja

### Pulpit

Pulpit do wyrenderowania.

### Zbiór danych filtrów

Tabela, której wiersze sterują renderowaniem: jeden plik PDF na wiersz.

### Ścieżka wyjściowa

Konto dokumentów i folder, do których zapisywane są pliki PDF.

### Opcje

- **Współbieżne generowanie PDF** — liczba renderowań wykonywanych jednocześnie. Domyślnie 8; zmniejsz ją, jeśli pulpit jest na tyle ciężki, że równoległe renderowania przekraczają limit czasu.
- **Czas oczekiwania na renderowanie (sekundy)** — występuje w konfiguracji kroku, ale **nie jest obecnie stosowany** przez moduł uruchamiający przepływy pracy. Jego ustawienie nie ma dziś żadnego skutku.

### Filtry pulpitu

Własne filtry pulpitu, każdy z jego **Identyfikatorem filtru pulpitu**. Są odczytywane z pulpitu podczas wypełniania mapowania.

### Mapowanie kolumn źródłowych

Kolumny zbioru danych filtrów i sposób użycia każdej z nich. Użyj **Sprawdź źródło › Wypełnij tabelę mapowania**, aby odczytać kolumny i filtry pulpitu; kolumna o nazwie takiej jak filtr pulpitu jest oznaczana jako filtr tego pulpitu. Ponowne wypełnienie zachowuje **Rodzaj** i **Zmapowaną kolumnę filtru** ustawione już dla kolumny.

Ustaw **Rodzaj** każdej kolumny:

- **Filtr kolumnowy** — wartość kolumny ustawia filtr pulpitu wskazany w polu **Zmapowana kolumna filtru**, który musi być jednym z filtrów pulpitu.
- **Nazwa pliku** — kolumna dostarcza nazwę każdego pliku PDF. Tylko jedna kolumna może być Nazwą pliku. Bez niej krok wyświetla ostrzeżenie i generuje nazwy automatycznie.
- **Brak filtra** — kolumna nie jest używana.

Co najmniej jedna kolumna musi być **Filtrem kolumnowym**.

## Co jest sprawdzane przy zapisie

Zapis kroku jest odrzucany, ze wskazaniem kolumny, gdy:

- Żadna kolumna nie jest Filtrem kolumnowym ze Zmapowaną kolumną filtru — *Oznacz co najmniej jedną kolumnę źródłową jako Filtr kolumnowy, wraz ze Zmapowaną kolumną filtru, którą ustawia.*
- Filtr kolumnowy nie ma Zmapowanej kolumny filtru lub wskazuje taką, której nie ma wśród filtrów pulpitu — *Zmapowana kolumna filtru 'Region' dla kolumny źródłowej 'region' nie jest jednym z filtrów pulpitu.*
- Więcej niż jedna kolumna jest Nazwą pliku — *Tylko jedna kolumna źródłowa może być Nazwą pliku; region i entity są nimi obie.*
- Kolumna Filtr kolumnowy lub Nazwa pliku nie ma typu danych — *Kolumna źródłowa 'region' nie ma typu danych; sprawdź źródło ponownie, aby go odświeżyć.* Niektóre kroki zapisane w formularzu kroku nie mają typów swoich kolumn i kończą się niepowodzeniem w każdym uruchomieniu, dopóki ich nie odzyskają. Uruchom **Sprawdź źródło › Wypełnij tabelę mapowania**, aby je przywrócić; Twoje oznaczenia Filtr kolumnowy i Nazwa pliku zostają zachowane.

## Powiązane

- [Kroki dokumentów](/pl/reference/workflow-steps/document/)
- [Pulpity (przewodnik)](/pl/guides/dashboards/)
- [Kroki raportów](/pl/reference/workflow-steps/reports/)
