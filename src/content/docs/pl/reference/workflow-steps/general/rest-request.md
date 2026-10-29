---
title: Żądanie REST
description: Wywołaj REST API w kroku przepływu pracy — importuj punkty końcowe z Postman, OpenAPI lub HAR i kieruj odpowiedź do tabeli lub zmiennych przepływu pracy.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/general/rest-request.md
---

## Opis

Krok **Żądanie REST** wywołuje REST API i kieruje odpowiedź do tabeli docelowej lub do zmiennych przepływu pracy. Zastępuje starsze kroki w stylu REST jednym, ujednoliconym krokiem w stylu Postman: wybierz punkt końcowy (ręczny, Postman, OpenAPI/Swagger lub HAR), edytuj nagłówki, zapytanie i treść, wyślij żądanie testowe i zapisz.

Pełny opis krok po kroku znajdziesz w [przewodniku po kroku Żądanie REST](/pl/guides/workflows/rest-request-step/).

Podczas edycji przeglądarka przechowuje lokalny szkic kroku. Jeśli zamkniesz lub odświeżysz stronę przed zapisaniem, po ponownym otwarciu kroku zostanie zaproponowane przywrócenie niezapisanego szkicu.

## Konfiguracja

### Żądanie

* **Źródło punktów końcowych** — `Manual`, `From the connection's API definition`, `Postman collection (file/URL)`, `OpenAPI / Swagger (URL/file)` lub `HAR archive (file)`. Użyj **Załaduj katalog**, aby wyświetlić punkty końcowe zaimportowanego źródła; wybranie jednego wypełnia jego metodę, adres URL, nagłówki, parametry zapytania i treść, z pytaniem, jeśli żądanie było edytowane. Trzy źródła plikowe oferują też **Wklej…**, co pozwala podać kolekcję lub specyfikację bezpośrednio zamiast wybierać plik.
* **Połączenie** *(opcjonalne)* — połączenie REST do uwierzytelniania i adresu bazowego; pomiń, aby wywołać pełny adres URL bezpośrednio. Skrót edycji obok selektora otwiera edytor wybranego połączenia do podglądu lub edycji.
* **Metoda** — `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, `HEAD`, `OPTIONS`.
* **Punkt końcowy** — ścieżka (z połączeniem) lub pełny adres URL.
* **Nagłówki** / **Parametry zapytania** — wiersze nazwa/wartość z przełącznikiem włącz/wyłącz.
* **Treść żądania** — ładunek żądania (JSON, formularz lub surowy).
* **Wyślij żądanie testowe** / **Kopiuj jako curl** / **Importuj z curl** — wyślij żądanie i sprawdź odpowiedź w miejscu; skopiuj równoważne polecenie curl (sekrety zamaskowane); albo wklej polecenie curl, aby wypełnić metodę, adres URL, nagłówki i treść.
* **Wyślij** — `One request` (domyślnie) lub `One request per table row`, aby rozdzielić żądanie na wiersze tabeli sterującej.

Zapisanie zmian żądania wychodzącego przed pomyślnym wykonaniem **Wyślij żądanie testowe** wymaga potwierdzenia. W trybie rozdzielania na wiersze **Testuj wiersz 1** jest udanym testem, który usuwa to ostrzeżenie.

Gdy **Wyślij** ma wartość `One request per table row`, wybierz **Tabela sterująca** (za pomocą selektora tabel lub wpisując nazwę) i użyj tokenów `{{row.column}}` w punkcie końcowym, zapytaniu, nagłówkach lub treści, aby podstawić wartości każdego wiersza. Menu wstawiania zmiennych punktu końcowego i treści zawierają kolumny wybranej tabeli sterującej. Opcjonalnie: **Filtr tabeli sterującej** (klauzula SQL `WHERE`), **Kolumny kluczowe** (przenoszone do każdego wiersza wynikowego), **Limit wierszy**, **Współbieżność**, **Maks. liczba żądań/s** (ogranicza tempo rozpoczynania żądań we wszystkich procesach roboczych, niezależnie od współbieżności; akceptuje ułamki, więc 0,5 wysyła jedno żądanie co dwie sekundy; 0 = bez limitu; wartość powyżej 1000 jest ograniczana do 1000 z ostrzeżeniem), **Add Idempotency-Key header** (wysyła stabilny nagłówek `Idempotency-Key` dla każdego wiersza w pojedynczym żądaniu POST/PUT/PATCH bez stronicowania, aby ponowne uruchomienia nie tworzyły duplikatów; w pozostałych przypadkach pomijane z ostrzeżeniem), **Continue on error** (zapisuje nieudany wiersz i ostrzega zamiast przerywać) oraz **Odpowiedź** (domyślnie `Parsed records`; `Text (one row per request)` zapisuje każdą odpowiedź jako wiersz z kolumnami `DownloadData` i `DownloadHeaders`; `Raw text, errors as rows` robi to samo z treścią dokładnie taką, jaką wysłał serwer, dodaje kolumnę `DownloadStatus` i zachowuje błąd HTTP lub transportu jako wiersz, z zamaskowanymi poświadczeniami w treści, nagłówkach i tekście błędu). **Testuj wiersz 1** wysyła żądanie dla pierwszego wiersza tabeli sterującej, abyś mógł wyświetlić podgląd rozdzielania przed uruchomieniem. Rozdzielanie na wiersze zapisuje do tabeli docelowej; nie może przechwytywać do zmiennych.

Gdy **Odpowiedź** ma wartość `Text (one row per request)`, obowiązują dwie dodatkowe opcje rozdzielania na wiersze:

* **Treść odpowiedzi** — `As returned` (domyślnie), `Visible page text` zapisuje w `DownloadData` widoczny tekst strony HTML zamiast jej znaczników, a `Raw bytes (Base64)` zapisuje bajty treści dokładnie takie, jakie wysłał serwer, zakodowane w base64, dla pliku lub innej odpowiedzi binarnej.
* **Kontynuuj odpytywanie, dopóki odpowiedź pasuje** — dla API, które odpowiada „jeszcze pracuję”, dopóki zadanie się nie zakończy. Podaj **Ścieżka odpowiedzi** (`$` dla całej odpowiedzi, a następnie `.name`, `[0]`, `['name']` lub `["name"]`), operator (`==`, `!=`, `<`, `<=`, `>` lub `>=`) i wartość wraz z typem (`Text`, `Number`, `True/False` lub `Empty`). Żądanie każdego wiersza jest wysyłane ponownie, dopóki odpowiedź pasuje, co **N seconds** (od 1 do 600, domyślnie 5) przez najwyżej **M requests per row** (od 1 do 1000, domyślnie 60); wiersz, który nadal pasuje po ostatnim żądaniu, kończy się niepowodzeniem.

Aby wysłać treść binarną, na przykład plik lub dźwięk zapisany jako tekst base64 w kolumnie, włącz **Treść to tekst base64: wyślij zdekodowane bajty** (`body_base64`). Przy jednym żądaniu na wiersz tabeli treść, po wypełnieniu jej tokenów `{{row.column}}`, jest odczytywana jako tekst base64, a wysyłane są bajty, na które się dekoduje.

Sekcje **Opcje odpowiedzi tekstowej** i **Logowanie, proxy i TLS** zawierają te pola. Używają ich także przekonwertowane przepływy pracy KNIME.

Przy jednym żądaniu na wiersz tabeli i **Odpowiedź** ustawionej na `Text (one row per request)`:

* **Dodaj status HTTP każdej odpowiedzi jako kolumnę DownloadStatus** (`include_status`) — dodaje status HTTP każdej odpowiedzi jako kolumnę `DownloadStatus`. **Kolumna statusu** (`status_column`) nazywa tę kolumnę inaczej, a jej ustawienie dodaje kolumnę.
* **Zachowaj wiersz nieudanego żądania, z DownloadStatus i DownloadError** (`keep_error_rows`) — nieudane żądanie zachowuje swój wiersz, z brakującą treścią oraz wypełnionymi `DownloadStatus` i `DownloadError`.
* **Zachowaj wiersz nieudanego żądania** (`keep_failed_rows`) — żądanie, które otrzymało odpowiedź HTTP 400 lub wyższą, zachowuje swój wiersz ze statusem, nagłówkami odpowiedzi i treścią błędu w `DownloadError`; żądanie bez odpowiedzi zachowuje tylko swoje kolumny kluczowe. Niepowodzenie nadal zatrzymuje krok, gdy **Continue on error** jest wyłączone. **Zakończ krok błędem dla statusu odpowiedzi** (`fail_on_status`) wymienia rodziny statusów, takie jak `5xx`, które kończą krok niepowodzeniem; odpowiedź z dowolnej innej rodziny jest zachowywana jako wiersz.
* `document` *(ustawiane za pomocą asystenta AI lub REST API)* — zapisuje każdą odpowiedź jako plik w tym folderze Document, `{account, path, file_name}`, gdzie `file_name` domyślnie jest ostatnim segmentem adresu URL. Wiersz zawiera `FilePath` zamiast treści.
* **Zapisz treść jako dokument strony internetowej** (`html_document`) — zapisuje każdą treść jako znormalizowany dokument HTML (`html`) lub jego postać XML (`xml`). **Zamień względne wartości href i src na bezwzględne** (`html_absolute_urls`, domyślnie true) zamienia względne wartości `href` i `src` na bezwzględne względem adresu URL żądania.
* **Typuj kolumnę treści według pierwszej udanej odpowiedzi** (`typed_body`) — typuje kolumnę treści według pierwszej udanej odpowiedzi: JSON, tekst lub binarna według jej `Content-Type`. Późniejsza odpowiedź innego rodzaju, JSON, który się nie parsuje, i pusta treść są brakujące.
* **Dodaj kolumnę na każdy nagłówek odpowiedzi** (`all_headers`) — dodaje kolumnę tekstową dla każdego nagłówka odpowiedzi, po kolumnie statusu; nagłówek, którego odpowiedź nie wysłała, jest brakujący.
* **Dodaj pliki cookie odpowiedzi (DownloadCookies)** (`cookies`) — dodaje `DownloadCookies`, czyli pliki cookie każdej odpowiedzi.

Przy jednym żądaniu na wiersz tabeli:

* **Pomiń wiersz, którego adres URL nie jest bezwzględnym adresem URL http(s)** (`skip_invalid_urls`) — wiersz, którego adres URL nie jest bezwzględnym adresem HTTP ani HTTPS, nie wysyła żądania i nie zapisuje wiersza. **Zakończ krok błędem, gdy adres URL wiersza nie jest bezwzględnym adresem URL http(s)** (`fail_invalid_urls`) kończy w takim przypadku krok niepowodzeniem.
* **Nie wysyłaj nagłówka, którego wartość z wiersza to NULL** (`skip_null_headers`) — nagłówek, którego wartość `{{row.column}}` to NULL, nie jest wysyłany. **Zakończ krok błędem, gdy wartość nagłówka z wiersza to NULL** (`fail_null_headers`) kończy w takim przypadku krok niepowodzeniem.
* **Operacja SOAP** (`soap`) — wywołuje operację z WSDL wskazanego przez punkt końcowy, raz na wiersz: `service`, `port` i `operation` (każde pierwsze, gdy puste), `inputs` mapujące każdy parametr na kolumnę lub stałą, `outputs` wskazujące elementy odpowiedzi do zapisania jako kolumny (kolumna na każdy element liścia, gdy puste) oraz `xml`, aby dodać element odpowiedzi jako XML. WSDL i adres usługi muszą być publicznymi adresami HTTP lub HTTPS.

Dla dowolnego żądania:

* **Odpowiadaj na wyzwanie HTTP Digest** (`digest_auth`) — odpowiada na wyzwanie HTTP Digest, używając nazwy użytkownika i hasła Basic Auth z połączenia. **Odpowiadaj na wyzwanie NTLM** (`ntlm_auth`) odpowiada na wyzwanie NTLM w ten sam sposób; zapisz nazwę użytkownika jako `DOMAIN\user`, aby podać domenę.
* `proxy` — wysyła żądania przez proxy HTTP lub SOCKS, ustawiane za pomocą **Protokół proxy** (`protocol`: `http`, `https`, `socks`, `socks4` lub `socks5`), **Host proxy** (`host`), **Port proxy** (`port`), **Hosty obsługiwane bezpośrednio** (wzorce hostów `excluded`) i **Nazwa użytkownika proxy** (`username`). Hasłem jest `proxy_password` połączenia, używane tylko wtedy, gdy `proxy_host` połączenia to ten host.

Odwołania `{{name}}` do zmiennych przepływu pracy (także `{{var.name}}` / `{{project_var.name}}`) są podstawiane w punkcie końcowym, nagłówkach, wartościach zapytania i treści w czasie uruchomienia. Podstawiane są tylko podwójne nawiasy klamrowe, więc pojedyncze nawiasy klamrowe w treści JSON pozostają dosłowne. Uruchomienia z czujnika/webhooka udostępniają też `{{trigger_sensor_id}}`, `{{trigger_sensor_type}}`, `{{trigger_fired_at}}` i `{{trigger_payload_json}}` (puste w uruchomieniach niewywołanych).

Edytor podświetla wykryte tokeny `{{...}}` w tabelach punktu końcowego, nagłówków i zapytania oraz w edytorze treści.

**Ponowienia** dotyczą tylko metod idempotentnych (GET/HEAD/OPTIONS/DELETE); POST/PUT/PATCH jest zawsze wysyłane raz, aby treść nieidempotentna nigdy nie została wysłana ponownie. **Ponowienia** akceptują wartości od 0 do 100. **Limit czasu (s)** to limit dla pojedynczego żądania, od 1 do 600 s; żądania testowe czekają najwyżej 300 s. Filtr katalogu, wklejanie i upuszczanie, narzędzia JSON, ostrzeżenia żądań i wyniki testów opisano w [kroku Żądanie REST](/pl/guides/workflows/rest-request-step/).

### Miejsce docelowe odpowiedzi

* **Tabela** *(domyślnie)* — parsuje odpowiedź do pola **Tabela docelowa** (wymagane; tylko tabele, nie widoki). Elementy sterujące: Format wiersza (`Object` lub `Array`; jedno żądanie na wiersz tabeli wymaga `Object`), Ścieżka elementów, Tryb stronicowania (`No Paging`, `Offset Paging`, `Page Number Paging`, `Next Page URL Paging`, `Cursor Paging` lub `Link Header Paging (RFC 5988)`), Parametry trybu, Ścieżki trybu, „Dump raw JSON instead of parsing rows”, Ponowienia, Limit czasu. Karta **Wybór danych tabeli** mapuje pola odpowiedzi na kolumny; **Sprawdź źródło → Populate** wypełnia ją na podstawie rzeczywistej odpowiedzi, co wymaga połączenia i pyta przed wysłaniem metody innej niż GET, HEAD lub OPTIONS. Opcje Podsumuj i Unikalne nie są oferowane.
* **Zmienne przepływu pracy** — wysyła jedno żądanie i ustawia `{prefix}_status`, `{prefix}_body`, `{prefix}_headers` i `{prefix}_elapsed_ms`. **Prefiks zmiennej** musi być zwykłym identyfikatorem i nie może być żadnym z: `cloud`, `project`, `model`, `date`.

## Działanie

* W trybie zmiennych krok wykonuje jedno żądanie; stronicowanie i parsowanie wierszy nie mają zastosowania.
* Przechwycone zmienne są przywoływane w dalszych krokach po nazwie, np. `{my_call_status}`.
