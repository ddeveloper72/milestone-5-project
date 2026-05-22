"""
Script to drop all Django tables from Azure SQL database.
Run this if you can't access Azure Portal Query Editor.
"""
import pyodbc
import os
from django.conf import settings

# Azure SQL connection details from .env
SERVER = 'myfreesqldbserver72.database.windows.net'
DATABASE = 'drone_app_v2'
USERNAME = 'developer@myfreesqldbserver72'
PASSWORD = 'M2Dnaa@5036089'

# Connection string
connection_string = (
    f'DRIVER={{ODBC Driver 18 for SQL Server}};'
    f'SERVER={SERVER};'
    f'DATABASE={DATABASE};'
    f'UID={USERNAME};'
    f'PWD={PASSWORD};'
    f'Encrypt=yes;TrustServerCertificate=no;Connection Timeout=120;'
)

# Tables to drop (in order to handle foreign key constraints)
tables_to_drop = [
    'django_admin_log',
    'auth_user_groups',
    'auth_user_user_permissions',
    'auth_group_permissions',
    'django_session',
    'blog_comment',
    'blog_post',
    'issue_tracker_comment',
    'issue_tracker_upvote',
    'issue_tracker_issue',
    'checkout_orderlineitem',
    'checkout_order',
    'userprofile_userprofile',
    'auth_permission',
    'auth_group',
    'auth_user',
    'django_content_type',
    'django_migrations',
]

print("Connecting to Azure SQL...")
try:
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    
    print("Dropping tables...")
    for table in tables_to_drop:
        try:
            print(f"  Dropping {table}...", end='')
            cursor.execute(f"DROP TABLE IF EXISTS [dbo].[{table}]")
            conn.commit()
            print(" ✓")
        except Exception as e:
            print(f" (already dropped or doesn't exist)")
            conn.rollback()
    
    # Verify all tables are dropped
    print("\nVerifying remaining tables...")
    cursor.execute("""
        SELECT TABLE_NAME 
        FROM INFORMATION_SCHEMA.TABLES 
        WHERE TABLE_SCHEMA = 'dbo' AND TABLE_TYPE = 'BASE TABLE'
    """)
    remaining = cursor.fetchall()
    
    if remaining:
        print(f"\n⚠️  {len(remaining)} tables still exist:")
        for row in remaining:
            print(f"  - {row[0]}")
    else:
        print("\n✅ All Django tables successfully dropped!")
        print("\nNow run: python manage.py migrate")
    
    cursor.close()
    conn.close()
    
except Exception as e:
    print(f"\n❌ Error: {e}")
    print("\nTry running the SQL script in Azure Portal instead:")
    print("1. Go to Azure Portal → SQL Database → drone_app_v2")
    print("2. Click 'Query editor'")
    print("3. Run the script from reset_azure_db.sql")
