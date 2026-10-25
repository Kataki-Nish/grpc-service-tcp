from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class GetProductRequest(_message.Message):
    __slots__ = ("product_id",)
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    product_id: int
    def __init__(self, product_id: _Optional[int] = ...) -> None: ...

class GetProductResponse(_message.Message):
    __slots__ = ("product_id", "title", "price", "is_available")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    TITLE_FIELD_NUMBER: _ClassVar[int]
    PRICE_FIELD_NUMBER: _ClassVar[int]
    IS_AVAILABLE_FIELD_NUMBER: _ClassVar[int]
    product_id: int
    title: str
    price: float
    is_available: bool
    def __init__(self, product_id: _Optional[int] = ..., title: _Optional[str] = ..., price: _Optional[float] = ..., is_available: _Optional[bool] = ...) -> None: ...

class UpdatePriceRequest(_message.Message):
    __slots__ = ("product_id", "new_price")
    PRODUCT_ID_FIELD_NUMBER: _ClassVar[int]
    NEW_PRICE_FIELD_NUMBER: _ClassVar[int]
    product_id: int
    new_price: float
    def __init__(self, product_id: _Optional[int] = ..., new_price: _Optional[float] = ...) -> None: ...

class UpdatePriceResponse(_message.Message):
    __slots__ = ("success", "message")
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_FIELD_NUMBER: _ClassVar[int]
    success: bool
    message: str
    def __init__(self, success: _Optional[bool] = ..., message: _Optional[str] = ...) -> None: ...
