---
title: Dodawanie konta zasobnika zarządzanego przez PlaidCloud
description: Dodaj w pełni zarządzany magazyn plików do PlaidCloud Document jednym krokiem — wybierz nazwę, a PlaidCloud skonfiguruje wszystko za Ciebie, bez konieczności konfigurowania czegokolwiek.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-managed-bucket-account.md
---

**Zasobnik zarządzany przez PlaidCloud** to najszybszy sposób dodania magazynu plików do Document. PlaidCloud tworzy magazyn i nim zarządza — nie trzeba nic wcześniej konfigurować ani zarządzać żadnymi danymi uwierzytelniającymi. Wystarczy podać nazwę.

Użyj zasobnika zarządzanego przez PlaidCloud, gdy chcesz mieć nowe, samodzielne miejsce na pliki Document. Aby połączyć magazyn, którym już dysponujesz i którym samodzielnie zarządzasz, wybierz zamiast tego jednego z pozostałych dostawców ze strony [Dodawanie nowych kont dokumentów](/pl/guides/documents/adding-accounts/).

## Konfiguracja

1. Zaloguj się do PlaidCloud
2. Wybierz obszar roboczy, w którym ma się znajdować nowe konto dokumentów
3. Przejdź do `Document > Manage Accounts`
4. Kliknij przycisk `+ New Account`
5. Wybierz `PlaidCloud Managed Bucket` jako Typ usługi
6. Wpisz nazwę i opcjonalny opis
7. Wpisz **Nazwę zasobnika**. Nazwy muszą mieć od 3 do 63 znaków, zawierać wyłącznie małe litery, cyfry, kropki lub łączniki oraz zaczynać się i kończyć literą lub cyfrą. Nazwa musi być **globalnie unikatowa** — jeśli jest już używana, pojawi się prośba o wybranie innej
8. Wybierz odpowiedni **Model zabezpieczeń** dla swojego przypadku użycia. Jeśli nie masz pewności, pozostaw `Private`
9. Kliknij przycisk Zapisz

PlaidCloud konfiguruje magazyn i ustawia Cię jako jego właściciela. Konto jest od razu gotowe do przeglądania i przesyłania plików — nie trzeba nic więcej konfigurować.

:::note
Zasobniki zarządzane przez PlaidCloud są dostępne w planach **Business** i **Enterprise**. Jeśli Twój plan ich nie obejmuje lub osiągnięto limit planu, formularz poinformuje o tym podczas próby utworzenia zasobnika.
:::

## Po utworzeniu

- Nazwa zasobnika jest stała po utworzeniu — nie można jej zmienić na istniejącym koncie.
- Usunięcie konta **pozostawia przechowywane pliki na miejscu**, więc usunięcie nigdy nie niszczy Twoich danych. Skontaktuj się z pomocą techniczną, jeśli chcesz usunąć sam magazyn.
- Zasobnik zarządzany przez PlaidCloud zachowuje się jak każde inne konto dokumentów pod względem [kontroli dostępu](/pl/guides/documents/account-management/control-document-account-access/), [własności](/pl/guides/documents/account-management/managing-document-account-owners/) i przeglądania.
