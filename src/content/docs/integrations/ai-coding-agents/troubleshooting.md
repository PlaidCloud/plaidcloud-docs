---
title: Troubleshooting
description: Common issues connecting AI agents to the PlaidCloud MCP server and how to fix them.
sidebar:
  order: 12
---

## Cursor (or Another Strict Client) Won't Connect at All

Symptom: the server never establishes a session in Cursor and similar strict clients, while the same workspace works in Claude Code.

Cause: a **trailing slash** on the server URL. Use `https://<your-workspace>.plaid.cloud/mcp` — not `.../mcp/`. Strict clients reject a trailing-slash URL (or won't follow the redirect the older path issued), whereas lenient clients like Claude Code tolerate it.

Fix: remove the trailing slash from the `url` in your config and reconnect. Every example in these guides uses the slash-free form.

## "failed to Connect" / "session Not Found"

Symptom: the client config looks correct but the server shows as failed in the client's MCP status panel. Server logs show 404 `Session not found` errors.

Cause: a known bug in some MCP clients (most notably Claude Code 2.1.111 with static `Authorization` headers) where the client doesn't preserve `mcp-session-id` between successive HTTP requests. PlaidCloud's MCP server runs in stateless HTTP mode to sidestep this — if you're seeing it on a tenant that hasn't been redeployed since the fix, ask your administrator to redeploy.

Until the redeploy lands, the OAuth flow (without static `Authorization` headers) still works because it uses a different code path in the client.

## "oauth Flow is Not in Progress" During Claude Code Login

Symptom: you authorize in the browser, paste the callback URL into Claude Code, and it says no flow is in progress.

Cause: the bridge's in-memory OAuth state is per-port and can be lost between the `authenticate` and `complete_authentication` tool calls — particularly in remote/SSH sessions where the browser callback can't reach `localhost`.

Fix: switch to the static Bearer flow. Open `https://<your-workspace>.plaid.cloud/mcp/setup/token` in a browser where you're signed into PlaidCloud, copy the snippet into your `.mcp.json`, and restart Claude Code.

## Token Expired

Symptom: tools that worked yesterday now return 401 Unauthorized.

Cause: static Bearer tokens follow your Keycloak realm's access-token-lifespan policy (typically a few hours to a day).

Fix: reload `https://<your-workspace>.plaid.cloud/mcp/setup/token` to mint a fresh token, paste it into your config. For long-lived sessions, prefer OAuth — clients that support it refresh tokens automatically.

## "no `access_token` in Session"

Symptom: opening `/mcp/setup/token` shows "Sign-in required" or "No access_token in session" even though you're signed into PlaidCloud.

Cause: your session was established through a sign-in path that didn't cache the Keycloak token (uncommon but possible).

Fix: sign out of PlaidCloud and sign back in through the standard login page. The new session will carry the access token.

## Tools Missing or Incomplete Catalog

Symptom: `mcp_introspect` returns fewer tools than expected, or specific tools you need aren't there.

Cause 1 — scopes: tools require specific PlaidCloud scopes (e.g. `analyze.workflow.write`). If your account lacks the scope, the tool will refuse to execute. Run `mcp_introspect(name='<tool>')` to see `required_scopes`. Ask your workspace admin to grant the scope or run the operation through an account that has it.

Cause 2 — version mismatch: an older deployment may not have all the tools described in the latest docs. Compare `mcp_introspect()`'s tool count to your current version's release notes; ask for a redeploy if needed.

## Multi-Tenant: Which Tenant Did the Agent Just Hit?

Symptom: you have multiple PlaidCloud tenants configured and the agent's response could've come from any of them.

Fix: include the tenant explicitly in your prompt ("in the **dev** tenant, list workflows…"). The MCP server names you chose in your config (e.g. `plaidcloud-prod`, `plaidcloud-dev`) double as identifiers the model can disambiguate against. For high-stakes operations, keep production toggled off in the connectors picker until you actively need it.

## Rate Limits and Quota

PlaidCloud's REST surface is rate-limited per requests-per-minute via the same middleware that fronts the UI. MCP calls share that limit. If an agent fires off a long burst of `find` calls (e.g. trying to enumerate every project + workflow + step), you may hit the limit. Use pagination (`cursor`, `limit`) and `count_only=True` for sizing checks instead of fetching the full result set.

Note that a find returns 25 rows per page by default (`step_find` returns 50), so enumerating a large set costs more calls than it used to — raise `limit` on a deliberate sweep rather than paging through at the default. Conversely, if you keep hitting the limit, `count_only=True` and a tighter `fields=[...]` projection usually mean you didn't need the sweep at all.

## A List Looks Short, or an Agent Says "That's All of Them"

Symptom: a find returned fewer rows than you expected, or the agent concluded a project has 25 tables when it has 300.

Fix: check the envelope. A capped page sets `next_cursor`, and a find tool also names the clipped list in `truncated` — either one means there is more to fetch. `total` reports the full count regardless, so compare it against the rows you got. Ask the agent to page with the cursor, or to re-run with a higher `limit`.

## Getting Help

For server-side issues — auth failures, tools returning errors with no obvious cause, missing tools — check the response's `error` envelope first. Every failure includes `code`, `retryable`, `message`, and often a `hint`. If the hint isn't enough, contact your PlaidCloud administrator or open a support ticket with the request ID (returned in the `X-Request-Id` response header).
