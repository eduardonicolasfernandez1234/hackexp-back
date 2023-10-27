from auth.models import UserEmployee


class UserEmployeeRepository:

    @staticmethod
    def create_user_employee(user_instance):
        UserEmployee.objects.create(user=user_instance)
