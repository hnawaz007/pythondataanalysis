ATTACH TABLE _ UUID '14f85e07-9cd0-4fda-bc0a-ab6e0e5d45f9'
(
    `productkey` Int256,
    `customerkey` Int256,
    `salesterritorykey` Int256,
    `salesordernumber` String,
    `totalproductcost` Decimal(36, 6),
    `salesamount` Decimal(36, 6),
    `id` Int32,
    `created_at` String
)
ENGINE = ReplacingMergeTree
PARTITION BY salesordernumber
ORDER BY (id, salesordernumber)
SETTINGS index_granularity = 8192
