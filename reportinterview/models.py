from django.db import models

# Create your models here.
# each Model is created as a sub-class of Django's Model class
"""
class Example(models.Model):
   text_field = models.CharField(max_length=200)
   date_field = models.DateTimeField('name')
   other_model = models.ForeignKey(OtherModel)
"""
class Book(models.Model):
    name = models.CharField(max_length=30)
    year = models.PositiveSmallIntegerField()
    case_count = 0
    frequency = 0
    average_grade = models.DecimalField(max_digits=3, decimal_places=2)
    average_confidence = models.DecimalField(max_digits=3, decimal_places=2)
    def __str__(self):
        return f'{self.name} {str(self.year)}'

class Case(models.Model):
    CASE_TYPE_CHOICES = [
        ('MS', "Market Sizing"),
        ('ME', "Market Entry"),
        ('P', "Profitability"),
        ('GS', "Growth Strategy"),
        ('MA', "M&A"),
        ('CR', "Competitive Response"),
        ('Pr', "Pricing"),
        ('V', "Valuation"),
        ('O', "Other"),
    ]
    book_id = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    industry = models.CharField(max_length=50)
    type = models.CharField(max_length=50, choices=CASE_TYPE_CHOICES, default='O')
    average_grade = models.DecimalField(max_digits=3, decimal_places=2)
    average_confidence = models.DecimalField(max_digits=3, decimal_places=2)
    frequency = models.IntegerField()

    def __str__(self):
        return self.name

class Skill(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Case_Skill(models.Model):
    case_id = models.ForeignKey(Case, on_delete=models.CASCADE)
    skill_id = models.ForeignKey(Skill, on_delete=models.CASCADE)
    has_skill = models.BooleanField()
    
    def __str__(self):
        return f'case_id: {self.case_id}; skill_id: {self.skill_id}; has_skill: {self.has_skill}'

class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    case_count = models.IntegerField()
    interviewee_time = models.IntegerField()
    interviewer_time = models.IntegerField()
    average_grade = models.DecimalField(max_digits=3, decimal_places=2)
    average_confidence = models.DecimalField(max_digits=3, decimal_places=2)
    is_admin = models.BooleanField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Interview(models.Model):
    case_id = models.ForeignKey(Case, on_delete=models.CASCADE)
    date = models.DateTimeField()
    grade = models.DecimalField(max_digits=3, decimal_places=2)
    duration = models.IntegerField()

    def __str__(self):
        return f'{self.case_id} from {self.date}'

class Interviewer(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    interview_id = models.ForeignKey(Interview, on_delete=models.CASCADE)
    Interviewer_notes = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.user_id} {self.interview_id}'

class Interviewee(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    interview_id = models.ForeignKey(Interview, on_delete=models.CASCADE)
    difficulty = models.IntegerField()
    confidence = models.IntegerField()
    interviewee_notes = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.user_id} {self.interview_id}'
