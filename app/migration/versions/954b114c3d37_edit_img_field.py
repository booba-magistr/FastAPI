"""edit img field

Revision ID: 954b114c3d37
Revises: 4acdfa2fbbea
Create Date: 2025-01-01 18:05:15.018701

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '954b114c3d37'
down_revision: Union[str, None] = '4acdfa2fbbea'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'img',
               existing_type=sa.TEXT(),
               nullable=True)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('product', 'img',
               existing_type=sa.TEXT(),
               nullable=False)
    # ### end Alembic commands ###
