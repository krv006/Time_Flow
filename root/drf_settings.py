REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        # todo Login qilmasdan turib get qila oladi
        # 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
        # todo Login qila olmagan xech qaysi bir userga xato get xam ochiq emas
        'rest_framework.permissions.IsAuthenticated',
        # 'apps.authentication.PhoneNumberBackend',
        # 'Time_Flow.apps.permissions.CustomIsAuthenticated'

    ],

    'DEFAULT_SCHEMA_CLASS': 'drf_spectacular.openapi.AutoSchema',

    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ),

    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
    ]

}

SPECTACULAR_SETTINGS = {
    'TITLE': 'Your Project API',
    'DESCRIPTION': 'Your project description',
    'VERSION': '1.0.0',
    'SERVE_INCLUDE_SCHEMA': False,
    # OTHER SETTINGS
}
