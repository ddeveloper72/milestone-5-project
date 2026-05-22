-- SQL Script to clean up Azure SQL database and prepare for fresh Django migrations
-- Run this in Azure Query Editor or SQL Server Management Studio

-- Drop all Django tables
DROP TABLE IF EXISTS [dbo].[django_admin_log];
DROP TABLE IF EXISTS [dbo].[auth_user_groups];
DROP TABLE IF EXISTS [dbo].[auth_user_user_permissions];
DROP TABLE IF EXISTS [dbo].[auth_group_permissions];
DROP TABLE IF EXISTS [dbo].[django_session];
DROP TABLE IF EXISTS [dbo].[auth_permission];
DROP TABLE IF EXISTS [dbo].[auth_group];
DROP TABLE IF EXISTS [dbo].[auth_user];

-- Drop blog app tables
DROP TABLE IF EXISTS [dbo].[blog_comment];
DROP TABLE IF EXISTS [dbo].[blog_post];

-- Drop issue tracker tables
DROP TABLE IF EXISTS [dbo].[issue_tracker_comment];
DROP TABLE IF EXISTS [dbo].[issue_tracker_issue];
DROP TABLE IF EXISTS [dbo].[issue_tracker_upvote];

-- Drop checkout tables
DROP TABLE IF EXISTS [dbo].[checkout_orderlineitem];
DROP TABLE IF EXISTS [dbo].[checkout_order];

-- Drop userprofile tables
DROP TABLE IF EXISTS [dbo].[userprofile_userprofile];

-- Drop Django system tables (IMPORTANT: Do this last!)
DROP TABLE IF EXISTS [dbo].[django_content_type];
DROP TABLE IF EXISTS [dbo].[django_migrations];

-- Verify all tables are dropped
SELECT TABLE_NAME 
FROM INFORMATION_SCHEMA.TABLES 
WHERE TABLE_SCHEMA = 'dbo' 
  AND TABLE_TYPE = 'BASE TABLE';
-- Should return no rows if successful
