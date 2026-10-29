---
title: Ein von PlaidCloud verwaltetes Bucket-Konto hinzufügen
description: Fügen Sie PlaidCloud Document in einem Schritt vollständig verwalteten Dateispeicher hinzu – wählen Sie einen Namen, und PlaidCloud richtet alles für Sie ein, ohne dass etwas zu konfigurieren ist.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/documents/adding-accounts/add-managed-bucket-account.md
---

Ein **von PlaidCloud verwalteter Bucket** ist der schnellste Weg, Document Dateispeicher hinzuzufügen. PlaidCloud erstellt und betreibt den Speicher für Sie – es ist vorab nichts einzurichten, und es sind keine Zugangsdaten zu verwalten. Sie vergeben lediglich einen Namen.

Verwenden Sie einen von PlaidCloud verwalteten Bucket, wenn Sie einen neuen, in sich geschlossenen Ort für Document-Dateien benötigen. Um Speicher anzubinden, den Sie bereits besitzen und selbst verwalten, wählen Sie stattdessen einen der anderen Anbieter auf der Seite [Neue Dokumentenkonten hinzufügen](/de/guides/documents/adding-accounts/).

## Einrichtung

1. Melden Sie sich bei PlaidCloud an
2. Wählen Sie den Workspace, in dem sich das neue Dokumentenkonto befinden soll
3. Gehen Sie zu `Document > Manage Accounts`
4. Klicken Sie auf die Schaltfläche `+ New Account`
5. Wählen Sie `PlaidCloud Managed Bucket` als **Diensttyp**
6. Geben Sie einen Namen und eine optionale Beschreibung ein
7. Geben Sie einen **Bucket-Namen** ein. Namen müssen 3–63 Zeichen lang sein, dürfen nur Kleinbuchstaben, Ziffern, Punkte oder Bindestriche enthalten und müssen mit einem Buchstaben oder einer Ziffer beginnen und enden. Der Name muss **global eindeutig** sein – ist er bereits vergeben, werden Sie aufgefordert, einen anderen zu wählen
8. Wählen Sie ein für Ihren Anwendungsfall geeignetes **Sicherheitsmodell**. Wenn Sie unsicher sind, belassen Sie es bei `Private`
9. Klicken Sie auf die Schaltfläche „Speichern“

PlaidCloud richtet den Speicher ein und macht Sie zu seinem Eigentümer. Das Konto kann sofort durchsucht werden und Uploads annehmen – es ist nichts weiter zu konfigurieren.

:::note
Von PlaidCloud verwaltete Buckets sind in den Tarifen **Business** und **Enterprise** verfügbar. Wenn Ihr Tarif sie nicht enthält oder Sie das Limit Ihres Tarifs erreicht haben, teilt Ihnen das Formular dies beim Versuch mit, einen zu erstellen.
:::

## Nach der Erstellung

- Der Bucket-Name steht nach der Erstellung fest – er kann bei einem vorhandenen Konto nicht geändert werden.
- Beim Löschen des Kontos **bleiben die gespeicherten Dateien erhalten**, sodass durch ein Löschen nie Ihre Daten zerstört werden. Wenden Sie sich an den Support, wenn der Speicher selbst entfernt werden soll.
- Ein von PlaidCloud verwalteter Bucket verhält sich wie jedes andere Dokumentenkonto in Bezug auf [Zugriffssteuerung](/de/guides/documents/account-management/control-document-account-access/), [Eigentümerschaft](/de/guides/documents/account-management/managing-document-account-owners/) und das Durchsuchen.
