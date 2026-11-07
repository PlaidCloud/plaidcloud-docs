---
title: Logowanie do PlaidXL
description: Połącz PlaidXL z obszarem roboczym PlaidCloud za pomocą adresu e-mail i zwykłego logowania, w tym jednokrotnego logowania i uwierzytelniania dwuskładnikowego, a następnie wyloguj się lub przełącz obszary robocze.
sidebar:
  label: Logowanie
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL loguje Cię jako Ciebie, używając tego samego logowania, którego używasz do PlaidCloud w przeglądarce. Nie trzeba wpisywać adresu serwera, a hasło nie jest przechowywane w skoroszycie.

## Logowanie

1. Otwórz okienko zadań: **PlaidCloud → Open PlaidXL** lub **Konto** w grupie **Połącz**.
2. W polu **Enter your email** wpisz adres e-mail używany do PlaidCloud i kliknij **Sign In**. PlaidXL zapamiętuje adres na następny raz.
3. Jeśli Twój adres e-mail należy do więcej niż jednego obszaru roboczego, wybierz jeden z listy **Select a workspace** i kliknij **Sign In**. PlaidXL zapamiętuje Twój wybór. Jeśli należysz do jednego obszaru roboczego, PlaidXL wybiera go automatycznie. Jeśli z adresem e-mail nie jest powiązany żaden obszar roboczy, okienko informuje o tym; sprawdź adres i spróbuj ponownie.
4. Excel pyta, czy zezwolić na okno podręczne. Zezwól na nie.
5. W oknie podręcznym zaloguj się w zwykły sposób:
   - **PlaidCloud sign-in** — adres e-mail, hasło i ewentualny kod dwuskładnikowy, który skonfigurowano.
   - **Single sign-on** — jeśli jesteś już zalogowany do swojej organizacji, ten krok przebiega automatycznie. W przeciwnym razie najpierw otwiera się strona logowania Twojej organizacji.
6. Gdy okno podręczne wyświetli komunikat **Authenticated successfully**, zamknij je, jeśli nie zamknęło się samo.

Nagłówek okienka zadań pokazuje teraz Twój obszar roboczy i projekt powiązany ze skoroszytem, a obok znajduje się menu konta. Przejdź do [Praca z tabelami i wymiarami](/pl/reference/cli/plaidxl/retrieve/).

Aby skonfigurować uwierzytelnianie dwuskładnikowe lub jednokrotne logowanie dla swojego konta, zobacz [Uwierzytelnianie członków](/pl/administration/access/member-authentication/).

### Logowanie kontem Office

Jeśli jesteś zalogowany do pakietu Office kontem służbowym z Microsoft Entra ID, a PlaidXL nie ma zapisanego logowania, znajduje Twoje obszary robocze na podstawie tego konta, więc nie musisz wpisywać adresu e-mail:

- **Jeden obszar roboczy** — PlaidXL zaczyna logować Cię do niego. Zezwól na okno podręczne, jeśli Excel o to zapyta; przy jednokrotnym logowaniu ten krok przebiega automatycznie. W Excelu w przeglądarce najpierw kliknij **Continue as** i swoje konto.
- **Kilka obszarów roboczych** — jeśli skoroszyt był ostatnio używany z jednym z nich, PlaidXL loguje Cię do tego obszaru. W przeciwnym razie wybierz jeden z listy **Select a workspace**.
- **Brak obszaru roboczego** — otwiera się ekran adresu e-mail z już wpisanym Twoim adresem.

Jeśli logujesz się innym adresem e-mail niż konto Office, PlaidXL informuje, którego adresu dotyczy logowanie. Po kliknięciu **Log out** PlaidXL czeka, aż zalogujesz się samodzielnie.

### Polecenia przed zalogowaniem

Przed zalogowaniem możesz kliknąć dowolne polecenie PlaidXL na wstążce. PlaidXL otwiera okienko zadań, aby Cię zalogować lub umożliwić wybór projektu, a następnie uruchamia polecenie w komórce, od której zaczęto.

## Pozostawanie zalogowanym

PlaidXL utrzymuje Twoje logowanie na tym komputerze i odnawia je w tle podczas pracy. Po otwarciu okienka zadań w kolejnej sesji od razu przechodzi ono do Twoich projektów. Jeśli logowanie całkowicie wygasło, PlaidXL ponownie prosi o adres e-mail. Krótki problem z siecią podczas odnawiania logowania nie powoduje wylogowania; PlaidXL próbuje ponownie.

## Co możesz zobaczyć

PlaidXL odczytuje dane z Twoimi uprawnieniami. Widzisz projekty, które możesz otworzyć w PlaidCloud, oraz zawarte w nich tabele i wymiary, i nic więcej. Jeśli brakuje projektu lub tabeli, poproś właściciela projektu o dostęp. Zobacz [Wyjaśnienie organizacji i obszarów roboczych](/pl/administration/access/overview/organizations-and-workspaces-explained/), aby dowiedzieć się, jak działa członkostwo w obszarze roboczym.

## Wylogowanie lub przełączenie obszarów roboczych

Kliknij menu konta (trzy kropki) w prawym górnym rogu okienka zadań. Pokazuje ono Twoje imię i nazwisko oraz obszar roboczy, a także trzy polecenia:

- **Keyboard shortcuts** wyświetla skróty klawiszowe PlaidXL, aby można je było zmienić. Zobacz [Skróty klawiszowe](/pl/reference/cli/plaidxl/ribbon/#skróty-klawiszowe).
- **Switch workspace** wylogowuje Cię i wraca do ekranu adresu e-mail, abyś mógł wybrać inny obszar roboczy w polu **Select a workspace**. Gdy pojawi się prośba, zaloguj się do nowego obszaru roboczego. Powrót do obszaru roboczego, do którego już się logowano, nie wymaga ponownego logowania, a anulowanie logowania zachowuje obszar roboczy, w którym byłeś.
- **Log out** usuwa Twoje logowanie i wraca do ekranu adresu e-mail.

Każde logowanie działa tylko dla obszaru roboczego, w którym zostało wykonane. Po tej zmianie wszyscy logują się jeszcze raz. Gdy jesteś wylogowany, **Zapisz** wyświetla komunikat **Sign in to PlaidCloud to save.**, a pobieranie wymiaru wyświetla komunikat **Sign in to PlaidCloud to retrieve a dimension.**

Twoje logowanie jest współdzielone przez wszystkie otwarte skoroszyty, ale każdy skoroszyt zachowuje własny projekt. Projekt skoroszytu należy do obszaru roboczego, więc po przełączeniu skoroszyt powiązany z projektem w poprzednim obszarze roboczym nie ma projektu, dopóki jakiegoś nie wybierzesz. Zobacz [Projekt należy do skoroszytu](/pl/reference/cli/plaidxl/retrieve/#projekt-należy-do-skoroszytu).

## Jasny i ciemny motyw

Okienko zadań stosuje motyw pakietu Office i zmienia się razem z nim.

## Klawiatura i czytniki ekranu

Wiersze na listach projektów, tabel i wymiarów przyjmują fokus klawiatury i reagują na **Enter** oraz **Spacja**. Zaznaczony wiersz jest odczytywany przez czytnik ekranu, a stany zaznaczenia i ostrzeżenia mają ikonę oprócz koloru.

## Powiązane

- [Instalacja PlaidXL](/pl/reference/cli/plaidxl/install/) — dodaj dodatek i otwórz okienko zadań
- [Rozwiązywanie problemów](/pl/reference/cli/plaidxl/troubleshooting/) — gdy okno podręczne logowania się nie otwiera lub brakuje obszaru roboczego
- [Przeglądanie obszarów roboczych i zarządzanie nimi](/pl/administration/access/overview/viewing-and-managing-workspaces/) — obszary robocze, do których należysz
