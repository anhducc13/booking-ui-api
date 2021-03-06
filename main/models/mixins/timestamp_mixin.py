import sqlalchemy as _sa
from sqlalchemy import func
from sqlalchemy.ext.declarative import declared_attr


class TimestampMixin:
    """
    Adds `created_at` and `updated_at` common columns to a derived
    declarative model.
    """

    # pylint: disable=invalid-name

    @declared_attr
    def created_at(self):
        return _sa.Column(_sa.TIMESTAMP, nullable=True)

    @declared_attr
    def updated_at(self):
        return _sa.Column(_sa.TIMESTAMP, server_default=func.now(),
                          default=func.now(), onupdate=func.now())
