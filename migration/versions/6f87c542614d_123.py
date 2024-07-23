"""123

Revision ID: 6f87c542614d
Revises: 207b908ed08f
Create Date: 2024-07-04 15:20:25.139469

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '6f87c542614d'
down_revision: Union[str, None] = '207b908ed08f'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
