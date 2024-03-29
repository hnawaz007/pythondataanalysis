from typing import Optional, Any, Type, TYPE_CHECKING
from typing_extensions import TypeAlias
from sqlalchemy import Table, Column
from sqlalchemy.sql import sqltypes, Select

from dlt.common.schema.typing import TColumnSchema, TTableSchemaColumns

# optionally create generics with any so they can be imported by dlt importer
if TYPE_CHECKING:
    SelectAny: TypeAlias = Select[Any]
    ColumnAny: TypeAlias = Column[Any]
else:
    SelectAny: TypeAlias = Type[Any]
    ColumnAny: TypeAlias = Type[Any]


def sqla_col_to_column_schema(sql_col: ColumnAny) -> Optional[TColumnSchema]:
    """Infer dlt schema column type from an sqlalchemy type.

    Precision and scale is inferred from that types that support it,
    such as numeric, varchar, int, bigint
    """
    sql_t = sql_col.type
    col = None

    if isinstance(sql_t, sqltypes.BigInteger):
        col = dict(name=sql_col.name, data_type="bigint", precision=64)
    elif isinstance(sql_t, sqltypes.SmallInteger):
        col = dict(name=sql_col.name, data_type="bigint", precision=16)
    elif isinstance(sql_t, sqltypes.Integer):
        col = dict(name=sql_col.name, data_type="bigint", precision=32)
    elif isinstance(sql_t, sqltypes.Numeric) and not isinstance(sql_t, sqltypes.Float):
        col = dict(
            name=sql_col.name,
            data_type="decimal",
            precision=sql_t.precision,
            scale=sql_t.scale,
        )
    elif isinstance(sql_t, sqltypes.String):
        col = dict(name=sql_col.name, data_type="text", precision=sql_t.length)
    elif isinstance(sql_t, sqltypes._Binary):
        col = dict(name=sql_col.name, data_type="binary", precision=sql_t.length)
    elif isinstance(sql_t, sqltypes.DateTime):
        col = dict(name=sql_col.name, data_type="timestamp")
    elif isinstance(sql_t, sqltypes.Date):
        col = dict(name=sql_col.name, data_type="date")
    elif isinstance(sql_t, sqltypes.Time):
        col = dict(name=sql_col.name, data_type="time")
    if col:
        return {key: value for key, value in col.items() if value is not None}  # type: ignore[return-value]
    return None


def table_to_columns(table: Table) -> TTableSchemaColumns:
    """Convert an sqlalchemy table to a dlt table schema.

    Only columns types supporting precision/scale are included in result.
    """
    return {
        col["name"]: col
        for col in (sqla_col_to_column_schema(c) for c in table.columns)
        if col is not None
    }
