---
title: "TM1: zapytanie do kostki (agent)"
description: "Odczytaj wycinek kostki z lokalnego serwera IBM TM1 / Planning Analytics, do którego chmura nie ma bezpośredniego dostępu — to samo zapytanie widoku/MDX/punktu widzenia co w kroku TM1: zapytanie do kostki, przekazywane przez zainstalowanego agenta PlaidLink."
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/ibm-planning-analytics/tm1-query-remote.md
---

## Opis

Lokalny odpowiednik kroku [TM1: zapytanie do kostki](/pl/reference/workflow-steps/ibm-planning-analytics/tm1-query/): ten sam odczyt — zapisany **widok** lub zapytanie **MDX** do kostki TM1, z opcjonalnym wycinkiem punktu widzenia (POV), zapisywany jako tabela projektu — przekazywany przez zainstalowanego [agenta PlaidLink](/pl/reference/cli/plaidlink/) w Twojej sieci zamiast wywoływany bezpośrednio z chmury. Użyj tego kroku zamiast TM1: zapytanie do kostki, gdy serwer TM1 jest osiągalny tylko z wnętrza Twojej sieci.

Ten krok pojawia się w menu kroków w sekcji **IBM TM1 / Planning Analytics**.

## Czym różni się od kroku TM1: zapytanie do kostki

| | TM1: zapytanie do kostki | TM1: zapytanie do kostki (agent) |
|---|---|---|
| Transport | Bezpośrednio z chmury przez REST | Przekazywany do agenta PlaidLink w Twojej sieci |
| Pola konfiguracji | — | Identyczne, plus wymagany **Agent** |
| Wykrywanie kostki / widoku | Na żywo, z połączonej bazy danych | Niedostępne — wpisz nazwy ręcznie |
| Podgląd przed zapisem | Tak | Niedostępny |

Wszystko inne — połączenie, baza danych, wybór widoku/MDX, wycinek punktu widzenia, Pomijaj komórki zerowe/puste, Limit wierszy i wzorzec przyrostowego wyodrębniania według okresu — działa dokładnie tak, jak opisano na stronie [TM1: zapytanie do kostki](/pl/reference/workflow-steps/ibm-planning-analytics/tm1-query/). Tylko poniższe różnice dotyczą wyłącznie tego kroku.

## Konfiguracja

### Źródło i cel

| Pole | Wymagane | Uwagi |
|---|---|---|
| Agent | Tak | Agent PlaidLink, do którego przekazywany jest ten odczyt. Jego kompilacja musi zawierać obsługę TM1 (zobacz [Wymagania](#wymagania) poniżej). |
| Połączenie TM1 | Tak | [Połączenie TM1](/pl/guides/connections/tm1/), przez które odbywa się odczyt. Selektor połączeń nie jest filtrowany według wybranego agenta — udostępnij połączenie agentowi osobno (zobacz niżej). |
| Środowisko | Tak | Środowisko połączenia. |
| Baza danych | Tak | Baza danych TM1 (instancja) do odpytania. |
| Kostka | Tak | Kostka TM1 do odpytania. Wpisywana ręcznie — ten krok nie ma wykrywania na żywo. |
| Tabela docelowa | Tak | Tabela projektu, w której ląduje zwrócony zestaw komórek. |

### Wycinek i opcje

Te same pola co w [TM1: zapytanie do kostki](/pl/reference/workflow-steps/ibm-planning-analytics/tm1-query/#wycinek) — Tryb źródła (Według widoku / Według MDX), Widok, MDX, Punkt widzenia, Pomijaj komórki zerowe/puste i Limit wierszy — wszystkie wpisywane, a nie wykrywane, i wszystkie sprawdzane podczas uruchamiania kroku, a nie w podglądzie.

## Brak wykrywania za pośrednictwem agenta

Selektory Kostka, Widok i Wymiar w kroku TM1: zapytanie do kostki odpytują połączony serwer na żywo podczas edycji kroku. Takie wykrywanie na żywo nie istnieje w tym kroku: agent jest osiągalny tylko podczas uruchomienia, a nie gdy formularz jest otwarty w Twojej przeglądarce. Kostka, widok i MDX są wpisywane, a nierozpoznana nazwa kończy uruchomienie czytelnym błędem, zamiast kończyć się po cichu niepowodzeniem. Z tego samego powodu nie ma przycisku **Podgląd** — podgląd musiałby dotrzeć do TM1, co potrafi tylko agent.

## Wymagania

Odczyt lokalnego serwera TM1 wymaga:

- **Zainstalowanego agenta PlaidLink** na maszynie z dostępem sieciowym do serwera TM1. Zobacz [Install PlaidLink](/pl/reference/cli/plaidlink/install/).
- **Kompilacji tego agenta zawierającej obsługę TM1.** PlaidCloud sprawdza deklarowane możliwości agenta przed przekazaniem; agent, którego kompilacja jest starsza niż ta możliwość, nie może obsłużyć żądania. **PlaidLink nie aktualizuje się automatycznie** — istniejącego agenta należy ręcznie przebudować lub zainstalować ponownie, aby uzyskać obsługę TM1. Zobacz [Upgrade PlaidLink](/pl/reference/cli/plaidlink/upgrade/).
- **Połączenia TM1 udostępnionego temu agentowi**, oprócz dostępu członków/grup, który już ma — nadaj je z listy `Actions > Agents` połączenia. Zobacz [Model zabezpieczeń](/pl/guides/connections/create-connection/#model-zabezpieczeń).

## Powiązane

- [TM1: zapytanie do kostki](/pl/reference/workflow-steps/ibm-planning-analytics/tm1-query/) — odpowiednik bezpośredni z chmury, który ten krok odzwierciedla.
- [TM1: odczytaj wymiar](/pl/reference/workflow-steps/ibm-planning-analytics/tm1-dimension-read/) — ładuje hierarchię TM1 do wymiaru PlaidCloud, bezpośrednio z chmury.
- [Połączenie z TM1 (przewodnik)](/pl/guides/connections/tm1/) — utwórz połączenie.
- [Łącznik TM1](/pl/reference/connectors/rest/tm1/) — opis pól połączenia, w tym ścieżki lokalnego agenta.
- [PlaidLink](/pl/reference/cli/plaidlink/) — instalowanie i uaktualnianie agentów.
- [Kroki IBM TM1 / Planning Analytics](/pl/reference/workflow-steps/ibm-planning-analytics/)
