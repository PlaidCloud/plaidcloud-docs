---
title: Galeria aplikacji
description: Dodaj aplikację Studio do galerii lub ją usuń oraz utwórz nową aplikację na podstawie wymienionej.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/gallery.md
---

Galeria aplikacji to półka, na której Twój obszar roboczy trzyma gotowe aplikacje Panel. Każdy, kto może wyświetlić projekt wymienionej aplikacji, może utworzyć własną kopię i ją zmieniać, dzięki czemu dobra aplikacja staje się punktem wyjścia, a nie czymś, co ludzie budują od nowa.

## Tworzenie aplikacji z galerii

1. W **Moje aplikacje Panel** wybierz **Nowa aplikacja Studio**.
2. W polu **Zacznij od** wybierz **Z galerii**.
3. Wybierz aplikację w polu **Aplikacja z galerii**. Jej opis pojawia się pod selektorem.
4. Nazwij aplikację, wybierz jej **Projekt** i wybierz **Utwórz**.

Możesz też wybrać **Galeria** na pasku narzędzi **Moje aplikacje Panel**, aby przeglądać samą galerię. Każda karta pokazuje nazwę, opis i projekt aplikacji oraz **Utwórz aplikację na tej podstawie…**. Galeria wymienia tylko aplikacje w projektach, które możesz wyświetlić.

Nowa aplikacja jest kopią plików wymienionej aplikacji. Twoja kopia i oryginał są oddzielne: zmiana jednej nigdy nie zmienia drugiej.

## Umieszczanie aplikacji na liście

Potrzebujesz dostępu do edycji projektu aplikacji. Na liście można umieścić tylko aplikacje utworzone w [Panel Studio](/pl/guides/panel-apps/studio/), które należą do projektu; aplikacje serwerowe, WASM i Dash nie mogą być wymienione.

1. Otwórz aplikację w Studio i wybierz **Galeria…**. Przycisk jest dostępny tylko dla aplikacji należącej do projektu.
2. Wpisz **Opis**, który ma być widoczny na karcie galerii.
3. Wybierz **Wyświetlaj w galerii** i potwierdź.

Aby zmienić opis, wybierz **Zaktualizuj wpis**. Aby usunąć aplikację z galerii, otwórz **Galeria…** i wybierz **Usuń z galerii**. Przeniesienie aplikacji do innego projektu również usuwa ją z galerii.

## Kto co widzi

Każdy, kto może wyświetlić projekt, może odczytać źródło wymienionej aplikacji, w tym zmiany, które opublikujesz później. Nie umieszczaj haseł ani prywatnych notatek w plikach wymienionej aplikacji. Wybranie umieszczenia aplikacji na liście najpierw prosi o potwierdzenie tego, a umieszczenie jest zapisywane w dzienniku inspekcji.

Osoby tworzące aplikację z galerii otrzymują kopię plików tylko z własnego folderu aplikacji. Nigdy nie widzą szczegółów repozytorium aplikacji, połączeń ani ustawień webhooków.

## Dalsze kroki

- [Panel Studio](/pl/guides/panel-apps/studio/) — edytuj i publikuj utworzoną kopię.
- [Zestaw Panel App Kit](/pl/guides/panel-apps/app-kit/) — komponenty, z których zbudowana jest większość aplikacji z galerii.
