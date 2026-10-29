---
title: Kontrolowanie wykonywania równoległego
description: Kontroluj równoległe wykonywanie kroków w przepływach pracy PlaidCloud, aby zoptymalizować wydajność przez jednoczesne uruchamianie niezależnych kroków.
sidebar:
  order: 13
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/guides/workflows/controlling-parallel-execution.md
---

Przepływy pracy w PlaidCloud mogą być wykonywane jako połączenie kroków szeregowych i operacji równoległych. Aby ustawić grupę kroków do równoległego uruchamiania, umieść kroki w grupie w hierarchii przepływu pracy. Kliknij folder grupy prawym przyciskiem myszy i wybierz opcję **Execute in Parallel**. Dzięki temu wszystkie kroki w grupie zostaną uruchomione jednocześnie i będą wykonywane równolegle. Po zakończeniu wszystkich kroków w grupie aktywowany zostanie kolejny krok lub grupa w przepływie pracy po tej grupie.

<figure style="margin:1.5rem 0;text-align:center;">
<svg viewBox="0 0 680 210" role="img" aria-label="Poprzedni krok zasila grupę oznaczoną jako Execute in Parallel. W grupie trzy kroki transformacji uruchamiają się jednocześnie i działają równolegle. Następny krok czeka, aż zakończą się wszystkie kroki w grupie." style="width:100%;max-width:680px;height:auto;">
  <defs><marker id="pe-arrow" markerWidth="9" markerHeight="9" refX="7" refY="4.5" orient="auto"><path d="M0,0 L8,4.5 L0,9 z" fill="var(--sl-color-gray-3)" /></marker></defs>
  <rect x="6" y="86" width="110" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="61" y="112" text-anchor="middle" font-size="12" fill="var(--sl-color-text)">poprzedni krok</text>
  <rect x="170" y="26" width="320" height="160" rx="12" fill="none" stroke="var(--sl-color-accent)" stroke-width="2" />
  <text x="182" y="20" font-size="12" font-weight="700" fill="var(--sl-color-accent)">Execute in Parallel</text>
  <circle cx="170" cy="108" r="6" fill="var(--sl-color-accent)" />
  <circle cx="490" cy="108" r="6" fill="var(--sl-color-accent)" />
  <rect x="210" y="42" width="130" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="275" y="63" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">transformacja 1</text>
  <rect x="210" y="91" width="130" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="275" y="112" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">transformacja 2</text>
  <rect x="210" y="140" width="130" height="34" rx="7" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="275" y="161" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">transformacja 3</text>
  <path d="M116 108 L164 108" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pe-arrow)" />
  <path d="M176 108 C192 108 194 59 206 59" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#pe-arrow)" />
  <path d="M176 108 L206 108" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#pe-arrow)" />
  <path d="M176 108 C192 108 194 157 206 157" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#pe-arrow)" />
  <path d="M340 59 C468 59 470 108 484 108" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#pe-arrow)" />
  <path d="M340 108 L484 108" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#pe-arrow)" />
  <path d="M340 157 C468 157 470 108 484 108" stroke="var(--sl-color-gray-3)" stroke-width="1.4" fill="none" marker-end="url(#pe-arrow)" />
  <path d="M496 108 L560 108" stroke="var(--sl-color-gray-3)" stroke-width="1.6" fill="none" marker-end="url(#pe-arrow)" />
  <rect x="562" y="86" width="112" height="44" rx="8" fill="var(--sl-color-gray-6)" stroke="var(--sl-color-gray-5)" />
  <text x="618" y="105" text-anchor="middle" font-size="11" fill="var(--sl-color-text)">następny krok</text>
  <text x="618" y="119" text-anchor="middle" font-size="10" fill="var(--sl-color-gray-3)">czeka na wszystkie</text>
</svg>
<figcaption style="font-size:0.85em;color:var(--sl-color-gray-3);margin-top:0.5rem;">Zgrupuj niezależne kroki i włącz <strong>Execute in Parallel</strong> — uruchomią się razem i będą działać jednocześnie. Następny krok aktywuje się dopiero po zakończeniu wszystkich z nich.</figcaption>
</figure>
