"""add dependency column

Revision ID: 76dd3cbeed21
Revises: d20e895e399a
Create Date: 2022-02-27 16:43:49.874467

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '76dd3cbeed21'
down_revision = 'd20e895e399a'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('releases', sa.Column('dependency', sa.Integer(), nullable=False, server_default='0'))
    pass


def downgrade():
    op.drop_column('releases', 'dependency')
    pass
