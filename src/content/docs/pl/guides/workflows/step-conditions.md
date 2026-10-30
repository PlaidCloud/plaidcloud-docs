---
title: Warunkowe wykonywanie kroków
description: Skonfiguruj warunkowe wykonywanie kroków przepływu pracy PlaidCloud, aby kontrolować, które kroki są uruchamiane, na podstawie wartości zmiennych i logiki.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/step-conditions.md
---

## Przegląd

Kroki przepływu pracy zwykle wykonują się w kolejności zdefiniowanej dla przepływu pracy. Często jednak przydatne jest, aby niektóre kroki wykonywały się tylko wtedy, gdy zostaną spełnione z góry określone warunki. Dzięki warunkom kroków możesz kontrolować wykonywanie na podstawie następujących opcji:
 - Wartości zmiennych
 - Tabela ma wiersze lub jest pusta
 - Tabela istnieje lub nie istnieje
 - Plik istnieje w Document
 - Pliku brakuje w Document
 - Wynik zapytania do tabeli
 - Spełnione są warunki daty i godziny

Do porównań zmiennych lub wyników zapytań do tabeli możesz używać następujących porównań:
 - Równe
 - Nie równa się
 - Zawiera
 - Nie zawiera
 - Zaczyna się od
 - Kończy się na
 - Większe niż
 - Mniejsze niż
 - Większe lub równe
 - Mniejsze lub równe

Ważne jest również to, że możesz mieć wiele warunków, które muszą zostać spełnione, aby krok się wykonał. To potężne narzędzie do dokładnego kontrolowania, kiedy krok ma się wykonać.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 640 190" role="img" aria-label="Warunek kroku decyduje, czy krok zostanie uruchomiony. Gdy poprzedni krok się zakończy, warunek jest sprawdzany; jeśli jest spełniony, krok się uruchamia, w przeciwnym razie krok jest pomijany, a przepływ pracy przechodzi do następnego kroku." style="width:100%;max-width:640px;height:auto;">
  <defs><marker id="sc3-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="74" width="104" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="66" y="100" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">poprzedni krok</text>
  <path d="M118 96 L150 96" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#sc3-arrow)" />
  <rect x="152" y="66" width="150" height="60" rx="10" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="227" y="90" text-anchor="middle" font-size="12" font-weight="700" fill="var(--sl-color-text)">warunek spełniony?</text>
  <text x="227" y="108" text-anchor="middle" font-size="9" fill="var(--sl-color-gray-3)">zmienna · wiersze · dokument istnieje</text>
  <path d="M302 82 C340 82 350 54 384 54" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#sc3-arrow)" />
  <text x="345" y="48" text-anchor="middle" font-size="10" fill="var(--sl-color-accent)">prawda</text>
  <path d="M302 110 C340 110 350 138 384 138" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" stroke-dasharray="5 4" marker-end="url(#sc3-arrow)" />
  <text x="345" y="132" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">fałsz</text>
  <rect x="386" y="34" width="128" height="40" rx="8" fill="var(--sl-color-accent)" fill-opacity="0.12" stroke="var(--sl-color-accent)" stroke-width="1.6" />
  <text x="450" y="59" text-anchor="middle" font-size="11" font-weight="700" fill="var(--sl-color-text)">krok się uruchamia</text>
  <rect x="386" y="118" width="128" height="40" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" stroke-dasharray="5 4" />
  <text x="450" y="143" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">krok pominięty</text>
  <path d="M514 54 C548 54 556 96 578 96" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#sc3-arrow)" />
  <path d="M514 138 C548 138 556 96 578 96" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#sc3-arrow)" />
  <text x="606" y="100" text-anchor="middle" font-size="10" fill="var(--sl-color-text)">dalej</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Warunek decyduje o kroku: spełniony → krok się uruchamia; niespełniony → jest pomijany. W obu przypadkach przepływ pracy przechodzi do następnego kroku. Warunki sprawdzają zmienne, to, czy tabela ma wiersze, lub to, czy dokument istnieje.</figcaption>
</figure>

## Dodawanie warunków i zarządzanie nimi

Aby włączyć i dodać warunki do kroku:
1) Znajdź krok, do którego chcesz dodać warunek
2) Kliknij krok prawym przyciskiem myszy i wybierz **Edytuj szczegóły kroku** albo kliknij jego ikonę koła zębatego i przejdź na kartę **Ogólne**
3) Przewiń do sekcji **Sprawdzenia warunków** u dołu karty **Ogólne**
4) Zaznacz pole wyboru **Sprawdź warunki przed uruchomieniem**, aby włączyć okno dialogowe i dodawać warunki.
5) W sekcji **Sprawdzenia warunków** po lewej stronie wybierz „+”, aby dodać nowy warunek
6) Dodaj warunek z sekcji z kartami po prawej stronie
7) Powtarzaj kroki 5 i 6 według potrzeb, aby dodać wszystkie warunki

## Wyświetlanie warunków na kanwie wizualnej

Warunki kroku są widoczne na kanwie wizualnej bez otwierania kroku. Łącznik prowadzący do kroku warunkowego jest **przerywany** i ma małą **tarczę** przy grocie strzałki. Przerywana linia pozwala rozpoznać warunek, gdy oddalisz widok tak bardzo, że tarcza jest zbyt mała, by ją dostrzec.

Kliknij tarczę, aby otworzyć krok z już przewiniętymi do widoku **Sprawdzeniami warunków** — możesz też kliknąć łącznik prawym przyciskiem myszy i wybrać **Edytuj warunki…**, co robi to samo. Tarcza na kafelku samego kroku, w lewym dolnym rogu, nadal oznacza krok jako warunkowy, tak jak dotychczas.

W dwóch przypadkach z założenia nie ma tarczy na strzałce:

- **Krok bez łącznika przychodzącego.** Krok uzależniony od daty lub zmiennej może znajdować się na początku przepływu pracy, bez niczego, co do niego prowadzi. Nie ma strzałki do oznaczenia, więc pojawia się tylko tarcza na kafelku.
- **Krok wewnątrz zwiniętej grupy.** Jego kafelek jest złożony w kafelek grupy, a strzałka kotwiczy się w grupie, nie w kroku, więc oznaczenie go przypisałoby warunek niewłaściwemu elementowi.

Krok z kilkoma łącznikami przychodzącymi dostaje jedną tarczę, a nie jedną na strzałkę.

:::note
Otwarcie warunków w ten sposób przenosi do sprawdzeń warunków w typach kroków korzystających z natywnego formularza kroku. Typ kroku, który nadal otwiera starsze okno konfiguracji, otwiera je od góry — warunki tam są, tylko nie są przewinięte do widoku.
:::

### Co tarcza pokazuje jako sprawdzane

Podpowiedź tarczy wymienia to, co krok faktycznie sprawdza, zamiast tylko informować,
że coś sprawdza:

```
Table Row Count (sales_2026) > 0 where region = 'EU'
Day of Week = Monday (UTC+2)
Project Variable (run_mode) = "full"
```

Wymienione są maksymalnie trzy sprawdzenia, a po nich liczba pozostałych — *…and 2 more checks* — aby
lista pozostała czytelna w kroku z wieloma warunkami. To samo podsumowanie pojawia się na
tarczy kafelka samego kroku, która jest jedyną, jaką ma krok bez łącznika przychodzącego.

Zaznaczenie kroku umieszcza tę samą listę w sekcji **Warunki** panelu
Inspektora, który jest wygodniejszym miejscem do czytania długiej listy.

Kilka rzeczy, jakich można się spodziewać po sformułowaniach:

- **Sprawdzenia dnia i miesiąca są czytane jako nazwy**, a nie liczby, pod którymi są przechowywane — *Day of
  Week = Monday*, a nie *Day of Week = 3*.
- **Strefa czasowa pojawia się tylko wtedy, gdy nie jest to UTC**, jak w *(UTC+2)* powyżej.
- **Filtr w sprawdzeniu tabeli jest pokazany** po `where`, skrócony, jeśli jest długi.
- **Porównanie zagregowane jest jako takie oznaczone** — *Query Value (aggregated sales_2026.amount) >=
  100* porównuje sumę w całej tabeli, podczas gdy *Query Value (sales_2026.amount) >= 100*
  porównuje wartość pojedynczego wiersza.
- **Sprawdzenie dokumentu pokazuje ścieżkę, ale nie konto.** Dwa warunki sprawdzające
  tę samą ścieżkę na różnych kontach Document wyglądają identycznie; otwórz krok, aby je
  odróżnić.
- **Tabela wybrana w przeglądarce drzewa jest pokazana z nazwą**, gdy przepływ pracy odczytuje lub
  zapisuje tę tabelę gdziekolwiek. Jeśli nie, sprawdzenie jest wymienione bez nazwy tabeli,
  a nie z wewnętrznym identyfikatorem.


### Ile kosztowałaby bramka

Najedź kursorem na tarczę bez klikania, a kanwa otoczy przerywanym podświetleniem krok warunkowy i wszystko, co jest za nim — kroki, które nie zostałyby uruchomione, gdyby ten warunek zablokował przepływ. Nic się nie zmienia; odsuń wskaźnik, a podświetlenie zniknie. Kroki *przed* nim nigdy nie są podświetlane: uruchamiają się tak czy inaczej.

To ten sam podgląd, który daje znacznik **wyłączone** wyłączonej grupy, z jedną różnicą w sformułowaniu, która ma znaczenie. Wyłączona grupa naprawdę jest wyłączona, więc jej znacznik mówi, ile kroków *zostanie* pominiętych. Warunek jest oceniany dopiero wtedy, gdy uruchomienie do niego dotrze, więc tarcza mówi, ile kroków *nie zostałoby uruchomionych*, **jeśli** warunek zablokuje przepływ. Równie dobrze może przepuścić wszystko.

### Co tarcza mówi o ostatnim uruchomieniu

Tarcza pokazuje także, co się stało podczas ostatniego uruchomienia, dzięki czemu możesz prześledzić zakończony przepływ i zobaczyć, gdzie się zatrzymał:

| Tarcza | Znaczenie |
| --- | --- |
| Zwykła tarcza | Krok jest warunkowy. Albo jeszcze się nie uruchomił, albo właśnie jest uruchomiony. |
| Tarcza ze znakiem **+** | Krok został uruchomiony podczas ostatniego uruchomienia. |
| Tarcza ze znakiem **−** | Krok nie został uruchomiony podczas ostatniego uruchomienia. |

Te trzy odróżnia się po kształcie, a nie po kolorze, a podpowiedź tarczy opisuje stan słowami. Aktualizuje się na żywo podczas uruchomienia przepływu pracy, więc nie musisz przeładowywać kanwy, aby obserwować, jak uruchomienie dociera do bramki.

:::caution
Tarcza ze znakiem **−** mówi, że krok nie został uruchomiony. Nie mówi, *dlaczego*, i nie należy odczytywać tego jako „warunek go zablokował”. Krok jest też zapisywany jako nieuruchomiony, gdy jest wyłączony, gdy jego grupa jest wyłączona, gdy krok przed nim zakończył się błędem lub gdy znalazł się poza zakresem częściowego uruchomienia. Przycisk **Wyświetl dzienniki** na pasku narzędzi otwiera [dziennik uruchomienia](/pl/guides/workflows/viewing-workflow-log/), który podaje powód każdego pominiętego kroku. Jedynym celowo wyłączonym przypadkiem jest krok zatrzymany w punkcie przerwania — zachowuje zwykłą tarczę, ponieważ zatrzymanie w tym miejscu było Twoją decyzją, a nie wynikiem uruchomienia.
:::


## Zarządzanie warunkami

W sekcji **Sprawdzenia warunków** możesz dodać tyle warunków, ile potrzeba. Dodając je, warto nadać im użyteczne nazwy, aby łatwo je później znaleźć.

Po dodaniu warunku wybierz go po lewej stronie, a kryteria oceny warunku będzie można edytować po prawej.

Aby zmienić nazwę warunku, wybierz go i edytuj pole **Nazwa** u góry panelu Konfiguracja po prawej stronie — albo kliknij warunek na liście dwukrotnie. Możesz też kliknąć warunek prawym przyciskiem myszy, aby użyć **Zmień nazwę** i **Usuń**; **Usuń** jest także dostępne pod przyciskiem „−” nad listą.

Warunek bez wybranego typu — na przykład przeniesiony ze starszego lub zaimportowanego przepływu pracy — nie może zostać oceniony. Jest traktowany jako niespełniony, więc krok jest pomijany, a komunikat kroku mówi, że warunek nie określa, co sprawdzać. Otwórz warunek i wybierz, co ma sprawdzać.


## Warunki zmiennych

Przy sprawdzaniu warunków zmiennych należy uzupełnić sekcję **Value Check Parameters**, aby można było wykonać porównanie.

W polu **Variable or Table Field** wpisz nazwę zmiennej. Wybierz typ porównania i wpisz wartość porównania.


## Podstawowe warunki tabeli

Jeśli warunek sprawdza, czy tabela ma wiersze, czy jest pusta, musisz też zdefiniować tabelę na karcie **Wybór danych tabeli**.


## Warunki istnienia tabeli

Warunek istnienia tabeli uruchamia krok tylko wtedy, gdy tabela została utworzona w hurtowni danych, albo tylko wtedy, gdy nie została. Nigdy nie odczytuje wierszy tabeli, a tabela zapisana z zerem wierszy istnieje. Nazwa tabeli, która nie pasuje do żadnej tabeli w projekcie, jest traktowana jako brakująca. Użyj go, aby zbudować tabelę przy pierwszym uruchomieniu i potem jej nie ruszać, albo aby pominąć krok odczytujący tabelę, której wcześniejszy krok mógł nie utworzyć.

Dwa typy sprawdzenia to `radio_table_exists` i `radio_table_not_exists`. Tabelę wybierasz tak samo jak w podstawowym warunku tabeli. Ustaw warunek za pomocą asystenta AI lub interfejsu API REST; karta **Sprawdzenia warunków** jeszcze go nie wymienia.

## Zaawansowane warunki tabeli

Przy użyciu zaawansowanych warunków tabeli należy uzupełnić sekcję **Value Check Parameters**, aby można było wykonać porównanie.

W polu **Variable or Table Field** wpisz nazwę pola z wyboru tabeli. Wybierz typ porównania i wpisz wartość porównania.

Na karcie **Wybór danych tabeli** wybierz tabelę i uzupełnij sekcję mapowania danych, podając co najmniej pole użyte w porównaniu warunku.

## Warunki ścieżki dokumentu

Jeśli warunek sprawdza, czy plik istnieje, wymaga to wybrania konta dokumentów i podania ścieżki dokumentu do sprawdzenia na karcie **Ścieżka dokumentu**. Folder pod tą ścieżką jest traktowany jako brakujący, ponieważ sprawdzany jest plik.

## Warunki daty i godziny

W przypadku wyborów daty lub godziny możesz dodać wiele warunków, jeśli potrzebna jest kombinacja warunków. Na przykład, jeśli chcesz, aby krok uruchamiał się tylko w poniedziałki o 2:05, utworzysz trzy warunki:
 - Warunek dnia tygodnia ustawiony na poniedziałek (1)
 - Godzina dnia ustawiona na 2
 - Minuta godziny ustawiona na 5

### Przesunięcie strefy czasowej

Każdy warunek daty i godziny ma własne **Przesunięcie strefy czasowej**, wymienione jako przesunięcie o całą liczbę godzin, nazwane od reprezentatywnej strefy — na przykład *Eastern Time (US & Canada) (UTC -5)* lub *Asia/Tokyo (UTC +9)*. Wprowadzone godziny są porównywane z zegarem w tej strefie.

Nowy warunek zaczyna od przesunięcia zgłaszanego przez przeglądarkę, więc w większości przypadków możesz je zostawić. Ustaw je świadomie, gdy harmonogram dotyczy innego miejsca niż to, w którym jesteś — na przykład zamknięcie, które działa według zegara zespołu finansowego. Dostępne są tylko pełne godziny, więc strefę z półgodzinnym przesunięciem, taką jak Indie (UTC +5:30), trzeba zaokrąglić do najbliższej pełnej godziny.

Warunek zapisany, zanim to ustawienie weszło w życie, nadal jest oceniany względem UTC, dopóki nie wybierzesz dla niego strefy, więc istniejące warunki zachowują się dokładnie tak jak dotąd.

:::caution
Warunki **Day of the week** obecnie porównują z UTC niezależnie od wybranego przesunięcia. Jeśli warunek dnia tygodnia ma przypadać na konkretny dzień w strefie odległej od UTC, pamiętaj, że może on różnić się od Twojego lokalnego dnia przez kilka godzin przed północą i po niej.
:::

### Dzień roboczy zamknięcia finansowego

Dla **Use Financial Close Workday** odliczanie zaczyna się od **0 dla 1. dnia miesiąca** — jak mówi podpowiedź obok pola. Zamknięcie, które odbywa się 5. dnia miesiąca, to więc `4`, a nie `5`.

:::caution
Ten warunek obecnie nigdy się nie spełnia, więc krok chroniony takim warunkiem nie zostanie uruchomiony. Do czasu rozwiązania tego problemu użyj warunku **Day of the month**. Wartości ujemne, przeznaczone do liczenia od końca miesiąca, również nie działają.
:::

## Ustawianie warunków za pomocą asystenta AI

Asystent AI połączony z Twoim obszarem roboczym może dodawać i zmieniać warunki kroku za Ciebie, zarówno podczas tworzenia kroku, jak i edycji istniejącego. Dostępny jest dla niego każdy opisany wcześniej typ warunku z wyjątkiem **Sprawdź zamknięcie finansowe Workday**: asystent może go zapisać, ale nigdy się nie spełnia, więc asystent ostrzega Cię zamiast pozwolić, by przeszło to niezauważone. Ten jeden ustaw samodzielnie na karcie **Warunki**.

Trzy rzeczy działają inaczej niż przy ręcznej edycji warunków:

- **Cała lista jest za każdym razem zastępowana.** Poproś o dodanie lub zmianę jednego warunku, a asystent wyśle pełną listę, więc każdy pominięty przez niego warunek zostanie usunięty. Jeśli nie masz pewności, że asystent ma je wszystkie, poproś go o wyświetlenie bieżących warunków kroku przed zapisem.
- **Warunek, którego nie można ocenić, jest odrzucany.** Warunek, który nie określa, co sprawdza, jest odrzucany zamiast zapisany, a krok zachowuje warunki, które już miał. Popraw żądanie i poproś ponownie.
- **Niekompletny warunek jest zapisywany z ostrzeżeniem.** Warunek bez wartości, z którą ma porównywać, lub warunki dodane bez zaznaczonego **Sprawdź warunki przed uruchomieniem** są zapisywane i zgłaszane jako ostrzeżenie. Otwórz kartę **Warunki** i dokończ je, bo w przeciwnym razie krok nie zachowa się tak, jak prosisz.

Asystent AI może też ustawić blokadę kroku, jego widoczność w widokach Menedżera i Eksploratora, ustawienia ponawiania oraz krok, do którego przejść w razie błędu.
