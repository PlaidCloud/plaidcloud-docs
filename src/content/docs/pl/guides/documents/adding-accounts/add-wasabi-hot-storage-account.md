---
title: Dodawanie konta Wasabi Hot Storage
description: Dodaj konto Wasabi Hot Storage do PlaidCloud, aby importować i eksportować pliki danych przy użyciu ekonomicznego magazynu w chmurze.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-wasabi-hot-storage-account.md
---

## Konfiguracja Wasabi Hot Storage


Te czynności należy wykonać w konsoli Wasabi Hot Storage


1. Zaloguj się do konta Wasabi Hot Storage lub je utwórz
2. Przejdź do sekcji `Buckets` w konsoli
3. Utwórz domyślny lub testowy zasobnik
4. Przejdź do sekcji Users w konsoli
5. Wybierz przycisk `Create User`
6. Po wyświetleniu monitu wpisz nazwę użytkownika i wybierz typ użytkownika `Programmatic (create API key)`
7. Pomiń przypisanie do grupy. Wybierz przycisk `Next`
8. Wybierz ikonę plusa obok zasady `WasabiFullAccess`, aby dołączyć zasadę do użytkownika. Wybierz przycisk `Next`.
9. Przejrzyj ustawienia użytkownika i wybierz `Create User`
10. Zachowaj klucze wygenerowane dla użytkownika, pobierając plik CSV lub kopiując i wklejając klucze w inne miejsce do późniejszego użycia. Tego klucza nie będzie można pobrać ponownie, więc zachowaj go. Jeśli musisz ponownie wygenerować klucz, po prostu wróć do kroku 5 powyżej.

Masz teraz wszystko, czego potrzebujesz, aby dodać konto Wasabi do modułu PlaidCloud Document.



## Konfiguracja w PlaidCloud Document

1. Zaloguj się do PlaidCloud
2. Wybierz obszar roboczy, w którym ma się znaleźć nowe konto dokumentów
3. Przejdź do `Document > Manage`
4. Wybierz przycisk **Nowe konto**
5. Wybierz `Wasabi Hot Storage` jako typ usługi
6. Wpisz nazwę i opis
7. Wpisz nazwę zasobnika i opcjonalny prefiks ścieżki w polu **Ścieżka początkowa** (np. `my-bucket` lub `my-bucket/data`). Pierwszy segment ścieżki to nazwa zasobnika.
8. Wybierz odpowiedni **Model zabezpieczeń** dla danego zastosowania. W razie wątpliwości pozostaw wartość `Private`.
9. Wklej klucz **Access Key** utworzony w kroku 10 powyżej w polu ID klucza dostępu w sekcji Dane uwierzytelniające
10. Wklej klucz **Secret Key** utworzony w kroku 10 powyżej w polu Tajny klucz dostępu w sekcji Dane uwierzytelniające
11. Wpisz **Region**, jeśli Twoje konto Wasabi korzysta z określonego regionu; w przeciwnym razie pozostaw pole puste
12. Wybierz przycisk Zapisz — nowe konto dokumentów jest aktywne
