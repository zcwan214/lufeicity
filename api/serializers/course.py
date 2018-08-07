
from rest_framework import serializers
from api import models


# 专题课
class CourseSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


#  专题课的详情表序列化
class CourseModelSerializer(serializers.ModelSerializer):
    level_name = serializers.CharField(source='get_level_display')
    hours = serializers.CharField(source='coursedetail.hours')
    course_slogan = serializers.CharField(source='coursedetail.course_slogan')
    # recommend_courses = serializers.CharField(source='coursedetail.recommend_courses.all')
    recommend_courses = serializers.SerializerMethodField()
    asked_question = serializers.SerializerMethodField()
    courseoutline = serializers.SerializerMethodField()
    coursechapter = serializers.SerializerMethodField()




    # 章节
    def get_coursechapter(self,row):
        coursechapter_list = row.coursechapters.all()
        return [{'name':item.name} for item in coursechapter_list]


# 大纲
    def get_courseoutline(self,row):
        courseoutline_list = row.coursedetail.courseoutline_set.all()
        return [{'content':item.content,'title':item.title} for item in courseoutline_list]

#  常见问题的方法
    def get_asked_question(self,row):
        asked_list = row.asked_question.all()
        return [{'question': item.question, 'answer': item.answer} for item in asked_list]


    def get_recommend_courses(self,row):
        recommend_list = row.coursedetail.recommend_courses.all()
        return [ {'id':item.id,'name':item.name} for item in recommend_list]

    class Meta:
        model = models.Course
        fields = ['id','name','level_name','hours','course_slogan','recommend_courses','asked_question',
                  'courseoutline','coursechapter']


# 学位课程的序列化
class DegreeSerializer(serializers.ModelSerializer):
    teachers = serializers.SerializerMethodField()
    scholarship = serializers.SerializerMethodField()


    class Meta:
        model = models.DegreeCourse
        fields = ['name','teachers','scholarship']

#   老师的方法
    def get_teachers(self, row):
        teacher_list = row.teachers.all()
        return [ {'name': item.name} for item in teacher_list]

#  奖学金方法
    def get_scholarship(self,row):
        schol_list = row.scholarship_set.all()
        return [{'value': item.value} for item in schol_list]
