from django.contrib import admin

from reviewer.models import Reviewer


# class ReviewerAdmin(admin.ModelAdmin):
#     """ Custom admin interface for `Reviewer` model """
#     list_display = (
#         'institute_name',
#         'address',
#         'office_mail',
#         'phone_number',
#         'website',
#         'institute_type',
#         'founded_in',
#         'affiliated_to',
#         'approved_by',
#     )
#     list_display_links = ('website',)
#     list_editale = ('address',)
#     list_filter = ('institute_type', 'affiliated_to', 'approved_by',)
#     search_fields = ('institute_name',)


admin.site.register(Reviewer)
