---
title: Wozu Umlagen nützlich sind
description: Erfahren Sie, warum Kostenumlagen in PlaidCloud für Prozesskostenrechnung, Weiterbelastung und Rentabilitätsanalyse nützlich sind.
sidebar:
  order: 2
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/getting-started/why-are-allocations-useful.md
---

Umlagen verteilen einen Pool von Werten (typischerweise Kosten, es funktioniert aber für jede Summengröße) anhand eines messbaren Treibers auf die Verbraucher. Sie beantworten die Frage: *Wenn uns diese Kosten entstehen, wie sollten sie den Objekten zugeordnet werden, die sie verursachen?*

## Häufige Anwendungsfälle

### Prozesskostenrechnung

Sie kennen Ihre gesamten Marketingausgaben für ein Quartal. Sie möchten sie anhand einer messbaren Größe – etwa Kampagnenstunden, generierte Leads oder qualifizierte Opportunities – bestimmten Produkten zuordnen. Eine Umlage verteilt den Marketing-Pool mit dem von Ihnen gewählten Treiber auf die Produkte und weist jedem Produkt damit seine Vollkosten zu.

### IT-Weiterbelastung

Sie geben $X für den Betrieb gemeinsam genutzter Infrastruktur aus (Rechenleistung, Speicher, Lizenzen). Jede Geschäftseinheit nutzt unterschiedlich viel davon. Eine Umlage verteilt die IT-Kosten anhand von Nutzungskennzahlen – VM-Stunden, Speicher in GB, Lizenzplätze – auf die Einheiten, sodass die GuV jeder Einheit widerspiegelt, was sie tatsächlich verbraucht hat.

### Verteilung von Shared Services

Finanzen, Personal, Recht, Facility-Management – zentrale Funktionen, die dem gesamten Unternehmen dienen. Umlagen verteilen deren Kosten auf die Bereiche, die sie bedienen, typischerweise nach Mitarbeiterzahl, Umsatz oder einer gewichteten Mischung.

### Verrechnungspreise

Für Organisationen mit mehreren Entitäten bilden Umlagen ab, wie interne Leistungen zwischen den Entitäten bepreist werden. Das Ergebnis steuert die Buchungen für den konzerninternen Verrechnungsverkehr.

### Rentabilitätsanalyse

Sie haben Umsatz auf Produkt- oder Kundenebene. Sie haben Kosten in verschiedenen Pools (Vertrieb, Support, Infrastruktur, Herstellkosten). Umlagen führen alles auf der Granularität von Produkt bzw. Kunde zusammen, sodass Sie die tatsächliche Marge sehen können.

### Stücklistenkalkulation

Die Kosten fließen eine Hierarchie von Komponenten hinab. Jeder Schritt in der Stückliste ist eine Umlage: Die Kosten von Unterbaugruppen werden auf Baugruppen verteilt, die von Baugruppen auf Fertigerzeugnisse und die von Fertigerzeugnissen auf SKUs.

## Wovor Umlagen Sie bewahren

Ohne eine Umlage-Engine würden Sie diese Modelle in Tabellenkalkulationen aufbauen – fehleranfällig, schwer zu prüfen und schwer mit aktualisierten Daten zu wiederholen. PlaidCloud-Umlagen bieten Ihnen:

- **Reproduzierbare Modelle**, die automatisch neu ausgeführt werden, sobald sich die Quelldaten aktualisieren
- **Prüfpfad**, der zeigt, welche Quellzeilen zu welchen Zielzeilen beigetragen haben
- **Mehrstufige Umlagen**, bei denen Ergebnisse in weitere Umlagen einfließen
- **Dimensionale Integration**, sodass Umlagen Ihre bestehenden Hierarchien berücksichtigen

## Nächste Schritte

- [Schnellstart für Umlagen](/de/guides/allocations/getting-started/allocations-quick-start/) — erstellen Sie eine in 30 Minuten
- [Regelbasiertes Tagging](/de/guides/allocations/getting-started/rule-based-tagging/) — steuern Sie das Umlageverhalten zeilenweise
- [Umlage konfigurieren](/de/guides/allocations/setup/configure-an-allocation/) — vollständige Konfigurationsreferenz
