---
title: Dlaczego alokacje są przydatne
description: Dowiedz się, dlaczego alokacje kosztów w PlaidCloud są przydatne w rachunku kosztów działań, rozliczeniach wewnętrznych i analizie rentowności.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/getting-started/why-are-allocations-useful.md
---

Alokacje rozdzielają pulę wartości (zwykle kosztów, ale działa to dla dowolnej wartości zagregowanej) między odbiorców na podstawie mierzalnego nośnika. Odpowiadają na pytanie: *jeśli ponosimy dany koszt, jak należy go przypisać do tego, co go generuje?*

## Typowe przypadki użycia

### Rachunek kosztów działań

Znasz łączne wydatki na marketing w danym kwartale. Chcesz przypisać je do konkretnych produktów na podstawie czegoś mierzalnego, na przykład godzin kampanii, liczby pozyskanych leadów lub kwalifikowanych szans sprzedaży. Alokacja rozdziela pulę marketingową między produkty według wybranego nośnika, dzięki czemu każdy produkt otrzymuje pełny koszt.

### Rozliczanie kosztów IT

Wydajesz kwotę X na utrzymanie współdzielonej infrastruktury (moc obliczeniowa, przestrzeń dyskowa, licencje). Każda jednostka biznesowa zużywa jej inną ilość. Alokacja rozdziela koszt IT między jednostki na podstawie wskaźników zużycia, takich jak godziny maszyn wirtualnych, GB przestrzeni dyskowej czy liczba licencji, aby rachunek zysków i strat każdej jednostki odzwierciedlał rzeczywiste zużycie.

### Dystrybucja usług wspólnych

Finanse, HR, dział prawny, zarządzanie obiektami: funkcje centralne obsługujące całą firmę. Alokacje rozdzielają ich koszt między obsługiwane działy, zazwyczaj według liczby pracowników, przychodów lub ważonej kombinacji obu.

### Ceny transferowe

W organizacjach wielojednostkowych alokacje modelują sposób wyceny usług wewnętrznych między jednostkami. Wynik stanowi podstawę zapisów dziennika dla rozliczeń wewnątrzgrupowych.

### Analiza rentowności

Masz przychody na poziomie produktu lub klienta. Masz koszty w różnych pulach (sprzedaż, wsparcie, infrastruktura, koszt własny sprzedaży). Alokacje łączą wszystko na poziomie szczegółowości produktu lub klienta, dzięki czemu widzisz rzeczywistą marżę.

### Kalkulacja kosztów według zestawienia materiałowego

Koszt przepływa w dół hierarchii komponentów. Każdy krok w zestawieniu materiałowym jest alokacją: koszty podzespołów rozdzielane są na zespoły, zespoły na wyroby gotowe, a wyroby gotowe na jednostki SKU.

## Przed czym chronią Cię alokacje

Bez silnika alokacji budowałbyś takie modele w arkuszach kalkulacyjnych, które są kruche, trudne do audytu i trudne do powtórzenia po aktualizacji danych. Alokacje PlaidCloud zapewniają:

- **Powtarzalne modele**, które uruchamiają się ponownie automatycznie po odświeżeniu danych źródłowych
- **Ścieżkę audytu** pokazującą, które wiersze źródłowe przyczyniły się do powstania których wierszy docelowych
- **Alokacje warstwowe**, w których wyniki zasilają kolejne alokacje
- **Integrację wymiarową**, dzięki której alokacje uwzględniają istniejące hierarchie

## Następne kroki

- [Szybki start z alokacjami](/pl/guides/allocations/getting-started/allocations-quick-start/) — zbuduj alokację w 30 minut
- [Tagowanie według reguł](/pl/guides/allocations/getting-started/rule-based-tagging/) — steruj zachowaniem alokacji dla poszczególnych wierszy
- [Konfigurowanie alokacji](/pl/guides/allocations/setup/configure-an-allocation/) — pełne omówienie konfiguracji
