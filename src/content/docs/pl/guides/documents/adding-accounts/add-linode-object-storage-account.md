---
title: Dodawanie konta Linode Object Storage
description: Dodaj konto Linode (Akamai) Object Storage do PlaidCloud, aby importować i eksportować pliki danych za pomocą magazynu w chmurze Linode zgodnego z S3.
sidebar:
  order: 11
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-linode-object-storage-account.md
---

## Konfiguracja Linode Object Storage

Poniższe kroki należy wykonać w Linode Cloud Manager.

1. Zaloguj się do [Linode Cloud Manager](https://cloud.linode.com)
2. Przejdź do **Object Storage** w lewym panelu bocznym
3. Utwórz zasobnik, jeśli jeszcze nie istnieje. Zanotuj nazwę zasobnika (nazywaną **label**) i region (np. `us-east-1`).
4. Przejdź do **Object Storage > Access Keys**
5. Kliknij **Create Access Key**
6. Nadaj kluczowi etykietę i wybierz zasobniki, do których ma mieć dostęp, z uprawnieniami do odczytu i zapisu
7. Kliknij **Create Access Key**
8. Skopiuj **Access Key** i **Secret Key**. Zapisz oba na potrzeby konfiguracji PlaidCloud Document poniżej. Klucz tajny jest wyświetlany tylko raz.
9. Zanotuj adres URL punktu końcowego dla regionu swojego zasobnika. Ma on postać `https://{region}.linodeobjects.com` (np. `https://us-east-1.linodeobjects.com`)

Masz teraz wszystko, czego potrzebujesz, aby dodać konto Linode Object Storage do PlaidCloud Document.


## Konfiguracja PlaidCloud Document

1. Zaloguj się do PlaidCloud
2. Wybierz obszar roboczy, w którym ma się znajdować nowe konto dokumentów
3. Przejdź do `Document > Manage Accounts`
4. Kliknij przycisk `+ New Account`
5. Wybierz `Linode Object Storage` jako Typ usługi
6. Wpisz nazwę i opis
7. Wpisz **Ścieżkę początkową** jako adres URL punktu końcowego, po którym następuje nazwa zasobnika: `https://us-east-1.linodeobjects.com/my-bucket`
8. Wpisz **Region** (np. `us-east-1`)
9. Wybierz odpowiedni **Model zabezpieczeń** dla swojego przypadku użycia. Jeśli nie masz pewności, pozostaw `Private`.
10. Wklej **Access Key** w polu ID klucza dostępu w sekcji Dane uwierzytelniające
11. Wklej **Secret Key** w polu Tajny klucz dostępu w sekcji Dane uwierzytelniające
12. Kliknij przycisk Zapisz, a nowe konto dokumentów będzie aktywne
