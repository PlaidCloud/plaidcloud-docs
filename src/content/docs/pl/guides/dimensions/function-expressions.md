---
title: Funkcje wymiarów dla wyrażeń i agregacji
description: Używaj wyrażeń funkcyjnych w wymiarach PlaidCloud, aby definiować wartości obliczane, logikę warunkową i dynamiczne właściwości członków.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/dimensions/function-expressions.md
---

## Funkcje używane w wyrażeniach hierarchii wymiaru

Na ekranie Hierarchia wymiaru można dodawać „agregacje” i „wyrażenia”. Ich opis znajduje się poniżej.

## Agregacje
Agregacja służy do wyświetlania zagregowanej wartości z tabeli (może to być „Sum”, „Count”, „Min” lub „Max”).
Poniższy obraz przedstawia agregację skonfigurowaną do pobierania wartości z tabeli „Wartości pozycji”, tak aby wartości mogły być wyświetlane dla każdego „Okresu” w hierarchii.

![Ładowanie wymiaru](/images/dimensions/expressions/dimension_expressions_1_agg.png)

Agregacje można filtrować, tak aby wyświetlane były tylko elementy pasujące do filtra. Na poniższym obrazie skonfigurowano agregację tak, aby pokazywała wartości dla wybranego elementu wymiaru „Konto”.

![Ładowanie wymiaru](/images/dimensions/expressions/dimension_expressions_2_agg.png)

Jeśli te filtry pozostaną puste, dane można filtrować za pomocą paska filtra wymiaru u góry ekranu, jak pokazano na poniższym obrazie:

![Ładowanie wymiaru](/images/dimensions/expressions/dimension_expressions_3_agg.png)

## Wyrażenia

Za pomocą wyrażeń można wyświetlać wartości obliczane na podstawie wartości z agregacji wyświetlanych dla wymiaru.
Wyrażenia buduje się za pomocą wzorów matematycznych, które mogą zawierać wiele rodzajów operatorów oraz kilka funkcji specjalnych. Zobacz [listę operatorów](https://mathjs.org/docs/expressions/syntax.html). Dostępne funkcje opisano poniżej.


## Funkcje
### Column(`<column_name>`)
Pobiera wartość z kolumny o podanej nazwie dla bieżącego wiersza/węzła.

Poniżej widać przykład wyrażenia zdefiniowanego tak, aby wyświetlało wynik pomnożenia Wartości pozycji przez 2.

![Ładowanie wymiaru](/images/dimensions/expressions/dimension_expressions_4_func_column.png)


![Ładowanie wymiaru](/images/dimensions/expressions/dimension_expressions_5_func_column.png)

### Childcount()

Zwraca liczbę elementów podrzędnych bieżącego wiersza/węzła. Jeśli bieżący wiersz/węzeł jest liściem, zwraca 0.

W poniższym przykładzie funkcja służy do zwrócenia średniej wartości węzłów podrzędnych węzła nadrzędnego.

![Ładowanie wymiaru](/images/dimensions/expressions/dimension_expressions_6_func_childcount.png)

![Ładowanie wymiaru](/images/dimensions/expressions/dimension_expressions_7_func_childcount.png)

### Leafcount()
Zwraca liczbę liści znajdujących się w drzewie dla bieżącego wiersza/węzła. Jeśli bieżący wiersz/węzeł jest liściem, zwraca 1.

![Ładowanie wymiaru](/images/dimensions/expressions/dimension_expressions_8_func_leafcount.png)

### Descendantcount()
Zwraca łączną liczbę elementów znajdujących się w drzewie dla bieżącego wiersza/węzła. Jeśli bieżący wiersz/węzeł jest liściem, zwraca 0.

![Ładowanie wymiaru](/images/dimensions/expressions/dimension_expressions_9_func_desccount.png)


### Siblingcount()
Zwraca liczbę elementów równorzędnych bieżącego wiersza/węzła.  Zwracana wartość obejmuje bieżący węzeł.

![Ładowanie wymiaru](/images/dimensions/expressions/dimension_expressions_10_func_siblingcount.png)


### Nodevalue("`<node_name>`","`<column_name>`")
Zwraca wartość z kolumny o podanej nazwie dla węzła o podanej nazwie.
Oto przykład, w którym funkcja służy do pokazania dla każdego wiersza/węzła procentu sumy „LIV”.

![Ładowanie wymiaru](/images/dimensions/expressions/dimension_expressions_11_func_nodevalue.png)

![Ładowanie wymiaru](/images/dimensions/expressions/dimension_expressions_12_func_nodevalue.png)


### Parentvalue("<column_name")
Zwraca wartość z podanej kolumny dla elementu nadrzędnego bieżącego węzła.
Ten przykład pokazuje, jaki procent wartości węzła nadrzędnego wykorzystuje węzeł podrzędny.

![Ładowanie wymiaru](/images/dimensions/expressions/dimension_expressions_13_func_parentvalue.png)

![Ładowanie wymiaru](/images/dimensions/expressions/dimension_expressions_14_func_parentvalue.png)

### Columntextcompare("<column_name", "`<text>`")

Zwraca wynik liczbowy informujący, czy tekst w kolumnie o podanej nazwie jest większy, mniejszy lub równy podanej wartości.

Jeśli tekst z kolumny jest równy podanemu tekstowi, funkcja zwraca 0.

Jeśli tekst z kolumny jest mniejszy od podanego tekstu, funkcja zwraca -1.

Jeśli tekst z kolumny jest większy od podanego tekstu, funkcja zwraca 0.


Poniższy przykład porównuje nazwę Okresu z „Jun”


![Ładowanie wymiaru](/images/dimensions/expressions/dimension_expressions_15_func_textcompare.png)

![Ładowanie wymiaru](/images/dimensions/expressions/dimension_expressions_16_func_textcompare.png)


## Wyrażenia warunkowe
Przedstawione powyżej przykłady są dość proste. Używając warunków w wyrażeniach, można tworzyć bardziej złożone wyrażenia.
W wyrażeniach warunki mają następującą postać:
`<condition>` ? `<value_if_true>` : `<value_if_false>`
np. „12 > 6 ? 1000: 0”

Łącząc wyrażenia zawierające zarówno warunki, jak i funkcje, można budować bardziej złożone wyrażenia, takie jak w tym przykładzie, gdzie do Wartości pozycji dodawane jest 100 000, jeśli miesiącem jest „Jun”

![Ładowanie wymiaru](/images/dimensions/expressions/dimension_expressions_17_cond.png)

![Ładowanie wymiaru](/images/dimensions/expressions/dimension_expressions_18_cond.png)


## Inny przykład: prosta alokacja

Ten przykład pokazuje, jaka część Wartości pozycji węzła nadrzędnego jest zużywana przy użyciu Wartości nośnika kosztów zasobów dla węzła liścia.

![Ładowanie wymiaru](/images/dimensions/expressions/dimension_expressions_19_alloc.png)

![Ładowanie wymiaru](/images/dimensions/expressions/dimension_expressions_20_alloc.png)

## Ograniczenia:
Obecnie nie można budować wyrażeń opartych na wartościach z innych wyrażeń. Wyrażenia można budować wyłącznie na wartościach z agregacji.
