ATTACH TABLE _ UUID '4615fe0c-0df4-4067-a8c5-0a217fa73233'
(
    `id` Int32,
    `var1` String,
    `var2` Date
)
ENGINE = MergeTree
ORDER BY id
SETTINGS index_granularity = 8192
