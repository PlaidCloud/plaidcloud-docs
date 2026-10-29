---
title: Dimension Delete
description: Löscht in einem Workflow-Schritt eine Dimension aus PlaidCloud, um hierarchische Datenstrukturen zu entfernen, die nicht mehr benötigt werden.
sidebar:
  order: 3
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-delete.md
---

## Beschreibung
Löscht eine Dimension samt aller zugehörigen Strukturen, Werte, Eigenschaften, Aliasnamen und Alternativhierarchien


![Dimension Clear](/images/dimension_clear.png)



## Dimensionsauswahl
### Dimension dynamisch angeben
Wenn **Dimensionen** oder **Pfade** dynamisch erstellt wurden, können dieselben Variablen verwendet werden, um sie zu löschen. Variablen im Löschvorgang sind nützlich, weil Sie den Schritt Dimension Delete dann nicht regelmäßig manuell anpassen müssen.



Ein Beispiel, das die Variable `current_month` verwendet, um die Dimension Materials dynamisch zu löschen:

```text
/Dimensions/{current_month}/Products/Materials
```

### Bestimmte Dimension verwenden

Wählen Sie im Dropdown-Menü eine bestimmte Dimension aus, die gelöscht werden soll.
