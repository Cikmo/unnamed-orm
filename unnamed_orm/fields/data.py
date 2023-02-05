#import datetime
#import functools
#import json
#from typing import Any, Callable, Union

#import orjson
#from ciso8601 import parse_datetime
from enum import Enum #, auto
import typing

class FieldBase:
    SQL_TYPE: str


class IntegerType(FieldBase):
    """A signed 32-bit integer field.
    
    This type is automatically infered when a field is annoted using the built-in `int` type.
    """

    SQL_TYPE = "INTEGER"

class BigIntType(FieldBase):
    """A signed 64-bit integer field."""
    
    SQL_TYPE = "BIGINT"

class SmallIntType(FieldBase):
    """A signed 16-bit integer field."""
    
    SQL_TYPE = "SMALLINT"

class CharType(FieldBase):
    """A fixed-length string field."""
    
    SQL_TYPE = "CHAR"

class TextType(FieldBase):
    """A variable-length string field."""
    
    SQL_TYPE = "TEXT"


class DataTypes(Enum):
    INTEGER = IntegerType
    BIGINT = BigIntType
    SMALLINT = SmallIntType
    CHAR = CharType
    TEXT = TextType


Integer = typing.Annotated[int, DataTypes.INTEGER]
BigInt = typing.Annotated[int, DataTypes.BIGINT]
SmallInt = typing.Annotated[int, DataTypes.SMALLINT]
Char = typing.Annotated[str, DataTypes.CHAR]
Text = typing.Annotated[str, DataTypes.TEXT]