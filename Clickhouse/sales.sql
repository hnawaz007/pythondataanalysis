CREATE TABLE default.sales
(
    `productkey` Int256,
    `customerkey` Int256,
    `salesterritorykey` Int256,
    `salesordernumber` String,
    `totalproductcost` Decimal(36,6),
    `salesamount` Decimal(36,6),
    `id` Int32,
    `created_at` String
)
ENGINE = ReplacingMergeTree
PARTITION BY salesordernumber
ORDER BY (id,salesordernumber)
SETTINGS index_granularity = 8192;