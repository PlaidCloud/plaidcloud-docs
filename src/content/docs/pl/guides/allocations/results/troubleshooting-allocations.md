---
title: Rozwiązywanie problemów z alokacjami
description: Rozwiązuj problemy z alokacjami PlaidCloud, w tym typowe błędy, problemy z konfiguracją i techniki debugowania wyników.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/results/troubleshooting-allocations.md
---

## Dlaczego nie można zapisać kroku alokacji

PlaidCloud sprawdza mapowanie kolumn kroku alokacji podczas jego zapisywania. Mapowanie, którego nie można uruchomić, jest w tym momencie odrzucane, z powiadomieniem **Nie można zapisać** zawierającym listę rzeczy do poprawienia, a formularz przełącza się na kartę z problemem. Wcześniej taki krok zapisywał się bez żadnych uwag, a następnie zatrzymywał przepływ pracy w trakcie uruchomienia — często po kilku minutach i z komunikatem wskazującym liczbę, a nie pole.

Nic nie jest sprawdzane, dopóki nie wybierzesz zarówno **Tabela wartości do alokacji**, jak i **Tabela danych sterujących**. Mapowanie kolumn jest budowane na podstawie tych dwóch tabel, więc dopóki obie nie zostaną ustawione, krok prosi jedynie o same tabele.

### Mapa źródła alokacji

**"No columns specified for allocation."**
Ustaw **Rola** co najmniej jednej kolumny na **Wartość do alokacji**. Ta kolumna zawiera wartości rozdzielane między cele.

**"Only numeric columns can be allocated, but ... is not numeric."**
Kolumna oznaczona jako **Wartość do alokacji** ma nienumeryczny **Typ**. Zmień typ na numeryczny — Numeric, Currency, Integer, Big Integer, Small Integer, Tiny Integer, Float, Double, Decimal, Serial lub Big Serial.

**"Rename the `alloc_status` target column."**
Alokacja zapisuje w tabeli wyników własną kolumnę `alloc_status`, więc kolumna docelowa o tej nazwie koliduje z nią. Zmień nazwę swojej kolumny.

### Mapa danych sterujących

**"No driver split value column found."**
Ustaw **Rola** jednej kolumny danych sterujących na **Wartość podziału**. Ta kolumna zawiera wagi lub wartości procentowe, według których alokacja dzieli.

**"The driver value column ... must be numeric."**
Zmień **Typ** kolumny **Wartość podziału** na numeryczny.

**"No driver relation columns specified."**
Ustaw **Rola** co najmniej jednej kolumny danych sterujących na **Relacja ze źródłem (mianownik)**. To ona wiąże wiersze danych sterujących z wierszami źródłowymi.

**"No allocation target columns are indicated."**
Ustaw **Rola** co najmniej jednej kolumny danych sterujących na **Cel alokacji (licznik)**. Te kolumny stają się celami alokacji i pojawiają się w tabeli wyników.

**"Driver relation columns do not exist in the source data."**
Kolumna oznaczona jako **Relacja ze źródłem (mianownik)** nie ma odpowiadającej jej kolumny o tej samej nazwie w **Mapa źródła alokacji**. Zmień jej nazwę, aby pasowała, albo dodaj kolumnę do mapy źródeł.

**"Allocation value column ... is also used as a numerator or denominator column."**
Ta sama nazwa kolumny jest jednocześnie **Wartość do alokacji** w mapie źródeł oraz **Relacja ze źródłem (mianownik)** lub **Cel alokacji (licznik)** w mapie danych sterujących. Zmień nazwę jednej z nich, aby alokowana wartość różniła się od kolumn opisujących, dokąd trafia.

### Tylko podział z użyciem wymiaru

**"Please select a hierarchy to use for the allocation dimension."**
Wybierz **Hierarchia wymiaru przypisania** na karcie **Ustawienia tabeli danych**. Zobacz [Konfigurowanie alokacji](/pl/guides/allocations/setup/configure-an-allocation/).

## Koszt osierocony


Koszt osierocony to....



## Nadmierna alokacja kosztu


Nadmierna alokacja kosztu ma miejsce, gdy otrzymujesz więcej kosztu na wyjściu...



## Nieprawidłowa alokacja kosztu


Nieprawidłowa alokacja kosztów zdarza się, gdy...
