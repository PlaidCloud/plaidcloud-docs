---
linktitle: API
title: "APIs"
type: swagger

weight: 1
description: Interactive API Documentation
---

If you want to send RPC (Remote Procedure Calls), like data reads or writes, you'll need to log in:

1. Click the green **Authorize** button (it should have an open padlock icon)
2. In the **client_id** text field, type the client id `swagger`
3. Click the green **Authorize** button beneath the scopes
4. A PlaidCloud login tab should open in your browser. Log in as you normally would.
5. You should now be logged in. You can close the Available Authorizations window.
6. You can now send RPC requests by going to the method you want and clicking **Try it out**
7. If you're logged in, you should get a response. If you have not successfully logged in, you'll get a 401 Unauthorized error.

{{< swaggerui >}}
