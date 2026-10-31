---
title: Alokacje rekurencyjne i wzajemne
description: Modeluj wieloprzebiegowy i wzajemny rozdział kosztów w PlaidCloud, łącząc kroki alokacji w jawne, etapowe przebiegi.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/setup/recursive-allocations.md
---

Niektóre modele kosztów wymagają, aby cel jednej alokacji stał się *źródłem* następnej — na przykład usługi wspólne, które wzajemnie z siebie korzystają (IT obsługuje HR, ale HR obsługuje także IT). PlaidCloud modeluje to przez **łączenie kroków alokacji w jawne, etapowe przebiegi**, a nie za pomocą jednego automatycznego solwera.

## Kiedy potrzebujesz wielu przebiegów

- **Usługi wzajemne** — dwie pule kosztów, które wzajemnie z siebie korzystają.
- **Warstwowe rozdziały** — koszty działów kaskadowo przechodzą przez hierarchię, a niższe poziomy muszą przejąć koszty wyższych poziomów przed ponowną alokacją.
- **Iteracyjne bilansowanie** — model zbliża się do stabilnego wyniku po kilku przebiegach (pula A alokuje część do B, B alokuje część z powrotem itd.).

## Jak to zamodelować

PlaidCloud **nie ma wbudowanego „trybu rekurencji” ani automatycznego solwera zbieżności**. Rekurencję budujesz samodzielnie, dodając osobny [krok allocation split](/pl/reference/workflow-steps/allocation/allocation-split/) dla każdego przebiegu i łącząc je w sekwencję:

1. Uruchom pierwszy przebieg jako zwykły allocation split.
2. W następnym przebiegu zbuduj źródło zawierające wynik poprzedniego przebiegu — zwykle przez połączenie (union) lub złączenie poprzedniego wyniku z powrotem z pulą — i zaalokuj ponownie.
3. Powtarzaj tyle przebiegów, ile potrzebuje Twój model.

Ponieważ każdy przebieg jest jawnym krokiem, **to Ty decydujesz, ile przebiegów zostanie uruchomionych**. Silnik nie rozwiązuje relacji wzajemnej jako jednego równoczesnego równania i nie ma ustawienia tolerancji, które automatycznie zatrzymałoby pętlę. Dodawaj przebiegi, aż reszta do ponownej alokacji będzie dla Twoich celów dostatecznie mała.

## Wskazówki

- Zacznij od alokacji **jednoprzebiegowej** i upewnij się, że prosty model zachowuje się zgodnie z oczekiwaniami, zanim dodasz przebiegi.
- Po każdym przebiegu sprawdź pozostałą niezaalokowaną resztę. Jeśli nie maleje z przebiegu na przebieg, wróć do relacji kluczy alokacji — prawdziwa zależność cykliczna nie ustabilizuje się, ile przebiegów by nie dodać.
- Każdy przebieg ponownie przetwarza swoje źródło, więc rekurencja jest kosztowna na dużych zbiorach danych. Przetestuj na fragmencie, zanim uruchomisz na pełnym źródle.

## Powiązane

- [Konfigurowanie alokacji](/pl/guides/allocations/setup/configure-an-allocation/) — konfiguracja podstawowa
- [Krok Allocation Split](/pl/reference/workflow-steps/allocation/allocation-split/) — krok przepływu pracy, który łączysz dla każdego przebiegu
- [Rozwiązywanie problemów z alokacjami](/pl/guides/allocations/results/troubleshooting-allocations/) — gdy reszty nie mają sensu
