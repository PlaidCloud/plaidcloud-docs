---
title: "Kopiowanie i wklejanie kroków"
description: Kopiuj i wklejaj kroki przepływu pracy między przepływami pracy PlaidCloud, aby ponownie wykorzystywać konfiguracje kroków i przyspieszyć tworzenie przepływów pracy.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/copy-paste-steps.md
---

## Kopiuj kroki


Często warto skopiować kroki zamiast za każdym razem zaczynać od zera. PlaidCloud umożliwia kopiowanie kroków w obrębie przepływu pracy, między przepływami pracy, a nawet do innych projektów. Można zaznaczyć i skopiować kilka kroków naraz. Zaznacz kroki przepływu pracy w hierarchii i kliknij przycisk **Kopiuj zaznaczone** u góry tabeli.



Spowoduje to umieszczenie zaznaczonych kroków w schowku i umożliwi wklejenie ich w bieżącym przepływie pracy lub w innym.

Schowek jest przechowywany w przeglądarce, więc zachowuje zawartość po ponownym załadowaniu strony i jest wspólny dla wszystkich otwartych kart PlaidCloud. Skopiuj krok w projekcie w jednej karcie, przełącz się na projekt w innej i wklej go tam. Schowek nie jest współdzielony między różnymi przeglądarkami, przeglądarkami na różnych komputerach ani z innymi osobami, a zmiana obszaru roboczego go czyści.

Jeden schowek obsługuje każde miejsce, w którym kopiujesz krok — tabelę kroków, starszą tabelę, którą otwierasz, przytrzymując Ctrl (lub Cmd) podczas otwierania przepływu pracy, oraz kanwę zaawansowanego przepływu pracy — dzięki temu możesz kopiować w dowolnym z nich i wklejać w dowolnym z nich. Skopiuj kilka kroków z tabeli i wklej je na kanwę zaawansowaną lub odwrotnie; to ten sam schowek.



Skopiowanie kroku tworzy w projekcie duplikat kroku — nowy krok z własną konfiguracją, niezależny od oryginału.

Krok może wystąpić w strukturze danego przepływu pracy co najwyżej raz. Opcje **Dołącz** i **Wstaw** zawsze wklejają nowy duplikat, więc nigdy nie napotykają tego ograniczenia. Wklejenie *odwołania* do kroku, który już umieszczono — zobacz **Wklejanie jako krok powiązany** poniżej — jest czymś innym: to ten sam krok, więc wklejenie go do przepływu pracy, który już go zawiera, w tym do przepływu pracy, z którego go skopiowano, zostaje odrzucone komunikatem wskazującym ten krok. Powiąż go zamiast tego z *innym* przepływem pracy.



## Wklej kroki


Po zaznaczeniu kroków do skopiowania i umieszczeniu ich w schowku możesz wkleić je do tego samego przepływu pracy lub do innego, nawet w innym projekcie. Podczas wklejania kroków do przepływu pracy dostępne są dwie opcje:


* Dołącz na końcu przepływu pracy
* Wstaw po ostatnim zaznaczonym wierszu

Opcja dołączania po prostu dodaje kroki na końcu wybranego przepływu pracy. Opcja wstawiania umieszcza skopiowane kroki po zaznaczonym wierszu. Pamiętaj, że jeśli do schowka skopiowano kilka kroków z różnych miejsc przepływu pracy, zostaną one wklejone w kolejności, ale bez informacji o zagnieżdżeniu hierarchii, jaką miały w momencie kopiowania. Wklejenie da płaską listę kroków do wstawienia. Może to być nieoczekiwane, ale jest bezpieczniejsze niż tworzenie w docelowym przepływie pracy całej struktury katalogów istniejącej w źródłowym przepływie pracy.


## Wklejanie jako krok powiązany


**Wklej → Dodaj kroki powiązane (zaawansowane)** umieszcza w docelowym przepływie pracy *ten sam* krok, a nie jego kopię. Oba miejsca to jeden krok: edytuj go w którymkolwiek z przepływów pracy, a zmieni się w obu, ponieważ istnieje tylko jeden krok do zmiany.


Krok powiązany można wkleić tylko do projektu, z którego został skopiowany. Powiązanie to drugie umiejscowienie kroku należącego do projektu, więc poza tym projektem nie ma sensu — jeśli wkleisz go do innego projektu, PlaidCloud odmówi i poinformuje, że należy użyć opcji **Dołącz** lub **Wstaw**, które kopiują kroki do projektu docelowego jako jego własne kroki.

Kroku powiązanego nie można też umieścić w przepływie pracy, który już go zawiera — byłby to ten sam krok dwukrotnie w strukturze jednego przepływu pracy, czego PlaidCloud nie dopuszcza. Najczęściej zdarza się to, gdy operacja powiązania wydaje się nie powieść i próbujesz ją powtórzyć: pierwsza próba faktycznie się udała, a ponowna zostaje odrzucona, aby nie uszkodzić przepływu pracy. Błąd wskazuje krok, dzięki czemu możesz potwierdzić, że już tam jest.


## Kopiowanie i wklejanie na kanwie zaawansowanej


W zaawansowanym przepływie pracy możesz kopiować i wklejać kroki bezpośrednio na kanwie za pomocą klawiatury, a powiązania między nimi zostaną przeniesione.


Zaznacz potrzebne kroki — przeciągnij ramkę wokół nich albo kliknij jeden i dodaj kolejne z klawiszem Shift lub Ctrl/Cmd — i naciśnij **Ctrl/Cmd+C**. Przejdź do przepływu pracy, w którym mają się znaleźć, w tym projekcie lub w innym, wskaż miejsce docelowe i naciśnij **Ctrl/Cmd+V**. Kroki zostaną skopiowane, ułożone tak jak wcześniej, i pozostaną zaznaczone, abyś mógł je przeciągnąć na miejsce. Obie czynności możesz też wykonać bez klawiatury. Kliknij prawym przyciskiem puste miejsce na kanwie i wybierz **Kopiuj N kroków** (widoczne po zaznaczeniu kroków) lub **Wklej N kroków tutaj** (widoczne, gdy schowek zawiera kroki); wklejone kroki trafią w miejsce kliknięcia. Gdy schowek zawiera kroki, na pasku narzędzi widać „N kroków z *przepływu pracy*" oraz przycisk **Wklej**, który wkleja je na środek widocznej części kanwy.


**Grupa jest wklejana jako grupa.** Kliknij nagłówek grupy, a zostaną zaznaczone razem grupa i wszystkie jej kroki; skopiuj, a ramka grupy i jej członkowie zostaną wklejeni jako całość. Ramka zaznaczenia narysowana wokół całej grupy zaznacza ją w ten sam sposób.


**Powiązania między skopiowanymi krokami są przenoszone; powiązania z krokami, których nie skopiowano, nie.** Krok z zaznaczenia, do którego prowadziło powiązanie z pozostawionego kroku, zostaje wklejony bez tego powiązania przychodzącego — po drugiej stronie nie ma z czym go połączyć. Wklejenie informuje o takiej sytuacji, więc utracone połączenie nigdy nie pozostaje niezauważone.


**Wklejenie do tego samego przepływu pracy** przesuwa kopie nieznacznie, aby nie wylądowały dokładnie na oryginałach. Wklejenie do przepływu pracy, który nie jest zaawansowany — zwykłej tabeli kroków — pomija układ kanwy i powiązania i po prostu dodaje kroki; wklejenie informuje o tym.


**Duże wklejenie jest wykonywane automatycznie w partiach.** Nic nie jest ograniczane i nic nie jest po cichu pomijane — wklejenie setek kroków po prostu pokazuje postęp w trakcie pracy i można je anulować. Jeśli wklejenia nie da się dokończyć, dodane już kroki są usuwane, aby nie zostawić częściowo wklejonego przepływu pracy; w rzadkim przypadku, gdy nie można usunąć niektórych z nich automatycznie, komunikat o tym informuje i podaje, ile ich pozostało, zamiast twierdzić, że wycofanie przebiegło bez śladu.


**Aby cofnąć wklejenie,** naciśnij **Ctrl/Cmd+Z** zaraz po nim — wklejone kroki zostaną usunięte. Gdy współpracownik zmieni przepływ pracy lub załadujesz go ponownie, to jednokrokowe cofnięcie przestaje działać, aby nie usunąć pracy, która nie jest już wyłącznie Twoja.


Kroki są kopiowane jako nowe, własne kroki. Wklejanie *tego samego* kroku w więcej niż jedno miejsce — opisane wyżej zachowanie kroków powiązanych — jest akcją tabeli kroków; na kanwie użyj opcji **Dodaj krok**, aby umieścić odwołanie w przepływie pracy, który jeszcze nie zawiera tego kroku.
