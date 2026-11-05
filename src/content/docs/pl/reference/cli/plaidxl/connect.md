---
title: Logowanie do PlaidXL
description: Połącz PlaidXL z obszarem roboczym PlaidCloud za pomocą adresu e-mail i zwykłego sposobu logowania, w tym jednokrotnego logowania i uwierzytelniania dwuskładnikowego, a następnie wyloguj się lub przełącz obszar roboczy.
sidebar:
  label: Logowanie
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL loguje Cię jako Ciebie, przy użyciu tego samego logowania, którego używasz do PlaidCloud w przeglądarce. Nie trzeba wpisywać adresu serwera, a w skoroszycie nie jest przechowywane żadne hasło.

## Logowanie

1. Otwórz okienko zadań: **PlaidCloud → Open PlaidXL** lub **Konto** w grupie **Połącz**.
2. W polu **Enter your email** wpisz adres e-mail używany do PlaidCloud i kliknij **Sign In**. PlaidXL zapamiętuje adres na przyszłość.
3. Jeśli Twój adres e-mail należy do więcej niż jednego obszaru roboczego, wybierz jeden z listy **Select a workspace** i kliknij **Sign In**. PlaidXL zapamiętuje Twój wybór. Jeśli należysz do jednego obszaru roboczego, PlaidXL wybiera go automatycznie. Jeśli z adresem e-mail nie jest powiązany żaden obszar roboczy, okienko informuje o tym; sprawdź adres i spróbuj ponownie.
4. Excel pyta, czy zezwolić na okno podręczne. Zezwól na nie.
5. W oknie podręcznym zaloguj się w zwykły sposób:
   - **Logowanie do PlaidCloud** — adres e-mail, hasło i ewentualny kod dwuskładnikowy, który skonfigurowano.
   - **Jednokrotne logowanie** — jeśli jesteś już zalogowany w swojej organizacji, ten krok przebiega automatycznie. W przeciwnym razie najpierw otwiera się strona logowania Twojej organizacji.
6. Gdy okno podręczne wyświetli komunikat **Authenticated successfully**, zamknij je, jeśli nie zamknęło się samo.

Nagłówek okienka zadań pokazuje teraz Twój obszar roboczy i projekt powiązany ze skoroszytem, a obok znajduje się menu konta. Przejdź dalej do artykułu [Praca z tabelami i wymiarami](/pl/reference/cli/plaidxl/retrieve/).

Aby skonfigurować uwierzytelnianie dwuskładnikowe lub jednokrotne logowanie dla swojego konta, zobacz [Uwierzytelnianie członków](/pl/administration/access/member-authentication/).

### Logowanie za pomocą konta Office

Jeśli w pakiecie Office zalogowano Cię kontem służbowym z Microsoft Entra ID, a PlaidXL nie ma zapisanego logowania, znajduje Twoje obszary robocze na podstawie tego konta, więc nie musisz wpisywać adresu e-mail:

- **Jeden obszar roboczy** — PlaidXL rozpoczyna logowanie do niego. Zezwól na okno podręczne, jeśli Excel o to zapyta; przy jednokrotnym logowaniu przebiega ono automatycznie. W programie Excel w sieci Web najpierw kliknij **Continue as** i wybierz swoje konto.
- **Kilka obszarów roboczych** — jeśli skoroszyt był ostatnio używany z jednym z nich, PlaidXL loguje Cię do tego obszaru. W przeciwnym razie wybierz jeden z listy **Select a workspace**.
- **Brak obszaru roboczego** — otwiera się ekran adresu e-mail z wypełnionym Twoim adresem.

Jeśli logujesz się innym adresem e-mail niż konto Office, PlaidXL informuje, którym. Po wybraniu **Log out** PlaidXL czeka, aż zalogujesz się samodzielnie.

### Polecenia przed zalogowaniem

Możesz kliknąć dowolne polecenie PlaidXL na wstążce, zanim się zalogujesz. PlaidXL otwiera okienko zadań, aby zalogować Cię lub umożliwić wybór projektu, a następnie uruchamia polecenie w komórce, od której zaczęto.

## Pozostawanie zalogowanym

PlaidXL utrzymuje Twoje logowanie na tym komputerze i odnawia je w tle podczas pracy. Gdy otworzysz okienko zadań w kolejnej sesji, od razu przechodzi do Twoich projektów. Jeśli logowanie całkowicie wygasło, PlaidXL ponownie prosi o adres e-mail. Krótki problem z siecią podczas odnawiania logowania nie powoduje wylogowania; PlaidXL ponawia próbę.

## Co możesz zobaczyć

PlaidXL odczytuje dane z Twoimi uprawnieniami. Widzisz projekty, które możesz otworzyć w PlaidCloud, oraz zawarte w nich tabele i wymiary, i nic więcej. Jeśli brakuje projektu lub tabeli, poproś właściciela projektu o dostęp. Zobacz [Organizacje i obszary robocze — objaśnienie](/pl/administration/access/overview/organizations-and-workspaces-explained/), aby dowiedzieć się, jak działa członkostwo w obszarze roboczym.

## Wylogowanie lub przełączenie obszaru roboczego

Kliknij menu konta (trzy kropki) w prawym górnym rogu okienka zadań. Pokazuje ono Twoją nazwę i obszar roboczy oraz trzy polecenia:

- **Keyboard shortcuts** wyświetla skróty PlaidXL, aby można było je zmienić. Zobacz [Skróty klawiaturowe](/pl/reference/cli/plaidxl/ribbon/#skróty-klawiszowe).
- **Switch workspace** wylogowuje Cię i wraca do ekranu adresu e-mail, aby można było wybrać inny obszar roboczy w polu **Select a workspace**.
- **Log out** usuwa Twoje logowanie i wraca do ekranu adresu e-mail.

Twoje logowanie jest wspólne dla wszystkich otwartych skoroszytów, ale każdy skoroszyt zachowuje własny projekt. Projekt skoroszytu należy do obszaru roboczego, więc po przełączeniu skoroszyt powiązany z projektem w poprzednim obszarze roboczym nie ma projektu, dopóki nie wybierzesz nowego. Zobacz [Projekt należy do skoroszytu](/pl/reference/cli/plaidxl/retrieve/#projekt-należy-do-skoroszytu).

## Motyw jasny i ciemny

Okienko zadań stosuje motyw pakietu Office i zmienia się wraz z nim.

## Klawiatura i czytniki ekranu

Wiersze na listach projektów, tabel i wymiarów przyjmują fokus klawiatury i reagują na **Enter** oraz **Spacja**. Zaznaczony wiersz jest odczytywany przez czytnik ekranu, a stany zaznaczenia i ostrzeżenia mają ikonę oprócz koloru.

## Powiązane

- [Instalacja PlaidXL](/pl/reference/cli/plaidxl/install/) — dodaj dodatek i otwórz okienko zadań
- [Rozwiązywanie problemów](/pl/reference/cli/plaidxl/troubleshooting/) — gdy okno podręczne logowania się nie otwiera lub brakuje obszaru roboczego
- [Przeglądanie obszarów roboczych i zarządzanie nimi](/pl/administration/access/overview/viewing-and-managing-workspaces/) — obszary robocze, do których należysz
