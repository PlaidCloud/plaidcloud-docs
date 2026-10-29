---
title: Zarządzanie błędami kroków
description: Obsługuj błędy kroków w przepływach pracy PlaidCloud, w tym powiadomienia o błędach, logikę ponawiania i opcje odzyskiwania po awarii.
sidebar:
  order: 9
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/managing-step-errors.md
---

Jeśli podczas przetwarzania przepływu pracy wystąpi błąd, wskaźnik błędu jest wyświetlany zarówno przy przepływie pracy, jak i przy kroku, w którym wystąpił. PlaidCloud może ponawiać nieudany krok wielokrotnie. Jest to często przydatne, gdy krok korzysta ze zdalnych systemów lub danych, które mogą nie być wysoce dostępne albo sporadycznie zawodzić z nieznanych przyczyn. Ponawianie można ustawić na wiele prób, a także dodać opóźnienie między próbami od sekund do godzin.



Krok, którego serwer zostanie utracony w trakcie uruchomienia, jest obsługiwany osobno, poza ponawianiem: krok, który można bezpiecznie powtórzyć, uruchamia się automatycznie ponownie, a taki, którego nie można, kończy się jednorazowo komunikatem **Przerwano**. Zobacz [Przerwane kroki](/pl/guides/workflows/run-a-workflow/#przerwane-kroki).

Gdy PlaidCloud odrzuca krok z przyczyny, którą można naprawić, na przykład z powodu brakującego uprawnienia lub nieprawidłowego ustawienia, dziennik kroku pokazuje ten komunikat zwykłymi słowami, a nie błąd serwera ze śladem stosu. Krok Model Loop, Model Run lub Macro Run, którego podrzędny przepływ pracy kończy się niepowodzeniem, pokazuje własny komunikat o błędzie przepływu podrzędnego, w postaci „Child workflow run failed:", po którym następuje treść komunikatu.

Jeśli nie wybrano ponawiania lub przekroczono maksymalną liczbę ponowień, krok zostaje oznaczony jako błąd. PlaidCloud udostępnia w takim przypadku trzy poziomy obsługi błędów:


* Zatrzymanie przepływu pracy po wystąpieniu błędu
* Oznaczenie kroku jako błędu, ale kontynuowanie przetwarzania przepływu pracy
* Oznaczenie kroku jako błędu i uruchomienie procesu przepływu pracy naprawczego zamiast kontynuowania bieżącego przepływu pracy

## Zatrzymanie przepływu pracy


Zatrzymanie przepływu pracy po błędzie kroku jest najczęstszym podejściem, ponieważ przepływy pracy powinny zasadniczo działać bez błędów. Powoduje to zatrzymanie przepływu pracy i wyświetlenie wskaźnika błędu zarówno przy kroku, jak i przy przepływie pracy. Błąd jest też wyświetlany w monitorze aktywności, ale nie są podejmowane żadne dalsze działania.



## Kontynuowanie przetwarzania


Każdy krok można ustawić w formularzu kroku tak, aby kontynuował mimo błędu. Jeśli to pole wyboru jest włączone, każdy krok zostanie oznaczony błędem, jeśli wystąpi, ale przepływ pracy potraktuje błąd jako zakończenie kroku i będzie działał dalej. Jest to często przydatne, gdy są kroki wykonujące zadania, które mogą kończyć się błędem przy brakujących danych, ale są nieszkodliwe dla całego procesu.



Ponieważ w tym scenariuszu przepływ pracy kontynuuje mimo błędu, nie wyświetla wskaźnika błędu i nadal pokazuje wskaźnik uruchomienia.



## Uruchomienie przepływu pracy naprawczego


Dzięki możliwości ustawienia przepływu pracy naprawczego w konfiguracji przepływu pracy błąd przepływu pracy natychmiast zatrzymuje przetwarzanie bieżącego przepływu pracy i rozpoczyna przetwarzanie przepływu pracy naprawczego. Pamiętaj, że jeśli krok jest oznaczony do kontynuowania mimo błędu, jego niepowodzenie nie uruchomi przepływu pracy naprawczego. Proces naprawczy uruchamiają tylko kroki, których niepowodzenie powodowałoby też zatrzymanie całego przepływu pracy.



Przepływ pracy naprawczy może służyć po prostu do powiadomienia osób o wystąpieniu awarii albo do wykonania innego złożonego przetwarzania w celu podjęcia próby automatycznego usunięcia podstawowych przyczyn niepowodzenia pierwotnego przepływu pracy.
