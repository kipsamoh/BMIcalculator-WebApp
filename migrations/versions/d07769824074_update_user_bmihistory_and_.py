"""Update User, BMIHistory, and ContactMessage models

Revision ID: d07769824074
Revises: 82e688e0f673
Create Date: 2024-07-12 12:37:30.094094

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd07769824074'
down_revision = '82e688e0f673'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bmi_history', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sa.String(length=50), nullable=False))

    with op.batch_alter_table('contact_message', schema=None) as batch_op:
        batch_op.add_column(sa.Column('time', sa.Time(), nullable=False))

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('age', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('age')

    with op.batch_alter_table('contact_message', schema=None) as batch_op:
        batch_op.drop_column('time')

    with op.batch_alter_table('bmi_history', schema=None) as batch_op:
        batch_op.drop_column('category')

    # ### end Alembic commands ###
