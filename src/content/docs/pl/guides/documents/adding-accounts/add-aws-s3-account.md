---
title: Dodawanie konta AWS S3
description: Dodaj konto magazynu AWS S3 do PlaidCloud, aby importować i eksportować pliki danych przy użyciu magazynu obiektów w chmurze Amazon.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-aws-s3-account.md
---

## Konfiguracja AWS S3

Te czynności należy wykonać w konsoli AWS.

1. Zaloguj się do konta Amazon Web Services (AWS) lub je utwórz
2. Przejdź do `All services > Storage > S3` w konsoli
3. Utwórz domyślny lub testowy zasobnik. Zanotuj nazwę zasobnika i region (np. `us-east-1`).
4. Przejdź do `All Services > Security Identity & Compliance > IAM > Users` w konsoli
5. Wybierz przycisk `Create User`
6. Po wyświetleniu monitu wpisz nazwę użytkownika i zaznacz tylko opcję `Access Key - Programmatic access`. Wybierz przycisk `Next: Permissions`.
7. Zaznacz pole opcji o nazwie `Attach existing policies directly`
8. W polu wyszukiwania filtru wpisz `s3`. Gdy lista zostanie zawężona do elementów związanych z S3, wybierz `AmazonS3FullAccess`, zaznaczając pole wyboru po lewej stronie. Wybierz przycisk `Next: Tags`.
9. Pomiń ten krok, wybierając przycisk `Next: Review`
10. Przejrzyj ustawienia użytkownika i wybierz `Create user`
11. Zachowaj klucze wygenerowane dla użytkownika, pobierając plik CSV lub kopiując i wklejając klucze w inne miejsce do późniejszego użycia. Tego klucza nie będzie można pobrać ponownie, więc zachowaj go. Jeśli musisz ponownie wygenerować klucz, po prostu wróć do kroku 5 powyżej.

Masz teraz wszystko, czego potrzebujesz, aby dodać konto S3 do modułu PlaidCloud Document.


## Konfiguracja PlaidCloud Document

1. Zaloguj się do PlaidCloud
2. Wybierz obszar roboczy, w którym ma się znaleźć nowe konto dokumentów
3. Przejdź do `Document > Manage`
4. Wybierz przycisk **Nowe konto**
5. Wybierz `Amazon S3` jako typ usługi
6. Wpisz nazwę i opis
7. Wpisz nazwę zasobnika i opcjonalny prefiks ścieżki w polu **Ścieżka początkowa** (np. `my-bucket` lub `my-bucket/data`). Pierwszy segment ścieżki to nazwa zasobnika.
8. Wybierz odpowiedni **Model zabezpieczeń** dla danego zastosowania. W razie wątpliwości pozostaw wartość `Private`.
9. Wklej klucz **Access Key** utworzony w kroku 11 powyżej w polu ID klucza dostępu w sekcji Dane uwierzytelniające
10. Wklej klucz **Secret Key** utworzony w kroku 11 powyżej w polu Tajny klucz dostępu w sekcji Dane uwierzytelniające
11. Wpisz **Region** zasobnika (np. `us-east-1`, `eu-west-1`). Jeśli pole pozostanie puste, domyślnie używana jest wartość `us-east-2`.
12. Wybierz przycisk Zapisz — nowe konto dokumentów jest aktywne
