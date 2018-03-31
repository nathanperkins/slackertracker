"""empty message

Revision ID: f981b330ee9b
Revises: 
Create Date: 2018-03-30 23:58:15.756900

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f981b330ee9b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('channel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('slack_id', sa.String(length=32), nullable=False),
    sa.Column('team_id', sa.String(length=32), nullable=False),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('is_private', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('team_id', sa.String(length=32), nullable=False),
    sa.Column('slack_id', sa.String(length=32), nullable=False),
    sa.Column('display_name', sa.String(length=128), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('slack_id')
    )
    op.create_table('reaction',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=32), nullable=False),
    sa.Column('team_id', sa.String(length=32), nullable=False),
    sa.Column('channel_id', sa.Integer(), nullable=True),
    sa.Column('sender_id', sa.Integer(), nullable=False),
    sa.Column('receiver_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['channel_id'], ['channel.id'], ),
    sa.ForeignKeyConstraint(['receiver_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['sender_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reaction')
    op.drop_table('user')
    op.drop_table('channel')
    # ### end Alembic commands ###
