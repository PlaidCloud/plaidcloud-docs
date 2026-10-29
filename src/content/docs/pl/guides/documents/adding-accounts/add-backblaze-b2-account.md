---
title: Dodawanie konta Backblaze B2
description: Dodaj konto magazynu Backblaze B2 do PlaidCloud, aby importować i eksportować pliki danych za pomocą niedrogiego magazynu obiektów w chmurze.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-backblaze-b2-account.md
---

## Konfiguracja Backblaze B2

Poniższe kroki należy wykonać w konsoli Backblaze B2.

1. Zaloguj się do [konsoli Backblaze B2](https://secure.backblaze.com/b2_buckets.htm)
2. Przejdź do **Buckets** i utwórz zasobnik, jeśli jeszcze nie istnieje. Zanotuj nazwę zasobnika.
3. Przejdź do **App Keys**
4. Kliknij **Add a New Application Key**
5. Nadaj kluczowi nazwę, wybierz zasobnik, do którego ma mieć dostęp, i wybierz odpowiednie uprawnienia (odczyt i zapis)
6. Kliknij **Create New Key**
7. Skopiuj **keyID** (to Twój Access Key) i **applicationKey** (to Twój Secret Key). Zapisz oba na potrzeby konfiguracji PlaidCloud Document poniżej. Klucz aplikacji jest wyświetlany tylko raz.
8. Zanotuj **S3 Endpoint** dla regionu swojego zasobnika. Ma on postać `https://s3.{region}.backblazeb2.com` (np. `https://s3.us-west-004.backblazeb2.com`). Można go znaleźć na stronie szczegółów zasobnika.

Masz teraz wszystko, czego potrzebujesz, aby dodać konto Backblaze B2 do PlaidCloud Document.


## Konfiguracja PlaidCloud Document

1. Zaloguj się do PlaidCloud
2. Wybierz obszar roboczy, w którym ma się znajdować nowe konto dokumentów
3. Przejdź do `Document > Manage Accounts`
4. Kliknij przycisk `+ New Account`
5. Wybierz `Backblaze B2` jako Typ usługi
6. Wpisz nazwę i opis
7. Wpisz **Ścieżkę początkową** jako punkt końcowy zgodny z S3, po którym następuje nazwa zasobnika: `https://s3.us-west-004.backblazeb2.com/my-bucket`
8. Wpisz **Region** swojego zasobnika (np. `us-west-004`)
9. Wybierz odpowiedni **Model zabezpieczeń** dla swojego przypadku użycia. Jeśli nie masz pewności, pozostaw `Private`.
10. Wklej **keyID** w polu ID klucza dostępu w sekcji Dane uwierzytelniające
11. Wklej **applicationKey** w polu Tajny klucz dostępu w sekcji Dane uwierzytelniające
12. Kliknij przycisk Zapisz, a nowe konto dokumentów będzie aktywne
