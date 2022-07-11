---
linktitle: API
title: "APIs"
type: swagger
sitemap:
  priority: 1.0
weight: 1
description: Interactive API Documentation
---

If you want to send rpc requests from here, you'll need to log in:

1. Click the green **Authorize** button (it should have an open padlock icon)
2. Scroll to the section of Available Authorizations that says **OAuth2 (OAuth2, implicit)**
3. In the **client_id** text field, type the client id `swagger`
4. Click the green **Authorize** button beneath the scopes
5. A plaidcloud login tab should open in your browser. Log in as you normally would
6. You should now be logged in. You can close the Available Authorizations window
7. You can now send rpc requests by going to the method you want and clicking **Try it out**
8. If you're logged in, you should get a response. If you have not successfully logged in, you'll get a 401 Unauthorized error.

{{< swaggerui src="https://atower.plaidcloud.io/openapi.json" >}}
