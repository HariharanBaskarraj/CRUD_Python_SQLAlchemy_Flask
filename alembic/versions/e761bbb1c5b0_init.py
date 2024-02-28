"""init

Revision ID: e761bbb1c5b0
Revises: 
Create Date: 2024-02-28 23:11:06.715962

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision: str = 'e761bbb1c5b0'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table('employees', sa.Column('id', sa.Integer, primary_key=True),
                    sa.Column('name', sa.String, nullable=False),
                    sa.Column('age', sa.Integer, nullable=False),
                    sa.Column('city', sa.String, nullable=False)
                    )


def downgrade() -> None:
    op.drop_table('employees')
