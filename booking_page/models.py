from django.db import models
from datetime import datetime
from django.contrib.auth.models import user

TREATMENT_CHOICES = (
    ("Anti Wrinkle - Consultation", "Anti Wrinkle - Consultation"),
    ("Anti Wrinkle - 1 Area", "Anti Wrinkle - 1 Area"),
    ("Anti Wrinkle - 2 Areas", "Anti Wrinkle - 2 Areas"),
    ("Anti Wrinkle - 3 Areas", "Anti Wrinkle - 3 Areas"),
    ("Dermal Filler - 0.5ml Lip Filler", "Dermal Filler - 0.5ml Lip Filler"),
    ("Dermal Filler - 1ml Lip Filler", "Dermal Filler - 1ml Lip Filler"),
    ("Dermal Filler - Lip Dissolving", "Dermal Filler - Lip Dissolving"),
    ("Skin Booster - Seventy Hyal / S-DNA", "Skin Booster - Seventy Hyal / S-DNA"),
    ("Skin Booster - Profilo", "Skin Booster - Profilo"),
    ("Skin Booster - Lumi Eyes", "Skin Booster - Lumi Eyes"),
    ("Facials - Basic Dermaplane", "Facials - Basic Dermaplane"),
    ("Facials - Luxury Dermaplane", "Facials - Luxury Dermaplane"),
    ("Facials - MYSA Signature Facial", "Facials - MYSA Signature Facial"),
    ("Lemon Bottle - Consultation", "Lemon Bottle - Consultation"),
    ("Lemon Bottle - Small Area (Chin, Jowls...)", "Lemon Bottle - Small Area (Chin, Jowls...)"),
    ("Lemon Bottle - Large Area (Tummy, Arms...)", "Lemon Bottle - Large Area (Tummy, Arms...)"),
    ("Vitamin B12 - 1 Injection", "Vitamin B12 - 1 Injection"),
    ("Vitamin B12 - Course of 5", "Vitamin B12 - Course of 5"),
)

TIME_CHOICES = (
    ("9AM", "9AM"),
    ("9:30AM", "9:30AM"),
    ("10AM", "10AM"),
    ("10:30AM", "10:30AM"),
    ("11AM", "11AM"),
    ("11:30AM", "11:30AM"),
    ("12PM", "12PM"),
    ("2PM", "2PM"),
    ("2:30PM", "2:30PM"),
    ("3PM", "3PM"),
    ("3:30PM", "3:30PM"),
    ("4PM", "4PM"),
    ("4:30PM", "4:30PM"),
    ("5PM", "5PM"),
)

class Appointments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    treatment = models.CharField(max_length=50, choices=TREATMENT_CHOICES, default="Anti Wrinkle")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICES, default="9AM")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def_str_(self)
    return f"{self.user.username} | day: {self.day} | time: {self.time}"