---
title: Zmiana języka
description: Wyświetlaj PlaidCloud w języku English (US), English (UK), Deutsch, Español, Français, Português (Portugal), Português (Brasil), Polski, 日本語, 한국어 lub 简体中文 i korzystaj ze swojego wyboru na innych urządzeniach.
sidebar:
  label: Zmiana języka
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/change-your-language.md
---

Interfejs PlaidCloud jest dostępny w jedenastu językach:

| Język | Pozycja w menu |
|---|---|
| angielski (USA) | English (US) |
| angielski (Wielka Brytania) | English (UK) |
| niemiecki | Deutsch |
| hiszpański | Español |
| francuski | Français |
| portugalski (Portugalia) | Português (Portugal) |
| portugalski (Brazylia) | Português (Brasil) |
| polski | Polski |
| japoński | 日本語 |
| koreański | 한국어 |
| chiński (uproszczony) | 简体中文 |

Każdy zaczyna w języku angielskim (USA). Nic się nie zmienia, dopóki nie wybierzesz języka.

## Zmiana języka

1. W nagłówku u góry kliknij przycisk **Język**, obok przycisku **Wygląd**. Jego menu wyświetla każdy język pod jego własną nazwą, więc znajdziesz swój niezależnie od tego, jaki język jest aktualnie wyświetlany.
2. Wybierz język.
3. Komunikat potwierdza, że PlaidCloud zostanie ponownie załadowany w tym języku. Niezapisane zmiany zostaną utracone, więc najpierw zapisz swoją pracę. Kliknij **Odśwież**, aby kontynuować, lub anuluj, aby zostać przy obecnym ustawieniu.

PlaidCloud zapisuje Twój wybór w profilu i ładuje się ponownie w nowym języku. Aby wrócić, wybierz **English (US)** w ten sam sposób.

## Gdzie obowiązuje Twój wybór

- **Inne urządzenia i przeglądarki.** Twój wybór podąża za Tobą. Jeśli logujesz się do tego samego obszaru roboczego na innym urządzeniu lub w innej przeglądarce, obowiązuje on od następnego załadowania strony.
- **Osobno dla każdego obszaru roboczego.** Wybór należy do Twojego profilu w jednym obszarze roboczym. Jeśli korzystasz z kilku obszarów roboczych, ustaw język w każdym z nich.

## Liczby i daty

Liczby i daty są wyświetlane w formacie wybranego języka. Na przykład w języku niemieckim tysiąc dwieście trzydzieści cztery i pół jest wyświetlane jako `1.234,5`. W języku polskim 1234567.89 jest wyświetlane jako `1 234 567,89`, a 12 października 2026 jako `12.10.2026`. Japoński i chiński pokazują tę datę jako `2026/10/12`, a koreański jako `26. 10. 12.`. English (UK) używa brytyjskiej pisowni i brytyjskich formatów.

Zmienia się tylko sposób wyświetlania. Wartości, które zapisujesz, eksportujesz lub wysyłasz do integracji, zachowują swój zwykły format.

## Wpisywanie po japońsku, koreańsku i chińsku

Metody wprowadzania japońskie, koreańskie i chińskie działają w polach liczbowych i innych polach ograniczających to, co można wpisać. Cyfry pełnej szerokości są konwertowane w trakcie pisania, więc `１２３` zmienia się w `123`.

## Co jeszcze podąża za Twoim językiem

Tekst, który PlaidCloud wysyła Ci z serwera, również odpowiada Twojemu językowi, w każdym języku oferowanym przez PlaidCloud:

- **E-maile.** E-maile systemowe, takie jak zaproszenia, resetowanie haseł, powiadomienia o przepływach pracy i migracjach oraz e-maile dotyczące rejestracji, rozliczeń i pomocy technicznej.
- **Ekrany logowania.** Ekrany logowania, ustawiania hasła i wylogowania oraz e-maile, które z nich wysyła Keycloak.
- **Komunikaty o błędach.** Komunikaty, które PlaidCloud pokazuje, gdy żądanie się nie powiedzie, w interfejsie, przez REST API i przez JSON-RPC.
- **Plik PDF dokumentacji projektu.** Plik PDF, który PlaidCloud generuje, aby udokumentować projekt.

## Jak PlaidCloud wybiera język

| Gdzie | Używany język |
|---|---|
| W PlaidCloud | Język wybrany przyciskiem **Język**. Strona logowania i e-maile odpowiadają temu samemu wyborowi. |
| Logowanie i inne ekrany przed zalogowaniem | Język przeglądarki. |
| Rejestracja | Język przeglądarki. PlaidCloud zapisuje go w Twojej organizacji, a e-maile dotyczące rozliczeń i konta wysyłane do organizacji go używają. |

Jeśli Twoja przeglądarka lub profil używa języka, którego PlaidCloud nie oferuje, tekst jest wyświetlany w języku angielskim (USA). Przeglądarki ustawione na chiński tradycyjny (zh-TW lub zh-HK) w przypadku tekstów z serwera wracają do języka angielskiego (USA).

## Co pozostaje po angielsku

- Komunikaty i dzienniki uruchomień przepływów pracy i kroków oraz strumień aktywności. Czyta je wiele osób, a utrzymanie ich w jednym języku ułatwia wyszukiwanie i zapewnia spójność.
- Tekst z asystenta AI i narzędzi MCP.
- E-maile, które piszesz samodzielnie, w tym szablony e-maili i e-maile wysyłane przez kroki raportów.
- Dokumentacja OpenAPI.
- Tekst błędów z silników SQL i wyrażeń.
- Ekrany rejestracji.
- Treści, które tworzysz, takie jak nazwy projektów, tabel i kroków.
