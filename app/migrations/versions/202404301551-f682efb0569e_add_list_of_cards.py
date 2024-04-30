"""Add list of cards

Revision ID: f682efb0569e
Revises: b274e709df40
Create Date: 2024-04-30 15:51:12.061605

"""

import csv
import os
from collections.abc import Sequence
from typing import Any

from alembic import op
from sqlmodel import UUID, String, column, table

# revision identifiers, used by Alembic.
revision: str = "f682efb0569e"
down_revision: str | None = "b274e709df40"
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, "../../db/cards.csv")


def read_csv_file_to_dict() -> list[dict[str, Any]]:
    with open(filename) as f:
        return list(csv.DictReader(f, fieldnames=["code", "name", "description"]))


table_name = "card"
card_table = table(
    table_name,
    column("id", UUID),
    column("name", String),
    column("description", String),
    column("code", String),
)


def upgrade() -> None:
    op.bulk_insert(card_table, read_csv_file_to_dict())


def downgrade() -> None:
    op.execute(f"delete from {table_name}")
