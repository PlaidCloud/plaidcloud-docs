---
title: Konektor SAP ECC i S/4HANA
description: Skonfiguruj w PlaidCloud połączenie SAP ECC / S/4HANA, aby przez RFC włączyć do przepływów pracy dane finansowe, logistyczne i operacyjne z SAP.
sidebar:
  order: 1
  label: SAP ECC / S/4HANA
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/connectors/erp/sap-ecc.md
---

Jeden typ połączenia obejmuje zarówno SAP ECC, jak i SAP S/4HANA. Oba systemy są osiągane w ten sam sposób — przez wywołania Remote Function Call do serwera aplikacji — więc PlaidCloud nie pyta, której generacji używasz. Na ekranie **Połączenia** wybierz **Nowy → Instancja SAP ECC / S/4HANA**.

Wszystkie [kroki przepływu pracy SAP](/pl/reference/workflow-steps/sap/) działają na połączeniu tego typu. Aby przeszukiwać SAP i wyodrębniać tabele, transakcje, raporty oraz zapisane zapytania SAP Query, zobacz [Wyodrębnienia ad hoc z SAP ECC / S/4HANA](/pl/guides/connections/sap-adhoc-extract/).

## Dokumentacja producenta

SAP usunął całą dokumentację ECC i obecnie udostępnia dokumentację tylko dla [S/4HANA](https://help.sap.com/docs/SAP_S4HANA_ON-PREMISE). Interfejsy RFC używane przez PlaidCloud są wspólne dla obu systemów.

## Konfiguracja

Te pola są widoczne podczas tworzenia lub edycji połączenia.

### Opis konta

| Pole | Typ | Opis |
|---|---|---|
| Nazwa konta | Tekst | Nazwa wyświetlana tego połączenia, widoczna wszędzie tam, gdzie krok wybiera połączenie. Wymagane. |
| Notatka | Tekst (wielowierszowy) | Opcjonalne uwagi o połączeniu — na który system wskazuje, kto jest jego właścicielem. |

### Środowisko SAP

| Pole | Typ | Opis |
|---|---|---|
| Klient | Tekst | Numer klienta SAP, np. `100`. Wymagane. |
| Język | Lista wyboru | Język logowania jako dwuliterowy kod SAP. Domyślnie `EN`. Wymagane. |
| Poziom śledzenia | Lista wyboru | Szczegółowość śledzenia RFC — Wyłączony, Krótki, Szczegółowy lub Pełny. Pozostaw Wyłączony, chyba że diagnozujesz problem z połączeniem. Wymagane. |
| Typ połączenia | Przycisk opcji | **Użyj pojedynczego połączenia bezpośredniego**, aby połączyć się z jednym serwerem aplikacji, lub **Użyj połączenia wielosystemowego z równoważeniem obciążenia**, aby połączyć się przez serwer komunikatów. Poniższe pola uaktywniają się zależnie od tego wyboru. |

Wybranie **Użyj pojedynczego połączenia bezpośredniego** włącza:

| Pole | Typ | Opis |
|---|---|---|
| Host | Tekst | Nazwa hosta lub adres IP serwera aplikacji. |
| Numer systemu | Tekst | Dwucyfrowy numer systemu SAP, np. `00`. |

Wybranie **Użyj połączenia wielosystemowego z równoważeniem obciążenia** włącza:

| Pole | Typ | Opis |
|---|---|---|
| Host MS | Tekst | Nazwa hosta lub adres IP serwera komunikatów. |
| Serwer MS | Tekst | Port lub nazwa usługi serwera komunikatów. |
| ID systemu | Tekst | Trzyznakowy identyfikator systemu SAP, np. `PRD`. |
| Grupa | Tekst | Grupa logowania, między którą rozkładane jest obciążenie, np. `PUBLIC`. |

### Dane uwierzytelniające

| Pole | Typ | Opis |
|---|---|---|
| Użytkownik | Tekst | Użytkownik logowania SAP dla wywołań RFC. Wymagane. |
| Hasło | Hasło | Hasło tego użytkownika. Tylko do zapisu — podczas edycji pozostaw puste, aby zachować zapisane hasło. |

### Użycie

| Pole | Typ | Opis |
|---|---|---|
| Aktywne (zezwalaj na dostęp) | Przełącznik | Określa, czy połączenie może być używane. Wyczyść, aby wstrzymać połączenie bez usuwania. |
| Tylko do odczytu | Przełącznik | Ogranicza połączenie do operacji odczytu. |

### Model zabezpieczeń

| Pole | Typ | Opis |
|---|---|---|
| Model zabezpieczeń | Lista wyboru | Kto może używać tego połączenia — Prywatne (tylko właściciele), Tylko wybrani członkowie, Tylko wybrane grupy zabezpieczeń lub Wszyscy członkowie obszaru roboczego. |

## Testowanie połączenia

**Testuj połączenie** w oknie połączenia loguje się podanymi powyżej danymi i zwraca wynik. Gdy edytujesz istniejące połączenie i zmieniasz jakiekolwiek ustawienie, wpisz hasło ponownie przed testem — zapisane hasło nie jest wysyłane razem z edytowanymi wartościami.
