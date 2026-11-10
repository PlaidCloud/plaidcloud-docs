---
title: Dodawanie konta Backblaze B2
description: Dodaj konto magazynu Backblaze B2 do PlaidCloud, aby importować i eksportować pliki danych przy użyciu niedrogiego magazynu obiektów w chmurze.
sidebar:
  order: 8
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-backblaze-b2-account.md
---

## Konfiguracja Backblaze B2

Te czynności należy wykonać w konsoli Backblaze B2.

1. Zaloguj się do [konsoli Backblaze B2](https://secure.backblaze.com/b2_buckets.htm)
2. Przejdź do sekcji **Buckets** i utwórz zasobnik, jeśli jeszcze nie istnieje. Zanotuj nazwę zasobnika.
3. Przejdź do sekcji **App Keys**
4. Wybierz **Add a New Application Key**
5. Nadaj kluczowi nazwę, wybierz zasobnik, do którego ma mieć dostęp, i wybierz odpowiednie uprawnienia (odczyt i zapis)
6. Wybierz **Create New Key**
7. Skopiuj wartości **keyID** (to Twój klucz Access Key) i **applicationKey** (to Twój klucz Secret Key). Zachowaj obie do konfiguracji w PlaidCloud Document opisanej poniżej. Klucz aplikacji jest wyświetlany tylko raz.
8. Zanotuj **S3 Endpoint** dla regionu zasobnika. Ma on postać `https://s3.{region}.backblazeb2.com` (np. `https://s3.us-west-004.backblazeb2.com`). Można go znaleźć na stronie szczegółów zasobnika.

Masz teraz wszystko, czego potrzebujesz, aby dodać konto Backblaze B2 do modułu PlaidCloud Document.


## Konfiguracja PlaidCloud Document

1. Zaloguj się do PlaidCloud
2. Wybierz obszar roboczy, w którym ma się znaleźć nowe konto dokumentów
3. Przejdź do `Document > Manage`
4. Wybierz przycisk **Nowe konto**
5. Wybierz `Backblaze B2` jako typ usługi
6. Wpisz nazwę i opis
7. W polu **Ścieżka początkowa** wpisz punkt końcowy zgodny z S3, a po nim nazwę zasobnika: `https://s3.us-west-004.backblazeb2.com/my-bucket`
8. Wpisz **Region** zasobnika (np. `us-west-004`)
9. Wybierz odpowiedni **Model zabezpieczeń** dla danego zastosowania. W razie wątpliwości pozostaw wartość `Private`.
10. Wklej wartość **keyID** w polu ID klucza dostępu w sekcji Dane uwierzytelniające
11. Wklej wartość **applicationKey** w polu Tajny klucz dostępu w sekcji Dane uwierzytelniające
12. Wybierz przycisk Zapisz — nowe konto dokumentów jest aktywne
