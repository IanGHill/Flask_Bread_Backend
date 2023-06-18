"""adjusted models - add recipe image url

Revision ID: f2e445b09e64
Revises: a7fa4c10140f
Create Date: 2023-06-18 20:53:03.256240

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f2e445b09e64'
down_revision = 'a7fa4c10140f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.add_column(sa.Column('image_url', sa.String(length=255), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.drop_column('image_url')

    # ### end Alembic commands ###
