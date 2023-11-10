---
title: Notify Via Twitter
slug: notify-via-twitter
weight: 8.0
description: Send a direct message from PlaidCloud
date: 2022-01-25T07:39:56
---


## Description


Send a Twitter Direct Message (DM) from [@plaidcloud](<https://twitter.com/plaidcloud>).



### Twitter Account


Specify the twitter account to receive the DM from @plaidcloud. This user must be following @plaidcloud to receive the message. It is allowable, although not required, to prefix the username with the at sign (@).



### Message


Enter the desired message. Analyze will not permit a value longer than 140 characters.


Please note that both Project Variables and Workflow Variables are available for use with this transform.


{{< warning >}}
When using variables, it is possible to generate messages which exceed the 140 character limit. If so, the message will NOT be sent. Instead the following error will be written to the log: *Twitter API returned a 403 (Forbidden), There was an error sending your message: The text of your direct message is over 140 characters.
{{< /warning >}}

## Examples

In this example, a DM is sent from [@PlaidCloud](<https://twitter.com/plaidcloud>) to [@tartansolutions](<https://twitter.com/tartansolutions>). System variables are used in the message. The final message reads, *Analyze Demo is running on #PlaidCloud*.
