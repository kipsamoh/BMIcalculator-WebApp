"""Initial migration.

Revision ID: 82e688e0f673
Revises: 
Create Date: 2024-07-09 09:36:13.396908

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82e688e0f673'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # Add is_admin column to User
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_admin', sa.Boolean(), nullable=True))
        batch_op.add_column(sa.Column('age', sa.Integer(), nullable=True, server_default='0'))  # Default to 0

    # Add category column to BMIHistory
    with op.batch_alter_table('bmi_history', schema=None) as batch_op:
        batch_op.add_column(sa.Column('category', sa.String(length=50), nullable=False, server_default='Unknown'))

    # Add time column to ContactMessage
    with op.batch_alter_table('contact_message', schema=None) as batch_op:
        batch_op.add_column(sa.Column('time', sa.Time(), nullable=True, server_default=sa.sql.expression.func.current_time()))


def downgrade():
    # Drop columns in reverse order
    with op.batch_alter_table('contact_message', schema=None) as batch_op:
        batch_op.drop_column('time')

    with op.batch_alter_table('bmi_history', schema=None) as batch_op:
        batch_op.drop_column('category')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('age')
        batch_op.drop_column('is_admin')
