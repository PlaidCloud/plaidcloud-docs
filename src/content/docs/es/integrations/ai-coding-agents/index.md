---
title: Agentes de IA (MCP)
description: Conecte Claude, Cursor, GitHub Copilot, Gemini y otros agentes de IA a su inquilino de PlaidCloud mediante el servidor del Model Context Protocol (MCP).
sidebar:
  label: Agentes de IA (MCP)
  order: 13
editUrl: https://github.com/PlaidCloud/plaidcloud-docs/edit/main/src/content/docs/integrations/ai-coding-agents/index.md
---

PlaidCloud expone un servidor [Model Context Protocol](https://modelcontextprotocol.io) (MCP) seleccionado en `/mcp` en cada espacio de trabajo. Los agentes de IA se conectan a él igual que a cualquier otro servidor MCP y luego llaman a las herramientas para leer proyectos, ejecutar flujos de trabajo, consultar tablas, administrar dimensiones y mucho más.

Las páginas de esta sección explican qué expone el servidor, cómo autenticarse y cómo configurar paso a paso los clientes de IA más habituales. Para conocer la arquitectura que hay detrás (la ruta gobernada que sigue cada solicitud de IA, cómo funciona la recuperación y cómo ejecutar su propio modelo), consulte [Arquitectura de IA y LLM](/es/integrations/ai-architecture/).

## Qué distingue el análisis con IA de PlaidCloud

- **[Respuestas en las que puede confiar](./honest-answers/)**: cada respuesta incluye una señal de confianza y advertencias en lenguaje claro, y PlaidCloud nunca inventa un número. Esta honestidad le permite actuar según una respuesta de IA sin volver a comprobarla manualmente.
- **[Rastreo de asignaciones](./tracing-allocations/)**: pregunte en lenguaje natural *por qué* cambió un resultado asignado, qué lo alimenta y qué efecto tendría un cambio hipotético.
- **[Rutas de análisis](./analysis-paths/)**: asigne nombres descriptivos y un valor predeterminado a sus tablas clave para poder preguntar simplemente “¿por qué subió esto el trimestre pasado?”.
- **[Crear paneles de control](./build-dashboards/)**: pida gráficos y paneles de control sobre sus tablas y vistas publicadas, a través de la misma conexión de PlaidCloud.
- **[Definiciones de métricas](./metric-definitions/)**: acuerde una sola vez cómo se calcula un número del negocio, de modo que todas las respuestas que lo usen lo calculen igual.

## Conecte su asistente

El camino más rápido es el botón **Conecte su IA** de la barra de herramientas del encabezado de PlaidCloud: elija su cliente y siga los pasos que muestra, incluida la URL del servidor MCP.

- [Primeros pasos](./getting-started/): qué expone el servidor MCP y cómo autenticarse.
- [Microsoft 365 Copilot](/es/integrations/microsoft-365-copilot/): lleve PlaidCloud a todo su equipo en Teams y Outlook.
- Configuración por cliente: [Claude Code](./claude-code/), [Claude Desktop](./claude-desktop/), [Cursor](./cursor/), [GitHub Copilot](./copilot/), [Gemini](./gemini/), [ChatGPT](./chatgpt/), [Grok](./grok/).
