from auth.models import User


class UserRepository:

    @staticmethod
    def create_user(serializer, user_type):
        instance = User()
        for field_name in instance.fields_for_create():
            setattr(instance, field_name, serializer.pop(field_name))
        instance.full_name = f'{instance.first_name} {instance.last_name}'
        instance.user_type = user_type
        instance.username = instance.email
        instance.set_password(serializer.pop('password'))
        instance.save()
        return instance

    @staticmethod
    def update_user(serializer, user_instance: User):
        for field_name in user_instance.fields_for_update():
            setattr(user_instance, field_name, serializer.pop(field_name))
        user_instance.full_name = f'{user_instance.first_name} {user_instance.last_name}'
        user_instance.username = user_instance.email
        user_instance.save()
        return user_instance

    @staticmethod
    def reset_password(serializer, user_instance: User):
        user_instance.set_password(serializer.pop('password'))
        user_instance.save()
        return user_instance
