---
title: Notify Via Email
description: Wysyłaj powiadomienia e-mail z kroku przepływu pracy PlaidCloud z możliwością dostosowania tematu, treści, odbiorców i opcji załączników.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-email.md
---

## Opis


Wysyłaj powiadomienia e-mail. Wiadomości są wysyłane z konta e-mail *[info@tartansolutions.com](mailto:info@tartansolutions.com)*. Nie jest wymagana konfiguracja poczty wychodzącej.



### Adresy e-mail


Podaj dowolną liczbę odbiorców wiadomości. Dopuszczalne separatory to średnik (;) i przecinek (,).



### DW, UDW i Odpowiedz do

**DW** (`cc_address`), **UDW** (`bcc_address`) i **Odpowiedz do** (`reply_to`) przyjmują adresy w takim samym formacie jak odbiorcy oraz akceptują zmienne projektu i przepływu pracy. Odbiorcy DW i UDW otrzymują tę samą wiadomość, a odpowiedzi trafiają na adres z pola Odpowiedz do. Dotyczą one treści zwykłej oraz opartej na szablonie Jinja. Ustawisz je w sekcji **Więcej opcji e-mail** na karcie **Komunikat**.

### Jeden e-mail na każdy wiersz

W sekcji **Więcej opcji e-mail** ustaw **Wyślij** (`request_source`) na **Jeden e-mail na wiersz tabeli** (`table`) i wybierz **Tabelę sterującą** (`driver_table`), aby wysłać jeden e-mail dla każdego wiersza tabeli zamiast jednej wiadomości. **Maksymalna liczba wierszy do wysłania** (`row_limit`) ogranicza liczbę użytych wierszy i domyślnie wynosi 10 000. Tabela sterująca musi być tabelą, a nie widokiem.

Użyj `{{row.column}}` w adresach, temacie, komunikacie i ścieżce załącznika, aby wstawić wartość z każdego wiersza. Kolumna, której tabela sterująca nie ma, powoduje niepowodzenie kroku. Wiersz bez adresu Do nie wysyła nic dla tego wiersza, a krok kończy się ostrzeżeniem wskazującym ten wiersz.

Ścieżka załącznika wypełniana z wiersza (`{{row.column}}`) musi wskazywać pojedynczy istniejący plik, nigdy folder, aby wiersz z błędnie wyliczoną ścieżką nie wysłał cudzych plików. Wiersz, w którym wartość tej ścieżki jest pusta, ścieżka wychodzi z folderu przez `..` albo plik nie istnieje, jest wysyłany bez załącznika, z ostrzeżeniem wskazującym ten wiersz. Wysyłka dla każdego wiersza wymaga zwykłej treści i nie jest dostępna z treścią opartą na szablonie Jinja.

### Komunikat


Podaj **Temat** i **Treść żądania** według potrzeb.



Uwaga: w tej transformacji zarówno Zmienne projektu, jak i zmienne przepływu pracy są dostępne w wierszu tematu oraz w treści wiadomości.



Dodatkowo w treści dozwolony jest standardowy kod HTML, aby dostosować wygląd wiadomości e-mail.


### Załączniki


Dołączanie plików do wiadomości e-mail jest bardzo proste. Wybierz plik lub folder z Dokumentów, aby go dołączyć. Jeśli wybierzesz folder, jego zawartość zostanie dołączona jako osobne pliki. Podstawianie zmiennych działa w ścieżkach, co daje większą kontrolę nad załącznikami przy wysyłaniu spersonalizowanych wiadomości.



Aby dołączyć kilka dokumentów, zaznacz **Dodaj załącznik do e-maila** i wymień je w sekcji **Więcej załączników** (`attachments`) w **Więcej opcji e-mail**, każdy z **Identyfikatorem konta** i **Ścieżką dokumentu**; są wysyłane razem z wybranym załącznikiem, a ścieżka może używać zmiennych i tokenów wiersza w ten sam sposób.

### Priorytet i zwykły tekst

W sekcji **Więcej opcji e-mail** pole **Priorytet** (`priority`) oznacza wiadomość jako **Niska**, **Normalny** lub **Wysoka** (`low`, `normal`, `high`), a **Wyślij jako** (`content_type`) ustawione na **Zwykły tekst** (`text`) wysyła treść jako zwykły tekst zamiast **HTML** (`html`, wartość domyślna).

### Treść (szablon Jinja)


Treść kroku jest tworzona jako **szablon Jinja** renderowany na podstawie jednej lub kilku **ramek**, co daje bogaty e-mail w formacie HTML. Każda ramka to nazwany wybór z jednej tabeli — Nazwa ramki, jedna tabela przepływu pracy oraz opcjonalny wybór kolumn, filtr where i agregacja (bez złączeń). Edytor otwiera się bezpośrednio w tym szablonie — lista ramek, treść szablonu, podgląd na żywo i przycisk **Wyślij test do mnie** — bez przełącznika między zwykłym tekstem a szablonem. Przycisk **Upiększ** oraz paleta wstawiania (`render_table(...)` dla ramki, `{{ cloud }}`, pętla for oraz filtry walut/tysięcy/procentów/dat) pomagają ukształtować szablon.

Odwołuj się do każdej ramki w szablonie jako `frames['<Frame Name>'].rows` i `frames['<Frame Name>'].columns`; szablon z jedną ramką może używać najwyższego poziomu `rows` / `columns`, powiązanych z pierwszą ramką. Szablon jest osobnym, izolowanym silnikiem renderowania — jako wartość obszaru roboczego rozwiązuje się tylko `cloud`, a starsze tokeny `{project}` / `{model}` / `{date}` w nim nie działają. Kroki utworzone przed wprowadzeniem Jinja otwierają się ze starą treścią automatycznie przekonwertowaną; treść, której nie da się bezpiecznie przekonwertować, pozostaje w zapasowym trybie zwykłego tekstu i nadal jest wysyłana ze starszym podstawianiem `{token}`. Zobacz [Wysyłanie powiadomień e-mail HTML opartych na szablonach](/pl/guides/workflows/notify-email-templates/), aby poznać dostępne zmienne szablonu, pomocnik `render_table`, znaczniki i atrybuty HTML, które przetrwają sanityzację wiadomości e-mail, oraz sposób migracji istniejących treści.



## Przykłady


W tym przykładzie użyto wszystkich zmiennych systemowych. Ponadto do sformatowania pierwszego wiersza treści użyto niewielkiego fragmentu HTML. Wykonanie tej transformacji wyśle następującą wiadomość e-mail:


* DO: [info@tartansolutions.com](mailto:info%40tartansolutions.com)
* OD: [info@tartansolutions.com](mailto:info%40tartansolutions.com) (pamiętaj, że wszystkie wiadomości są wysyłane z tego adresu)
* Temat: DEMO – Workflow Analyze Demo Running
