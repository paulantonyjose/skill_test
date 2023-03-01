from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources,fields
from .models import TableTwo,TableOne
from import_export.widgets import ForeignKeyWidget




class TableTwoResource(resources.ModelResource):
    table_one = fields.Field(
        column_name='table_one',
        attribute='table_one',
        widget=ForeignKeyWidget(TableOne, field='name'))

    class Meta:
        model = TableTwo
        fields = ('id', 'class_name', 'weight', 'other_details', 'table_one')

@admin.register(TableTwo)
class TableTwoAdmin(ImportExportModelAdmin):
    resource_class = TableTwoResource


admin.site.register(TableOne)