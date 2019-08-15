"""empty message

Revision ID: ecdb79545d4f
Revises: dea8bbc191dc
Create Date: 2019-08-14 18:19:24.236663

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ecdb79545d4f'
down_revision = 'dea8bbc191dc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=300), nullable=False),
    sa.Column('email', sa.String(length=200), nullable=True),
    sa.Column('passworhash', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('todos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('task', sa.String(length=200), nullable=False),
    sa.Column('done', sa.Integer(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('active', sa.Integer(), nullable=True),
    sa.Column('token', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('todos')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
