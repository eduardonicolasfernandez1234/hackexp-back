from authentication.models import UserEmployee


class UserEmployeeRepository:

    @staticmethod
    def create_user_employee(user_instance, business_id: int):
        UserEmployee.objects.create(user=user_instance, business_id=business_id)
