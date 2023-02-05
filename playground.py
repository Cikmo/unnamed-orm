"""This is a playground for testing out new ideas and code snippets."""

import typing
from unnamed_orm.fields.data import BigInt, Text

from pydantic import BaseModel #, Field



class Foo(BaseModel):
    name: Text
    number: BigInt
    number2: None | BigInt = None


x = Foo(name="foo", number=1234556)
type_annotations = typing.get_type_hints(x, include_extras=True)
print(type_annotations)
print("--------------------")

# Pydantic method to infer types. Doesn't work for Annotated types, so I need to implement my own.
# I will probably need to implement a custom BaseModel subclass anyways to add support for various database interactions and stuff.
print(x.schema())

print("--------------------")




# Basic attempt at inferring custom db types from Annotated types. Will need to be improved to handle unions, etc.
# as well as check that that the types are valid. This can be implemented as a method on the custom BaseModel subclass.
# Perhaps in a metaclass that does the check on type checking, so that errors are shown in the editor.
fields = {}
for key, value in type_annotations.items():
    if typing.get_origin(value) is not typing.Annotated:
        if typing.get_origin(value) is typing.Union:
            for l in typing.get_args(value):
                if typing.get_origin(l) is typing.Annotated:
                    t = typing.get_args(l)[1]
                    fields[key] = t
    else:
        t = typing.get_args(value)[1]
        fields[key] = t

print(fields)