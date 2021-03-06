"""learning migrations 1

Revision ID: 9a1b3ee8d4ad
Revises: 
Create Date: 2020-03-08 21:38:21.111064

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mssql

# revision identifiers, used by Alembic.
revision = '9a1b3ee8d4ad'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('service')
    op.drop_index('ix_invoice_company_id', table_name='invoice')
    op.drop_index('ix_invoice_owner_id', table_name='invoice')
    op.drop_index('ix_invoice_payment_detail_id', table_name='invoice')
    op.drop_table('invoice')
    op.drop_table('product')
    op.drop_table('payment_detail')
    op.drop_index('ix_invoice_line_invoice_id', table_name='invoice_line')
    op.drop_index('ix_invoice_line_product_id', table_name='invoice_line')
    op.drop_index('ix_invoice_line_service_id', table_name='invoice_line')
    op.drop_table('invoice_line')
    op.drop_table('users')
    op.drop_table('company')
    op.drop_table('clients')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clients',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('active_status', mssql.BIT(), autoincrement=False, nullable=False),
    sa.Column('created_by', sa.VARCHAR(collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('creation_time', sa.DATETIME(), autoincrement=False, nullable=False),
    sa.Column('updated_by', sa.VARCHAR(collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('update_time', sa.DATETIME(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('phone', sa.VARCHAR(collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('address_1', sa.VARCHAR(collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('address_2', sa.VARCHAR(collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('post_code', sa.VARCHAR(collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], name='FK__clients__owner_i__4E88ABD4'),
    sa.PrimaryKeyConstraint('id', name='PK__clients__3213E83F3C0C35C0')
    )
    op.create_table('company',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('active_status', mssql.BIT(), autoincrement=False, nullable=False),
    sa.Column('created_by', sa.VARCHAR(collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('creation_time', sa.DATETIME(), autoincrement=False, nullable=False),
    sa.Column('updated_by', sa.VARCHAR(collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('update_time', sa.DATETIME(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('contact_person', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('email', sa.VARCHAR(length=50, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('phone', sa.VARCHAR(length=25, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('address_ln_1', sa.VARCHAR(length=100, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('address_ln_2', sa.VARCHAR(length=100, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(length=50, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('postal_code', sa.VARCHAR(length=15, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], name='FK__company__owner_i__4BAC3F29'),
    sa.PrimaryKeyConstraint('id', name='PK__company__3213E83FE11281F0')
    )
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('active_status', mssql.BIT(), autoincrement=False, nullable=False),
    sa.Column('created_by', sa.VARCHAR(collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('creation_time', sa.DATETIME(), autoincrement=False, nullable=False),
    sa.Column('updated_by', sa.VARCHAR(collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('update_time', sa.DATETIME(), autoincrement=False, nullable=False),
    sa.Column('username', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('password_hash', sa.VARCHAR(length=128, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='PK__users__3213E83FE62C9958')
    )
    op.create_table('invoice_line',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('active_status', mssql.BIT(), autoincrement=False, nullable=False),
    sa.Column('created_by', sa.VARCHAR(collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('creation_time', sa.DATETIME(), autoincrement=False, nullable=False),
    sa.Column('updated_by', sa.VARCHAR(collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('update_time', sa.DATETIME(), autoincrement=False, nullable=False),
    sa.Column('invoice_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('service_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('product_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('quantity', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('charge', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['invoice_id'], ['invoice.id'], name='FK__invoice_l__invoi__66603565'),
    sa.ForeignKeyConstraint(['product_id'], ['invoice.id'], name='FK__invoice_l__produ__68487DD7'),
    sa.ForeignKeyConstraint(['service_id'], ['invoice.id'], name='FK__invoice_l__servi__6754599E'),
    sa.PrimaryKeyConstraint('id', name='PK__invoice___3213E83F3144F170')
    )
    op.create_index('ix_invoice_line_service_id', 'invoice_line', ['service_id'], unique=False)
    op.create_index('ix_invoice_line_product_id', 'invoice_line', ['product_id'], unique=False)
    op.create_index('ix_invoice_line_invoice_id', 'invoice_line', ['invoice_id'], unique=False)
    op.create_table('payment_detail',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('active_status', mssql.BIT(), autoincrement=False, nullable=False),
    sa.Column('created_by', sa.VARCHAR(collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('creation_time', sa.DATETIME(), autoincrement=False, nullable=False),
    sa.Column('updated_by', sa.VARCHAR(collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('update_time', sa.DATETIME(), autoincrement=False, nullable=False),
    sa.Column('acc_name', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('bank_name', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('sort_code', sa.VARCHAR(length=6, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('acc_number', sa.VARCHAR(length=8, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], name='FK__payment_d__owner__5165187F'),
    sa.PrimaryKeyConstraint('id', name='PK__payment___3213E83FE1985A29')
    )
    op.create_table('product',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('active_status', mssql.BIT(), autoincrement=False, nullable=False),
    sa.Column('created_by', sa.VARCHAR(collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('creation_time', sa.DATETIME(), autoincrement=False, nullable=False),
    sa.Column('updated_by', sa.VARCHAR(collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('update_time', sa.DATETIME(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(length=254, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('price', sa.NUMERIC(precision=12, scale=6), autoincrement=False, nullable=True),
    sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], name='FK__product__owner_i__5441852A'),
    sa.PrimaryKeyConstraint('id', name='PK__product__3213E83FD1F2D2DB')
    )
    op.create_table('invoice',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('active_status', mssql.BIT(), autoincrement=False, nullable=False),
    sa.Column('created_by', sa.VARCHAR(collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('creation_time', sa.DATETIME(), autoincrement=False, nullable=False),
    sa.Column('updated_by', sa.VARCHAR(collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('update_time', sa.DATETIME(), autoincrement=False, nullable=False),
    sa.Column('invoice_date', sa.DATETIME(), autoincrement=False, nullable=False),
    sa.Column('company_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('payment_detail_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['company_id'], ['company.id'], name='FK__invoice__company__5CD6CB2B'),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], name='FK__invoice__owner_i__5EBF139D'),
    sa.ForeignKeyConstraint(['payment_detail_id'], ['payment_detail.id'], name='FK__invoice__payment__5DCAEF64'),
    sa.PrimaryKeyConstraint('id', name='PK__invoice__3213E83F3C9DBD09')
    )
    op.create_index('ix_invoice_payment_detail_id', 'invoice', ['payment_detail_id'], unique=False)
    op.create_index('ix_invoice_owner_id', 'invoice', ['owner_id'], unique=False)
    op.create_index('ix_invoice_company_id', 'invoice', ['company_id'], unique=False)
    op.create_table('service',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False, mssql_identity_start=1, mssql_identity_increment=1),
    sa.Column('active_status', mssql.BIT(), autoincrement=False, nullable=False),
    sa.Column('created_by', sa.VARCHAR(collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('creation_time', sa.DATETIME(), autoincrement=False, nullable=False),
    sa.Column('updated_by', sa.VARCHAR(collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('update_time', sa.DATETIME(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=64, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False),
    sa.Column('description', sa.VARCHAR(length=254, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=True),
    sa.Column('charge', sa.FLOAT(precision=53), autoincrement=False, nullable=True),
    sa.Column('owner_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['owner_id'], ['users.id'], name='FK__service__owner_i__571DF1D5'),
    sa.PrimaryKeyConstraint('id', name='PK__service__3213E83F5ED8B3B1')
    )
    # ### end Alembic commands ###
