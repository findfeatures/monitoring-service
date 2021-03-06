"""Created Api Requests table

Revision ID: fa9201a8d71b
Revises: 
Create Date: 2020-01-02 16:40:02.089541

"""
import sqlalchemy as sa
from alembic import op


# revision identifiers, used by Alembic.
revision = "fa9201a8d71b"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "api_requests",
        sa.Column("id", sa.Integer(), nullable=False),
        sa.Column(
            "created_datetime_utc",
            sa.DateTime(),
            server_default=sa.text("(now() at time zone 'utc')"),
            nullable=False,
        ),
        sa.Column("url", sa.Text(), nullable=True),
        sa.Column("method", sa.Text(), nullable=True),
        sa.Column("duration", sa.Text(), nullable=False),
        sa.Column("status", sa.Text(), nullable=True),
        sa.Column("status_code", sa.Integer(), nullable=True),
        sa.Column("remote_addr", sa.Text(), nullable=True),
        sa.PrimaryKeyConstraint("id"),
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("api_requests")
    # ### end Alembic commands ###
