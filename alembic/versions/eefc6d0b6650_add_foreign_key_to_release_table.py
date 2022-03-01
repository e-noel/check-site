"""add foreign key to release table

Revision ID: eefc6d0b6650
Revises: 631a73181b3c
Create Date: 2022-02-27 17:03:58.350682

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eefc6d0b6650'
down_revision = '631a73181b3c'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('releases', sa.Column('owner_id', sa.Integer(), nullable=False))
    op.create_foreign_key('releases_users_fk', source_table='releases', referent_table='users', local_cols=['owner_id'], remote_cols=['id'], ondelete='CASCADE')
    pass


def downgrade():
    op.drop_constraint('releases_users_fk', table_name='releases')
    op.drop_column('releases', 'owner_id')
    pass
