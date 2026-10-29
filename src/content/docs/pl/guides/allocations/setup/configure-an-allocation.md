---
title: Konfigurowanie alokacji
description: Skonfiguruj alokację PlaidCloud, w tym dane źródłowe, dane sterujące, mapowanie celów, metody alokacji i opcje przetwarzania.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/setup/configure-an-allocation.md
---

## Cel

Alokacje umożliwiają rozbicie wartości (zazwyczaj kosztów) na bardziej szczegółowy poziom przez zastosowanie klucza alokacji. Alokacje służą wielu celom, w tym między innymi **Activity-Based Costing**, **IT & Shared Service Chargeback**, obliczaniu pełnego kosztu wytworzenia i dostarczenia klientom towaru lub usługi itp. Są podstawowym narzędziem analizy finansowej i fundamentem operacji raportowania zarządczego, takich jak **Customer & Product Profitability**. Są też przydatnym mechanizmem do ustalania i zarządzania globalnymi cenami transferowymi towarów i usług między spółkami powiązanymi.

## Konfigurowanie transformacji alokacji

W praktyce alokacje konfiguruje się w PlaidCloud podobnie jak inne transformacje danych, takie jak złączenia i wyszukiwania. Aby transformacja alokacji zakończyła się powodzeniem, trzeba ustawić cztery parametry konfiguracji.

1. **Określ dane przed alokacją**: wskaż tabelę danych przed alokacją w sekcji **Tabela wartości do alokacji** transformacji alokacji.
2. **Określ dane sterujące**: dane sterujące będą podstawą współczynników używanych w alokacji. Wybierz tabelę danych sterujących w sekcji **Tabela danych sterujących** transformacji alokacji.
3. **Określ tabelę wyników**: dane po alokacji muszą być zapisane w tabeli. Wskaż tabelę w sekcji **Tabela wyników alokacji** w części wyników transformacji alokacji.
4. **Określ wymiar przypisania**: alokacje wymagają wymiaru przypisania, którego celem jest określenie, jak zostanie przypisany każdy rekord lub zestaw rekordów danych przed alokacją. Wskaż wymiar przypisania w sekcji **Hierarchia wymiaru przypisania** transformacji alokacji.

Poza tymi czterema, dwie karty mapowania wymagają ustawienia **Role** kolumn, zanim krok się zapisze: kolumna **Wartość do alokacji** w **Mapa źródła alokacji** oraz kolumny **Wartość podziału**, **Relacja ze źródłem (mianownik)** i **Cel alokacji (licznik)** w **Mapa danych sterujących**. PlaidCloud sprawdza je podczas zapisu i wskazuje, czego brakuje — zobacz [Rozwiązywanie problemów z alokacjami](/pl/guides/allocations/results/troubleshooting-allocations/#dlaczego-nie-można-zapisać-kroku-alokacji).

## Kluczowe pojęcia

Suma wartości w zaalokowanym zbiorze danych powinna zgadzać się z sumą wartości w źródłowych danych przed alokacją

Alokacje są dostępne w PlaidCloud jako opcja transformacji. Aby skonfigurować alokację, najpierw skonfiguruj przypisania, a następnie skonfiguruj transformację alokacji tak, aby używała przypisań do alokowania rekordów przychodzących za pomocą wskazanej tabeli sterującej.

Przypisania to specjalne wymiary. Są dostępne w sekcji Wymiary projektu PlaidCloud.

Aby skonfigurować wymiar przypisania, wykonaj następujące kroki:

1. Na ekranie projektu przejdź do karty Wymiary
2. Utwórz nowy wymiar
