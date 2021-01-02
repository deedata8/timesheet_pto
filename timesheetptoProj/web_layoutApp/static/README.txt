Configure project settings for static files.
Run: 'python manage.py collectstatic'  to generate static files at project level for deployment






# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
#when deploying, the host will collect all static files into one dir
#run python manage.py collectstatic to see this happen 
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'pagesApp/static')
]