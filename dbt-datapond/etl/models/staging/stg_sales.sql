SELECT *
FROM {{ source('external_source', 'salesdata') }}
