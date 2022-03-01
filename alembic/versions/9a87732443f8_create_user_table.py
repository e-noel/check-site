"""create user table

Revision ID: 9a87732443f8
Revises: 76dd3cbeed21
Create Date: 2022-02-27 16:55:33.748882

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9a87732443f8'
down_revision = '76dd3cbeed21'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
    'users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('created_at', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()'), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    pass


def downgrade():
    op.drop_table('users')
    pass
