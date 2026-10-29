---
title: Dodawanie konta Wasabi Hot Storage
description: Dodaj konto Wasabi Hot Storage do PlaidCloud, aby importować i eksportować pliki danych z użyciem ekonomicznego magazynu w chmurze.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-wasabi-hot-storage-account.md
---

## Konfiguracja Wasabi Hot Storage


Te czynności należy wykonać w konsoli Wasabi Hot Storage


1. Zaloguj się do konta Wasabi Hot Storage lub utwórz je
2. Przejdź do `Buckets` w konsoli
3. Utwórz domyślny lub testowy zasobnik
4. Przejdź do Users w konsoli
5. Wybierz przycisk `Create User`
6. Po wyświetleniu monitu wpisz nazwę użytkownika i wybierz użytkownika typu `Programmatic (create API key)`
7. Pomiń przypisanie do grupy. Wybierz przycisk `Next`
8. Wybierz ikonę plusa obok zasady `WasabiFullAccess`, aby dołączyć ją do użytkownika. Wybierz przycisk `Next`.
9. Przejrzyj ustawienia użytkownika i wybierz `Create User`
10. Zapisz klucze wygenerowane dla użytkownika, pobierając plik CSV lub kopiując klucze w miejsce, z którego skorzystasz później. Nie będzie można ponownie pobrać tego klucza, więc zadbaj o jego zachowanie. Jeśli musisz wygenerować klucz ponownie, wróć do kroku 5 powyżej.

Masz już wszystko, czego potrzeba do dodania konta Wasabi do PlaidCloud Document.



## Konfiguracja PlaidCloud Document

1. Zaloguj się do PlaidCloud
2. Wybierz obszar roboczy, w którym ma się znajdować nowe konto dokumentów
3. Przejdź do `Document > Manage Accounts`
4. Wybierz przycisk `+ New Account`
5. Wybierz `Wasabi Hot Storage` jako **Typ usługi**
6. Wpisz nazwę i opis
7. Wpisz nazwę zasobnika i opcjonalny prefiks ścieżki w polu **Ścieżka początkowa** (np. `my-bucket` lub `my-bucket/data`). Pierwszy segment ścieżki to nazwa zasobnika.
8. Wybierz **Model zabezpieczeń** odpowiedni do danego zastosowania. W razie wątpliwości pozostaw `Private`.
9. Wklej **Access Key** utworzony w kroku 10 powyżej w polu ID klucza dostępu w sekcji Dane uwierzytelniające
10. Wklej **Secret Key** utworzony w kroku 10 powyżej w polu Tajny klucz dostępu w sekcji Dane uwierzytelniające
11. Wpisz **Region**, jeśli Twoje konto Wasabi korzysta z określonego regionu; w przeciwnym razie pozostaw puste
12. Wybierz przycisk Zapisz, a nowe konto dokumentów zacznie działać
