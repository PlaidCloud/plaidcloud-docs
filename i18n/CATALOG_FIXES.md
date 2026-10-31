# PlaidClient catalog defects found while translating the docs

These are bugs in the live UI translations (`PlaidClient/plaid/source/translation/<lc>.po`). File and fix them in
PlaidClient. Until they ship, the docs work around them in `i18n/glossary_overrides/<locale>.json`. Drop each override
once the catalog is fixed.

## The same msgid has two senses (needs `msgctxt`)

| msgid | Senses | Current msgstr | Locales |
|---|---|---|---|
| `Run` | button (verb) vs. a run (noun) | noun: Ausführung, Ejecución, Exécution, Execução, Uruchomienie | de, es, fr, pt-br, pt-pt, pl |
| `Advanced` | workflow type vs. advanced settings | ja 詳細 ("details"); the workflow type should be 高度 | ja |
| `Open` / `Closed` | period status vs. open/close a thing | zh-cn 打开 / 已关闭; period status should be 未结账 / 已结账 | zh-cn (check the other locales) |
| `Driver` / `driver` | allocation driver vs. Macro "Driver" tab vs. device driver | pl Nośnik kosztów / sterownik; zh-cn 驱动因素 (the Macro tab should be 驱动) | pl, zh-cn |

## Wrong sense or inconsistent with related strings

| Locale | msgid | Current | Should be |
|---|---|---|---|
| de, es, fr, pt-br, pt-pt, pl | `Load sample` | statistical sample (Stichprobe laden, Cargar muestra, Charger l'échantillon, Carregar amostra, Załaduj próbkę) | example data (Beispiel laden, Cargar ejemplo, Charger l'exemple, Carregar exemplo, Załaduj przykład) |
| ja | `○ Open` | ○ 未解決 ("unresolved") | ○ 未締め |
| zh-cn | `○ Open` | ○ 未结 | ○ 未结账 |
| ja | `Open dimensions` | 未解決のディメンション | ディメンションを開く |
| ja | `Data loaded` | データをロードしました (a sentence) | ロード済みデータ (a label) |
| ja | `Allocation drivers` | 配賦ドライバ | 配賦ドライバー (long-vowel form, as in `Driver`) |
| ko | `Profit Center` | 손익 센터 | 이익 센터 |
| pl | `Readable` | Czytelne ("legible") | Dostępne do odczytu |
| pl | "Nie używane" (two words) | | Nieużywane. It isn't a plain msgid in the extracted catalog, so check the plural and `%` entries. |
| es | `Allocation drivers` | Impulsores de asignación | Inductores de asignación (matches `Driver` → Inductor) |
| pt-pt | `Driver`, `driver`, `Driver Table`, `Allocation drivers` | Driver, driver, Tabela de drivers, Direcionadores de alocação (Brazilian) | Indutor, indutor, Tabela de indutores, Indutores de alocação |
| de | `Allocation drivers` | Verteilungstreiber | Consider Umlagetreiber, since `Allocations` → Umlagen. The docs keep the catalog form. |

## Docs bold labels with no catalog entry (check: missing `tr()`, or different wording in the docs)

Most frequent across the corpus: Validate Only, Continue On Error, Test Only Mode, Refresh All Tables, Available
columns, Join Map, Pinned, Project Default, Access Key, Secret Key, Ask Weave, Post-Join Filter, Sanitize Workbook,
SP Entity ID, Matching Worksheet, Run As, Is filterable, Allocation Results Table. The docs keep these in English
consistently until the catalog has them.
