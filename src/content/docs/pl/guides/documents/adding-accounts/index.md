---
title: Dodawanie nowych kont dokumentów
description: Połącz z PlaidCloud magazyn dokumentów w chmurze i lokalny — S3, GCS, Azure Blob, Google Drive, OneDrive, SFTP, WebDAV i inne.
sidebar:
  label: Dodawanie nowych kont dokumentów
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/index.md
---

Połącz z PlaidCloud magazyn dokumentów w chmurze i lokalny — S3, Google Cloud Storage, Azure Blob, Google Drive, OneDrive, SFTP, WebDAV i inne. Każdy dostawca ma własne dane uwierzytelniające i własny przebieg połączenia.

Najszybszą opcją jest **Zasobnik zarządzany przez PlaidCloud**, w którym PlaidCloud konfiguruje i obsługuje magazyn za Ciebie — wystarczy wybrać nazwę, bez żadnej dodatkowej konfiguracji. Aby połączyć magazyn, który już posiadasz, wybierz odpowiedniego dostawcę poniżej.

## Zapisane klucze tajne są tylko do zapisu

Klucz tajny konta, czyli pole o nazwie **Klucz prywatny / hasło** lub, zależnie od typu konta, **Tajny klucz dostępu**, **Klucz konta**, **Klucz tajny klienta**, **Token dostępu**, **Hasło**, **Klucz JSON użytkownika systemowego** albo **Poświadczenia OAuth2 JSON**, jest tylko do zapisu, podobnie jak **RSA Private Key** konta SFTP. Po zapisaniu nigdy nie są wyświetlane ponownie — ani w formularzu, ani w API, ani asystentowi AI. Podczas edycji konta pole jest puste i wyświetla podpowiedź *Paste the value; leave blank on edit to keep the saved one.* Pozostaw je puste, aby zachować zapisany klucz tajny, albo wklej nowy, aby go zastąpić.

Zmiana miejsca, z którym łączy się konto, wymaga ponownego wprowadzenia jego klucza tajnego. Jeśli zmienisz pierwszą część **Ścieżki początkowej** (w przypadku magazynu w chmurze — zasobnik lub kontener), **Host lub adres IP** albo **Port połączenia SSH** konta SFTP, lub **ID dzierżawy OneDrive** konta OneDrive, wklej także klucz tajny, w przeciwnym razie zapis zostanie odrzucony z komunikatem *Changing where the account connects needs its secret entered again*. Zapobiega to wysłaniu klucza tajnego na wybrany przez kogoś serwer przez osobę, która może edytować konto, ale nigdy nie widziała jego klucza tajnego.

Asystent AI połączony przez konektor MCP PlaidCloud może także tworzyć i aktualizować konta, podając typ magazynu, dane uwierzytelniające i ścieżkę początkową. Dane uwierzytelniające są tylko do zapisu i są ukryte podczas ponownego odczytu konta. Przykład krok po kroku znajdziesz w [Dodawanie konta OneDrive / SharePoint](/pl/guides/documents/adding-accounts/add-onedrive-account/#tworzenie-konta-za-pomocą-asystenta-ai).
