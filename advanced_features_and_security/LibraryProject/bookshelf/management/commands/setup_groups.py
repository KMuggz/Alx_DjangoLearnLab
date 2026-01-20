from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from bookshelf.models import Book

class Command(BaseCommand):
    help = 'Sets up groups and permissions for the bookshelf app'

    def handle(self, *args, **kwargs):
        # get the content type for the Book model
        content_type = ContentType.objects.get_for_model(Book)

        # fetched the permissions defined in Book's Meta class
        # using get_or_create to ensure the script is idempotent
        view_perm, _ = Permission.objects.get_or_create(
            codename='can_view', 
            content_type=content_type,
            defaults={'name': 'Can view book'}
        )
        create_perm, _ = Permission.objects.get_or_create(
            codename='can_create', 
            content_type=content_type,
            defaults={'name': 'Can create book'}
        )
        edit_perm, _ = Permission.objects.get_or_create(
            codename='can_edit', 
            content_type=content_type,
            defaults={'name': 'Can edit book'}
        )
        delete_perm, _ = Permission.objects.get_or_create(
            codename='can_delete', 
            content_type=content_type,
            defaults={'name': 'Can delete book'}
        )

        # create Groups and Assign Permissions

        # viewers - can only view
        viewers_group, _ = Group.objects.get_or_create(name='Viewers')
        viewers_group.permissions.add(view_perm)

        # editors - can view, create, and edit
        editors_group, _ = Group.objects.get_or_create(name='Editors')
        editors_group.permissions.set([view_perm, create_perm, edit_perm])

        # admins - can do everything
        admins_group, _ = Group.objects.get_or_create(name='Admins')
        admins_group.permissions.set([view_perm, create_perm, edit_perm, delete_perm])

        self.stdout.write(self.style.SUCCESS("Groups and permissions have been set up successfully."))