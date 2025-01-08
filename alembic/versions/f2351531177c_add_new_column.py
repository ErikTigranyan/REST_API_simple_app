"""add new column

Revision ID: f2351531177c
Revises: 000000000000
Create Date: 2025-01-08 19:08:10.612078

"""
from typing import Sequence, Union
from alembic import op
from sqlalchemy import Column, String, Date

# revision identifiers, used by Alembic.
revision: str = 'f2351531177c'
down_revision: Union[str, None] = '000000000000'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.add_column('artist', Column('dod', Date, nullable = True))
    op.add_column('artwork', Column('year', String(200), nullable = True))

def downgrade() -> None:
    op.drop_column('artist', 'dod')
    op.drop_column('artwork', 'year')
