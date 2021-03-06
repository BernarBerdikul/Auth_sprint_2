from . import api
from .auth_history import AuthHistory
from .change_password import ChangePassword
from .login import UserLogin
from .logout import UserLogoutAccess, UserLogoutRefresh
from .profile import Profile
from .registration import UserRegistration
from .token_refresh import TokenRefresh

api.add_resource(UserRegistration, "/registration")
api.add_resource(UserLogin, "/login")
api.add_resource(UserLogoutAccess, "/logout/access")
api.add_resource(UserLogoutRefresh, "/logout/refresh")
api.add_resource(TokenRefresh, "/token/refresh")
api.add_resource(Profile, "/me/users")
api.add_resource(AuthHistory, "/auth_history")
api.add_resource(ChangePassword, "/change_password")
