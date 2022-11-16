"""empty message

Revision ID: 82229f8f41ba
Revises: ffdc0a98111c
Create Date: 2022-11-15 20:11:40.405287

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '82229f8f41ba'
down_revision = 'ffdc0a98111c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('questions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('body', sa.String(length=2000), nullable=True),
    sa.Column('postCategory', sa.String(length=25), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('answers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('questionId', sa.Integer(), nullable=True),
    sa.Column('body', sa.String(length=2000), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['questionId'], ['questions.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('votes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('questionId', sa.Integer(), nullable=True),
    sa.Column('voteDirection', sa.String(), nullable=True),
    sa.Column('created_on', sa.Date(), nullable=True),
    sa.Column('updated_on', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['questionId'], ['questions.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('comments',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('userId', sa.Integer(), nullable=True),
    sa.Column('answerId', sa.Integer(), nullable=True),
    sa.Column('body', sa.String(length=2000), nullable=False),
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('updated_on', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['answerId'], ['answers.id'], ),
    sa.ForeignKeyConstraint(['userId'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('comments')
    op.drop_table('votes')
    op.drop_table('answers')
    op.drop_table('questions')
    # ### end Alembic commands ###
