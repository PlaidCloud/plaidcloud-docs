---
title: Logowanie do PlaidXL
description: Połącz PlaidXL ze swoim obszarem roboczym PlaidCloud za pomocą adresu e-mail i zwykłego sposobu logowania, w tym logowania jednokrotnego i uwierzytelniania dwuskładnikowego, a następnie wyloguj się lub przełącz obszary robocze.
sidebar:
  label: Logowanie
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL loguje Cię jako Ciebie, używając tego samego logowania, którego używasz do PlaidCloud w przeglądarce. Nie trzeba wpisywać adresu serwera, a hasło nie jest przechowywane w skoroszycie.

## Logowanie

1. Otwórz okienko zadań: **PlaidCloud → Show Taskpane**.
2. W polu **Enter your email** wpisz adres e-mail używany do PlaidCloud i kliknij **Sign In**.
3. Jeśli Twój adres e-mail należy do więcej niż jednego obszaru roboczego, wybierz jeden z nich w polu **Select a tenant** i kliknij **Sign In**. (*Tenant* w PlaidXL to Twój obszar roboczy PlaidCloud). Jeśli należysz do jednego obszaru roboczego, PlaidXL wybierze go za Ciebie.
4. Excel zapyta, czy zezwolić na okno podręczne. Zezwól.
5. W oknie podręcznym zaloguj się w zwykły sposób:
   - **Logowanie do PlaidCloud** — adres e-mail, hasło i ewentualny kod dwuskładnikowy, który skonfigurowano.
   - **Logowanie jednokrotne** — jeśli jesteś już zalogowany w swojej organizacji, ten krok przechodzi automatycznie. W przeciwnym razie najpierw otworzy się strona logowania Twojej organizacji.
6. Gdy w oknie podręcznym pojawi się komunikat **Authenticated successfully**, zamknij je, jeśli nie zamknęło się samo.

W okienku zadań widać teraz **Connected to** z identyfikatorem Twojego obszaru roboczego **as** i Twoją nazwą użytkownika, a poniżej listę projektów. Przejdź dalej do [Praca z tabelami i wymiarami](/pl/reference/cli/plaidxl/retrieve/).

Aby skonfigurować uwierzytelnianie dwuskładnikowe lub logowanie jednokrotne dla swojego konta, zobacz [Uwierzytelnianie członków](/pl/administration/access/member-authentication/).

## Pozostawanie zalogowanym

PlaidXL utrzymuje Twoje zalogowanie na tym komputerze i odnawia je w tle w trakcie pracy. Po otwarciu okienka zadań w kolejnej sesji od razu przechodzi do Twoich projektów. Jeśli logowanie całkowicie wygasło, PlaidXL ponownie prosi o adres e-mail.

## Co możesz zobaczyć

PlaidXL odczytuje dane z Twoimi uprawnieniami. Widzisz projekty, które możesz otworzyć w PlaidCloud, oraz zawarte w nich tabele i wymiary, i nic więcej. Jeśli brakuje projektu lub tabeli, poproś właściciela projektu o dostęp. Zobacz [Organizacje i obszary robocze — wyjaśnienie](/pl/administration/access/overview/organizations-and-workspaces-explained/), aby dowiedzieć się, jak działa członkostwo w obszarze roboczym.

## Wylogowanie lub przełączanie obszarów roboczych

Kliknij **Logout** u góry okienka zadań. PlaidXL usuwa Twoje zalogowanie i wraca do ekranu z adresem e-mail.

Aby pracować w innym obszarze roboczym, wyloguj się, zaloguj ponownie i wybierz inny obszar roboczy w polu **Select a tenant**. PlaidXL pracuje z jednym obszarem roboczym naraz, dla każdego otwartego skoroszytu.

## Motyw jasny i ciemny

Okienko zadań podąża za motywem pakietu Office. Aby przypiąć je do motywu jasnego lub ciemnego, kliknij przycisk słońca lub księżyca w lewym górnym rogu okienka zadań.

## Powiązane

- [Instalacja PlaidXL](/pl/reference/cli/plaidxl/install/) — dodaj dodatek i otwórz okienko zadań
- [Rozwiązywanie problemów](/pl/reference/cli/plaidxl/troubleshooting/) — gdy okno logowania się nie otwiera lub brakuje obszaru roboczego
- [Wyświetlanie obszarów roboczych i zarządzanie nimi](/pl/administration/access/overview/viewing-and-managing-workspaces/) — obszary robocze, do których należysz
