"""second

Revision ID: d4da589a645a
Revises: 87053f14d450
Create Date: 2024-07-04 15:04:16.839881

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'd4da589a645a'
down_revision: Union[str, None] = '87053f14d450'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
