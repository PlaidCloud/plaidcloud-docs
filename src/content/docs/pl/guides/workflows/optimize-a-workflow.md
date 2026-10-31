---
title: Optymalizacja przepływu pracy
description: Przyspiesz zaawansowany przepływ pracy, odbudowując jego zależności na podstawie pochodzenia danych i scalając łańcuchy kroków wyodrębniania, przy czym każde scalenie jest weryfikowane na Twoich danych przed zastosowaniem.
sidebar:
  order: 19.6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/optimize-a-workflow.md
---

Funkcja **Optymalizuj** analizuje zaawansowany przepływ pracy i proponuje zmiany, które przyspieszają jego działanie. Każdą zmianę widzisz, zanim cokolwiek się wydarzy, wybierasz te, które chcesz zastosować, i możesz później cofnąć wynik.

Optymalizacja działa na zaawansowanych przepływach pracy (DAG). W przypadku standardowego przepływu pracy najpierw wybierz **Konwertuj na zaawansowany...**; zobacz [Zaawansowane przepływy pracy](/pl/guides/workflows/advanced-workflows/#wybór-typu-przepływu-pracy).

## Optymalizacja przepływu pracy

1. Na liście **Przepływy pracy** kliknij prawym przyciskiem myszy zaawansowany przepływ pracy i wybierz **Optymalizuj...**. Przepływ pracy nie może być uruchomiony ani wstrzymany, a Ty potrzebujesz do niego uprawnień do zapisu.
2. Okno **Optymalizuj przepływ pracy** pokazuje nagłówek, taki jak *34 steps → 30 steps · 12 steps can run in parallel*. Jeśli przepływ pracy ma historię uruchomień, dodawane jest *~11 s faster per run*.
3. Pod nagłówkiem znajduje się po jednym wierszu na każdą zmianę, z polem wyboru, krokami, których dotyczy, znaczeniem dla przepływu pracy oraz zaoszczędzonym czasem, mierzonym jako zmiana czasu uruchomienia w czasie rzeczywistym. Wszystkie są zaznaczone; odznacz te, których nie chcesz.
4. Lista **Nie można zoptymalizować** wymienia kroki, których optymalizacja nie ruszyła, wraz z konkretnym powodem dla każdego; zobacz [Dlaczego kroku nie można zoptymalizować](#dlaczego-kroku-nie-można-zoptymalizować).
5. Wybierz **Apply N changes**.

Jeśli w przepływie pracy nie ma już nic do poprawy, okno informuje o tym.

## Dwa rodzaje zmian

### Odbudowa zależności na podstawie pochodzenia danych

Optymalizacja odczytuje, które tabele każdy krok czyta i zapisuje, i przerysowuje połączenia tak, aby krok czekał tylko na kroki, których tabel używa. Kroki, które nie współdzielą tabel, są uruchamiane równolegle.

- Krok nie czeka już na niepowiązane kroki, więc nie zatrzymuje się, gdy niepowiązany krok zakończy się niepowodzeniem. Niepowodzenie przenosi się wzdłuż nowych zależności.
- Częściowe uruchomienie według zakresu kroków, takie jak **Uruchom od tego miejsca**, podąża za nowymi zależnościami.
- Serwer nadal ogranicza, ile kroków jest uruchamianych jednocześnie.
- Kroki, które wskazują swoje tabele po nazwie lub ścieżce, są rozumiane tak samo jak kroki używające identyfikatorów tabel. Nazwa musi pasować dokładnie do jednej tabeli w projekcie; nazwy pasującej do kilku tabel, odwołania używającego zmiennej ani tabeli w innym projekcie nie można prześledzić.
- Wyłączony krok nigdy nie wnosi kolejności i nie liczy się do kroków, które mogą działać równolegle.
- Optymalizacja pomija tę zmianę, gdy harmonogram lub inny przepływ pracy uruchamia zakres kroków tego przepływu pracy.

### Scalanie łańcucha kroków wyodrębniania w jeden

Łańcuch kroków Extract Data, z których każdy czyta tabelę zapisaną przez poprzedni, staje się jednym krokiem, który czyta pierwsze źródło i zapisuje ostatni wynik.

Każde scalenie jest weryfikowane przed zastosowaniem. Optymalizacja uruchamia oryginalne kroki i krok scalony na Twoich bieżących danych do tymczasowych tabel roboczych i porównuje oba wyniki wiersz po wierszu. Scalenie jest stosowane tylko wtedy, gdy są identyczne. Twój przepływ pracy i jego tabele nie są ruszane podczas weryfikacji.

- Zmiana nazwy, po której następuje filtr, na przykład krok Select, po którym następuje filtr, może zostać scalona w jeden krok.
- Gdy całego łańcucha nie można scalić, optymalizacja proponuje najdłuższą część, którą można.
- Tabele w środku scalonego łańcucha nie są już zapisywane przez przepływ pracy. Są zachowane, a nie usuwane, i zmiana je wymienia.
- Scalenie, którego wyniki się różnią lub którego nie można zweryfikować, nie jest stosowane, a wyniki podają powód. Scalenia wymagają tabeli źródłowej z danymi.

## Dlaczego kroku nie można zoptymalizować

Każdy wiersz na liście **Nie można zoptymalizować** podaje własną przyczynę:

| Przyczyna | Co oznacza |
|---|---|
| Agregacje | Krok podsumowuje wiersze, więc nie można go wchłonąć w sąsiedni krok. |
| Dwa filtry | Łańcucha z dwoma filtrami nie można zamienić w jeden krok. |
| Filtr na liczbie zmiennoprzecinkowej, która może się zaokrąglić | Scalenie mogłoby zmienić, które wiersze przechodzą, więc filtr zostaje tam, gdzie jest. |
| Krok, który uruchamia kod użytkownika | Wyrażeń, skryptów i podobnych kroków nie można zweryfikować jako równoważnych. |
| Tabela czytana przez więcej niż jeden krok | Tabela w środku łańcucha jest potrzebna gdzie indziej. |
| Wyłączony krok | Wyłączony krok nie jest scalany i nie wnosi kolejności. |
| Element kontenera wykonania | Kroki w kontenerze wykonania są uruchamiane jako całość. |
| Brak dostępnej liczby wierszy | Liczby wierszy tabeli źródłowej nie można odczytać, nawet na żywo, więc scalenia nie można dopasować rozmiarem do weryfikacji. |
| Nie można zidentyfikować tabeli | Nazwa tabeli w kroku nie pasuje do żadnej tabeli lub pasuje do więcej niż jednej, używa zmiennej albo wskazuje inny projekt. |
| Zabezpieczenia na poziomie wierszy lub zbyt duża tabela | Tabela jest objęta zabezpieczeniami na poziomie wierszy lub jest zbyt duża, aby ją zweryfikować automatycznie. |

Kontenery wizualne, które tylko grupują kroki na kanwie, nie uniemożliwiają scalenia. Gdy scalenie usuwa z nich kroki, scalony krok zajmuje ich miejsce, a pusty kontener jest usuwany. Cofnięcie przywraca układ dokładnie.

## Śledzenie postępu

Po zastosowaniu okno **Optymalizowanie przepływu pracy** pokazuje fazę: *Verifying (3 of 6 runs)...*, *Comparing results...* i *Applying...*. Po zakończeniu wyniki wymieniają, co zostało **Zastosowano**, w tym na ilu wierszach zweryfikowano każde scalenie, oraz co **Nie zastosowano**, z powodem dla każdego.

Jeśli przepływ pracy zmienił się w trakcie weryfikacji, których to dotyczy, są pomijane, a okno podaje ich liczbę. Jeśli zastosowanie się nie powiedzie, przepływ pracy jest przywracany do stanu sprzed operacji.

Uruchomienie, które rozpoczyna się podczas zatwierdzania zmian, jest na chwilę opóźniane, a nie odrzucane.

## Cofanie optymalizacji

Kliknij prawym przyciskiem myszy przepływ pracy i wybierz **Cofnij optymalizację...** albo użyj **Cofnij optymalizację** w wynikach. Potwierdź, a kroki, ustawienia i układ przepływu pracy wrócą do stanu sprzed optymalizacji. Zmiany wprowadzone w przepływie pracy od tego czasu zostaną utracone.

Cofnięcie wymaga punktów przywracania, które nie są dostępne w każdej dzierżawie. Dzierżawa bez nich nie może zastosować optymalizacji.

## Optymalizacja przez API i asystentów AI

Optymalizacja jest dostępna także przez REST API oraz przez narzędzie `workflow_optimize` dla asystentów AI, z tymi samymi krokami podglądu, zastosowania i cofnięcia.

## Następne kroki

- [Zaawansowane przepływy pracy](/pl/guides/workflows/advanced-workflows/) — kanwa, połączenia i elementy sterujące uruchamianiem
- [Kontrolowanie wykonywania równoległego](/pl/guides/workflows/controlling-parallel-execution/) — uruchamianie kroków w tym samym czasie
- [Uruchamianie przepływu pracy](/pl/guides/workflows/run-a-workflow/) — uruchamianie przepływu pracy od początku do końca
