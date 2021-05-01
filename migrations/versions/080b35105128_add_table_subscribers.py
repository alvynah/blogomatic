"""Add table subscribers

Revision ID: 080b35105128
Revises: 5916c57d96e9
Create Date: 2021-05-01 22:57:22.449563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '080b35105128'
down_revision = '5916c57d96e9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('subscribers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subscribers_email'), 'subscribers', ['email'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_subscribers_email'), table_name='subscribers')
    op.drop_table('subscribers')
    # ### end Alembic commands ###
