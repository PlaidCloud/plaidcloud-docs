---
title: Tworzenie aplikacji Panel z Weave
description: Opisz aplikację, której potrzebujesz, pozwól Weave napisać ją w Panel Studio i zatwierdź dokładną zmianę, zanim cokolwiek zostanie zapisane.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/build-with-weave.md
---

Weave potrafi pisać i zmieniać aplikacje Panel za Ciebie. Działa w [Panel Studio](/pl/guides/panel-apps/studio/) na otwartej aplikacji, a nic z tego, co proponuje, nie zmienia aplikacji, dopóki tego nie zatwierdzisz.

## Zapytaj Weave

1. Otwórz aplikację w Panel Studio.
2. Wybierz **Ask Weave** i opisz, czego potrzebujesz, na przykład „Dodaj filtr regionu i wykres przychodów według miesięcy”.

Weave już zna aplikację, nad którą pracuje: jej pliki, stan kompilacji i ewentualne błędy kompilacji oraz tabelę lub widok, na których jest oparta. Nie musisz wklejać do rozmowy kodu ani błędów. Jeśli kompilacja się nie powiedzie, poproś Weave o jej naprawę.

## Zatwierdzanie zmiany

Gdy Weave chce zmienić kod aplikacji, pokazuje kartę zatwierdzenia z pełną różnicą: każdą dodawaną i usuwaną linią, plik po pliku.

1. Przeczytaj różnicę.
2. Wybierz **Zatwierdź**, aby zapisać zmianę w wersji roboczej aplikacji, lub **Odrzuć**, aby ją odrzucić.

Zatwierdzenie zapisuje wersję roboczą. Nie publikuje jej. Obejrzyj wynik w podglądzie, a gdy będziesz zadowolony, [opublikuj](/pl/guides/panel-apps/studio/#publikowanie) ją.

### Zatwierdzanie tylko w przeglądarce

Zmianę kodu możesz zatwierdzić tylko w PlaidCloud w przeglądarce. W aplikacji mobilnej PlaidCloud możesz odrzucić proponowaną zmianę kodu, ale nie możesz jej zatwierdzić. Inne zmiany Weave nadal można zatwierdzać na telefonie. Zobacz [Weave w aplikacji mobilnej](/pl/guides/mobile-app/weave-on-mobile/).

## Następne kroki

- [Panel Studio](/pl/guides/panel-apps/studio/) — zapis, podgląd i publikowanie.
- [Zestaw narzędzi aplikacji Panel](/pl/guides/panel-apps/app-kit/) — komponenty, z których korzysta Weave.
