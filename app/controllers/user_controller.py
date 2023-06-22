
# Ajoutez d'autres fonctions de contrôleur pour les opérations CRUD (create, update, delete) des utilisateurs.
from app.models.user import User

class UserController:
    def get_all_users(self):
        return User.objects.all()

    def get_user(self, user_id):
        return User.objects.get(id=user_id)

    def create_user(self, name, email):
        user = User(name=name, email=email)
        user.save()

    def update_user(self, user, name, email):
        user.name = name
        user.email = email
        user.save()

    def delete_user(self, user):
        user.delete()
