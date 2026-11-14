---
title: Galeria aplikacji
description: Dodaj aplikację Studio do galerii lub usuń ją z niej oraz utwórz nową aplikację na podstawie wystawionej.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/gallery.md
---

Galeria aplikacji to półka, na której Twój obszar roboczy przechowuje gotowe aplikacje Panel. Każdy, kto może wyświetlać projekt wystawionej aplikacji, może utworzyć własną kopię w projekcie, który może edytować, i ją zmieniać, dzięki czemu dobra aplikacja staje się punktem wyjścia, zamiast być budowana od nowa.

## Tworzenie aplikacji z galerii

1. W **Aplikacje** wybierz **Nowa aplikacja** > **Studio**.
2. W polu **Zacznij od** wybierz **Z galerii**.
3. Wybierz aplikację w polu **Aplikacja z galerii**. Jej opis jest wyświetlany pod selektorem.
4. Nadaj aplikacji nazwę, wybierz jej **Projekt** i wybierz **Utwórz**.

Możesz też wybrać **Nowa aplikacja** > **Z galerii…**, aby przeglądać samą galerię. Wyświetla każdą aplikację z jej nazwą, projektem i opisem oraz przyciskiem **Utwórz aplikację na tej podstawie…**. Galeria wyświetla tylko aplikacje w projektach, które możesz wyświetlać.

Nowa aplikacja jest kopią plików wystawionej aplikacji. Twoja kopia i oryginał są odrębne: zmiana jednej nigdy nie zmienia drugiej.

## Wystawianie aplikacji

Potrzebujesz dostępu do edycji projektu aplikacji. Wystawić można tylko aplikacje utworzone w [Panel Studio](/pl/guides/panel-apps/studio/), które należą do projektu; aplikacji serwerowych, WASM i Dash nie można.

1. Otwórz aplikację w Studio i wybierz **Galeria…**. Przycisk jest dostępny tylko dla aplikacji, która należy do projektu.
2. Wprowadź **Opis**, który ma być wyświetlany na karcie galerii.
3. Wybierz **Wyświetlaj w galerii** i potwierdź.

Aby zmienić opis, wybierz **Zaktualizuj wpis**. Aby usunąć aplikację z galerii, otwórz **Galeria…** i wybierz **Usuń z galerii**. Przeniesienie aplikacji do innego projektu również usuwa ją z galerii.

## Kto co widzi

Każdy, kto może wyświetlać projekt, może odczytać kod źródłowy wystawionej aplikacji, w tym zmiany publikowane później. Nie umieszczaj haseł ani prywatnych notatek w plikach wystawionej aplikacji. Wybranie wystawienia aplikacji najpierw prosi o potwierdzenie tego, a wystawienie jest rejestrowane w dzienniku audytu.

Osoby tworzące z galerii otrzymują kopię plików tylko z własnego folderu aplikacji. Nigdy nie widzą szczegółów repozytorium aplikacji, połączeń ani ustawień webhooków.

## Następne kroki

- [Panel Studio](/pl/guides/panel-apps/studio/) — edytuj i publikuj utworzoną kopię.
- [Zestaw Panel App Kit](/pl/guides/panel-apps/app-kit/) — komponenty, z których zbudowana jest większość aplikacji z galerii.
