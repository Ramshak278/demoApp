from rest_framework_simplejwt.tokens import RefreshToken


def get_token_for_user(user):
    refreshToken = RefreshToken.for_user(user)
    return {
        'access':str(refreshToken.access_token)
    }
