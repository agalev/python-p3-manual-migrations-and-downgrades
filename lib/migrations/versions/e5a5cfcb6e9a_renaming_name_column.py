"""Renaming name column

Revision ID: e5a5cfcb6e9a
Revises: 42846badc8c5
Create Date: 2023-03-27 08:51:33.179945

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e5a5cfcb6e9a'
down_revision = '791279dd0760'
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.alter_column('students', 'name', new_column_name='student_name')


def downgrade() -> None:
    op.alter_column('students', 'student_name', new_column_name='name')
