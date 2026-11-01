---
title: Logowanie do PlaidXL
description: Połącz PlaidXL z obszarem roboczym PlaidCloud za pomocą adresu e-mail i zwykłego logowania, w tym logowania jednokrotnego i uwierzytelniania dwuskładnikowego, a następnie wyloguj się lub zmień obszar roboczy.
sidebar:
  label: Logowanie
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL loguje Cię jako Ciebie, przy użyciu tego samego logowania, którego używasz do PlaidCloud w przeglądarce. Nie trzeba wpisywać adresu serwera, a hasło nie jest przechowywane w skoroszycie.

## Zaloguj się

1. Otwórz okienko zadań: **PlaidCloud → Open PlaidXL**.
2. W polu **Enter your email** wpisz adres e-mail używany w PlaidCloud i kliknij **Sign In**. PlaidXL zapamięta adres na następny raz.
3. Jeśli Twój adres e-mail należy do więcej niż jednego obszaru roboczego, wybierz jeden z listy **Select a workspace** i kliknij **Sign In**. PlaidXL zapamięta Twój wybór. Jeśli należysz do jednego obszaru roboczego, PlaidXL wybierze go za Ciebie. Jeśli do adresu e-mail nie jest przypisany żaden obszar roboczy, okienko poinformuje o tym; sprawdź adres i spróbuj ponownie.
4. Excel pyta, czy zezwolić na okno podręczne. Zezwól na nie.
5. W oknie podręcznym zaloguj się w zwykły sposób:
   - **Logowanie PlaidCloud** — adres e-mail, hasło i ewentualny kod dwuskładnikowy, który skonfigurowano.
   - **Logowanie jednokrotne** — jeśli logowanie w Twojej organizacji jest już aktywne, ten krok przebiega automatycznie. W przeciwnym razie najpierw otworzy się strona logowania Twojej organizacji.
6. Gdy w oknie podręcznym pojawi się komunikat **Authenticated successfully**, zamknij je, jeśli nie zamknęło się samo.

Nagłówek okienka zadań pokazuje teraz Twój obszar roboczy i projekt powiązany ze skoroszytem, a obok znajduje się menu konta. Przejdź do artykułu [Praca z tabelami i wymiarami](/pl/reference/cli/plaidxl/retrieve/).

Aby skonfigurować uwierzytelnianie dwuskładnikowe lub logowanie jednokrotne dla swojego konta, zobacz [Uwierzytelnianie członków](/pl/administration/access/member-authentication/).

## Pozostawanie zalogowanym

PlaidXL utrzymuje Twoje logowanie na tym komputerze i odnawia je w tle podczas pracy. Gdy w kolejnej sesji otworzysz okienko zadań, od razu przejdzie ono do Twoich projektów. Jeśli logowanie całkowicie wygasło, PlaidXL ponownie poprosi o adres e-mail. Krótki problem z siecią podczas odnawiania logowania nie powoduje wylogowania; PlaidXL spróbuje ponownie.

## Co możesz zobaczyć

PlaidXL odczytuje dane z Twoimi uprawnieniami. Widzisz projekty, które możesz otworzyć w PlaidCloud, oraz zawarte w nich tabele i wymiary — nic więcej. Jeśli brakuje projektu lub tabeli, poproś właściciela projektu o dostęp. Zobacz [Wyjaśnienie organizacji i obszarów roboczych](/pl/administration/access/overview/organizations-and-workspaces-explained/), aby dowiedzieć się, jak działa członkostwo w obszarze roboczym.

## Wyloguj się lub zmień obszar roboczy

Kliknij menu konta (trzy kropki) w prawym górnym rogu okienka zadań. Pokazuje ono Twoje imię i nazwisko oraz obszar roboczy, a także dwa polecenia:

- **Log out** usuwa Twoje logowanie i wraca do ekranu z adresem e-mail.
- **Switch workspace** wylogowuje Cię i wraca do ekranu z adresem e-mail, co pozwala wybrać inny obszar roboczy w polu **Select a workspace**.

Twoje logowanie jest współdzielone przez wszystkie otwarte skoroszyty, ale każdy skoroszyt zachowuje własny projekt. Projekt skoroszytu należy do obszaru roboczego, więc po zmianie skoroszyt powiązany z projektem w poprzednim obszarze roboczym nie ma projektu, dopóki jakiegoś nie wybierzesz. Zobacz [Projekt należy do skoroszytu](/pl/reference/cli/plaidxl/retrieve/#projekt-należy-do-skoroszytu).

## Motyw jasny i ciemny

Okienko zadań podąża za motywem pakietu Office i zmienia się wraz z nim.

## Klawiatura i czytniki ekranu

Wiersze na listach projektów, tabel i wymiarów przyjmują fokus klawiatury i reagują na klawisze **Enter** i **Spacja**. Czytnik ekranu zapowiada zaznaczony wiersz, a stany zaznaczenia i ostrzeżenia mają ikonę oprócz koloru.

## Powiązane

- [Instalacja PlaidXL](/pl/reference/cli/plaidxl/install/) — dodaj dodatek i otwórz okienko zadań
- [Rozwiązywanie problemów](/pl/reference/cli/plaidxl/troubleshooting/) — gdy okno logowania się nie otwiera lub brakuje obszaru roboczego
- [Wyświetlanie obszarów roboczych i zarządzanie nimi](/pl/administration/access/overview/viewing-and-managing-workspaces/) — obszary robocze, do których należysz
