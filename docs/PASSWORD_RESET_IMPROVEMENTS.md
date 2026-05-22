# Password Reset System - Improvements & Documentation

## What Was Fixed

### 1. **Email Configuration (settings.py)**
- ✅ Added `EMAIL_BACKEND` - Required for Django to send emails
- ✅ Added `DEFAULT_FROM_EMAIL` - Sets the "From" address
- ✅ Added `SERVER_EMAIL` - Used for server error notifications
- ✅ Added `PASSWORD_RESET_TIMEOUT` - Links expire after 1 hour (security best practice)

### 2. **URL Structure (url_reset.py)**
- ✅ Fixed inconsistent URL paths (was mixing `password_reset` and `reset` prefixes)
- ✅ Added explicit template names for all views
- ✅ Added `success_url` for proper redirects
- ✅ Fixed path structure to match Django standards:
  - Request: `/reset/password_reset/`
  - Email sent: `/reset/password_reset/done/`
  - Confirm: `/reset/reset/<uidb64>/<token>/`
  - Complete: `/reset/reset/done/`

### 3. **Email Template (password_reset_email.html)**
- ✅ Created proper plain-text email template
- ✅ Includes reset link, username, and expiry info
- ✅ Security message if not requested

### 4. **User Experience**
- ✅ Updated completion page with prominent "Log In" button
- ✅ Existing "Forgot Password?" link on login page
- ✅ Clear messaging throughout the flow

## How to Test

### 1. Test Email Configuration
```powershell
python test_email_config.py
```
This will send a test email to verify your SMTP setup works.

### 2. Test Password Reset Flow
1. Go to login page: http://localhost:8000/accounts/login/
2. Click "Reset Password" link
3. Enter your email address
4. Check your email inbox (and spam folder!)
5. Click the reset link
6. Enter new password twice
7. Log in with new password

### 3. Production Testing (Heroku)
Same flow as above, but use: https://ddeveloper72-custom-drone.herokuapp.com/accounts/login/

## Gmail Configuration

### Current Setup
- **Email**: ddeveloper72@gmail.com
- **Password**: App Password (16 characters)
- **SMTP**: smtp.gmail.com:587 with TLS

### Important Notes

1. **App Passwords Required**
   - Gmail requires App Passwords if 2FA is enabled
   - Regular passwords won't work anymore
   - Generate at: https://myaccount.google.com/apppasswords

2. **2-Factor Authentication**
   - Must be enabled on your Google account
   - Required to create App Passwords

3. **Security Settings**
   - "Less secure apps" no longer supported by Gmail
   - App Passwords are the modern, secure method

### Troubleshooting Email Issues

#### Email Not Received?
1. ✅ Check spam/junk folder
2. ✅ Verify email address is correct in database
3. ✅ Run `python test_email_config.py` to test SMTP
4. ✅ Check Heroku logs: `heroku logs --tail -a ddeveloper72-custom-drone`

#### SMTP Authentication Failed?
1. ✅ Regenerate App Password in Google Account
2. ✅ Update `EMAIL_PASSWORD` in `.env` and Heroku config vars
3. ✅ Ensure 2FA is enabled on Google account

#### Reset Link Expired?
- Links expire after 1 hour (configurable via `PASSWORD_RESET_TIMEOUT`)
- User must request a new reset

## Environment Variables

### Local (.env file)
```env
EMAIL_ADDRESS=ddeveloper72@gmail.com
EMAIL_PASSWORD=your_16_char_app_password
```

### Heroku (Config Vars)
```bash
heroku config:set EMAIL_ADDRESS=ddeveloper72@gmail.com -a ddeveloper72-custom-drone
heroku config:set EMAIL_PASSWORD=your_16_char_app_password -a ddeveloper72-custom-drone
```

## Alternative Email Providers

If Gmail causes issues, consider these alternatives:

### 1. **SendGrid** (Recommended for production)
- Free tier: 100 emails/day
- No SMTP restrictions
- Better deliverability
```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_HOST_USER = 'apikey'
EMAIL_HOST_PASSWORD = env('SENDGRID_API_KEY')
EMAIL_PORT = 587
EMAIL_USE_TLS = True
```

### 2. **Mailgun**
- Free tier: 5,000 emails/month
- Good for testing and production

### 3. **Amazon SES**
- Pay-as-you-go pricing
- Extremely reliable
- Requires AWS account

## Security Best Practices

1. ✅ **Password Reset Timeout**: 1 hour (can extend if needed)
2. ✅ **HTTPS Only**: Production must use HTTPS
3. ✅ **Email Validation**: Django validates email format
4. ✅ **Token Encryption**: Django uses secure tokens
5. ✅ **No Username Disclosure**: Doesn't reveal if email exists

## File Structure

```
accounts/
├── url_reset.py          # Password reset URLs
├── views.py              # Login/logout views
└── templates/
    └── login.html        # Has "Reset Password" link

templates/registration/
├── password_reset_form.html        # Enter email
├── password_reset_done.html        # Check inbox message
├── password_reset_confirm.html     # Enter new password
├── password_reset_complete.html    # Success + login button
├── password_reset_email.html       # Email content (plain text)
└── password_reset_subject.txt      # Email subject

drone_debug/
└── settings.py           # Email configuration
```

## Migration Notes

- No database migrations required
- Only configuration and template changes
- Safe to deploy immediately

## Commit Summary

Files modified:
- `drone_debug/settings.py` - Added email backend and timeout
- `accounts/url_reset.py` - Fixed URL structure
- `templates/registration/password_reset_email.html` - New email template
- `templates/registration/password_reset_complete.html` - Better UX
- `test_email_config.py` - Email testing utility (NEW)

## Next Steps

1. Test locally: `python test_email_config.py`
2. Test full flow on localhost
3. Deploy to Heroku
4. Test on production
5. Monitor Heroku logs for any email errors

## Support

If issues persist:
1. Check Heroku logs: `heroku logs --tail -a ddeveloper72-custom-drone | grep email`
2. Verify Django version is compatible (4.2.16 ✅)
3. Consider switching to SendGrid for production reliability
