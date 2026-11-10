---
title: Dodawanie konta zasobnika zarządzanego przez PlaidCloud
description: Dodaj w pełni zarządzany magazyn plików do modułu PlaidCloud Document w jednym kroku — wybierz nazwę, a PlaidCloud skonfiguruje wszystko za Ciebie, bez żadnej konfiguracji z Twojej strony.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-managed-bucket-account.md
---

**Zasobnik zarządzany przez PlaidCloud** to najszybszy sposób na dodanie magazynu plików do modułu Document. PlaidCloud tworzy magazyn i nim zarządza — nie trzeba niczego wcześniej konfigurować ani zarządzać poświadczeniami. Wystarczy nadać mu nazwę.

Użyj zasobnika zarządzanego przez PlaidCloud, gdy potrzebujesz nowego, samodzielnego miejsca do przechowywania plików modułu Document. Aby połączyć magazyn, który już posiadasz i którym zarządzasz samodzielnie, wybierz zamiast tego jednego z pozostałych dostawców na stronie [Dodawanie nowych kont dokumentów](/pl/guides/documents/adding-accounts/).

## Konfiguracja

1. Zaloguj się do PlaidCloud
2. Wybierz obszar roboczy, w którym ma się znaleźć nowe konto dokumentów
3. Przejdź do `Document > Manage`
4. Wybierz przycisk **Nowe konto**
5. Wybierz `PlaidCloud Managed Bucket` jako typ usługi
6. Wpisz nazwę i opcjonalny opis
7. Wpisz **Nazwa zasobnika**. Nazwa musi mieć od 3 do 63 znaków, zawierać tylko małe litery, cyfry, kropki lub łączniki oraz zaczynać się i kończyć literą lub cyfrą. Nazwa musi być **globalnie unikatowa** — jeśli jest już używana, pojawi się prośba o wybranie innej
8. Wybierz odpowiedni **Model zabezpieczeń** dla danego zastosowania. W razie wątpliwości pozostaw wartość `Private`
9. Wybierz przycisk Zapisz

PlaidCloud konfiguruje magazyn i ustawia Cię jako jego właściciela. Konto jest od razu gotowe do przeglądania i przesyłania plików — nie trzeba niczego więcej konfigurować.

:::note
Zasobniki zarządzane przez PlaidCloud są dostępne w planach **Business** i **Enterprise**. Jeśli Twój plan ich nie obejmuje lub osiągnięto limit planu, formularz poinformuje o tym przy próbie utworzenia zasobnika.
:::

## Po utworzeniu

- Nazwa zasobnika jest stała po jego utworzeniu — nie można jej zmienić w istniejącym koncie.
- Usunięcie konta **pozostawia przechowywane pliki na miejscu**, więc usunięcie nigdy nie niszczy danych. Jeśli chcesz usunąć sam magazyn, skontaktuj się z pomocą techniczną.
- Zasobnik zarządzany przez PlaidCloud działa jak każde inne konto dokumentów w zakresie [kontroli dostępu](/pl/guides/documents/account-management/control-document-account-access/), [własności](/pl/guides/documents/account-management/managing-document-account-owners/) i przeglądania.
