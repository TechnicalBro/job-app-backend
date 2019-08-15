"""empty message

Revision ID: 1237e897b93d
Revises: 180f23f0c79a
Create Date: 2019-02-20 14:04:57.264976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1237e897b93d'
down_revision = '180f23f0c79a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_job_experience', sa.Column('job_category_id', sa.Integer(), nullable=False))
    op.drop_constraint('user_job_experience_job_type_id_fkey', 'user_job_experience', type_='foreignkey')
    op.create_foreign_key(None, 'user_job_experience', 'job_category', ['job_category_id'], ['id'])
    op.drop_column('user_job_experience', 'job_type_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_job_experience', sa.Column('job_type_id', sa.INTEGER(), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'user_job_experience', type_='foreignkey')
    op.create_foreign_key('user_job_experience_job_type_id_fkey', 'user_job_experience', 'job_category', ['job_type_id'], ['id'])
    op.drop_column('user_job_experience', 'job_category_id')
    # ### end Alembic commands ###
