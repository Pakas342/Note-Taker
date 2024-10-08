"""Category to Project relationship changed, many to one

Revision ID: 97a07f69c7f9
Revises: 11a51b8a9144
Create Date: 2024-08-19 23:29:27.871978

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '97a07f69c7f9'
down_revision = '11a51b8a9144'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('project_category')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('project_category',
    sa.Column('category_id', sa.INTEGER(), nullable=False),
    sa.Column('project_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['category_id'], ['category.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['project.id'], ),
    sa.PrimaryKeyConstraint('category_id', 'project_id')
    )
    # ### end Alembic commands ###
