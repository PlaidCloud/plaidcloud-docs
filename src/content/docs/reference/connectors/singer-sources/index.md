---
title: Singer Sources
description: The catalog of Singer tap connectors available as PlaidCloud Singer sources — Stripe, GitHub, databases, and 130+ more SaaS and API sources, each linking to its connector docs.
---

PlaidCloud can pull data from the SaaS apps, APIs, and databases below using [Singer](https://www.singer.io/) taps. Pick one as the **Tap** when you create a [Singer Source connection](/guides/connections/singer-sources/); the connection form then shows that tap's exact configuration fields, each with inline help.

For the full set of options a source supports, see its connector repository (linked in the table). The list below is the current curated, permissively licensed catalog and grows over time — the **Tap** dropdown in the connection editor is always the live source of truth.

## Available Sources (135)

| Source | Tap | Configuration reference |
|--------|-----|-------------------------|
| Aircall | `tap-aircall` | [TicketSwap/tap-aircall](https://github.com/TicketSwap/tap-aircall) |
| Airtable | `tap-airtable` | [tomasvotava/tap-airtable](https://github.com/tomasvotava/tap-airtable) |
| Amazon Advertising | `tap-amazon-advertising` | [dbt-labs/tap-amazon-advertising](https://github.com/dbt-labs/tap-amazon-advertising) |
| Amazon MWS | `tap-amazon-mws` | [adswerve/singer-tap-amazon-mws](https://github.com/adswerve/singer-tap-amazon-mws) |
| Anvil | `tap-anvil` | [svinstech/tap-anvil](https://github.com/svinstech/tap-anvil) |
| Apache Log Files | `tap-apachelog` | [omelark/tap-apachelog](https://github.com/omelark/tap-apachelog) |
| Apaleo | `tap-apaleo` | [felixkoch/tap-apaleo](https://github.com/felixkoch/tap-apaleo) |
| Apple Health | `tap-applehealth` | [felippecaso/tap-applehealth](https://github.com/felippecaso/tap-applehealth) |
| Apple Search Ads | `tap-apple-search-ads` | [mighty-digital/tap-apple-search-ads](https://github.com/mighty-digital/tap-apple-search-ads) |
| AskNicely | `tap-ask-nicely` | [Mashey/tap-ask-nicely](https://github.com/Mashey/tap-ask-nicely) |
| AT Internet | `tap-atinternet` | [GendarmerieNationale/tap-atinternet](https://github.com/GendarmerieNationale/tap-atinternet) |
| Athena | `tap-athena` | [MeltanoLabs/tap-athena](https://github.com/MeltanoLabs/tap-athena) |
| AWS Cost Explorer | `tap-aws-cost-explorer` | [albert-marrero/tap-aws-cost-explorer](https://github.com/albert-marrero/tap-aws-cost-explorer) |
| BambooHR | `tap-bamboohr` | [AutoIDM/autoidm-tap-bamboohr](https://github.com/AutoIDM/autoidm-tap-bamboohr) |
| BigQuery | `tap-bigquery` | [anelendata/tap-bigquery](https://github.com/anelendata/tap-bigquery) |
| Bitso | `tap-bitso` | [edgarrmondragon/tap-bitso](https://github.com/edgarrmondragon/tap-bitso) |
| Bling | `tap-bling` | [Ricardo-Muhlstedt/tap-bling](https://github.com/Ricardo-Muhlstedt/tap-bling) |
| Cassandra | `tap-cassandra` | [datarts-tech/tap-cassandra](https://github.com/datarts-tech/tap-cassandra) |
| Chorusai | `tap-chorusai` | [andyoneal/tap-chorusai](https://github.com/andyoneal/tap-chorusai) |
| ChurnZero | `tap-churnzero` | [MarkEstey/tap-churnzero](https://github.com/MarkEstey/tap-churnzero) |
| CircleCI | `tap-circle-ci` | [MeltanoLabs/tap-circle-ci](https://github.com/MeltanoLabs/tap-circle-ci) |
| ClickHouse | `tap-clickhouse` | [akurdyukov/tap-clickhouse](https://github.com/akurdyukov/tap-clickhouse) |
| Clickup | `tap-clickup` | [AutoIDM/tap-clickup](https://github.com/AutoIDM/tap-clickup) |
| ClinicalTrials.gov | `tap-clinicaltrials` | [edgarrmondragon/tap-clinicaltrials](https://github.com/edgarrmondragon/tap-clinicaltrials) |
| Clockify | `tap-clockify` | [quantile-taps/tap-clockify](https://github.com/quantile-taps/tap-clockify) |
| Cloudwatch | `tap-cloudwatch` | [meltanolabs/tap-cloudwatch](https://github.com/meltanolabs/tap-cloudwatch) |
| Codat | `tap-codat` | [manuphatak/tap-codatio](https://github.com/manuphatak/tap-codatio) |
| Codecov | `tap-codecov` | [pulumi/tap-codecov](https://github.com/pulumi/tap-codecov) |
| Contentful | `tap-contentful` | [GtheSheep/tap-contentful](https://github.com/GtheSheep/tap-contentful) |
| CrateDB | `tap-cratedb` | [crate/meltano-tap-cratedb](https://github.com/crate/meltano-tap-cratedb) |
| CSV | `tap-csv` | [MeltanoLabs/tap-csv](https://github.com/MeltanoLabs/tap-csv) |
| Dagster | `tap-dagster` | [voxmedia/tap-dagster](https://github.com/voxmedia/tap-dagster) |
| dbt Artifacts | `tap-dbt-artifacts` | [Matatika/tap-dbt-artifacts](https://github.com/Matatika/tap-dbt-artifacts) |
| dbt Cloud | `tap-dbt` | [meltanolabs/tap-dbt](https://github.com/meltanolabs/tap-dbt) |
| Delighted | `tap-delighted` | [TicketSwap/tap-delighted](https://github.com/TicketSwap/tap-delighted) |
| Domo | `tap-domo` | [Mashey/tap-domo](https://github.com/Mashey/tap-domo) |
| DuckDB | `tap-duckdb` | [MeltanoLabs/tap-duckdb](https://github.com/MeltanoLabs/tap-duckdb) |
| DynamoDB | `tap-dynamodb` | [MeltanoLabs/tap-dynamodb](https://github.com/MeltanoLabs/tap-dynamodb) |
| Exact | `tap-exact` | [TicketSwap/tap-exact](https://github.com/TicketSwap/tap-exact) |
| exchangerate.host | `tap-exchangeratehost` | [anelendata/tap-exchangeratehost](https://github.com/anelendata/tap-exchangeratehost) |
| FaB DB | `tap-fabdb` | [dwallace0723/tap-fabdb](https://github.com/dwallace0723/tap-fabdb) |
| Feed | `tap-feed` | [jawats/tap-feed](https://github.com/jawats/tap-feed) |
| Fleetio | `tap-fleetio` | [fleetio/tap-fleetio](https://github.com/fleetio/tap-fleetio) |
| Formbricks | `tap-formbricks` | [emilklindt/tap-formbricks](https://github.com/emilklindt/tap-formbricks) |
| Formula 1 | `tap-f1` | [ReubenFrankel/tap-f1](https://github.com/ReubenFrankel/tap-f1) |
| GainsightPX | `tap-gainsightpx` | [Widen/tap-gainsightpx](https://github.com/Widen/tap-gainsightpx) |
| Geekbot | `tap-geekbot` | [edgarrmondragon/tap-geekbot](https://github.com/edgarrmondragon/tap-geekbot) |
| Geospatial datasets | `tap-geo` | [celine-eu/tap-geo](https://github.com/celine-eu/tap-geo) |
| GitHub | `tap-github` | [MeltanoLabs/tap-github](https://github.com/MeltanoLabs/tap-github) |
| GMail | `tap-gmail` | [MeltanoLabs/tap-gmail](https://github.com/MeltanoLabs/tap-gmail) |
| GMail CSV/Excel Attachments | `tap-gmail-csv` | [food-spotter/tap-gmail-csv](https://github.com/food-spotter/tap-gmail-csv) |
| Google Analytics | `tap-google-analytics` | [MeltanoLabs/tap-google-analytics](https://github.com/MeltanoLabs/tap-google-analytics) |
| Google Play (Reviews Scraper) | `tap-google-play` | [edgarrmondragon/tap-google-play](https://github.com/edgarrmondragon/tap-google-play) |
| Google Play Store (GCS Export) | `tap-playstore` | [haleemur/tap-playstore](https://github.com/haleemur/tap-playstore) |
| Google Search Console | `tap-google-search-console` | [MeltanoLabs/tap-google-search-console](https://github.com/MeltanoLabs/tap-google-search-console) |
| Greenhouse | `tap-greenhouse` | [codyss/tap-greenhouse](https://github.com/codyss/tap-greenhouse) |
| GRIB | `tap-grib` | [celine-eu/tap-grib](https://github.com/celine-eu/tap-grib) |
| Healthchecks.io | `tap-healthchecksio` | [reservoir-data/tap-healthchecksio](https://github.com/reservoir-data/tap-healthchecksio) |
| HighLevel | `tap-gohighlevel` | [MeltanoLabs/tap-gohighlevel](https://github.com/MeltanoLabs/tap-gohighlevel) |
| IBM DB2 | `tap-db2` | [danielptv/tap-db2](https://github.com/danielptv/tap-db2) |
| Iceberg | `tap-iceberg` | [shaped-ai/tap-iceberg](https://github.com/shaped-ai/tap-iceberg) |
| Immuta | `tap-immuta` | [immuta/tap-immuta](https://github.com/immuta/tap-immuta) |
| Impact | `tap-impact` | [voxmedia/tap-impact-publisher](https://github.com/voxmedia/tap-impact-publisher) |
| Instagram | `tap-instagram` | [prratek/tap-instagram](https://github.com/prratek/tap-instagram) |
| Instantly AI | `tap-instantly-ai` | [strvcom/tap-instantly-ai](https://github.com/strvcom/tap-instantly-ai) |
| Intercom | `tap-intercom` | [TicketSwap/tap-intercom](https://github.com/TicketSwap/tap-intercom) |
| Jaffle Shop Generator | `tap-jaffle-shop` | [MeltanoLabs/tap-jaffle-shop](https://github.com/MeltanoLabs/tap-jaffle-shop) |
| Jotform | `tap-jotform` | [reservoir-data/tap-jotform](https://github.com/reservoir-data/tap-jotform) |
| KiotViet | `tap-kiotviet` | [chienazazaz/tap-kiotviet](https://github.com/chienazazaz/tap-kiotviet) |
| Klaviyo | `tap-klaviyo` | [hotgluexyz/tap-klaviyo](https://github.com/hotgluexyz/tap-klaviyo) |
| Lever | `tap-lever` | [dbt-labs/tap-lever](https://github.com/dbt-labs/tap-lever) |
| Mailchimp | `tap-mailchimp` | [lovepopcards/tap-mailchimp](https://github.com/lovepopcards/tap-mailchimp) |
| Mailjet | `tap-mailjet` | [Somtom/tap-mailjet](https://github.com/Somtom/tap-mailjet) |
| Megaphone | `tap-megaphone` | [yujoy/tap-megaphone](https://github.com/yujoy/tap-megaphone) |
| Mercado Pago | `tap-mercadopago` | [a-rusi/tap-mercadopago](https://github.com/a-rusi/tap-mercadopago) |
| Messagebird | `tap-messagebird` | [MeltanoLabs/tap-messagebird](https://github.com/MeltanoLabs/tap-messagebird) |
| Microsoft Dataverse | `tap-dataverse` | [mjsqu/tap-dataverse](https://github.com/mjsqu/tap-dataverse) |
| Microsoft Graph | `tap-ms-graph` | [Slalom-Consulting/tap-ms-graph](https://github.com/Slalom-Consulting/tap-ms-graph) |
| Microsoft SQL Server | `tap-mssql` | [BuzzCutNorman/tap-mssql](https://github.com/BuzzCutNorman/tap-mssql) |
| Miro | `tap-miro` | [Slalom-Consulting/tap-miro](https://github.com/Slalom-Consulting/tap-miro) |
| MongoDB | `tap-mongodb` | [MeltanoLabs/tap-mongodb](https://github.com/MeltanoLabs/tap-mongodb) |
| NASA | `tap-nasa` | [edgarrmondragon/tap-nasa](https://github.com/edgarrmondragon/tap-nasa) |
| New Relic | `tap-newrelic` | [fixdauto/tap-newrelic](https://github.com/fixdauto/tap-newrelic) |
| NHL Stats API | `tap-nhl` | [bicks-bapa-roob/tap-nhl](https://github.com/bicks-bapa-roob/tap-nhl) |
| Open-Meteo | `tap-openmeteo` | [celine-eu/tap-openmeteo](https://github.com/celine-eu/tap-openmeteo) |
| OpenProject | `tap-openproject` | [netspective-labs/tap-openproject](https://github.com/netspective-labs/tap-openproject) |
| Oracle | `tap-oracle` | [Hamza-Bouali/tap-oracle](https://github.com/Hamza-Bouali/tap-oracle) |
| Outbrain | `tap-outbrain` | [dbt-labs/tap-outbrain](https://github.com/dbt-labs/tap-outbrain) |
| Parquet | `tap-parquet` | [AE-nv/tap-parquet](https://github.com/AE-nv/tap-parquet) |
| Partnerize | `tap-partnerize` | [voxmedia/tap-partnerize](https://github.com/voxmedia/tap-partnerize) |
| Partoo | `tap-partoo` | [GendarmerieNationale/tap-partoo](https://github.com/GendarmerieNationale/tap-partoo) |
| Peloton | `tap-peloton` | [MeltanoLabs/tap-peloton](https://github.com/MeltanoLabs/tap-peloton) |
| Pipedream | `tap-pipedream` | [edgarrmondragon/tap-pipedream](https://github.com/edgarrmondragon/tap-pipedream) |
| PodBean | `tap-podbean` | [Slalom-Consulting/tap-podbean](https://github.com/Slalom-Consulting/tap-podbean) |
| PowerBI | `tap-powerbi-metadata` | [dataops-tk/tap-powerbi-metadata](https://github.com/dataops-tk/tap-powerbi-metadata) |
| Prometheus | `tap-prometheus` | [signal-ai/tap-prometheus](https://github.com/signal-ai/tap-prometheus) |
| Pulumi Cloud | `tap-pulumi-cloud` | [MeltanoLabs/tap-pulumi-cloud](https://github.com/MeltanoLabs/tap-pulumi-cloud) |
| Pushbullet | `tap-pushbullet` | [edgarrmondragon/tap-pushbullet](https://github.com/edgarrmondragon/tap-pushbullet) |
| PxWeb API | `tap-pxwebapi` | [storebrand/tap-pxwebapi](https://github.com/storebrand/tap-pxwebapi) |
| PyPI Stats | `tap-pypistats` | [edgarrmondragon/tap-pypistats](https://github.com/edgarrmondragon/tap-pypistats) |
| Qualified | `tap-qualified` | [z3z1ma/tap-qualified](https://github.com/z3z1ma/tap-qualified) |
| Quickbase | `tap-quickbase` | [MainspringEnergy/tap-quickbase-json](https://github.com/MainspringEnergy/tap-quickbase-json) |
| Read the Docs | `tap-readthedocs` | [edgarrmondragon/tap-readthedocs](https://github.com/edgarrmondragon/tap-readthedocs) |
| Recruitee | `tap-recruitee` | [rawwar/tap-recruitee](https://github.com/rawwar/tap-recruitee) |
| Reddit Ads | `tap-redditads` | [Ella6882/tap-redditads](https://github.com/Ella6882/tap-redditads) |
| Redshift | `tap-redshift` | [Monad-Inc/tap-redshift](https://github.com/Monad-Inc/tap-redshift) |
| REST API | `tap-rest-api-msdk` | [Widen/tap-rest-api-msdk](https://github.com/Widen/tap-rest-api-msdk) |
| Rick and Morty API | `tap-rickandmorty` | [clrcrl/tap-rickandmorty](https://github.com/clrcrl/tap-rickandmorty) |
| SaasOptics | `tap-saasoptics` | [datarts-tech/tap-saasoptics](https://github.com/datarts-tech/tap-saasoptics) |
| Salesloft | `tap-salesloft` | [MarkEstey/firehose-tap-salesloft](https://github.com/MarkEstey/firehose-tap-salesloft) |
| Service Titan | `tap-service-titan` | [MeltanoLabs/tap-service-titan](https://github.com/MeltanoLabs/tap-service-titan) |
| SharePoint Sites | `tap-sharepointsites` | [storebrand/tap-sharepointsites](https://github.com/storebrand/tap-sharepointsites) |
| Shiphero | `tap-shiphero` | [definite-app/tap-shiphero](https://github.com/definite-app/tap-shiphero) |
| Shopify (GraphQL) | `tap-shopify` | [sehnem/tap-shopify](https://github.com/sehnem/tap-shopify) |
| Shortcut (formerly Clubhouse) | `tap-shortcut` | [edgarrmondragon/tap-shortcut](https://github.com/edgarrmondragon/tap-shortcut) |
| Showpad | `tap-showpad` | [z3z1ma/tap-showpad](https://github.com/z3z1ma/tap-showpad) |
| Slack | `tap-slack` | [MeltanoLabs/tap-slack](https://github.com/MeltanoLabs/tap-slack) |
| Smartsheet | `tap-smartsheet` | [brooklyn-data/tap-smartsheet](https://github.com/brooklyn-data/tap-smartsheet) |
| Socrata | `tap-socrata` | [MeltanoLabs/tap-socrata](https://github.com/MeltanoLabs/tap-socrata) |
| Spreadsheets | `tap-spreadsheets` | [celine-eu/tap-spreadsheets](https://github.com/celine-eu/tap-spreadsheets) |
| SSB Klass API | `tap-ssb-klass` | [storebrand/tap-ssb-klass](https://github.com/storebrand/tap-ssb-klass) |
| StackExchange | `tap-stackexchange` | [MeltanoLabs/tap-stackexchange](https://github.com/MeltanoLabs/tap-stackexchange) |
| Staffwise | `tap-staffwise` | [chartica/tap-staffwise](https://github.com/chartica/tap-staffwise) |
| Strava | `tap-strava` | [dluftspring/tap-strava](https://github.com/dluftspring/tap-strava) |
| Stripe | `tap-stripe` | [TicketSwap/tap-stripe](https://github.com/TicketSwap/tap-stripe) |
| Substack | `tap-substack` | [tripleaceme/tap-substack](https://github.com/tripleaceme/tap-substack) |
| Tempo | `tap-tempo` | [Broscorp-net/tap-tempo](https://github.com/Broscorp-net/tap-tempo) |
| Tiktok Business | `tap-tiktok-business` | [hkuffel/tap-tiktok-business](https://github.com/hkuffel/tap-tiktok-business) |
| Twitter | `tap-twitter` | [voxmedia/tap-twitter](https://github.com/voxmedia/tap-twitter) |
| Typeform | `tap-typeform` | [albert-marrero/tap-typeform](https://github.com/albert-marrero/tap-typeform) |
| Udemy for Business | `tap-udemy-for-business` | [immuta/tap-udemy-for-business](https://github.com/immuta/tap-udemy-for-business) |
| Upwork | `tap-upwork` | [Automattic/tap-upwork](https://github.com/Automattic/tap-upwork) |
| Userflow | `tap-userflow` | [kingalban/tap-userflow](https://github.com/kingalban/tap-userflow) |
| Zendesk Sell | `tap-zendesk-sell` | [leag/tap-zendesk-sell](https://github.com/leag/tap-zendesk-sell) |
| Zoom | `tap-zoom` | [robby-rob-slalom/tap-zoom](https://github.com/robby-rob-slalom/tap-zoom) |
