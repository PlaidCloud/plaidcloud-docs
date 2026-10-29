---
title: Notify via Slack
description: Wysyłaj powiadomienia Slack z kroku przepływu pracy PlaidCloud, aby informować kanały lub użytkowników o zdarzeniach, błędach i stanie przepływu pracy.
sidebar:
  order: 6
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-slack.md
---

Dodanie powiadomień Slack z przepływu pracy składa się z dwóch części:


1. Utwórz zewnętrzne połączenie Slack Webhook
2. Dodaj kroki powiadomień Slack do swoich przepływów pracy

## Dodawanie kroku powiadomienia Slack do przepływu pracy


Dodanie kroku powiadomienia Slack do przepływu pracy wygląda tak samo jak dodanie innych kroków. Po dodaniu kroku otwórz jego konfigurację, wypełnij formularz i zapisz go. Możesz teraz przetestować powiadomienie Slack.



## Dołączanie pliku

Wybierz dokument w polu **Plik do przesłania**, aby wysłać go na kanał z wiadomością jako komentarzem. Webhook nie może przenosić pliku, dlatego załącznik jest wysyłany przez token bota w połączeniu Slack:

- Dodaj **Token bota** do połączenia. To token `xoxb-` aplikacji Slack z zakresem `files:write`, a aplikacja musi zostać zaproszona na kanał.
- Wpisz w kroku **identyfikator kanału**, na przykład `C0123ABCD`, a nie nazwę kanału. Przesyłanie plików w Slack przyjmuje tylko identyfikatory, a bez niego krok kończy się niepowodzeniem. Aby znaleźć identyfikator, otwórz szczegóły kanału w Slack i przewiń na dół.
- Jeśli dokument nie zostanie znaleziony, wiadomość jest wysyłana przez webhook bez niego, a krok ostrzega, podając ścieżkę dokumentu.

## Formatowanie wiadomości Slack


Slack oferuje wiele opcji formatowania, w tym dodawanie obrazów i wspominanie użytkowników. Szczegóły znajdziesz w dokumentacji [Slack Text Formatting](https://api.slack.com/reference/surfaces/formatting).



## Tworzenie zewnętrznego połączenia Slack Webhook


To jednorazowa konfiguracja, która pozwala PlaidCloud wysyłać powiadomienia Slack w Twoim imieniu. Slack umożliwia utworzenie aplikacji Webhook (ogólnego sposobu wysyłania powiadomień przez internet). Po utworzeniu aplikacji Webhook w Slack dodaj otrzymane dane uwierzytelniające do PlaidCloud, aby umożliwić jej użycie.



### Tworzenie aplikacji Slack Webhook


Te czynności musi wykonać administrator Slack. Aby utworzyć aplikację Slack Webhook:


1. W Slack otwórz menu sterowania obszarem roboczym i wybierz `Settings & administration > Manage Apps`
2. Wybierz `Custom Integrations` z listy kategorii aplikacji
3. Wybierz `Incoming Webhooks` z listy aplikacji
4. Wybierz przycisk `Add to Slack`
5. Na następnym ekranie wybierz kanał Slack, na którym mają być publikowane wiadomości, i kontynuuj. To kanał domyślny, ale można go zastąpić w każdym powiadomieniu, w tym wysyłać wiadomości prywatne do wybranych osób.
6. Skopiuj wyświetlony adres URL webhooka. Będzie potrzebny później, więc zachowaj go w bezpiecznym miejscu. Wygląda mniej więcej tak: `https://hooks.slack.com/services/T04QZ1435/G02TGBFTOP8/K9GZrR2ThdJz1uSiL9YeZxoR`
7. Przed zapisaniem możesz dostosować wygląd, nazwę i emoji. Są to tylko wartości domyślne i można je zastąpić w każdym kroku powiadomienia w przepływie pracy PlaidCloud.

### Konfiguracja połączenia zewnętrznego w PlaidCloud


Te czynności musi wykonać administrator obszaru roboczego PlaidCloud z uprawnieniami do tworzenia Zewnętrznych połączeń danych. Aby utworzyć połączenie:


1. Przejdź do `Analyze > Tools > External Data Connections`
2. W opcji `+ New Connection` wybierz Slack Webhook
3. Uzupełnij nazwę i opis oraz wklej adres URL webhooka z kroku 6 powyżej. Podana tu nazwa będzie wyświetlana jako opcja wyboru w kroku przepływu pracy, więc jeśli to możliwe, powinna być opisowa. Każdy, kto zna ten adres URL, może publikować na Twoim kanale, dlatego pole **Adres URL webhooka** maskuje go podczas wklejania i po ponownym otwarciu połączenia jest puste; pozostaw je puste, aby zachować zapisany adres URL.
4. Aby wysyłać załączniki, wklej także token bota aplikacji Slack w polu **Token bota (do przesyłania plików)**. Połączenie może zawierać adres URL webhooka, token bota lub oba. Token bota jest maskowany tak samo jak adres URL webhooka i po ponownym otwarciu połączenia jest pusty.
5. Wybierz przycisk `+ Create`


## Przykłady

Brak przykładów...
