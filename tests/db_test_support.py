from typing import Any, List

import sqlalchemy
from sqlalchemy import RowMapping

from starter.database_support.database_template import DatabaseTemplate


class TestDatabaseTemplate(DatabaseTemplate):
    def __init__(self) -> None:
        db = sqlalchemy.create_engine(
            url='postgresql://localhost:5432/capstone_starter_test?user=capstone_starter&password=capstone_starter',
            pool_size=4
        )
        super().__init__(db)

    def clear(self):
        pass

    def query_to_dict(self, statement: str, **kwargs: Any) -> List[RowMapping]:
        return [
            row._mapping
            for row in (self.query(statement, **kwargs))
        ]
