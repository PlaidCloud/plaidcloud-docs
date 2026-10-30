---
title: Dodawanie konta MinIO
description: Dodaj konto magazynu MinIO do PlaidCloud, aby importować i eksportować pliki danych z użyciem samodzielnie hostowanego magazynu obiektów zgodnego z S3.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-minio-account.md
---

## Konfiguracja MinIO

Te czynności należy wykonać w konsoli MinIO Console lub za pomocą interfejsu CLI `mc`.

1. Zaloguj się do konsoli MinIO Console (np. `https://your-minio-host:9001`)
2. Przejdź do **Buckets** i utwórz zasobnik, jeśli jeszcze nie istnieje. Zanotuj nazwę zasobnika.
3. Przejdź do **Identity > Users** (lub **Access Keys**)
4. Utwórz nowego użytkownika lub konto usługi z uprawnieniami do odczytu i zapisu w docelowym zasobniku
5. Skopiuj **Access Key** i **Secret Key** wygenerowane dla użytkownika. Zapisz oba, ponieważ będą potrzebne w poniższej konfiguracji PlaidCloud Document.
6. Zanotuj adres URL punktu końcowego MinIO (np. `https://play.min.io` lub `https://minio.yourcompany.com`)

Masz już wszystko, czego potrzeba do dodania konta MinIO do PlaidCloud Document.


## Konfiguracja PlaidCloud Document

1. Zaloguj się do PlaidCloud
2. Wybierz obszar roboczy, w którym ma się znajdować nowe konto dokumentów
3. Przejdź do `Document > Manage Accounts`
4. Wybierz przycisk `+ New Account`
5. Wybierz `MinIO` jako **Typ usługi**
6. Wpisz nazwę i opis
7. Wpisz **Ścieżkę początkową** jako adres URL punktu końcowego MinIO, a po nim nazwę zasobnika i opcjonalny prefiks: `https://minio.yourcompany.com/my-bucket/optional/prefix`
8. Wpisz **Region**, jeśli wdrożenie MinIO korzysta z regionów; w przeciwnym razie pozostaw puste
9. Wybierz **Model zabezpieczeń** odpowiedni do danego zastosowania. W razie wątpliwości pozostaw `Private`.
10. Wklej **Access Key** w polu ID klucza dostępu w sekcji Dane uwierzytelniające
11. Wklej **Secret Key** w polu Tajny klucz dostępu w sekcji Dane uwierzytelniające
12. Wybierz przycisk Zapisz, a nowe konto dokumentów zacznie działać
