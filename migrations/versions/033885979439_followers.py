"""followers

Revision ID: 033885979439
Revises: 9522b92b5ae8
Create Date: 2019-08-29 18:47:15.006473

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '033885979439'
down_revision = '9522b92b5ae8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=True),
    sa.Column('followed_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], )
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
