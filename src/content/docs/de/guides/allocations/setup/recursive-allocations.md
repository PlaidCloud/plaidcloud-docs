---
title: Rekursive und wechselseitige Umlagen
description: Bilden Sie in PlaidCloud mehrstufige und wechselseitige Kostenverteilungen ab, indem Sie Umlageschritte zu expliziten, gestaffelten Durchläufen verketten.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/setup/recursive-allocations.md
---

Manche Kostenmodelle erfordern, dass das Ziel einer Umlage zur *Quelle* der nächsten wird — zum Beispiel bei Shared Services, die einander nutzen (die IT bedient die Personalabteilung, aber die Personalabteilung bedient auch die IT). PlaidCloud bildet dies ab, indem **Umlageschritte zu expliziten, gestaffelten Durchläufen verkettet** werden, nicht über einen einzelnen automatischen Solver.

## Wann Sie mehrere Durchläufe brauchen

- **Wechselseitige Leistungen** — zwei Kostenpools, die einander nutzen.
- **Gestaffelte Verteilungen** — Bereichskosten laufen durch eine Hierarchie nach unten, und die unteren Ebenen müssen die oberen Ebenen aufnehmen, bevor sie weiter umlegen.
- **Iterativer Ausgleich** — das Modell nähert sich nach mehreren Durchläufen einem stabilen Ergebnis (Pool A legt einen Teil auf B um, B legt einen Teil zurück um und so weiter).

## So bilden Sie es ab

PlaidCloud hat **keinen integrierten „Rekursionsmodus“ und keinen automatischen Konvergenz-Solver**. Sie bauen die Rekursion selbst auf, indem Sie für jeden Durchlauf einen eigenen [Allocation Split-Schritt](/de/reference/workflow-steps/allocation/allocation-split/) hinzufügen und die Schritte der Reihe nach verbinden:

1. Führen Sie den ersten Durchlauf als normalen Allocation Split aus.
2. Erstellen Sie für den nächsten Durchlauf eine Quelle, die die Ausgabe des vorherigen Durchlaufs enthält — typischerweise, indem Sie das vorherige Ergebnis per Union oder Join wieder in den Pool einbinden — und legen Sie erneut um.
3. Wiederholen Sie dies für so viele Durchläufe, wie Ihr Modell braucht.

Da jeder Durchlauf ein expliziter Schritt ist, **entscheiden Sie, wie viele Durchläufe ausgeführt werden**. Die Engine löst die wechselseitige Beziehung nicht als einzelne simultane Gleichung, und es gibt keine Toleranzeinstellung, die die Schleife automatisch beendet. Fügen Sie Durchläufe hinzu, bis der noch umzulegende Rest für Ihre Zwecke klein genug ist.

## Tipps

- Beginnen Sie mit einer Umlage in **einem Durchlauf** und vergewissern Sie sich, dass sich das einfache Modell wie erwartet verhält, bevor Sie Durchläufe hinzufügen.
- Prüfen Sie nach jedem Durchlauf den verbleibenden nicht umgelegten Rest. Wenn er von Durchlauf zu Durchlauf nicht kleiner wird, überprüfen Sie die Treiberbeziehungen — eine echte zirkuläre Abhängigkeit kommt auch mit beliebig vielen Durchläufen nicht zur Ruhe.
- Jeder Durchlauf verarbeitet seine Quelle erneut, daher ist Rekursion bei großen Datensätzen aufwendig. Testen Sie an einem Ausschnitt, bevor Sie die gesamte Quelle verarbeiten.

## Verwandte Themen

- [Umlage konfigurieren](/de/guides/allocations/setup/configure-an-allocation/) — Basiskonfiguration
- [Allocation Split-Schritt](/de/reference/workflow-steps/allocation/allocation-split/) — der Workflow-Schritt, den Sie für jeden Durchlauf verketten
- [Umlagen beheben](/de/guides/allocations/results/troubleshooting-allocations/) — wenn Reste keinen Sinn ergeben
