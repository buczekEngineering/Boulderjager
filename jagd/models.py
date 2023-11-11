from django.contrib.auth.models import User
from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER_CHOICES = [
        ('woman', 'Woman'),
        ('man', 'Man'),
    ]
    COMPETITION_CHOICES = [
        ("pro", "Pro"),
        ("amateur", "Amateur"),
        ("u18", "u18"),
    ]
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='man')
    mode = models.CharField(max_length=10, choices=COMPETITION_CHOICES, default='amateur')


class Boulder(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pro_catgeories = ["pro_woman", "pro_man"]
    all_categories = ["amateur_woman", "amateur_man"]
    boulder_1 = models.CharField(max_length=100, default="None")
    category_1 = models.JSONField(default=all_categories)
    boulder_2 = models.CharField(max_length=100, default="None")
    category_2 = models.JSONField(default=all_categories)
    boulder_3 = models.CharField(max_length=100, default="None")
    category_3 = models.JSONField(default=all_categories)
    boulder_4 = models.CharField(max_length=100, default="None")
    category_4 = models.JSONField(default=all_categories)
    boulder_5 = models.CharField(max_length=100, default="None")
    category_5 = models.JSONField(default=all_categories)
    boulder_6 = models.CharField(max_length=100, default="None")
    category_6 = models.JSONField(default=all_categories)
    boulder_7 = models.CharField(max_length=100, default="None")
    category_7 = models.JSONField(default=all_categories)
    boulder_8 = models.CharField(max_length=100, default="None")
    category_8 = models.JSONField(default=all_categories)
    boulder_9 = models.CharField(max_length=100, default="None")
    category_9 = models.JSONField(default=all_categories)
    boulder_10 = models.CharField(max_length=100, default="None")
    category_10 = models.JSONField(default=all_categories)
    boulder_11 = models.CharField(max_length=100, default="None")
    category_11 = models.JSONField(default=all_categories)
    boulder_12 = models.CharField(max_length=100, default="None")
    category_12 = models.JSONField(default=all_categories)
    category_13 = models.JSONField(default=all_categories)
    boulder_13 = models.CharField(max_length=100, default="None")
    category_14 = models.JSONField(default=all_categories)
    boulder_14 = models.CharField(max_length=100, default="None")
    category_15 = models.JSONField(default=all_categories)
    boulder_15 = models.CharField(max_length=100, default="None")
    category_16 = models.JSONField(default=all_categories)
    boulder_16 = models.CharField(max_length=100, default="None")
    category_17 = models.JSONField(default=all_categories)
    boulder_17 = models.CharField(max_length=100, default="None")
    category_18 = models.JSONField(default=all_categories)
    boulder_18 = models.CharField(max_length=100, default="None")
    category_19 = models.JSONField(default=all_categories)
    boulder_19 = models.CharField(max_length=100, default="None")
    category_20 = models.JSONField(default=all_categories)
    boulder_20 = models.CharField(max_length=100, default="None")
    category_21 = models.JSONField(default=all_categories)
    boulder_21 = models.CharField(max_length=100, default="None")
    category_22 = models.JSONField(default=all_categories)
    boulder_22 = models.CharField(max_length=100, default="None")
    category_23 = models.JSONField(default=all_categories)
    boulder_23 = models.CharField(max_length=100, default="None")
    category_24 = models.JSONField(default=all_categories)
    boulder_24 = models.CharField(max_length=100, default="None")
    category_25 = models.JSONField(default=all_categories)
    boulder_25 = models.CharField(max_length=100, default="None")
    category_26 = models.JSONField(default=all_categories)
    boulder_26 = models.CharField(max_length=100, default="None")
    category_27 = models.JSONField(default=all_categories)
    boulder_27 = models.CharField(max_length=100, default="None")
    category_28 = models.JSONField(default=all_categories)
    boulder_28 = models.CharField(max_length=100, default="None")
    category_29 = models.JSONField(default=all_categories)
    boulder_29 = models.CharField(max_length=100, default="None")
    category_30 = models.JSONField(default=all_categories)
    boulder_30 = models.CharField(max_length=100, default="None")
    category_31 = models.JSONField(default=pro_catgeories)
    boulder_31 = models.CharField(max_length=100, default="None")
    category_32 = models.JSONField(default=pro_catgeories)
    boulder_32 = models.CharField(max_length=100, default="None")
    category_33 = models.JSONField(default=pro_catgeories)
    boulder_33 = models.CharField(max_length=100, default="None")
    category_34 = models.JSONField(default=pro_catgeories)
    boulder_34 = models.CharField(max_length=100, default="None")
    category_35 = models.JSONField(default=pro_catgeories)
    boulder_35 = models.CharField(max_length=100, default="None")
    category_36 = models.JSONField(default=pro_catgeories)
    boulder_36 = models.CharField(max_length=100, default="None")
    category_37 = models.JSONField(default=pro_catgeories)
    boulder_37 = models.CharField(max_length=100, default="None")
    category_38 = models.JSONField(default=pro_catgeories)
    boulder_38 = models.CharField(max_length=100, default="None")
    category_39 = models.JSONField(default=pro_catgeories)
    boulder_39 = models.CharField(max_length=100, default="None")
    category_40 = models.JSONField(default=pro_catgeories)
    boulder_40 = models.CharField(max_length=100, default="None")
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    points = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        # Calculate points based on boulder values
        self.points = self.calculate_points()
        super(Boulder, self).save(*args, **kwargs)

    def calculate_points(self):

        boulder2points_mapping = {"None": 0, "Bonus": 1, "Top": 2}

        # Calculate points for each boulder and sum them up
        points = sum(boulder2points_mapping.get(boulder, 0) for boulder in [self.boulder_1, self.boulder_2, self.boulder_3])

        return points


class VerificationCode(models.Model):
    code = models.CharField(max_length=10, unique=True)
    is_valid = models.BooleanField(default=True)

    def __str__(self):
        return self.code