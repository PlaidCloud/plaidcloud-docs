---
title: Wyświetlanie projektów
description: Wyświetlaj i przeglądaj dostępne projekty PlaidCloud, w tym szczegóły projektu, stan, członkostwo i powiązane zasoby danych.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/projects/viewing-projects.md
---

## Opis


W **Analyze** funkcja Projekty zapewnia poziom podziału, który znacznie ułatwia kontrolowanie dostępu i modyfikowanie uprawnień. Projekty zapewniają podstawowe rozdzielenie danych w obrębie karty obszaru roboczego.



Projekty należą do Analyze, a przepływy pracy należą do projektów, co oznacza, że projekty zawierają przepływy pracy. Mówiąc prosto, przepływy pracy wykonują szeroki zakres zadań, w tym potoki transformacji danych, analizę danych, a nawet procesy ETL. Więcej informacji o przepływach pracy znajdziesz w sekcji „Przepływy pracy”.



## Dostęp do projektów


**Aby uzyskać dostęp do projektów:**


1. Otwórz Analyze
2. Wybierz „Projekty” na górnym pasku menu

Wyświetla to hierarchię projektów. Zobaczysz w niej hierarchię projektów, do których masz dostęp. W obszarze roboczym mogą istnieć dodatkowe projekty, ale jeśli nie jesteś ich właścicielem ani nie zostałeś do nich przypisany, nie będą dla Ciebie widoczne.


## Panel aktywności

Panel **Aktywność** po prawej stronie okna Projekty pokazuje, co się uruchomiło w Twoich projektach, czy się powiodło i kto co zmienił. Wyświetla aktywność wszystkich projektów, do których masz dostęp, od najnowszej, pod nagłówkiem każdego dnia. Sprawdza nowe zdarzenia mniej więcej co 15 sekund, gdy okno Projekty jest aktywnym oknem, a karta przeglądarki jest widoczna.

Nagłówek każdego dnia brzmi **Dzisiaj**, **Wczoraj** lub zawiera datę i podsumowanie wierszy z tego dnia, na przykład „12 uruchomień · Niepowodzenie: 1 · 3 zmiany”. Nagłówek dnia, który przewijasz, pozostaje na górze listy.

### Uruchomienia

Uruchomienie przepływu pracy ma jeden wiersz. Ikona pokazuje wynik, a po najechaniu na nią kursorem widać nazwę stanu: Zakończone powodzeniem, Niepowodzenie, Ostrzeżenie, Zatrzymano lub Rozpoczęto. Wiersze z niepowodzeniem lub ostrzeżeniem mają też kolorowy pasek wzdłuż lewej krawędzi.

- **Pierwszy wiersz** podaje nazwę przepływu pracy i czas: „teraz”, minuty lub godziny temu w przypadku dzisiejszych uruchomień albo godzinę w przypadku wcześniejszego dnia. Najedź kursorem na czas, aby zobaczyć pełną datę.
- **Drugi wiersz** podaje, kto uruchomił przepływ pracy i w którym projekcie, na przykład „mike: uruchomiono · CFO Services”, „Uruchomienie zaplanowane · CFO Services” lub „Uruchomienie czujnika · CFO Services”. Po prawej widać czas trwania uruchomienia albo **Niepowodzenie** lub **Zatrzymano** wraz z czasem trwania. Zatrzymane uruchomienie podaje, kto je zatrzymał.
- **Trzeci wiersz**, jeśli jest, pokazuje, co poszło nie tak. Gdy krok zakończył się niepowodzeniem lub ostrzeżeniem podczas uruchomienia, widać nazwę kroku i jego komunikat, a gdy problemy miały też inne kroki, dodatkowo „+2 więcej”. Kliknij ten wiersz, aby otworzyć przepływ pracy przy tym kroku.

Gdy uruchomienie trwa, jest wymienione w sekcji [Uruchomione teraz](#uruchomione-teraz). Po jego zakończeniu wiersz pokazuje wynik. Przepływ pracy uruchomiony przez inny przepływ pracy, przez krok Przepływ pracy: uruchom lub jako makro, nie ma własnego wiersza, a problem kroku wewnątrz niego pojawia się w wierszu uruchomienia, które go wywołało. Problem kroku, którego uruchomienia nie ma na liście, ma własny wiersz, na przykład „Niepowodzenie kroku · CRM Pipeline · CFO Services”.

Zmiany, na przykład w przepływach pracy, krokach, tabelach, wymiarach i projektach, mają po jednym wierszu, na przykład „mike: zmodyfikowano krok · CFO Services” pod nazwą kroku.

Większość wierszy otwiera to, co nazywają, po kliknięciu lub naciśnięciu na nich klawisza Enter. Uruchomienie lub przepływ pracy, który został utworzony, zmodyfikowany, zaimportowany lub wyeksportowany, otwiera jego projekt na karcie **Przepływy pracy** z zaznaczonym tym przepływem pracy. Problem kroku albo krok, który został utworzony, zmodyfikowany, usunięty, skopiowany lub przeniesiony, otwiera przepływ pracy przy tym kroku. Tabela, która została utworzona, przemianowana, opublikowana lub której publikację cofnięto, otwiera się w Eksploratorze tabel, wymiar, który został utworzony lub zmodyfikowany, otwiera się do edycji, a projekt, który został utworzony, zmodyfikowany, zaimportowany, wyeksportowany lub którego kopię zapasową utworzono albo którego zabezpieczenia zmieniono, otwiera się.

### Powtarzające się wiersze

Następujące po sobie edycje tego samego rodzaju, wykonane przez tę samą osobę na tym samym obiekcie, zwijają się w jeden wiersz, podobnie jak następujące po sobie udane uruchomienia tego samego przepływu pracy, rozpoczęte w ten sam sposób przez tę samą osobę lub ten sam harmonogram. Kliknij **3 edycje** lub **4 uruchomień** w wierszu, aby zobaczyć każde z nich, i kliknij ponownie, aby je zwinąć.

### Uruchomione teraz

Przepływy pracy, które są uruchomione teraz, są wymienione w sekcji **Uruchomione teraz** nad listą, wraz z informacją, kto je rozpoczął i jak długo trwają. Wstrzymane uruchomienie ma oznaczenie **Wstrzymano**. Kliknij nazwę przepływu pracy, aby zaznaczyć go na liście **Przepływy pracy** jego projektu, lub kliknij **Zatrzymaj**, aby zatrzymać to uruchomienie.

### Akcje po najechaniu kursorem

Najedź kursorem na wiersz uruchomienia lub przejdź do niego za pomocą klawiatury, aby wyświetlić dwa przyciski z ikonami, których podpowiedzi brzmią **Otwórz dziennik** i **Uruchom przepływ pracy**:

- **Otwórz dziennik** otwiera dziennik projektu przefiltrowany do tego przepływu pracy. Wiersz problemu kroku również ma ten przycisk.
- **Uruchom przepływ pracy** uruchamia przepływ pracy ponownie.

**Zatrzymaj** i **Uruchom przepływ pracy** są dozwolone dla tych samych członków, którzy mogą zatrzymywać i uruchamiać przepływ pracy z jego własnych ekranów. **Uruchom przepływ pracy** uruchamia cały przepływ pracy z jego ustawieniami domyślnymi, nawet jeśli uruchomienie w wierszu dotyczyło pojedynczego kroku, zakresu kroków lub symulacji.

### Problemy i filtry

Gdy w załadowanej aktywności są uruchomienia lub kroki zakończone niepowodzeniem lub ostrzeżeniem, nagłówek panelu pokazuje licznik, na przykład **2 problemów**, oznaczony jako błąd, jeśli którykolwiek z nich zakończył się niepowodzeniem. Kliknij go, aby wyświetlić tylko te wiersze.

Pasek na dole panelu wybiera, co pokazuje lista:

| Wybór | Pokazuje |
|---|---|
| **Wszystkie** | Wszystko |
| **Uruchomienia** | Uruchomienia przepływów pracy |
| **Zmiany** | Zmiany w przepływach pracy, krokach, tabelach, wymiarach, projektach i nie tylko |
| **Problemy** | Uruchomienia i kroki zakończone niepowodzeniem lub ostrzeżeniem |
| **Moje** | Twoje własne uruchomienia i zmiany |

Wpisz tekst w polu **Filtr**, aby pokazać tylko wiersze, w których nazwa przepływu pracy, projektu, kroku, tabeli, wymiaru lub członka zawiera ten tekst. Pasek kończy się liczbą pasujących zdarzeń, na przykład **12 zdarzenia**. Panel zapamiętuje w tej przeglądarce dokonany wybór.

### Nowe od ostatniej wizyty

Wiersz **Nowe od ostatniej wizyty** oddziela to, co pojawiło się od poprzedniej wizyty, od tego, co już widziano. Pokazuje się, gdy wybrano **Wszystkie** i w polu **Filtr** nic nie wpisano. Wizyta kończy się, gdy przełączysz się do innego okna lub zamkniesz okno Projekty, a wiersz przesuwa się przy kolejnym otwarciu okna Projekty lub ponownym załadowaniu strony.

### Pokaż wcześniejsze

Lista zaczyna się od ostatnich 7 dni. Kliknij **Pokaż wcześniejsze** na końcu listy, aby załadować do 500 kolejnych zdarzeń z 30 dni poprzedzających najstarsze załadowane zdarzenie, i kliknij ponownie, aby cofnąć się dalej. Przycisk znika, gdy w ciągu 30-dniowego okresu nie ma żadnej aktywności.

### Klawiatura

Naciśnij Tab, aby przejść do wiersza, a następnie użyj klawiszy strzałek w górę i w dół, aby przechodzić między wierszami, i klawisza Enter, aby otworzyć wiersz, na którym jesteś. Klawisz Tab przenosi również do akcji wiersza wyświetlanych po najechaniu kursorem.

### Ograniczenia

- **Ostatnia wizyta jest zapamiętywana dla każdej przeglądarki.** W innej przeglądarce lub na innym urządzeniu wiersz **Nowe od ostatniej wizyty** odzwierciedla Twoją ostatnią wizytę tam.
- **Liczniki opisują aktywność załadowaną w panelu.** Licznik problemów, **Problemy** i podsumowania dni obejmują początkowo najnowsze 500 zdarzeń z ostatnich 7 dni, a w miarę korzystania z **Pokaż wcześniejsze** — więcej. Nie są to sumy dla Twoich projektów.
- **Uruchomienie w kolejce jest pokazane jako Rozpoczęto** i pojawia się w sekcji **Uruchomione teraz**, gdy faktycznie się rozpocznie. Jego czas trwania liczy się od chwili umieszczenia w kolejce.
- **Problemy kroków z makra wewnątrz makra** nie są pokazywane w wierszu uruchomienia najwyższego poziomu.
- **Przepływ pracy uruchamiany często** ma wiele wierszy. Udane uruchomienia obok siebie zwijają się, ale uruchomienia dwóch przepływów pracy, które działają na zmianę, nie.
- **Uruchomienia sprzed wydania tego panelu** są pokazane jako Rozpoczęto, bez wyniku, a zatrzymania sprzed tego czasu nie pojawiają się.
- **Zdarzenie zapisane z opóźnieniem**, gdy nowsze już się pojawiły, pojawia się po ponownym załadowaniu strony.
- **Okno Projekty pozostawione otwarte i nieużywane przez ponad 30 dni** wznawia od 30 dni wstecz.
- **Gdy w ciągu ostatnich 7 dni nie było aktywności**, panel pokazuje komunikat „Brak aktywności w ostatnich 7 dniach.”, a przycisk **Pokaż wcześniejsze** się nie pojawia, więc nie można załadować wcześniejszej aktywności.
