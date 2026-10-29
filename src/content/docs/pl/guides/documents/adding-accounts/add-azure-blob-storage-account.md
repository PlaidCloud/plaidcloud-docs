---
title: Dodawanie konta Azure Blob Storage
description: Dodaj konto Azure Blob Storage do PlaidCloud, aby importować i eksportować pliki danych za pomocą magazynu obiektów w chmurze Microsoft Azure.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-azure-blob-storage-account.md
---

## Konfiguracja Azure Blob Storage

Poniższe kroki należy wykonać w portalu Azure.

1. Zaloguj się do [portalu Azure](https://portal.azure.com)
2. Przejdź do **Storage accounts** i wybierz lub utwórz konto magazynu
3. W lewym panelu bocznym w sekcji **Security + networking** wybierz **Access keys**
4. Skopiuj **Storage account name** i jedną z wartości **Key**. Zapisz obie na potrzeby konfiguracji PlaidCloud Document poniżej.
5. Przejdź do **Containers** w sekcji **Data storage** i utwórz kontener, jeśli jeszcze nie istnieje. Zanotuj nazwę kontenera.

Masz teraz wszystko, czego potrzebujesz, aby dodać konto Azure Blob Storage do PlaidCloud Document.


## Konfiguracja PlaidCloud Document

1. Zaloguj się do PlaidCloud
2. Wybierz obszar roboczy, w którym ma się znajdować nowe konto dokumentów
3. Przejdź do `Document > Manage Accounts`
4. Kliknij przycisk `+ New Account`
5. Wybierz `Azure Blob Storage` jako Typ usługi
6. Wpisz nazwę i opis
7. Wpisz nazwę kontenera i opcjonalny prefiks ścieżki w polu **Ścieżka początkowa** (np. `my-container/data`). Pierwszy segment ścieżki to nazwa kontenera.
8. Wybierz odpowiedni **Model zabezpieczeń** dla swojego przypadku użycia. Jeśli nie masz pewności, pozostaw `Private`.
9. Wklej **Storage account name** w polu Nazwa konta w sekcji Dane uwierzytelniające
10. Wklej **Key** w polu Klucz konta w sekcji Dane uwierzytelniające
11. Kliknij przycisk Zapisz, a nowe konto dokumentów będzie aktywne
