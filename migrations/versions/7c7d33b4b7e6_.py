"""empty message

Revision ID: 7c7d33b4b7e6
Revises: a930cbe05aa9
Create Date: 2021-04-15 01:08:30.338870

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '7c7d33b4b7e6'
down_revision = 'a930cbe05aa9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('customer_orders', 'ord_date3')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer_orders', sa.Column('ord_date3', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
