"""empty message

Revision ID: 1a175aef56e2
Revises: 54fb5675650f
Create Date: 2021-04-15 01:03:56.307239

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a175aef56e2'
down_revision = '54fb5675650f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer_orders', sa.Column('order_id', sa.Integer(), nullable=True))
    op.drop_column('customer_orders', 'orderid')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer_orders', sa.Column('orderid', sa.INTEGER(), autoincrement=False, nullable=True))
    op.drop_column('customer_orders', 'order_id')
    # ### end Alembic commands ###