"""create users table

Revision ID: dda662b6775d
Revises: 
Create Date: 2023-04-01 22:27:11.119142

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dda662b6775d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        'user',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('user_name', sa.String(50), nullable=False),
        sa.Column('user_pass', sa.String(50), nullable=False),
        sa.Column('user_role', sa.Enum('user', 'admin', name='role'), nullable=False)
    )

def downgrade():
    op.drop_table('account')