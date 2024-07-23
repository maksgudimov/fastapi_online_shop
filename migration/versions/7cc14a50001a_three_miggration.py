"""three_miggration

Revision ID: 7cc14a50001a
Revises: d4da589a645a
Create Date: 2024-07-04 15:08:26.713587

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7cc14a50001a'
down_revision: Union[str, None] = 'd4da589a645a'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
