---
title: Logowanie do PlaidXL
description: Połącz PlaidXL ze swoim obszarem roboczym PlaidCloud za pomocą adresu e-mail i zwykłego logowania, w tym jednokrotnego logowania i uwierzytelniania dwuskładnikowego, a następnie wyloguj się lub przełącz obszar roboczy.
sidebar:
  label: Logowanie
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/cli/plaidxl/connect.md
---

PlaidXL loguje Cię jako Ciebie, przy użyciu tego samego logowania, którego używasz do PlaidCloud w przeglądarce. Nie trzeba wpisywać adresu serwera, a hasło nie jest przechowywane w skoroszycie.

## Logowanie

1. Otwórz okienko zadań: **PlaidCloud → Open PlaidXL** albo **Konto** w grupie **Połącz**.
2. W polu **Enter your email** wpisz adres e-mail używany w PlaidCloud i kliknij **Sign In**. PlaidXL zapamiętuje adres na następny raz.
3. Jeśli Twój adres e-mail należy do więcej niż jednego obszaru roboczego, wybierz jeden z listy **Select a workspace** i kliknij **Sign In**. PlaidXL zapamiętuje Twój wybór. Jeśli należysz do jednego obszaru roboczego, PlaidXL wybiera go automatycznie. Jeśli do adresu e-mail nie jest przypisany żaden obszar roboczy, okienko poinformuje o tym; sprawdź adres i spróbuj ponownie.
4. Excel pyta, czy zezwolić na wyskakujące okno. Zezwól.
5. W wyskakującym oknie zaloguj się w zwykły sposób:
   - **PlaidCloud sign-in** — Twój adres e-mail, hasło i ewentualny kod uwierzytelniania dwuskładnikowego, który skonfigurowano.
   - **Single sign-on** — jeśli jesteś już zalogowany w swojej organizacji, ten krok przebiega automatycznie. W przeciwnym razie najpierw otwiera się strona logowania Twojej organizacji.
6. Gdy w wyskakującym oknie pojawi się komunikat **Authenticated successfully**, zamknij je, jeśli nie zamknęło się samo.

Nagłówek okienka zadań pokazuje teraz Twój obszar roboczy i projekt powiązany ze skoroszytem, a obok niego menu konta. Przejdź do [Praca z tabelami i wymiarami](/pl/reference/cli/plaidxl/retrieve/).

Aby skonfigurować uwierzytelnianie dwuskładnikowe lub jednokrotne logowanie dla swojego konta, zobacz [Uwierzytelnianie członków](/pl/administration/access/member-authentication/).

### Logowanie za pomocą konta Office

Jeśli jesteś zalogowany w pakiecie Office na konto służbowe z Microsoft Entra ID, a PlaidXL nie ma zapisanego logowania, znajduje Twoje obszary robocze na podstawie tego konta, więc nie musisz wpisywać adresu e-mail:

- **Jeden obszar roboczy** — PlaidXL rozpoczyna logowanie do niego. Zezwól na wyskakujące okno, jeśli Excel o to zapyta; przy jednokrotnym logowaniu przebiega ono automatycznie. W programie Excel w sieci Web najpierw kliknij **Continue as** i swoje konto.
- **Kilka obszarów roboczych** — jeśli skoroszyt był ostatnio używany z jednym z nich, PlaidXL loguje Cię do tego obszaru. W przeciwnym razie wybierz jeden z listy **Select a workspace**.
- **Brak obszaru roboczego** — otwiera się ekran adresu e-mail z wypełnionym Twoim adresem.

Jeśli logujesz się na inny adres e-mail niż konto Office, PlaidXL podaje, który to adres. Po kliknięciu **Log out** PlaidXL czeka, aż zalogujesz się samodzielnie.

### Polecenia przed zalogowaniem

Możesz kliknąć dowolne polecenie PlaidXL na wstążce, zanim się zalogujesz. PlaidXL otwiera okienko zadań, aby Cię zalogować lub umożliwić wybór projektu, a następnie uruchamia polecenie w komórce, od której zaczynasz.

## Pozostawanie zalogowanym

PlaidXL utrzymuje Twoje logowanie na tym komputerze i odnawia je w tle w trakcie pracy. Gdy w kolejnej sesji otworzysz okienko zadań, od razu przechodzi ono do Twoich projektów. Jeśli logowanie całkowicie wygasło, PlaidXL ponownie prosi o adres e-mail. Krótki problem z siecią podczas odnawiania logowania nie powoduje wylogowania; PlaidXL próbuje ponownie.

## Co możesz zobaczyć

PlaidXL odczytuje dane z Twoimi uprawnieniami. Widzisz projekty, które możesz otworzyć w PlaidCloud, oraz zawarte w nich tabele i wymiary, i nic więcej. Jeśli brakuje projektu lub tabeli, poproś właściciela projektu o dostęp. Zobacz [Organizacje i obszary robocze — objaśnienie](/pl/administration/access/overview/organizations-and-workspaces-explained/), aby dowiedzieć się, jak działa członkostwo w obszarze roboczym.

## Wylogowanie lub przełączenie obszaru roboczego

Kliknij menu konta (trzy kropki) w prawym górnym rogu okienka zadań. Pokazuje ono Twoje imię i nazwisko oraz obszar roboczy, a także trzy polecenia:

- **Keyboard shortcuts** wyświetla skróty klawiszowe PlaidXL, aby można je było zmienić. Zobacz [Skróty klawiszowe](/pl/reference/cli/plaidxl/ribbon/#skróty-klawiszowe).
- **Switch workspace** wylogowuje Cię i wraca do ekranu adresu e-mail, aby można było wybrać inny obszar roboczy z listy **Select a workspace**. Gdy pojawi się prośba, zaloguj się do nowego obszaru roboczego. Powrót do obszaru roboczego, do którego już się logowano, nie wymaga ponownego logowania, a anulowanie logowania pozostawia Cię w dotychczasowym obszarze roboczym.
- **Log out** usuwa Twoje logowanie i wraca do ekranu adresu e-mail.

Każde logowanie działa tylko dla obszaru roboczego, w którym zostało wykonane. Po tej zmianie każdy loguje się jednorazowo ponownie. Gdy jesteś wylogowany, po kliknięciu **Zapisz** pojawia się komunikat **Sign in to PlaidCloud to save.**, a przy pobieraniu wymiaru — komunikat **Sign in to PlaidCloud to retrieve a dimension.**

Twoje logowanie jest współdzielone przez wszystkie otwarte skoroszyty, ale każdy skoroszyt zachowuje własny projekt. Projekt skoroszytu należy do obszaru roboczego, więc po przełączeniu skoroszyt powiązany z projektem w poprzednim obszarze roboczym nie ma projektu, dopóki go nie wybierzesz. Zobacz [Projekt należy do skoroszytu](/pl/reference/cli/plaidxl/retrieve/#projekt-należy-do-skoroszytu).

## Jasny i ciemny motyw

Okienko zadań odpowiada aplikacji internetowej PlaidCloud: ma firmowy niebieski kolor, karty i listy w stylu szyny oraz tabele, wymiary, projekty i kolumny w ograniczonych przewijanych kartach. Podąża za motywem pakietu Office i zmienia się wraz z nim. W wąskim okienku karty układają się po trzy w dwóch rzędach; od szerokości 560 pikseli układają się w jednym rzędzie.

## Klawiatura i czytniki ekranu

Wiersze na listach projektów, tabel i wymiarów przyjmują fokus klawiatury i reagują na klawisze **Enter** i **Spacja**. Zaznaczony wiersz jest odczytywany przez czytnik ekranu, stany zaznaczenia i ostrzeżenia mają ikonę oprócz koloru, a element z fokusem klawiatury ma wyraźną obwódkę fokusu.

## Liczby

Każda liczba pokazywana w okienku zadań, taka jak liczby wierszy i kolumn oraz komunikaty o odświeżaniu, przeliczaniu, Explain, Formulas, Report i planowaniu, jest zgodna z językiem wyświetlania programu Excel. Niemiecki Excel pokazuje na przykład 4.812.233. Wartości zapisywane w komórkach nie zmieniają się.

## Powiązane

- [Instalacja PlaidXL](/pl/reference/cli/plaidxl/install/) — dodaj dodatek i otwórz okienko zadań
- [Rozwiązywanie problemów](/pl/reference/cli/plaidxl/troubleshooting/) — gdy wyskakujące okno logowania się nie otwiera lub brakuje obszaru roboczego
- [Wyświetlanie obszarów roboczych i zarządzanie nimi](/pl/administration/access/overview/viewing-and-managing-workspaces/) — obszary robocze, do których należysz
