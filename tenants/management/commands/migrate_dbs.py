from django.core.management.commands.migrate import Command as MigrationCommand

from django.db import connection
from tenants.utils import get_tenants_map


class Command(MigrationCommand):
    def handle(self, *args, **options):
        with connection.cursor() as cursor:
            dbs = get_tenants_map().values()
            for db in dbs:
                super(Command, self).handle(*args, **options)