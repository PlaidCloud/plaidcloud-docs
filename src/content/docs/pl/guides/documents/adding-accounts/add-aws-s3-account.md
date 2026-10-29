---
title: Dodawanie konta AWS S3
description: Dodaj konto magazynu AWS S3 do PlaidCloud, aby importować i eksportować pliki danych za pomocą magazynu obiektów w chmurze Amazon.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-aws-s3-account.md
---

## Konfiguracja AWS S3

Poniższe kroki należy wykonać w konsoli AWS.

1. Zaloguj się na konto Amazon Web Services (AWS) lub je utwórz
2. W konsoli przejdź do `All services > Storage > S3`
3. Utwórz domyślny lub testowy zasobnik. Zanotuj nazwę zasobnika i region (np. `us-east-1`).
4. W konsoli przejdź do `All Services > Security Identity & Compliance > IAM > Users`
5. Kliknij przycisk `Create User`
6. Po wyświetleniu monitu wpisz nazwę użytkownika i wybierz wyłącznie `Access Key - Programmatic access`. Kliknij przycisk `Next: Permissions`.
7. Zaznacz opcję `Attach existing policies directly`
8. W polu wyszukiwania filtra wpisz `s3`. Gdy lista zawęzi się do pozycji związanych z S3, zaznacz `AmazonS3FullAccess`, wybierając pole po lewej stronie. Kliknij przycisk `Next: Tags`.
9. Pomiń ten krok, klikając przycisk `Next: Review`
10. Przejrzyj ustawienia użytkownika i kliknij `Create user`
11. Zachowaj wygenerowane dla użytkownika klucze, pobierając plik CSV lub kopiując je w inne miejsce do późniejszego użycia. Nie będzie można ponownie pobrać tego klucza, więc zadbaj o jego zachowanie. Jeśli musisz ponownie wygenerować klucz, wróć do kroku 5 powyżej.

Masz teraz wszystko, czego potrzebujesz, aby dodać konto S3 do PlaidCloud Document.


## Konfiguracja PlaidCloud Document

1. Zaloguj się do PlaidCloud
2. Wybierz obszar roboczy, w którym ma się znajdować nowe konto dokumentów
3. Przejdź do `Document > Manage Accounts`
4. Kliknij przycisk `+ New Account`
5. Wybierz `Amazon S3` jako Typ usługi
6. Wpisz nazwę i opis
7. Wpisz nazwę zasobnika i opcjonalny prefiks ścieżki w polu **Ścieżka początkowa** (np. `my-bucket` lub `my-bucket/data`). Pierwszy segment ścieżki to nazwa zasobnika.
8. Wybierz odpowiedni **Model zabezpieczeń** dla swojego przypadku użycia. Jeśli nie masz pewności, pozostaw `Private`.
9. Wklej **Access Key** utworzony w kroku 11 powyżej w polu ID klucza dostępu w sekcji Dane uwierzytelniające
10. Wklej **Secret Key** utworzony w kroku 11 powyżej w polu Tajny klucz dostępu w sekcji Dane uwierzytelniające
11. Wpisz **Region** swojego zasobnika (np. `us-east-1`, `eu-west-1`). Jeśli pole pozostanie puste, domyślnie używany jest `us-east-2`.
12. Kliknij przycisk Zapisz, a nowe konto dokumentów będzie aktywne
