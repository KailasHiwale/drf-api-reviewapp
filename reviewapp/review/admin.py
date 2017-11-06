from django.contrib import admin

from review.models.institute import Institute
from review.models.course import Course
from review.models.institute_course import InstituteCourse
from review.models.review_model import Review


class InstituteAdmin(admin.ModelAdmin):
    """ Custom admin interface for `Institute` model """
    list_display = (
        'institute_name',
        'address',
        'office_mail',
        'phone_number',
        'website',
        'institute_type',
        'founded_in',
        'affiliated_to',
        'approved_by',
    )
    list_display_links = ('institute_name', 'website',)
    list_editale = ('address',)
    list_filter = ('institute_type', 'affiliated_to', 'approved_by',)
    search_fields = ('institute_name',)


class CourseAdmin(admin.ModelAdmin):
    """ Custom admin interface for `Course` model """
    list_display = ('course_name', 'course_detail',)
    list_editale = ('course_details',)
    list_filter = ('course_name',)
    search_fields = ('course_name',)


class InstituteCourseAdmin(admin.ModelAdmin):
    """ Custom admin interface for `InstituteCourse` model """
    list_display = ('institute', 'course',)


class ReviewAdmin(admin.ModelAdmin):
    """ Custom admin interface for `Review` model """
    list_display = (
        'institute',
        'reviewer',
        'overall_rating',
        'review_title',
        'merits',
        'demerits',
        'advice',
    )
    list_editale = ('merits', 'demerits', 'advice',)
    list_filter = ('overall_rating',)
    search_fields = ('institute',)


admin.site.register(Institute, InstituteAdmin)
admin.site.register(Course, CourseAdmin)
admin.site.register(InstituteCourse, InstituteCourseAdmin)
admin.site.register(Review, ReviewAdmin)
