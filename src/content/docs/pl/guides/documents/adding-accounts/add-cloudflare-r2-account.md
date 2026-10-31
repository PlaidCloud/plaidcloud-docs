---
title: Dodawanie konta Cloudflare R2
description: Dodaj konto magazynu Cloudflare R2 do PlaidCloud, aby importować i eksportować pliki danych za pomocą magazynu obiektów Cloudflare bez opłat za transfer wychodzący.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-cloudflare-r2-account.md
---

## Konfiguracja Cloudflare R2

Poniższe kroki należy wykonać w panelu Cloudflare.

1. Zaloguj się do [panelu Cloudflare](https://dash.cloudflare.com)
2. Wybierz swoje konto, a następnie przejdź do **R2 Object Storage** w lewym panelu bocznym
3. Utwórz zasobnik, jeśli jeszcze nie istnieje. Zanotuj nazwę zasobnika.
4. Przejdź do **R2 Object Storage > Manage R2 API Tokens**
5. Kliknij **Create API Token**
6. Nadaj tokenowi nazwę, wybierz zasobniki, do których ma mieć dostęp, i wybierz uprawnienia **Object Read & Write**
7. Kliknij **Create API Token**
8. Skopiuj **Access Key ID** i **Secret Access Key**. Zapisz oba na potrzeby konfiguracji PlaidCloud Document poniżej. Klucz tajny jest wyświetlany tylko raz.
9. Zanotuj **S3 API endpoint** swojego konta. Ma on postać `https://{account_id}.r2.cloudflarestorage.com` i jest wyświetlany na stronie przeglądu R2.

Masz teraz wszystko, czego potrzebujesz, aby dodać konto Cloudflare R2 do PlaidCloud Document.


## Konfiguracja PlaidCloud Document

1. Zaloguj się do PlaidCloud
2. Wybierz obszar roboczy, w którym ma się znajdować nowe konto dokumentów
3. Przejdź do `Document > Manage Accounts`
4. Kliknij przycisk `+ New Account`
5. Wybierz `Cloudflare R2` jako Typ usługi
6. Wpisz nazwę i opis
7. Wpisz **Ścieżkę początkową** jako punkt końcowy R2, po którym następuje nazwa zasobnika: `https://{account_id}.r2.cloudflarestorage.com/my-bucket`
8. Pole **Region** można ustawić na `auto` lub pozostawić puste — R2 automatycznie wybiera najbliższy region
9. Wybierz odpowiedni **Model zabezpieczeń** dla swojego przypadku użycia. Jeśli nie masz pewności, pozostaw `Private`.
10. Wklej **Access Key ID** w polu ID klucza dostępu w sekcji Dane uwierzytelniające
11. Wklej **Secret Access Key** w polu Tajny klucz dostępu w sekcji Dane uwierzytelniające
12. Kliknij przycisk Zapisz, a nowe konto dokumentów będzie aktywne
