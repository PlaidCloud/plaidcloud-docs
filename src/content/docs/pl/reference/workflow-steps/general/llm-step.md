---
title: Krok LLM
description: Uruchom prompt względem modelu LLM z ograniczonym dostępem do odczytu i/lub zapisu danych projektu, gdzie model zapisuje wyniki bezpośrednio przez serwer MCP.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/llm-step.md
---

## Opis

**Krok LLM** wysyła prompt do dużego modelu językowego. Przy połączeniu LLM z Anthropic model otrzymuje ograniczony dostęp do tabel projektu, wymiarów i dokumentów, które powiążesz — **Odczyt**, **Zapis** lub oba dla każdego obiektu — i zapisuje wyniki bezpośrednio w powiązaniach z włączonym zapisem. Powiązanie z zapisem jest wyjściem kroku; nie ma osobnego formatu wyjściowego.

Pełny opis krok po kroku znajdziesz w [przewodniku po kroku LLM](/pl/guides/workflows/llm-step/).

## Konfiguracja

* **Połączenie LLM** *(wymagane)* — połączenie rodzaju LLM (na przykład Anthropic). Jego **Dostęp agenta** musi mieć wartość **Odczyt i zapis** dla każdego powiązania z zapisem. Wartość **Pełny** również zezwala na zapis, dopóki nie zostanie usunięta 15 stycznia 2027 r., a krok, który jej używa, po zakończeniu zapisuje ostrzeżenie w dzienniku. Przy **Odczyt i zapis** krok zapisuje tylko w powiązaniach z zaznaczonym Zapisem i nie może uruchamiać SQL, który zapisuje, ani tworzyć tabel.
* **Model** *(opcjonalne)* — domyślnie model domyślny połączenia. Z połączeniem Anthropic działa dowolny model Claude, także starsze, takie jak Claude Sonnet 4.5.
* **Prompt** *(wymagane)* — obsługuje odwołania `{{tables.NAME}}`, `{{dimensions.NAME}}` i `{{documents.NAME}}` do powiązanych obiektów.
* **Schemat wyniku** *(opcjonalne dla Anthropic; wymagane dla innych dostawców)* — Schemat JSON (korzeń `"type": "object"`) dla przechwytywanego ustrukturyzowanego podsumowania; przy Anthropic pozostaw puste, gdy praca modelu to zapisy przez MCP. Dostawcy inni niż Anthropic nie mają dostępu do MCP, więc schemat jest wymagany.
* **Powiązania** — tabele, wymiary i dokumenty, do których model ma dostęp, każdy wybrany selektorem i z nadanym **Odczytem** i/lub **Zapisem**. Tabele z zapisem otrzymują wstawiane wiersze, wymiary z zapisem otrzymują węzły, a dokumenty z zapisem otrzymują przesłane pliki.
* **Limity** — Maks. liczba tokenów wyjściowych (od 1024 do 128 000) i czas życia poświadczeń (od 60 do 3600 sekund).

## Działanie

* Wywołanie modelu działa we własnym zadaniu. Krótkotrwałe, ograniczone poświadczenie jest tworzone na czas uruchomienia i unieważniane po jego zakończeniu.
* Dostęp jest kontrolowany dla każdego obiektu i każdego pola wyboru: model odczytuje tylko obiekty powiązane z Odczytem i zapisuje tylko obiekty powiązane z Zapisem — nigdy obiektu, którego nie powiązałeś. Zapis wymaga istniejącego obiektu docelowego; krok go nie tworzy.
* Każde uruchomienie wykonuje płatne wywołanie dostawcy i zapisuje dane w powiązanych obiektach.

## Co jest sprawdzane przy zapisie

* **Schemat wyniku** — jeśli go podasz, musi być poprawnym JSON, obiektem JSON i deklarować `"type": "object"` w korzeniu. W przeciwnym razie zapis jest odrzucany, na przykład z komunikatem *The result schema must declare "type": "object" at its root.*
* **Powiązania i połączenie** — tylko połączenie Anthropic daje modelowi dostęp do powiązań. Zapis kroku z powiązaniami przy połączeniu innego dostawcy jest odrzucany, z komunikatem wskazującym dostawcę i proszącym o *Remove the bindings or choose an Anthropic connection.* Powiązanie z zaznaczonym **Zapisem** wymaga połączenia, którego **Dostęp agenta** dopuszcza zapis. Przy połączeniu tylko do odczytu zapis jest odrzucany z komunikatem *The selected LLM connection has Read-only Agent Access, so a binding with Write checked could not write. Set the connection to 'Read & write' or uncheck Write on the bindings.* Krok zapisany przez API bez połączenia jest sprawdzany względem domyślnego połączenia LLM obszaru roboczego, na którym też działa: tego, które administrator oznaczył jako domyślne, a w przeciwnym razie ostatnio zaktualizowanego. Bez oznaczonego przez administratora połączenia domyślnego edycja innego połączenia LLM czyni je domyślnym i może spowodować odrzucenie następnego zapisu kroku.
