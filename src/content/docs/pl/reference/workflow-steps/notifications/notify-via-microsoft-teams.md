---
title: Notify via Microsoft Teams
description: Wysyłaj powiadomienia Microsoft Teams z kroku przepływu pracy PlaidCloud, aby informować kanały lub użytkowników o zdarzeniach i stanie przepływu pracy.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/notifications/notify-via-microsoft-teams.md
---

Dodanie powiadomień Microsoft Teams z przepływu pracy składa się z dwóch części:


1. Utwórz zewnętrzne połączenie Microsoft Teams
2. Dodaj kroki powiadomień Microsoft Teams do swoich przepływów pracy

## Dodawanie kroku powiadomienia Microsoft Teams do przepływu pracy


Dodanie kroku powiadomienia Microsoft Teams do przepływu pracy wygląda tak samo jak dodanie innych kroków. Po dodaniu kroku otwórz jego konfigurację, wypełnij formularz i zapisz go. Możesz teraz przetestować powiadomienie Microsoft Teams.



## Formatowanie wiadomości Microsoft Teams


Teams oferuje wiele opcji formatowania, w tym dodawanie obrazów i wspominanie użytkowników. Szczegóły znajdziesz w dokumentacji [Teams Message Text Formatting](https://support.microsoft.com/en-us/office/use-markdown-formatting-in-teams-4d10bd65-55e2-4b2d-a1f3-2bebdcd2c772).



## Tworzenie zewnętrznego połączenia Microsoft Teams


To jednorazowa konfiguracja, która pozwala PlaidCloud wysyłać powiadomienia Microsoft Teams w Twoim imieniu. Microsoft Teams umożliwia utworzenie aplikacji Webhook (ogólnego sposobu wysyłania powiadomień przez internet). Po utworzeniu aplikacji Webhook w Microsoft Teams dodaj otrzymane dane uwierzytelniające do PlaidCloud, aby umożliwić jej użycie.



### Tworzenie aplikacji Webhook w Microsoft Teams


Te czynności musi wykonać administrator Microsoft Teams. Postępuj zgodnie z krokami opisanymi tutaj: [Creating Incoming Webhook (Microsoft Teams Documentation)](https://docs.microsoft.com/en-us/microsoftteams/platform/webhooks-and-connectors/how-to/add-incoming-webhook#create-incoming-webhook-1).



### Konfiguracja połączenia zewnętrznego w PlaidCloud


Te czynności musi wykonać administrator obszaru roboczego PlaidCloud z uprawnieniami do tworzenia Zewnętrznych połączeń danych. Aby utworzyć połączenie:


1. Przejdź do `Analyze > Tools > External Data Connections`
2. W opcji `+ New Connection` wybierz Microsoft Teams Webhook
3. Uzupełnij nazwę i opis oraz wklej adres URL webhooka wygenerowany podczas tworzenia webhooka powyżej. Podana tu nazwa będzie wyświetlana jako opcja wyboru w kroku przepływu pracy, więc jeśli to możliwe, powinna być opisowa. Każdy, kto zna ten adres URL, może publikować na Twoim kanale, dlatego pole **Adres URL webhooka** maskuje go podczas wklejania i po ponownym otwarciu połączenia jest puste; pozostaw je puste, aby zachować zapisany adres URL.
4. Wybierz przycisk `+ Create`


## Przykłady

Brak przykładów...
