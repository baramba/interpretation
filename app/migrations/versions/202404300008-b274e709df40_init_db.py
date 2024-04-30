"""Init DB

Revision ID: b274e709df40
Revises:
Create Date: 2024-04-30 00:08:28.238949

"""
from collections.abc import Sequence

import sqlalchemy as sa
import sqlmodel
from alembic import op

# revision identifiers, used by Alembic.
revision: str = "b274e709df40"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "card",
        sa.Column("id", sqlmodel.sql.sqltypes.GUID(), server_default=sa.text("gen_random_uuid()"), nullable=True),
        sa.Column("created", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
        sa.Column("name", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("description", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("code", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_table(
        "prediction",
        sa.Column("text", sqlmodel.sql.sqltypes.AutoString(), nullable=False),
        sa.Column("id", sqlmodel.sql.sqltypes.GUID(), server_default=sa.text("gen_random_uuid()"), nullable=True),
        sa.Column("created", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
        sa.Column("updated", sa.DateTime(), server_default=sa.text("now()"), nullable=False),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("prediction")
    op.drop_table("card")
    # ### end Alembic commands ###
