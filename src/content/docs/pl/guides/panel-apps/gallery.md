---
title: Galeria aplikacji
description: Dodaj aplikację Studio do galerii lub usuń ją z galerii oraz utwórz nową aplikację na podstawie aplikacji z galerii.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/gallery.md
---

Galeria aplikacji to półka, którą twój obszar roboczy prowadzi dla gotowych aplikacji Panel. Każdy, kto może wyświetlić projekt wymienionej aplikacji, może utworzyć własną kopię w projekcie, który może edytować, i ją zmienić, dzięki czemu dobra aplikacja staje się punktem wyjścia, a nie czymś, co ludzie budują od nowa.

## Utwórz aplikację z galerii

1. W obszarze **Moje aplikacje Panel** wybierz **Nowa aplikacja Studio**.
2. W polu **Zacznij od** wybierz **Z galerii**.
3. Wybierz aplikację w polu **Aplikacja z galerii**. Jej opis jest widoczny pod selektorem.
4. Nazwij aplikację, wybierz jej **Projekt** i wybierz **Utwórz**.

Możesz też wybrać **Galeria** na pasku narzędzi **Moje aplikacje Panel**, aby przeglądać samą galerię. Wyświetla ona każdą aplikację z jej nazwą, projektem i opisem oraz przyciskiem **Utwórz aplikację na tej podstawie…**. Galeria wyświetla tylko aplikacje w projektach, które możesz wyświetlić.

Nowa aplikacja jest kopią plików wymienionej aplikacji. Twoja kopia i oryginał są niezależne: zmiana jednego nigdy nie zmienia drugiego.

## Dodaj swoją aplikację do galerii

Potrzebujesz dostępu do edycji projektu aplikacji. Do galerii można dodać tylko aplikacje utworzone w [Panel Studio](/pl/guides/panel-apps/studio/), które należą do projektu; aplikacje serwerowe, WASM i Dash nie mogą być dodane.

1. Otwórz aplikację w Studio i wybierz **Galeria…**. Przycisk jest dostępny tylko dla aplikacji, która należy do projektu.
2. Wpisz **Opis**, który ma być wyświetlany na karcie galerii.
3. Wybierz **Wyświetlaj w galerii** i potwierdź.

Aby zmienić opis, wybierz **Zaktualizuj wpis**. Aby usunąć aplikację z galerii, otwórz **Galeria…** i wybierz **Usuń z galerii**. Przeniesienie aplikacji do innego projektu również usuwa ją z galerii.

## Kto co widzi

Każdy, kto może wyświetlić projekt, może odczytać kod źródłowy wymienionej aplikacji, w tym zmiany opublikowane później. Nie umieszczaj haseł ani prywatnych notatek w plikach aplikacji dodanej do galerii. Wybór dodania aplikacji najpierw prosi o potwierdzenie tego, a dodanie jest zapisywane w dzienniku inspekcji.

Osoby tworzące aplikację z galerii otrzymują kopię plików tylko z własnego folderu aplikacji. Nigdy nie widzą szczegółów repozytorium aplikacji, połączeń ani ustawień webhooków.

## Następne kroki

- [Panel Studio](/pl/guides/panel-apps/studio/) — edytuj i opublikuj utworzoną kopię.
- [Zestaw narzędzi aplikacji Panel](/pl/guides/panel-apps/app-kit/) — komponenty, z których zbudowana jest większość aplikacji z galerii.
