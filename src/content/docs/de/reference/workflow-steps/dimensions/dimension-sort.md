---
title: Dimension Sort
description: Sortiert Dimensionsmitglieder in einem PlaidCloud-Workflow-Schritt automatisch, um eine einheitliche Reihenfolge innerhalb Ihrer Hierarchien zu erhalten.
sidebar:
  order: 5
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-sort.md
---

## Beschreibung

Sortiert die Mitglieder einer Dimension unter ihren übergeordneten Elementen – alphabetisch, nach Wert, nach Eigenschaft oder nach einer benutzerdefinierten Reihenfolgespalte. Erspart das mühsame manuelle Ziehen von Hierarchiemitgliedern in die richtige Reihenfolge, besonders nützlich nach einem Massenladen oder einer größeren Umstrukturierung.

Arbeitet direkt auf der Dimension; eine Quell- oder Zieltabelle ist nicht erforderlich.


## Dimensionsauswahl
### Dimension dynamisch angeben
Wenn **Dimensionen** oder **Pfade** dynamisch erstellt wurden, können dieselben Variablen verwendet werden, um sie zu sortieren. Variablen im Sortiervorgang sind nützlich, weil Sie den Schritt Dimension Sort dann nicht regelmäßig manuell anpassen müssen.



Ein Beispiel, das die Variable `current_month` verwendet, um die Dimension Materials dynamisch zu sortieren:

```text
/Dimensions/{current_month}/Products/Materials
```

### Bestimmte Dimension verwenden

Wählen Sie im Dropdown-Menü eine bestimmte Dimension aus, die sortiert werden soll.
