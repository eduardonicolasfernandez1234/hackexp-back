from authentication.models import UserBusiness


class UserBusinessRepository:

    @staticmethod
    def create_user_business(user_instance):
        UserBusiness.objects.create(user=user_instance)
