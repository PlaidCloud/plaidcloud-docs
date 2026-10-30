---
title: Dimension Create
description: Erstellen Sie in einem PlaidCloud-Workflow-Schritt eine neue hierarchische Dimension, um Ihr Klassifizierungssystem für Daten zu strukturieren.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-create.md
---

## Beschreibung
Erstellt eine Dimension zur Verwendung und zum Laden.


![Dimension Create](/images/dimension_create.png)

## Zu erstellende Dimension
### Name
Sie können für die zu erstellende Dimension entweder einen festen Namen verwenden oder Variablen für eine dynamische Benennung einbinden.


Variablen sind nützlich, wenn Dimensionen regelmäßig aktualisiert werden und die historische Sicht erhalten bleiben soll.

Ein Beispiel, das die Variable `current_month` für die dynamische Benennung der Dimension verwendet:

```text
dimension_name_{current_month}
```
### Pfad
Mit Pfaden legen Sie Ordnerstrukturen an, in denen die Dimensionen gespeichert werden. Auch hier können Sie Variablen verwenden, um die Ordnerstruktur dynamisch zu gestalten.
Ein Beispiel, das die Variable `current_month` für die dynamische Benennung eines Ordners verwendet:

```text
/Dimensions/{current_month}/Product/
```

### Memo
Das Feld „Memo“ dient zum Speichern von Kommentaren oder Notizen.
