-- Add bio for duncan user
-- This script adds a professional bio to duncan's UserProfile

-- First, ensure the UserProfile exists for user 'duncan'
-- If it doesn't exist, this will create it
INSERT INTO userprofile_userprofile (user_id, bio, location, birth_date)
SELECT 
    id,
    'Software engineer and drone enthusiast with a passion for debugging complex systems. When not wrestling with code, you''ll find me piloting custom-built drones or helping fellow makers troubleshoot their builds. Believer in open collaboration and the power of community knowledge. Always learning, always flying!',
    'Ireland',
    NULL
FROM auth_user 
WHERE username = 'duncan'
AND id NOT IN (SELECT user_id FROM userprofile_userprofile);

-- If the profile already exists, update it
UPDATE userprofile_userprofile
SET 
    bio = 'Software engineer and drone enthusiast with a passion for debugging complex systems. When not wrestling with code, you''ll find me piloting custom-built drones or helping fellow makers troubleshoot their builds. Believer in open collaboration and the power of community knowledge. Always learning, always flying!',
    location = 'Ireland'
WHERE user_id = (SELECT id FROM auth_user WHERE username = 'duncan');
