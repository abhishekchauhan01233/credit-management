from django.db import models

# Create your models here.
roles = (
    ('Intern','Intern'),
    ('Mentor','Mentor'),
)

class user_model(models.Model):
    user_id = models.BigIntegerField()
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=320, blank=False)
    credit = models.BigIntegerField()

    def __str__(self):
        return self.email

    class Meta:
        verbose_name_plural = 'USERS'

class transaction_model(models.Model):
    from_email = models.EmailField(max_length=320, blank=False)
    to_email = models.EmailField(max_length=320, blank=False)
    date = models.DateField(max_length=20)
    credit = models.BigIntegerField()
    current_time = models.TimeField()

    def __str__(self):
        return self.from_email

    class Meta:
        verbose_name_plural = 'TRANSACTIONS HISTORY'

class feedback_model(models.Model):
    name = models.CharField(max_length=200, blank=False)
    role = models.CharField(max_length=200, choices=roles, blank=False)
    feedback = models.CharField(max_length=200, blank=False)

    def __str__(self):
        return self.role

    class Meta:
        verbose_name_plural = 'FEEDBACK'