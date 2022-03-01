"""create release table

Revision ID: d20e895e399a
Revises: 
Create Date: 2022-02-27 16:33:30.539844

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd20e895e399a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
    'releases', 
    sa.Column('id', sa.Integer(), nullable=False, primary_key=True), 
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('release_date', sa.TIMESTAMP(timezone=True), server_default=sa.text('now()')),
    sa.Column('is_archived', sa.Boolean(), nullable=True, server_default='False')
    )
    pass


def downgrade():
    op.drop_table('releases')
    pass
