---
title: Dodawanie konta Cloudflare R2
description: Dodaj konto magazynu Cloudflare R2 do PlaidCloud, aby importować i eksportować pliki danych przy użyciu magazynu obiektów Cloudflare bez opłat za transfer wychodzący.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-cloudflare-r2-account.md
---

## Konfiguracja Cloudflare R2

Te czynności należy wykonać w panelu Cloudflare.

1. Zaloguj się do [panelu Cloudflare](https://dash.cloudflare.com)
2. Wybierz swoje konto, a następnie przejdź do sekcji **R2 Object Storage** na pasku bocznym po lewej stronie
3. Utwórz zasobnik, jeśli jeszcze nie istnieje. Zanotuj nazwę zasobnika.
4. Przejdź do **R2 Object Storage > Manage R2 API Tokens**
5. Wybierz **Create API Token**
6. Nadaj tokenowi nazwę, wybierz zasobniki, do których ma mieć dostęp, i wybierz uprawnienia **Object Read & Write**
7. Wybierz **Create API Token**
8. Skopiuj wartości **Access Key ID** i **Secret Access Key**. Zachowaj obie do konfiguracji w PlaidCloud Document opisanej poniżej. Klucz tajny jest wyświetlany tylko raz.
9. Zanotuj **S3 API endpoint** swojego konta. Ma on postać `https://{account_id}.r2.cloudflarestorage.com` i jest wyświetlany na stronie przeglądu R2.

Masz teraz wszystko, czego potrzebujesz, aby dodać konto Cloudflare R2 do modułu PlaidCloud Document.


## Konfiguracja w PlaidCloud Document

1. Zaloguj się do PlaidCloud
2. Wybierz obszar roboczy, w którym ma się znaleźć nowe konto dokumentów
3. Przejdź do `Document > Manage`
4. Wybierz przycisk **Nowe konto**
5. Wybierz `Cloudflare R2` jako typ usługi
6. Wpisz nazwę i opis
7. W polu **Ścieżka początkowa** wpisz punkt końcowy R2, a po nim nazwę zasobnika: `https://{account_id}.r2.cloudflarestorage.com/my-bucket`
8. W polu **Region** można ustawić wartość `auto` lub pozostawić je puste — R2 automatycznie wybiera najbliższy region
9. Wybierz odpowiedni **Model zabezpieczeń** dla danego zastosowania. W razie wątpliwości pozostaw wartość `Private`.
10. Wklej wartość **Access Key ID** w polu ID klucza dostępu w sekcji Dane uwierzytelniające
11. Wklej wartość **Secret Access Key** w polu Tajny klucz dostępu w sekcji Dane uwierzytelniające
12. Wybierz przycisk Zapisz — nowe konto dokumentów jest aktywne
