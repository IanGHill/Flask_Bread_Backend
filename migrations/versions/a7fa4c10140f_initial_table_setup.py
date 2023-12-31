"""initial table setup

Revision ID: a7fa4c10140f
Revises: 
Create Date: 2023-06-18 12:35:24.985548

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7fa4c10140f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('ingredient_category',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('ingredient_category', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_ingredient_category_name'), ['name'], unique=False)

    op.create_table('raw_material_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('raw_material_type', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_raw_material_type_name'), ['name'], unique=False)

    op.create_table('recipe_type',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('recipe_type', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_recipe_type_name'), ['name'], unique=False)

    op.create_table('supplier',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('contact_first_name', sa.String(length=64), nullable=True),
    sa.Column('contact_last_name', sa.String(length=64), nullable=True),
    sa.Column('telephone_number', sa.String(length=20), nullable=True),
    sa.Column('email_address', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('supplier', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_supplier_name'), ['name'], unique=False)

    op.create_table('raw_material',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('pack_size', sa.Integer(), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('raw_material_type_id', sa.Integer(), nullable=True),
    sa.Column('supplier_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['raw_material_type_id'], ['raw_material_type.id'], ),
    sa.ForeignKeyConstraint(['supplier_id'], ['supplier.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('raw_material', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_raw_material_name'), ['name'], unique=False)

    op.create_table('recipe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('recipe_type_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['recipe_type_id'], ['recipe_type.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_recipe_name'), ['name'], unique=False)

    op.create_table('ingredient',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('recipe_id', sa.Integer(), nullable=True),
    sa.Column('ingredient_category_id', sa.Integer(), nullable=True),
    sa.Column('raw_material_id', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['ingredient_category_id'], ['ingredient_category.id'], ),
    sa.ForeignKeyConstraint(['raw_material_id'], ['raw_material.id'], ),
    sa.ForeignKeyConstraint(['recipe_id'], ['recipe.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('ingredient')
    with op.batch_alter_table('recipe', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_recipe_name'))

    op.drop_table('recipe')
    with op.batch_alter_table('raw_material', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_raw_material_name'))

    op.drop_table('raw_material')
    with op.batch_alter_table('supplier', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_supplier_name'))

    op.drop_table('supplier')
    with op.batch_alter_table('recipe_type', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_recipe_type_name'))

    op.drop_table('recipe_type')
    with op.batch_alter_table('raw_material_type', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_raw_material_type_name'))

    op.drop_table('raw_material_type')
    with op.batch_alter_table('ingredient_category', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_ingredient_category_name'))

    op.drop_table('ingredient_category')
    # ### end Alembic commands ###
