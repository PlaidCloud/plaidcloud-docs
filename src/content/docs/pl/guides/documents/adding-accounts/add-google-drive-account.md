---
title: Dodawanie konta Google Drive
description: Dodaj konto magazynu Google Drive do PlaidCloud, aby importować i eksportować pliki danych przy użyciu magazynu w chmurze Google Drive.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-google-drive-account.md
---

## Konfiguracja Google Drive

Te czynności należy wykonać w konsoli Google Cloud, aby utworzyć konto usługi, którego PlaidCloud może używać do uzyskiwania dostępu do Google Drive.

### Tworzenie projektu Google Cloud

1. Zaloguj się do [konsoli Google Cloud](https://console.cloud.google.com)
2. Utwórz nowy projekt lub wybierz istniejący

### Włączanie interfejsu Google Drive API

1. Przejdź do **APIs & Services > Library**
2. Wyszukaj **Google Drive API**
3. Wybierz go i kliknij **Enable**

### Tworzenie konta usługi

1. Przejdź do **APIs & Services > Credentials**
2. Wybierz **+ Create Credentials > Service account**
3. Wpisz nazwę konta usługi (np. `plaidcloud-drive`)
4. Wybierz **Create and Continue**
5. Opcjonalnie nadaj role (np. **Viewer** do odczytu lub **Editor** do odczytu i zapisu). Wybierz **Continue**.
6. Wybierz **Done**

### Generowanie klucza konta usługi

1. Na liście **Service Accounts** wybierz właśnie utworzone konto usługi
2. Przejdź do karty **Keys**
3. Wybierz **Add Key > Create new key**
4. Wybierz format **JSON** i wybierz **Create**
5. Zostanie pobrany plik klucza JSON. Przechowuj go w bezpiecznym miejscu — zawiera poświadczenia, których będzie używać PlaidCloud.

### Udostępnianie zawartości Dysku koncie usługi

1. Skopiuj adres e-mail konta usługi (np. `plaidcloud-drive@your-project.iam.gserviceaccount.com`)
2. W Google Drive udostępnij foldery, do których PlaidCloud ma mieć dostęp, temu adresowi e-mail, nadając dostęp **Editor**

Masz teraz wszystko, czego potrzebujesz, aby dodać konto Google Drive do modułu PlaidCloud Document.


## Konfiguracja PlaidCloud Document

1. Zaloguj się do PlaidCloud
2. Wybierz obszar roboczy, w którym ma się znaleźć nowe konto dokumentów
3. Przejdź do `Document > Manage`
4. Wybierz przycisk **Nowe konto**
5. Wybierz `Google Drive` jako typ usługi
6. Wpisz nazwę i opis
7. Wpisz ścieżkę udostępnionego folderu w polu **Ścieżka początkowa** lub pozostaw je puste, aby uzyskać dostęp do całej udostępnionej zawartości
8. Wybierz odpowiedni **Model zabezpieczeń** dla danego zastosowania. W razie wątpliwości pozostaw wartość `Private`.
9. Wklej całą zawartość pliku klucza JSON w polu Poświadczenia OAuth2 JSON w sekcji Dane uwierzytelniające
10. Wybierz przycisk Zapisz — nowe konto dokumentów jest aktywne
