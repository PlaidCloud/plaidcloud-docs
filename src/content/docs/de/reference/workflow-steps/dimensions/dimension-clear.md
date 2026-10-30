---
title: Dimension Clear
description: Entfernt in einem Workflow-Schritt alle Mitglieder aus einer PlaidCloud-Dimension und erhält dabei die Struktur und Konfiguration der Dimension.
sidebar:
  order: 1
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/reference/workflow-steps/dimensions/dimension-clear.md
---

## Beschreibung
Leert den Inhalt einer Dimension einschließlich Struktur, Werten, Aliasnamen, Eigenschaften und Alternativhierarchien


![Dimension Clear](/images/dimension_clear.png)



## Dimensionsauswahl
### Dimension dynamisch angeben
Wenn **Dimensionen** oder **Pfade** dynamisch erstellt wurden, können dieselben Variablen verwendet werden, um sie zu leeren. Variablen im Löschvorgang sind nützlich, weil Sie den Schritt Dimension Clear dann nicht regelmäßig manuell anpassen müssen.



Ein Beispiel, das die Variable `current_month` verwendet, um die Dimension Materials dynamisch zu leeren:

```text
/Dimensions/{current_month}/Products/Materials
```

### Bestimmte Dimension verwenden

Wählen Sie im Dropdown-Menü eine bestimmte Dimension aus, die geleert werden soll.
