---
title: Alerty tekstowe
description: Wyraź zgodę na otrzymywanie alertów o przepływach pracy PlaidCloud jako wiadomości tekstowych na Twój amerykański numer telefonu komórkowego i wyłącz je ponownie.
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/text-alerts.md
---

Przepływy pracy mogą wysyłać Ci SMS-y, gdy wymagają uwagi, za pomocą kroku [Notify Via SMS](/pl/reference/workflow-steps/notifications/notify-via-sms/). Przepływ pracy może wysłać Ci SMS dopiero po tym, jak sam wyrazisz zgodę.

## Włączanie alertów tekstowych

1. Otwórz menu użytkownika w prawym górnym rogu i wybierz **Alerty tekstowe**.
2. Wpisz swój **Numer telefonu komórkowego w USA**.
3. Zaznacz **Wyrażam zgodę na otrzymywanie SMS-owych alertów o przepływach pracy PlaidCloud na ten numer.** Przeczytaj informacje powyżej oraz linki **SMS Terms** i **SMS Privacy Policy**.
4. Kliknij **Wyślij kod**. PlaidCloud wyśle na Twój numer SMS-em 6-cyfrowy kod. Dotarcie wiadomości może zająć minutę lub dwie.
5. Wpisz **Kod potwierdzający** w ciągu 10 minut i kliknij **Potwierdź**.

Po wysłaniu kodu przycisk odlicza 60 sekund, a następnie przybiera postać **Wyślij kod ponownie**. Ponowne wysłanie, gdy Twój kod jest nadal ważny, wysyła ten sam kod, więc działa każda z wiadomości, która dotrze. Możesz zażądać 3 kodów na numer telefonu dziennie i 3 na osobę na godzinę.

Okno pokazuje wtedy **Alerty tekstowe są włączone dla** Twojego zamaskowanego numeru. Obsługiwane są tylko amerykańskie numery telefonów komórkowych. Mogą obowiązywać opłaty za wiadomości i transmisję danych, a częstotliwość wiadomości jest różna.

## Wyłączanie alertów tekstowych

Otwórz **Alerty tekstowe** i kliknij **Zatrzymaj alerty SMS** albo odpowiedz **STOP** na dowolny SMS. Odpowiedz **HELP**, aby uzyskać pomoc.

## Ponowne włączenie po STOP

Odpowiedź STOP blokuje wszystkie SMS-y na Twój numer. Wyślij SMS-em **START** na numer alertów pokazany w oknie, a następnie wyślij nowy kod i potwierdź go.

## Gdy coś pójdzie nie tak

| Komunikat | Co zrobić |
|---|---|
| That code is not right | Sprawdź wiadomość i wpisz kod ponownie. |
| That code has expired | Kliknij **Wyślij kod**, aby otrzymać nowy. |
| Too many wrong codes | Po 5 błędnych kodach kliknij **Wyślij kod**, aby otrzymać nowy. |
| Enter a valid US mobile number | Użyj 10-cyfrowego amerykańskiego numeru telefonu komórkowego. |
| Too many requests | Osiągnięto limit kodów. Odczekaj kilka minut i **Spróbuj ponownie**. |
| Text alerts are not available for your workspace right now | Spróbuj ponownie później. |

Nie używaj alertów tekstowych do przesyłania danych osobowych dotyczących zdrowia ani finansów. Pytania: support@plaidcloud.com.
