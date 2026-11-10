---
title: Dodawanie konta MinIO
description: Dodaj konto magazynu MinIO do PlaidCloud, aby importować i eksportować pliki danych przy użyciu samodzielnie hostowanego magazynu obiektów zgodnego z S3.
sidebar:
  order: 7
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-minio-account.md
---

## Konfiguracja MinIO

Te czynności należy wykonać w konsoli MinIO lub za pomocą interfejsu wiersza poleceń `mc`.

1. Zaloguj się do konsoli MinIO (np. `https://your-minio-host:9001`)
2. Przejdź do sekcji **Buckets** i utwórz zasobnik, jeśli jeszcze nie istnieje. Zanotuj nazwę zasobnika.
3. Przejdź do **Identity > Users** (lub **Access Keys**)
4. Utwórz nowego użytkownika lub konto usługi z dostępem do odczytu i zapisu w zasobniku docelowym
5. Skopiuj wartości **Access Key** i **Secret Key** wygenerowane dla użytkownika. Zachowaj obie do konfiguracji w PlaidCloud Document opisanej poniżej.
6. Zanotuj adres URL punktu końcowego MinIO (np. `https://play.min.io` lub `https://minio.yourcompany.com`)

Masz teraz wszystko, czego potrzebujesz, aby dodać konto MinIO do modułu PlaidCloud Document.


## Konfiguracja PlaidCloud Document

1. Zaloguj się do PlaidCloud
2. Wybierz obszar roboczy, w którym ma się znaleźć nowe konto dokumentów
3. Przejdź do `Document > Manage`
4. Wybierz przycisk **Nowe konto**
5. Wybierz `MinIO` jako typ usługi
6. Wpisz nazwę i opis
7. W polu **Ścieżka początkowa** wpisz adres URL punktu końcowego MinIO, a po nim nazwę zasobnika i opcjonalny prefiks: `https://minio.yourcompany.com/my-bucket/optional/prefix`
8. Wpisz **Region**, jeśli wdrożenie MinIO korzysta z regionów; w przeciwnym razie pozostaw pole puste
9. Wybierz odpowiedni **Model zabezpieczeń** dla danego zastosowania. W razie wątpliwości pozostaw wartość `Private`.
10. Wklej wartość **Access Key** w polu ID klucza dostępu w sekcji Dane uwierzytelniające
11. Wklej wartość **Secret Key** w polu Tajny klucz dostępu w sekcji Dane uwierzytelniające
12. Wybierz przycisk Zapisz — nowe konto dokumentów jest aktywne
