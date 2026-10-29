---
title: "Schritte kopieren und einfügen"
description: Kopieren Sie Workflow-Schritte zwischen PlaidCloud-Workflows und fügen Sie sie ein, um Schrittkonfigurationen wiederzuverwenden und die Workflow-Entwicklung zu beschleunigen.
sidebar:
  order: 4
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/copy-paste-steps.md
---

## Schritte kopieren


Oft ist es sinnvoll, Schritte zu kopieren, statt jedes Mal von vorn zu beginnen. In PlaidCloud können Sie Schritte innerhalb eines Workflows, zwischen Workflows und sogar in andere Projekte kopieren. Sie können mehrere Schritte gleichzeitig zum Kopieren auswählen. Wählen Sie die Workflow-Schritte in der Hierarchie aus und klicken Sie oben in der Tabelle auf die Schaltfläche **Ausgewählte kopieren**.



Dadurch werden die ausgewählten Schritte in die Zwischenablage gelegt, sodass Sie sie im aktuellen Workflow oder in einem anderen einfügen können.

Die Zwischenablage wird in Ihrem Browser gehalten. Sie bleibt daher beim erneuten Laden der Seite erhalten und wird von allen geöffneten PlaidCloud-Registerkarten gemeinsam genutzt. Kopieren Sie aus einem Projekt in einer Registerkarte, wechseln Sie in einer anderen Registerkarte zu einem Projekt und fügen Sie dort ein. Die Zwischenablage wird nicht zwischen verschiedenen Browsern, zwischen Browsern auf unterschiedlichen Rechnern oder mit anderen Personen geteilt, und beim Wechsel des Workspace wird sie geleert.

Eine einzige Zwischenablage dient allen Stellen, an denen Sie einen Schritt kopieren – der Schrittetabelle, der älteren Tabelle, die Sie öffnen, indem Sie beim Öffnen eines Workflows Strg (oder Cmd) gedrückt halten, und der Arbeitsfläche eines erweiterten Workflows. Sie können also an jeder dieser Stellen kopieren und an jeder einfügen. Kopieren Sie einige Schritte aus einer Tabelle und fügen Sie sie auf einer erweiterten Arbeitsfläche ein oder umgekehrt; es ist dieselbe Zwischenablage.



Beim Kopieren eines Schritts entsteht innerhalb des Projekts ein duplizierter Schritt – ein neuer Schritt mit eigener Konfiguration, unabhängig vom Original.

Ein Schritt kann in der Struktur eines Workflows höchstens einmal vorkommen. **Anfügen** und **Einfügen** fügen immer ein frisches Duplikat ein, sodass dabei dieses Problem nie auftritt. Anders verhält es sich beim Einfügen eines *Verweises* auf einen bereits platzierten Schritt – siehe **Als verknüpften Schritt einfügen** weiter unten: Es ist derselbe Schritt. Das Einfügen in einen Workflow, der ihn bereits enthält, einschließlich des Workflows, aus dem Sie ihn kopiert haben, wird daher mit einer Meldung abgelehnt, die den Schritt nennt. Verknüpfen Sie ihn stattdessen in einen *anderen* Workflow.



## Schritte einfügen


Nachdem Sie Schritte zum Kopieren ausgewählt und in die Zwischenablage gelegt haben, können Sie diese in denselben Workflow oder in einen anderen Workflow einfügen, auch in einem anderen Projekt. Beim Einfügen der Schritte in den Workflow stehen zwei Optionen zur Verfügung:


* Am Ende des Workflows anfügen
* Nach der zuletzt ausgewählten Zeile einfügen

Die Option „Anfügen“ hängt die Schritte einfach an das Ende des ausgewählten Workflows an. Die Option „Einfügen“ fügt die kopierten Schritte nach der ausgewählten Zeile ein. Beachten Sie: Wenn mehrere Schritte aus verschiedenen Bereichen eines Workflows in die Zwischenablage kopiert wurden, werden sie zwar der Reihe nach eingefügt, enthalten aber keine verschachtelten Hierarchieinformationen aus dem Zeitpunkt des Kopierens. Das Einfügen erzeugt ausschließlich eine flache Liste von Schritten. Das mag unerwartet sein, ist aber sicherer, als die gesamte Verzeichnisstruktur des Quell-Workflows im Ziel-Workflow nachzubilden.


## Als verknüpften Schritt einfügen


**Einfügen → Verknüpfte Schritte hinzufügen (Erweitert)** platziert *denselben* Schritt im Ziel-Workflow, nicht eine Kopie davon. Beide Platzierungen sind ein und derselbe Schritt: Wenn Sie ihn in einem der Workflows bearbeiten, ändern sich beide, denn es gibt nur einen Schritt, der geändert wird.


Ein verknüpfter Schritt kann nur in das Projekt eingefügt werden, aus dem er kopiert wurde. Eine Verknüpfung ist eine zweite Platzierung eines Schritts, der einem Projekt gehört, und hat deshalb außerhalb dieses Projekts keine Bedeutung. Wenn Sie in ein anderes Projekt einfügen, lehnt PlaidCloud dies ab und weist Sie darauf hin, stattdessen **Anfügen** oder **Einfügen** zu verwenden. Diese kopieren die Schritte als eigenständige Schritte in das Zielprojekt.

Ein verknüpfter Schritt kann auch nicht in einen Workflow eingefügt werden, der ihn bereits enthält – das wäre derselbe Schritt zweimal in der Struktur eines Workflows, was PlaidCloud ablehnt. Dies tritt am ehesten auf, wenn ein Verknüpfungsvorgang fehlgeschlagen zu sein scheint und Sie ihn erneut versuchen: Der erste Versuch ist tatsächlich durchgegangen, und der erneute Versuch wird abgelehnt, statt den Workflow zu beschädigen. Die Fehlermeldung nennt den Schritt, sodass Sie bestätigen können, dass er bereits vorhanden ist.


## Kopieren und Einfügen auf der erweiterten Arbeitsfläche


In einem erweiterten Workflow können Sie Schritte direkt auf der Arbeitsfläche per Tastatur kopieren und einfügen, und die Verknüpfungen zwischen ihnen werden mitkopiert.


Wählen Sie die gewünschten Schritte aus – ziehen Sie einen Rahmen darum oder klicken Sie auf einen Schritt und fügen Sie mit Umschalt- oder Strg/Cmd-Klick weitere hinzu – und drücken Sie **Strg/Cmd+C**. Wechseln Sie zu dem Workflow, in den die Schritte sollen, ob in diesem oder einem anderen Projekt, zeigen Sie auf die Stelle, an der sie landen sollen, und drücken Sie **Strg/Cmd+V**. Die Schritte werden so angeordnet eingefügt, wie sie waren, und bleiben ausgewählt, sodass Sie sie an die richtige Stelle ziehen können. Beides geht auch ohne Tastatur: Klicken Sie mit der rechten Maustaste auf eine leere Stelle der Arbeitsfläche und wählen Sie **N Schritte kopieren** (wird angezeigt, wenn Schritte ausgewählt sind) oder **N Schritte hier einfügen** (wird angezeigt, wenn die Zwischenablage Schritte enthält); die eingefügten Schritte landen dort, wo Sie geklickt haben. Enthält die Zwischenablage Schritte, zeigt die Symbolleiste „N Schritte aus *Workflow*“ mit einer Schaltfläche **Einfügen** an, die in die Mitte des Arbeitsflächenbereichs einfügt, den Sie gerade sehen.


**Eine Gruppe kommt als Gruppe an.** Klicken Sie auf die Kopfzeile einer Gruppe, um die Gruppe samt allen ihren Schritten gemeinsam auszuwählen; kopieren Sie, und der Gruppenrahmen und seine Mitglieder werden als Einheit eingefügt. Ein Auswahlrahmen, der eine ganze Gruppe umschließt, wählt sie auf dieselbe Weise aus.


**Die Verknüpfungen zwischen den kopierten Schritten werden mitgenommen; Verknüpfungen zu Schritten, die Sie nicht kopiert haben, nicht.** Ein Schritt in Ihrer Auswahl, der von einem Schritt gespeist wurde, den Sie zurückgelassen haben, kommt ohne diese eingehende Verknüpfung an – am anderen Ende gibt es nichts, womit sie verbunden werden könnte. Beim Einfügen werden Sie darüber informiert, damit eine entfallene Verbindung nie unbemerkt bleibt.


**Beim Einfügen in denselben Workflow** werden die Kopien leicht versetzt, damit sie nicht genau auf den Originalen landen. Beim Einfügen in einen Workflow, der nicht erweitert ist – eine gewöhnliche Schrittetabelle –, entfallen die Anordnung auf der Arbeitsfläche und die Verknüpfungen, und die Schritte werden einfach hinzugefügt; das Einfügen teilt Ihnen dies mit.


**Ein großer Einfügevorgang wird automatisch in Stapeln ausgeführt.** Nichts wird begrenzt und nichts stillschweigend verworfen – beim Einfügen von Hunderten Schritten wird einfach der Fortschritt angezeigt, und Sie können den Vorgang abbrechen. Kann ein Einfügevorgang nicht abgeschlossen werden, werden die bereits hinzugefügten Schritte wieder entfernt, damit kein halb eingefügter Workflow zurückbleibt. In dem seltenen Fall, dass sich einige davon nicht automatisch entfernen lassen, nennt die Meldung die Anzahl der verbleibenden Schritte, statt ein sauberes Zurücksetzen zu behaupten.


**Um einen Einfügevorgang rückgängig zu machen,** drücken Sie unmittelbar danach **Strg/Cmd+Z** – die eingefügten Schritte werden entfernt. Hat ein Mitarbeiter den Workflow inzwischen geändert oder haben Sie ihn neu geladen, tritt dieses einstufige Rückgängigmachen zurück, statt Arbeit zu entfernen, die nicht mehr allein Ihre ist.


Schritte werden als neue, eigenständige Schritte kopiert. Denselben Schritt an mehreren Stellen einzufügen – das oben beschriebene Verhalten bei verknüpften Schritten – ist eine Aktion der Schrittetabelle; auf der Arbeitsfläche verwenden Sie **Schritt hinzufügen**, um einen Verweis in einem Workflow zu platzieren, der diesen Schritt noch nicht enthält.
