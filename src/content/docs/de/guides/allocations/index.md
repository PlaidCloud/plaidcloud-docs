---
title: Umlagezuordnungen
description: Konfigurieren Sie PlaidCloud-Umlagemodelle für Kostenaufteilung, Prozesskostenrechnung, IT-Weiterbelastung und treiberbasierte Verteilung.
sidebar:
  label: Übersicht
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/allocations/index.md
---

Umlagen verteilen Werte von einer Gruppe von Zeilen („Quelle“) auf eine andere („Ziel“) anhand von Treiberdaten und Regeln. PlaidCloud unterstützt regelbasiertes Tagging, Umlageaufteilung, dimensionsgesteuerte Umlagen und rekursive Umlagen für Verrechnungspreise, IT-Weiterbelastung und ähnliche Kostenverteilungsprobleme.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 260" role="img" aria-label="Eine Umlage verteilt einen Quellkostenpool im Verhältnis zu Treiberdaten auf Ziele. Ein Quellpool von 1000 Dollar durchläuft Treiber wie Nutzung oder Mitarbeiterzahl und wird zu 50, 30 und 20 Prozent auf die Ziele A, B und C aufgeteilt. In einem rekursiven Modell kann ein Ziel für einen weiteren Durchlauf zurückgeführt werden." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="al-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="14" y="98" width="150" height="60" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="89" y="122" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Quellpool</text>
  <text x="89" y="140" text-anchor="middle" font-size="11" fill="var(--sl-color-gray-3)">$1,000</text>
  <path d="M164 128 L244 128" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#al-arrow)" />
  <rect x="246" y="98" width="142" height="60" rx="8" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="317" y="122" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Treiber / Basis</text>
  <text x="317" y="140" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">Nutzung · Mitarbeiterzahl…</text>
  <path d="M388 118 C450 100 452 62 496 62" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#al-arrow)" />
  <path d="M388 128 L496 132" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#al-arrow)" />
  <path d="M388 138 C450 156 452 202 496 202" stroke="var(--sl-color-gray-3)" stroke-width="1.5" fill="none" marker-end="url(#al-arrow)" />
  <text x="444" y="78" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">50%</text>
  <text x="450" y="126" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">30%</text>
  <text x="444" y="188" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">20%</text>
  <rect x="498" y="40" width="168" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="582" y="66" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Ziel A — $500</text>
  <rect x="498" y="110" width="168" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="582" y="136" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Ziel B — $300</text>
  <rect x="498" y="180" width="168" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="582" y="206" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">Ziel C — $200</text>
  <path d="M582 224 C582 250 90 250 89 160" stroke="var(--sl-color-gray-3)" stroke-width="1.3" fill="none" stroke-dasharray="5 4" marker-end="url(#al-arrow)" />
  <text x="330" y="248" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">rekursiv: Ein Ziel kann den nächsten Durchlauf speisen</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Werte aus einem Quellpool werden im Verhältnis zu den Treiberdaten auf Ziele aufgeteilt. Rekursive Modelle führen Ergebnisse für einen weiteren Durchlauf zurück, bis sich die Zahlen stabilisieren.</figcaption>
</figure>
