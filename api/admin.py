from django.contrib import admin

# Register your models here.
from api import models
admin.site.register([models.Course,
                     models.CourseCategory,
                     models.CourseChapter,
                     models.CourseDetail,
                     models.CourseOutline,
                     models.CourseSection,
                     models.CourseSubCategory,
                     models.DegreeCourse,
                     models.Homework,
                     models.OftenAskedQuestion,
                     models.PricePolicy,
                     models.Scholarship,
                     models.Teacher,])