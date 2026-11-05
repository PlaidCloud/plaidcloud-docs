---
title: Logowanie do PlaidXL
description: Połącz PlaidXL ze swoim obszarem roboczym PlaidCloud za pomocą adresu e-mail i zwykłego logowania, w tym logowania jednokrotnego i uwierzytelniania dwuskładnikowego, a następnie wyloguj się lub przełącz obszar roboczy.
sidebar:
  label: Logowanie
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL loguje Cię jako Ciebie, używając tego samego logowania, którego używasz do PlaidCloud w przeglądarce. Nie wpisujesz adresu serwera, a hasło nie jest przechowywane w skoroszycie.

## Logowanie

1. Otwórz okienko zadań: **PlaidCloud → Open PlaidXL** albo **Konto** w grupie **Połącz**.
2. W polu **Enter your email** wpisz adres e-mail używany w PlaidCloud i kliknij **Sign In**. PlaidXL zapamięta adres na następny raz.
3. Jeśli Twój adres e-mail należy do więcej niż jednego obszaru roboczego, wybierz jeden z listy **Select a workspace** i kliknij **Sign In**. PlaidXL zapamięta Twój wybór. Jeśli należysz do jednego obszaru roboczego, PlaidXL wybierze go za Ciebie. Jeśli z adresem e-mail nie jest powiązany żaden obszar roboczy, okienko poinformuje o tym; sprawdź adres i spróbuj ponownie.
4. Excel zapyta, czy zezwolić na okno podręczne. Zezwól.
5. W oknie podręcznym zaloguj się w zwykły sposób:
   - **PlaidCloud sign-in** — adres e-mail, hasło i ewentualny kod dwuskładnikowy, który skonfigurowano.
   - **Single sign-on** — jeśli jesteś już zalogowany w swojej organizacji, ten krok przebiega automatycznie. W przeciwnym razie najpierw otworzy się strona logowania Twojej organizacji.
6. Gdy okno podręczne wyświetli komunikat **Authenticated successfully**, zamknij je, jeśli nie zamknęło się samo.

Nagłówek okienka zadań pokazuje teraz Twój obszar roboczy i projekt powiązany ze skoroszytem, a obok menu konta. Przejdź dalej do [Praca z tabelami i wymiarami](/pl/reference/cli/plaidxl/retrieve/).

Aby skonfigurować uwierzytelnianie dwuskładnikowe lub logowanie jednokrotne dla swojego konta, zobacz [Uwierzytelnianie członków](/pl/administration/access/member-authentication/).

### Logowanie kontem Office

Jeśli jesteś zalogowany w pakiecie Office kontem służbowym z Microsoft Entra ID, a PlaidXL nie ma zapisanego logowania, znajduje Twoje obszary robocze na podstawie tego konta, więc nie musisz wpisywać adresu e-mail:

- **Jeden obszar roboczy** — PlaidXL zaczyna logować Cię do niego. Zezwól na okno podręczne, jeśli Excel o to poprosi; przy logowaniu jednokrotnym przebiega ono automatycznie. W Excelu w przeglądarce najpierw kliknij **Continue as** i swoje konto.
- **Kilka obszarów roboczych** — wybierz jeden z listy **Select a workspace**. Obszar roboczy, z którym skoroszyt był ostatnio używany, jest już zaznaczony.
- **Brak obszaru roboczego** — otwiera się ekran adresu e-mail z wypełnionym adresem.

Jeśli logujesz się innym adresem e-mail niż konto Office, PlaidXL poda, którym. Po **Log out** PlaidXL czeka, aż zalogujesz się samodzielnie.

### Polecenia przed zalogowaniem

Przed zalogowaniem możesz kliknąć dowolne polecenie PlaidXL na wstążce. PlaidXL otworzy okienko zadań, aby Cię zalogować lub umożliwić wybór projektu, a następnie wykona polecenie na komórce, od której zaczęto.

## Pozostawanie zalogowanym

PlaidXL utrzymuje Twoje logowanie na tym komputerze i odnawia je w tle podczas pracy. Gdy w kolejnej sesji otworzysz okienko zadań, przejdzie od razu do Twoich projektów. Jeśli logowanie całkowicie wygasło, PlaidXL ponownie poprosi o adres e-mail. Krótki problem z siecią podczas odnawiania logowania nie wyloguje Cię; PlaidXL spróbuje ponownie.

## Co możesz zobaczyć

PlaidXL odczytuje dane z Twoimi uprawnieniami. Widzisz projekty, które możesz otworzyć w PlaidCloud, oraz zawarte w nich tabele i wymiary — nic więcej. Jeśli brakuje projektu lub tabeli, poproś właściciela projektu o dostęp. Zasady członkostwa w obszarze roboczym opisano w artykule [Organizacje i obszary robocze — wyjaśnienie](/pl/administration/access/overview/organizations-and-workspaces-explained/).

## Wylogowanie lub przełączenie obszaru roboczego

Kliknij menu konta (trzy kropki) w prawym górnym rogu okienka zadań. Pokazuje ono Twoje imię i nazwisko oraz obszar roboczy, a także trzy polecenia:

- **Keyboard shortcuts** wyświetla skróty PlaidXL, aby można je było zmienić. Zobacz [Skróty klawiszowe](/pl/reference/cli/plaidxl/ribbon/#skróty-klawiszowe).
- **Switch workspace** wylogowuje i wraca do ekranu adresu e-mail, aby można było wybrać inny obszar roboczy w polu **Select a workspace**.
- **Log out** usuwa logowanie i wraca do ekranu adresu e-mail.

Logowanie jest wspólne dla wszystkich otwartych skoroszytów, ale każdy skoroszyt zachowuje własny projekt. Projekt skoroszytu należy do obszaru roboczego, więc po przełączeniu skoroszyt powiązany z projektem w poprzednim obszarze roboczym nie ma projektu, dopóki go nie wybierzesz. Zobacz [Projekt należy do skoroszytu](/pl/reference/cli/plaidxl/retrieve/#projekt-należy-do-skoroszytu).

## Jasny i ciemny motyw

Okienko zadań podąża za motywem pakietu Office i zmienia się wraz z nim.

## Klawiatura i czytniki ekranu

Wiersze na listach projektów, tabel i wymiarów przyjmują fokus klawiatury i reagują na klawisze **Enter** i **Spacja**. Zaznaczony wiersz jest odczytywany przez czytnik ekranu, a stany zaznaczenia i ostrzeżenia mają ikonę, a nie tylko kolor.

## Powiązane

- [Instalacja PlaidXL](/pl/reference/cli/plaidxl/install/) — dodaj dodatek i otwórz okienko zadań
- [Rozwiązywanie problemów](/pl/reference/cli/plaidxl/troubleshooting/) — gdy okno logowania się nie otwiera lub brakuje obszaru roboczego
- [Wyświetlanie obszarów roboczych i zarządzanie nimi](/pl/administration/access/overview/viewing-and-managing-workspaces/) — obszary robocze, do których należysz
