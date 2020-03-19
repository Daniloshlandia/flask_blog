"""empty message

Revision ID: e35f202c5127
Revises: e6b93365e26d
Create Date: 2020-03-19 23:24:58.810892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e35f202c5127'
down_revision = 'e6b93365e26d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('youtube_id', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'youtube_id')
    # ### end Alembic commands ###