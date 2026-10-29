---
title: Dodawanie konta Google Drive
description: Dodaj konto magazynu Google Drive do PlaidCloud, aby importować i eksportować pliki danych za pomocą magazynu w chmurze Google Drive.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-google-drive-account.md
---

## Konfiguracja Google Drive

Poniższe kroki należy wykonać w Google Cloud Console, aby utworzyć konto usługi, którego PlaidCloud może używać do uzyskiwania dostępu do Google Drive.

### Tworzenie projektu Google Cloud

1. Zaloguj się do [Google Cloud Console](https://console.cloud.google.com)
2. Utwórz nowy projekt lub wybierz istniejący

### Włączanie interfejsu Google Drive API

1. Przejdź do **APIs & Services > Library**
2. Wyszukaj **Google Drive API**
3. Wybierz go i kliknij **Włącz**

### Tworzenie konta usługi

1. Przejdź do **APIs & Services > Credentials**
2. Wybierz **+ Create Credentials > Service account**
3. Wpisz nazwę konta usługi (np. `plaidcloud-drive`)
4. Wybierz **Utwórz** i **Kontynuuj**
5. Opcjonalnie przyznaj role (np. **Viewer** tylko do odczytu lub **Editor** do odczytu i zapisu). Wybierz **Kontynuuj**.
6. Wybierz **Gotowe**

### Generowanie klucza konta usługi

1. Na liście **Service Accounts** wybierz właśnie utworzone konto usługi
2. Przejdź do karty **Keys**
3. Wybierz **Dodaj klucz > Utwórz nowe**
4. Wybierz format **JSON** i wybierz **Utwórz**
5. Zostanie pobrany plik klucza JSON. Zapisz ten plik w bezpiecznym miejscu — zawiera poświadczenia, których będzie używać PlaidCloud.

### Udostępnianie zawartości Dysku koncie usługi

1. Skopiuj adres e-mail konta usługi (np. `plaidcloud-drive@your-project.iam.gserviceaccount.com`)
2. W Google Drive udostępnij folder lub foldery, do których PlaidCloud ma mieć dostęp, temu adresowi e-mail, przyznając dostęp **Editor**

Masz teraz wszystko, czego potrzebujesz, aby dodać konto Google Drive do PlaidCloud Document.


## Konfiguracja PlaidCloud Document

1. Zaloguj się do PlaidCloud
2. Wybierz obszar roboczy, w którym ma się znajdować nowe konto dokumentów
3. Przejdź do `Document > Manage Accounts`
4. Kliknij przycisk `+ New Account`
5. Wybierz `Google Drive` jako Typ usługi
6. Wpisz nazwę i opis
7. Wpisz ścieżkę udostępnionego folderu w polu **Ścieżka początkowa** lub pozostaw je puste, aby uzyskać dostęp do całej udostępnionej zawartości
8. Wybierz odpowiedni **Model zabezpieczeń** dla swojego przypadku użycia. Jeśli nie masz pewności, pozostaw `Private`.
9. Wklej całą zawartość pliku klucza JSON w polu Poświadczenia OAuth2 JSON w sekcji Dane uwierzytelniające
10. Kliknij przycisk Zapisz, a nowe konto dokumentów będzie aktywne
