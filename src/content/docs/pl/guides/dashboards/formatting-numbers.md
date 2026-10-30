---
title: Formatowanie liczb i innych typów danych
description: Formatuj liczby w pulpitach PlaidCloud, w tym waluty, wartości procentowe, miejsca dziesiętne i niestandardowe wzorce wyświetlania liczb.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dashboards/formatting-numbers.md
---

## Formatowanie liczb i innych typów danych

W PlaidCloud są 2 sposoby formatowania liczb. Pierwszy to bezpośrednie przekształcenie wartości w tabelach, a drugi (częstszy) to sformatowanie ich przy wyświetlaniu, aby wartości nie traciły precyzji w tabeli, a użytkownik widział je w czytelniejszej, bardziej odpowiedniej postaci.

Jak sformatować wartość wyświetlaną na pulpicie w wybrany przeze mnie sposób?
Podstawowym sposobem wyświetlania wartości jest obiekt wykresu na pulpicie. Wykresy mogą być tabelami, dużymi liczbami (Big Number), wykresami słupkowymi itd. Każdy obiekt wykresu może mieć nieco inne miejsce lub sposób wyświetlania wartości. Na przykład w tabelach można zmienić format każdej kolumny, a w przypadku Big Number — format liczby.

Aby zmienić format, edytuj wykres i znajdź pole `D3 FORMAT` lub `NUMBER FORMAT`. W przypadku wykresu Big Number kliknij kartę `CUSTOMIZE`, a zobaczysz `NUMBER FORMAT`. W przypadku tabeli kliknij kartę `CUSTOMIZE`, wybierz kolumnę liczbową (oznaczoną znakiem #) w `CUSTOMIZE COLUMN`, a zobaczysz pole `D3 FORMAT`.

Wartość domyślna to `Adaptive formatting`. Dostosowuje ona format do wartości. Jeśli jednak chcesz ustalić stały format (np. $12.23 lub 12,345,678), wybierz żądany format z listy rozwijanej lub wpisz ręcznie inną wartość (jeśli pole na to pozwala).

## Formatowanie D3 — co to jest?

Formatowanie D3 to uporządkowany, sformalizowany sposób wyświetlania wyników danych w określonym formacie. Na przykład w pewnych sytuacjach możesz chcieć wyświetlić dużą wartość jako 3B (3 miliardy), co w formacie D3 zapisuje się jako `.3s`, albo jako 3,001,238,383, co zapisuje się jako `,d`. Innym częstym przykładem jest decyzja, czy przedstawiać wartości w dolarach z dokładnością do 2 miejsc dziesiętnych, czy zaokrąglić je do pełnego dolara: $,d lub $,.2f, aby pokazać znak dolara, przecinki, 2 miejsca dziesiętne i zapis stałoprzecinkowy.
Aby zgłębić temat D3, odwiedź tę witrynę: [GitHub D3](https://github.com/d3/d3-format)


## Ogólny format D3

Ogólna struktura D3 jest następująca:

`[​[fill]align][sign][symbol][0][width][,][.precision][~][type]`

Wypełnienie (fill) może być dowolnym znakiem (np. kropką, x lub czymkolwiek innym). Jeśli używasz znaku wypełnienia, po nim następuje znak `align`, który musi być jednym z następujących:

`>` - Wyrównanie do prawej w dostępnej przestrzeni. (Zachowanie domyślne).
`<` - Wyrównanie do lewej w dostępnej przestrzeni.
`^` - Wyśrodkowanie w dostępnej przestrzeni.
`=` - jak >, ale ze znakiem i symbolem po lewej stronie wypełnienia.

`sign` może mieć wartość:
`-` - puste dla zera lub liczby dodatniej i znak minus dla ujemnej. (Zachowanie domyślne.)
`+` - znak plus dla zera lub liczby dodatniej i znak minus dla ujemnej.
`(` - nic dla zera lub liczby dodatniej i nawiasy dla ujemnej.
(spacja) - spacja dla zera lub liczby dodatniej i znak minus dla ujemnej.

`symbol` może mieć wartość:
`$` - zastosuj symbol waluty.

Opcja `zero` (0) włącza dopełnianie zerami; niejawnie ustawia fill na 0, a align na =.

`width` określa minimalną szerokość pola; jeśli nie jest podana, szerokość zostanie ustalona na podstawie zawartości. Na przykład przy wartości 8 szerokość pola wyniesie 8 znaków.

Opcja `comma` (,) włącza używanie przecinków jako separatorów (np. tysięcy).

W zależności od typu `precision` może oznaczać liczbę cyfr po przecinku dziesiętnym (typy f i %) albo liczbę cyfr znaczących (typy ​, g, r, s i p). Jeśli precyzja nie jest podana, domyślnie wynosi 6 dla wszystkich typów oprócz (none), dla którego domyślnie wynosi 12.

Opcja `tilde` ~ usuwa nieznaczące zera końcowe we wszystkich typach formatów. Najczęściej używa się jej razem z typami r, s i %.

`types`
|Typ  |   Opis                                                                                      |
|-----|---------------------------------------------------------------------------------------------|
|f    |zapis stałoprzecinkowy. **(częsty)**
|d    |zapis dziesiętny, zaokrąglony do liczby całkowitej. **(częsty)**
|%    |pomnożenie przez 100, a następnie zapis dziesiętny ze znakiem procenta. **(częsty)**
|g    |zapis dziesiętny lub wykładniczy, zaokrąglony do cyfr znaczących.
|r    |zapis dziesiętny, zaokrąglony do cyfr znaczących.
|s    |zapis dziesiętny z przedrostkiem SI, zaokrąglony do cyfr znaczących.
|p    |pomnożenie przez 100, zaokrąglenie do cyfr znaczących, a następnie zapis dziesiętny ze znakiem procenta.

## Przykłady
|Wyrażenie|Dane wejściowe|Wynik|Uwagi|
|----------|-----|------|-----|
|,d|12345.67|12,346|zaokrągla wartość do najbliższej liczby całkowitej, dodaje przecinki
|,.2f|12345.678|12,345.68|Dodaje przecinki, 2 miejsca dziesiętne, zaokrągla do 2 miejsc po przecinku
|$,.2f|12345.67|$12,345.67|Dodaje symbol $, przecinki, 2 cyfry po przecinku dziesiętnym
|$,d|12345.67|$12,346|
|.&lt;10,|151925|151,925...|kropki po lewej stronie wartości, szerokość 10 znaków, z przecinkami
|0>10|12345|0000012345|dopełnia wartość zerami po lewej stronie, szerokość 10 znaków. Dobrze sprawdza się do ustalania stałej szerokości wartości kodu 
|,.2%|13.215|1,321.50%|przecinki, 2 cyfry po przecinku dziesiętnym, konwersja na wartość procentową i wyświetlenie symbolu %
|x^+$16,.2f|123456|xx+$123,456.00xx| wypełnienie znakiem „x", wyśrodkowanie, symbol +/-, symbol $, szerokość 16 znaków, przecinki, 2 miejsca dziesiętne
