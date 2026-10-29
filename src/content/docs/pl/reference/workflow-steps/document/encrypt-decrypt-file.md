---
title: Encrypt File and Decrypt File (kroki)
description: Szyfruj lub odszyfrowuj cały plik dokumentu algorytmem AES lub Blowfish albo dodawaj lub usuwaj hasło skoroszytu Excel w kroku przepływu pracy PlaidCloud.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/document/encrypt-decrypt-file.md
---

## Opis

**Dokument: szyfrowanie pliku** szyfruje jeden plik na koncie dokumentów i zapisuje wynik do innego pliku. **Dokument: odszyfrowanie pliku** robi odwrotnie. Oba kroki mają te same ustawienia. Używaj ich, aby odbierać zaszyfrowane pliki od partnera, odszyfrowywać je przed odczytem przez import oraz szyfrować eksport, zanim trafi do innego systemu.

## Pliki

| Ustawienie | Wymagane | Co robi |
| --- | --- | --- |
| Plik źródłowy | Tak | Plik do zaszyfrowania lub odszyfrowania. |
| Plik docelowy | Tak | Plik do zapisania. Musi być innym plikiem niż źródłowy, aby ponowne uruchomienie nigdy nie działało na własnym wyniku. |
| Usuń plik źródłowy po zapisaniu pliku docelowego | Nie | Usuwa plik źródłowy po bezpiecznym zapisaniu pliku docelowego. |

Brak pliku źródłowego nie jest błędem: krok kończy się ostrzeżeniem ze wskazaniem ścieżki, niczego nie zapisuje, a przepływ pracy jest kontynuowany. Pusty plik źródłowy powoduje zapisanie pustego pliku docelowego z ostrzeżeniem, z wyjątkiem szyfrowania pustego pliku algorytmem AES lub Blowfish, które zapisuje prawdziwy zaszyfrowany plik. Nie można użyć konta dokumentów Smartsheet, ponieważ nie da się z niego odczytać plików z powrotem.

## Parametry

| Ustawienie | Co robi |
| --- | --- |
| Algorytm | W grupie Szyfr: **AES-128 (klucz 16-bajtowy)**, **AES-192 (klucz 24-bajtowy)**, **AES-256 (klucz 32-bajtowy)**, **Blowfish (klucz 4–56 bajtów)** lub **Hasło skoroszytu Excel**. |
| Tryb | **CBC** (domyślnie), **ECB** lub **GCM**. Blowfish przyjmuje tylko CBC lub ECB. |
| Zmienna klucza | Zmienna przepływu pracy lub projektu, która przechowuje klucz szyfrowania, na przykład `{aes_key}`. Wymagana dla AES i Blowfish. |
| Kodowanie klucza i IV | Sposób zapisu klucza i IV: **Tekst (UTF-8)**, **Szesnastkowo** lub **Base64**. |
| Stałe IV | Wektor inicjujący. Pozostaw puste, a szyfrowanie rozpocznie plik losowym IV, które odszyfrowanie odczytuje z początku pliku. Szyfrowanie GCM zawsze używa losowego IV, więc dla GCM pozostaw puste. |
| Zmienna hasła skoroszytu | Zmienna przepływu pracy lub projektu, która przechowuje hasło ustawiane w skoroszycie Excel lub z niego usuwane, na przykład `{xlsx_password}`. Wymagana dla **Hasło skoroszytu Excel**. |

CBC i ECB uzupełniają dane metodą PKCS7, a GCM dodaje 16-bajtowy znacznik uwierzytelniający po zaszyfrowanych danych. Plik GCM może mieć do 256 MB. Błędny klucz lub IV zatrzymuje krok z błędem i nie pozostawia częściowego pliku.

## Klucze przechowywane w zmiennych

**Zmienna klucza** i **Zmienna hasła skoroszytu** przyjmują wyłącznie odwołanie do zmiennej, takie jak `{aes_key}`, nigdy sam klucz ani hasło: zapis kroku z czymkolwiek innym jest odrzucany. Umieść tajny element w [zmiennej przepływu pracy](/pl/guides/workflows/manage-workflow-variables/) lub zmiennej projektu, aby był ustawiony w jednym miejscu i nigdy nie pojawiał się w kroku, jego wersjach, kopiach ani w tym, co odczytuje asystent AI. Krok odczytuje wartość zmiennej podczas uruchomienia. **Stałe IV** jest polem hasła, więc jego wartość jest ukryta w formularzu.

Kroki, które przed wprowadzeniem tej reguły przechowywały wpisany klucz lub hasło, miały je automatycznie przeniesione do nowej zmiennej projektu, widocznej tylko dla Architektów, i teraz odwołują się do tej zmiennej.

## Powiązane

- [Kroki dokumentów](/pl/reference/workflow-steps/document/)
- [Zarządzanie zmiennymi przepływu pracy](/pl/guides/workflows/manage-workflow-variables/)
