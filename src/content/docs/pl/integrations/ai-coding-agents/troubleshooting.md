---
title: Rozwiązywanie problemów
description: Typowe problemy z łączeniem agentów AI z serwerem MCP PlaidCloud i sposoby ich rozwiązania.
sidebar:
  order: 12
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/troubleshooting.md
---

## Cursor (lub inny restrykcyjny klient) w ogóle się nie łączy

Objaw: serwer nigdy nie nawiązuje sesji w Cursorze i podobnych restrykcyjnych klientach, podczas gdy ten sam obszar roboczy działa w Claude Code.

Przyczyna: **ukośnik końcowy** w adresie URL serwera. Użyj `https://<your-workspace>.plaid.cloud/mcp`, a nie `.../mcp/`. Restrykcyjni klienci odrzucają adres URL z ukośnikiem końcowym (albo nie podążają za przekierowaniem, które wystawiała starsza ścieżka), natomiast mniej restrykcyjni klienci, jak Claude Code, go tolerują.

Rozwiązanie: usuń ukośnik końcowy z `url` w konfiguracji i połącz się ponownie. Wszystkie przykłady w tych przewodnikach używają formy bez ukośnika.

## „failed to Connect" / „session Not Found"

Objaw: konfiguracja klienta wygląda poprawnie, ale serwer jest pokazywany jako niepołączony w panelu stanu MCP klienta. W dziennikach serwera widać błędy 404 `Session not found`.

Przyczyna: znany błąd w niektórych klientach MCP (przede wszystkim w Claude Code 2.1.111 ze statycznymi nagłówkami `Authorization`), w których klient nie zachowuje `mcp-session-id` między kolejnymi żądaniami HTTP. Serwer MCP PlaidCloud działa w bezstanowym trybie HTTP, aby to obejść. Jeśli widzisz ten problem w dzierżawie, która nie została ponownie wdrożona od czasu poprawki, poproś administratora o ponowne wdrożenie.

Do czasu ponownego wdrożenia przepływ OAuth (bez statycznych nagłówków `Authorization`) nadal działa, ponieważ korzysta z innej ścieżki kodu w kliencie.

## Strona „application Access Request"

Objaw: po zalogowaniu do PlaidCloud podczas autoryzacji OAuth trafiasz na stronę zatytułowaną **Application Access Request**, która wskazuje aplikację i identyfikator URI przekierowania, i musisz kliknąć Approve, aby przepływ był kontynuowany.

Przyczyna: to zachowanie oczekiwane. Każda autoryzacja OAuth przez serwer MCP PlaidCloud wyświetla tę stronę, aby przed wydaniem tokenu można było potwierdzić, z czym się łączysz. Strona wskazuje aplikację wysyłającą żądanie oraz identyfikator URI przekierowania, na który zostaną przesłane poświadczenia. Sprawdź, czy oba pasują do klienta, z którym faktycznie się łączysz, i nie zatwierdzaj żądania, którego nie zainicjowano.

Połączony już klient nie widzi tej strony ponownie podczas odświeżania tokenu. Wraca ona tylko przy nowej autoryzacji (pierwsze połączenie albo po wygaśnięciu lub unieważnieniu tokenu odświeżania).

Rozwiązanie: nie ma nic do naprawy. Zatwierdź stronę, aby kontynuować. Jeśli autoryzację rozpoczęto w jednej przeglądarce (lub profilu), a strona wyświetla się w innej, nie zostanie ona ukończona: zgoda jest powiązana z przeglądarką, która rozpoczęła przepływ. Rozpocznij autoryzację od nowa w tej samej przeglądarce, w której jesteś zalogowany do PlaidCloud.

## „oauth Flow is Not in Progress" podczas logowania w Claude Code

Objaw: autoryzujesz w przeglądarce, wklejasz adres URL wywołania zwrotnego do Claude Code, a on zgłasza, że żaden przepływ nie jest w toku.

Przyczyna: stan OAuth mostu, przechowywany w pamięci, jest przypisany do portu i może zostać utracony między wywołaniami narzędzi `authenticate` i `complete_authentication`, zwłaszcza w sesjach zdalnych/SSH, w których wywołanie zwrotne przeglądarki nie może dotrzeć do `localhost`.

Rozwiązanie: przełącz się na statyczny przepływ Bearer. Otwórz `https://<your-workspace>.plaid.cloud/mcp/setup/token` w przeglądarce, w której jesteś zalogowany do PlaidCloud, skopiuj fragment do pliku `.mcp.json` i uruchom ponownie Claude Code.

## Token wygasł

Objaw: narzędzia, które działały wczoraj, zwracają teraz 401 Unauthorized.

Przyczyna: statyczne tokeny Bearer podlegają polityce czasu ważności tokenów dostępu w Twojej domenie Keycloak (zwykle od kilku godzin do doby).

Rozwiązanie: odśwież stronę `https://<your-workspace>.plaid.cloud/mcp/setup/token`, aby wygenerować nowy token, i wklej go do konfiguracji. W przypadku długotrwałych sesji wybierz OAuth: klienci, którzy go obsługują, odświeżają tokeny automatycznie.

## „no `access_token` in Session"

Objaw: otwarcie `/mcp/setup/token` pokazuje „Sign-in required" lub „No access_token in session", mimo że jesteś zalogowany do PlaidCloud.

Przyczyna: Twoja sesja została nawiązana przez ścieżkę logowania, która nie zapisała tokenu Keycloak w pamięci podręcznej (rzadkie, ale możliwe).

Rozwiązanie: wyloguj się z PlaidCloud i zaloguj ponownie przez standardową stronę logowania. Nowa sesja będzie zawierać token dostępu.

## Brakujące narzędzia lub niepełny katalog

Objaw: `mcp_introspect` zwraca mniej narzędzi, niż oczekiwano, albo brakuje konkretnych potrzebnych narzędzi.

Przyczyna 1 — zakresy: narzędzia wymagają określonych zakresów PlaidCloud (np. `analyze.workflow.write`). Jeśli Twoje konto nie ma zakresu, narzędzie odmówi wykonania. Uruchom `mcp_introspect(name='<tool>')`, aby zobaczyć `required_scopes`. Poproś administratora obszaru roboczego o przyznanie zakresu albo wykonaj operację za pomocą konta, które go ma.

Przyczyna 2 — niezgodność wersji: starsze wdrożenie może nie mieć wszystkich narzędzi opisanych w najnowszej dokumentacji. Porównaj liczbę narzędzi zwracaną przez `mcp_introspect()` z informacjami o wydaniu dla Twojej bieżącej wersji i w razie potrzeby poproś o ponowne wdrożenie.

## Wiele dzierżaw: do której dzierżawy odwołał się agent?

Objaw: masz skonfigurowanych wiele dzierżaw PlaidCloud, a odpowiedź agenta mogła pochodzić z dowolnej z nich.

Rozwiązanie: podaj dzierżawę wprost w poleceniu („w dzierżawie **dev** wyświetl przepływy pracy…"). Nazwy serwerów MCP wybrane w konfiguracji (np. `plaidcloud-prod`, `plaidcloud-dev`) służą też jako identyfikatory, według których model może rozróżniać dzierżawy. W przypadku operacji o wysokiej stawce zostaw środowisko produkcyjne wyłączone w selektorze konektorów, dopóki naprawdę go nie potrzebujesz.

## Limity szybkości i limity przydziału

Powierzchnia REST PlaidCloud ma limit liczby żądań na minutę, stosowany przez to samo oprogramowanie pośredniczące, które obsługuje interfejs użytkownika. Wywołania MCP współdzielą ten limit. Jeśli agent wyśle długą serię wywołań `find` (np. próbując wyliczyć wszystkie projekty, przepływy pracy i kroki), możesz osiągnąć limit. Do sprawdzania rozmiaru używaj stronicowania (`cursor`, `limit`) i `count_only=True` zamiast pobierania pełnego zbioru wyników.

Zwróć uwagę, że wywołanie find domyślnie zwraca 25 wierszy na stronę (`step_find` zwraca 50), więc wyliczenie dużego zbioru kosztuje więcej wywołań niż dawniej. Przy celowym pełnym przeglądzie zwiększ `limit`, zamiast stronicować z wartością domyślną. Z kolei jeśli stale osiągasz limit, `count_only=True` i węższa projekcja `fields=[...]` zwykle oznaczają, że pełny przegląd nie był potrzebny.

## Lista wygląda na krótką albo agent mówi „to wszystkie"

Objaw: wywołanie find zwróciło mniej wierszy, niż oczekiwano, albo agent uznał, że projekt ma 25 tabel, a ma ich 300.

Rozwiązanie: sprawdź kopertę odpowiedzi. Ograniczona strona ustawia `next_cursor`, a narzędzie find wskazuje też obciętą listę w `truncated`. Każde z nich oznacza, że jest więcej do pobrania. `total` podaje pełną liczbę niezależnie od tego, więc porównaj ją z liczbą otrzymanych wierszy. Poproś agenta, aby stronicował za pomocą kursora albo uruchomił zapytanie ponownie z większym `limit`.

## Wynik wygląda jak `{"_fmt": "cols", ...}`

Objaw: narzędzie zwróciło `{"_fmt": "cols", "cols": [...], "rows": [[...]]}` zamiast oczekiwanej listy obiektów.

To zamierzony kształt dla dużego wyniku, w którym wszystkie wiersze mają te same pola: nazwy pól są wysyłane raz, a nie powtarzane w każdym wierszu. Wiersz *i* to `dict(zip(cols, rows[i]))`. Agenci są o tym informowani przy połączeniu i obsługują to bez dodatkowych poleceń. Jeśli czytasz te odpowiedzi we własnym kodzie, obsłuż oba kształty, ponieważ małe i nieregularne wyniki nadal przychodzą jako zwykłe tablice obiektów. Nic innego w kopercie się nie zmienia i żadna wartość nie jest modyfikowana. Zobacz [Pierwsze kroki z agentami do kodowania z AI](/pl/integrations/ai-coding-agents/getting-started/#wyniki-zorientowane-kolumnowo).

## Uzyskiwanie pomocy

W przypadku problemów po stronie serwera — błędów uwierzytelniania, narzędzi zwracających błędy bez oczywistej przyczyny, brakujących narzędzi — najpierw sprawdź kopertę `error` w odpowiedzi. Każda awaria zawiera `code`, `retryable`, `message`, a często także `hint`. Jeśli wskazówka nie wystarcza, skontaktuj się z administratorem PlaidCloud lub otwórz zgłoszenie do pomocy technicznej, podając identyfikator żądania (zwracany w nagłówku odpowiedzi `X-Request-Id`).
