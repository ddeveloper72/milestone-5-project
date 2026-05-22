#!/usr/bin/env python
"""
Add bio to duncan's user profile
Run this with: python add_duncan_bio.py
"""
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'drone_debug.settings')
django.setup()

from django.contrib.auth.models import User
from userprofile.models import UserProfile

# Bio text for duncan
bio_text = """Software engineer and drone enthusiast with a passion for debugging complex systems. When not wrestling with code, you'll find me piloting custom-built drones or helping fellow makers troubleshoot their builds. Believer in open collaboration and the power of community knowledge. Always learning, always flying!"""

try:
    # Get or create duncan's profile
    duncan = User.objects.get(username='duncan')
    profile, created = UserProfile.objects.get_or_create(user=duncan)
    
    # Update bio and location
    profile.bio = bio_text
    profile.location = 'Ireland'
    profile.save()
    
    if created:
        print(f"✅ Created new profile for {duncan.username}")
    else:
        print(f"✅ Updated existing profile for {duncan.username}")
    
    print(f"📝 Bio: {profile.bio[:50]}...")
    print(f"📍 Location: {profile.location}")
    
except User.DoesNotExist:
    print("❌ User 'duncan' not found. Please create the user first.")
except Exception as e:
    print(f"❌ Error: {e}")
