from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission

class Command(BaseCommand):
    help = 'Create default user groups and assign custom permissions'

    def handle(self, *args, **kwargs):
        # Create or get the groups
        editors, _ = Group.objects.get_or_create(name='Editors')
        viewers, _ = Group.objects.get_or_create(name='Viewers')
        admins, _ = Group.objects.get_or_create(name='Admins')

        # Get the permissions
        perms = Permission.objects.filter(codename__in=[
            'can_create', 'can_view', 'can_edit', 'can_delete'
        ])
        perm = {p.codename: p for p in perms}

        # Assign permissions
        editors.permissions.set([perm['can_create'], perm['can_edit']])
        viewers.permissions.set([perm['can_view']])
        admins.permissions.set(perms)

        self.stdout.write(self.style.SUCCESS('✅ Groups and permissions created successfully.'))

