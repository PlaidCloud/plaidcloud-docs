---
title: Parallele Ausführung steuern
description: Steuern Sie die parallele Ausführung von Schritten in PlaidCloud-Workflows und optimieren Sie die Leistung, indem Sie unabhängige Schritte gleichzeitig ausführen.
sidebar:
  order: 13
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/controlling-parallel-execution.md
---

Workflows in PlaidCloud können als Kombination aus seriellen Schritten und parallelen Operationen ausgeführt werden. Um eine Gruppe von Schritten parallel auszuführen, legen Sie die Schritte in einer Gruppe innerhalb der Workflow-Hierarchie ab. Klicken Sie mit der rechten Maustaste auf den Gruppenordner und wählen Sie die Option **Execute in Parallel**. Dadurch werden alle Schritte der Gruppe gleichzeitig ausgelöst und parallel ausgeführt. Sobald alle Schritte der Gruppe abgeschlossen sind, wird der nächste Schritt oder die nächste Gruppe im Workflow nach dieser Gruppe aktiviert.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 210" role="img" aria-label="Ein vorheriger Schritt speist eine Gruppe, die mit Execute in Parallel gekennzeichnet ist. In der Gruppe werden drei Transformationsschritte gleichzeitig ausgelöst und laufen zugleich. Der nächste Schritt wartet, bis jeder Schritt der Gruppe abgeschlossen ist." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="pe-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="6" y="86" width="110" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="61" y="112" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">vorheriger Schritt</text>
  <rect x="170" y="26" width="320" height="160" rx="12" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="182" y="20" font-size="12" font-weight="700" fill="var(--sl-color-accent)">Execute in Parallel</text>
  <circle cx="170" cy="108" r="6" fill="var(--sl-color-accent)" />
  <circle cx="490" cy="108" r="6" fill="var(--sl-color-accent)" />
  <rect x="210" y="42" width="130" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="275" y="63" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Transformation 1</text>
  <rect x="210" y="91" width="130" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="275" y="112" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Transformation 2</text>
  <rect x="210" y="140" width="130" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="275" y="161" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">Transformation 3</text>
  <path d="M116 108 L164 108" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pe-arrow)" />
  <path d="M176 108 C192 108 194 59 206 59" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#pe-arrow)" />
  <path d="M176 108 L206 108" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#pe-arrow)" />
  <path d="M176 108 C192 108 194 157 206 157" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#pe-arrow)" />
  <path d="M340 59 C468 59 470 108 484 108" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#pe-arrow)" />
  <path d="M340 108 L484 108" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#pe-arrow)" />
  <path d="M340 157 C468 157 470 108 484 108" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#pe-arrow)" />
  <path d="M496 108 L560 108" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pe-arrow)" />
  <rect x="562" y="86" width="112" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="618" y="105" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">nächster Schritt</text>
  <text x="618" y="119" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">wartet auf alle</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Gruppieren Sie unabhängige Schritte und aktivieren Sie <strong>Execute in Parallel</strong> – sie werden gemeinsam ausgelöst und laufen gleichzeitig. Der nächste Schritt wird erst aktiviert, nachdem alle abgeschlossen sind.</figcaption>
</figure>
