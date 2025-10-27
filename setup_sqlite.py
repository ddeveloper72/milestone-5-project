#!/usr/bin/env python3
"""
Quick setup script - Configure project to use SQLite for immediate testing
"""
import os

def setup_sqlite_for_quick_start():
    """Configure project to use SQLite temporarily"""
    env_file = '.env'
    
    print('🔧 Setting up SQLite for quick development...')
    
    # Read current .env
    with open(env_file, 'r') as f:
        lines = f.readlines()
    
    # Comment out MySQL config and add SQLite flag
    new_lines = []
    for line in lines:
        if line.strip().startswith('MYSQL_'):
            new_lines.append(f'# {line}')  # Comment out MySQL
        else:
            new_lines.append(line)
    
    # Add SQLite configuration
    new_lines.append('\n# SQLite Configuration for quick development\n')
    new_lines.append('USE_SQLITE=True\n')
    
    # Write back
    with open(env_file, 'w') as f:
        f.writelines(new_lines)
    
    print('✅ SQLite configuration added to .env')
    print('💡 This will create a local db.sqlite3 file for development')
    print('📝 You can switch back to MySQL later by removing USE_SQLITE=True')

if __name__ == '__main__':
    setup_sqlite_for_quick_start()