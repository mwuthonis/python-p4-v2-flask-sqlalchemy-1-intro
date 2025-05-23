"""Added constraints to Pet model

Revision ID: b4dddecf8542
Revises: 9d064dc0b2bb
Create Date: 2025-05-20 14:41:07.565005

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b4dddecf8542'
down_revision = '9d064dc0b2bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pets', schema=None) as batch_op:
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=False)
        batch_op.alter_column('species',
               existing_type=sa.VARCHAR(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pets', schema=None) as batch_op:
        batch_op.alter_column('species',
               existing_type=sa.VARCHAR(),
               nullable=True)
        batch_op.alter_column('name',
               existing_type=sa.VARCHAR(),
               nullable=True)

    # ### end Alembic commands ###
