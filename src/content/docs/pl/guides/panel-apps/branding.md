---
title: Branding projektu i projekty aplikacji
description: Ustaw kolory marki i logo raz dla projektu, aby wszystkie aplikacje Panel w nim były spójne, oraz przypisuj aplikacje Panel do projektu podczas publikowania lub później.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/panel-apps/branding.md
---

Aplikacja Panel należy do projektu. Projekt pełni dla aplikacji dwie funkcje: z niego aplikacja domyślnie odczytuje swoje tabele oraz przechowuje on kolory i logo, które aplikacja nosi. Ustaw branding raz, a każda aplikacja w projekcie go przejmie.

## Nadawanie projektowi brandingu

1. Otwórz projekt i przejdź do jego karty **Strona główna**.
2. W grupie **Panel App Branding** kliknij **Edit Branding**.
3. Ustaw dowolne kolory. Kliknij próbkę, aby wybrać kolor, lub wpisz wartość szesnastkową, na przykład `#0078d4`.
4. Opcjonalnie wybierz logo.
5. Sprawdź **Podgląd**, a następnie kliknij **Zapisz**.

Tylko Menedżerowie i Architekci mogą zapisać branding. Pozostali członkowie projektu widzą formularz tylko do odczytu.

**Reset to default** czyści wszystkie kolory i logo. Zapis zastępuje całą markę, więc kolor pozostawiony pusty wraca do domyślnego koloru PlaidCloud.

### Kolory

| Ustawienie | Co koloruje |
|---|---|
| **Brand** | Przyciski, aktywną kartę, uchwyty suwaków i inne podstawowe kontrolki. |
| **Brand accent** | Akcenty drugorzędne. |
| **Brand hover** | Podstawową kontrolkę, gdy wskaźnik znajduje się nad nią. |
| **Brand pressed** | Podstawową kontrolkę, gdy jest wciśnięta. |
| **Header background** | Pasek nagłówka aplikacji. |
| **Header text** | Tytuł i nazwę użytkownika w nagłówku. |
| **Link** | Łącza. |
| **Text on brand** | Tekst znajdujący się na kontrolce w kolorze marki. |

To jedyne osiem ustawień. Kolory muszą być 3- lub 6-cyfrowymi wartościami szesnastkowymi. Powierzchnie, tekst podstawowy i obramowania zachowują wygląd PlaidCloud w trybie jasnym i ciemnym, więc marka nie może sprawić, że aplikacja stanie się nieczytelna.

### Logo

Logo to obraz z [konta dokumentów](/pl/guides/documents/) w obszarze roboczym projektu.

1. Prześlij obraz do folderu o nazwie `branding` na najwyższym poziomie konta dokumentów.
2. W **Edit Branding** wybierz **Konto dokumentów**, a następnie obraz w polu **Image in the branding/ folder**.

Logo może być plikiem PNG, JPEG, GIF, WebP lub SVG o rozmiarze do 512 KB. Pojawia się po prawej stronie nagłówka aplikacji. Obraz musi znajdować się bezpośrednio w `branding/` lub w folderze w nim, a każdy, kto zapisuje branding, musi mieć możliwość odczytu konta.

### Kiedy zmiany są widoczne

Aplikacja odczytuje swój branding, gdy rozpoczyna się sesja przeglądającego. Zapisane zmiany są widoczne przy następnym otwarciu lub ponownym wczytaniu aplikacji.

## Przypisywanie aplikacji do projektu

### Podczas publikowania

Okno **Opublikuj serwerową aplikację Panel** ma selektor **Projekt** w sekcji **Ustawienia katalogu**. Wybierz projekt, do którego należy aplikacja. Aby opublikować aplikację w projekcie, musisz mieć do niego dostęp. Po opublikowaniu aplikacji projekt jest ustalony; aby przenieść aplikację, użyj **Przypisz**, jak opisano poniżej.

Aplikacja opublikowana z projektem domyślnie odczytuje tabele tego projektu, więc `table("sales")` nie wymaga argumentu projektu.

### Dla istniejących aplikacji

1. Otwórz **Moje aplikacje Panel**.
2. Kliknij ikonę **Przypisz** w wierszu aplikacji, którą chcesz przenieść.
3. Wybierz **Projekt** i kliknij **Przegląd**.
4. Przeczytaj wynik. Wymienia on członków obszaru roboczego, którzy mogą dziś otworzyć aplikację, ale nie są członkami projektu.
5. Kliknij **Przypisz**.

Przegląd niczego nie zmienia. Kolumna **Projekt** w **Moje aplikacje Panel** pokazuje projekt każdej aplikacji.

### Dostęp

Obecnie projekt nie zmienia tego, kto może otworzyć aplikację: przeglądający, którzy mogli ją otworzyć wcześniej, nadal mogą. Z czasem dostęp do aplikacji będzie wynikał z członkostwa w jej projekcie, dlatego **Przegląd** wymienia członków spoza projektu, abyś mógł najpierw ich dodać.

## Następne kroki

- [Zestaw narzędzi aplikacji Panel](/pl/guides/panel-apps/app-kit/) — komponenty, które korzystają z Twojego brandingu.
- [Tworzenie aplikacji Panel](/pl/guides/panel-apps/creating/) — opublikuj aplikację w projekcie.
