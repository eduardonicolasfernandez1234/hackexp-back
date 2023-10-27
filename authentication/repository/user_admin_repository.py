from authentication.models import UserAdmin


class UserAdminRepository:

    @staticmethod
    def create_user_admin(user_instance):
        UserAdmin.objects.create(user=user_instance)
