"""add index

Revision ID: 8cb8f8777556
Revises: f2351531177c
Create Date: 2025-01-08 20:30:06.935005

"""
from typing import Sequence, Union

from alembic import op


# revision identifiers, used by Alembic.
revision: str = '8cb8f8777556'
down_revision: Union[str, None] = 'f2351531177c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_index('ix_artist_full_name', 'artist', ['full_name'])
    op.create_index('ix_storage_storage_name', 'storage', ['storage_name'])

def downgrade() -> None:
    op.drop_index('ix_artist_full_name', 'artist')
    op.drop_index('ix_storage_storage_name', 'storage')