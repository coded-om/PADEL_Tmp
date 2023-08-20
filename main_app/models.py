from typing import Any
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from datetime import datetime


class Coustomer(models.Model):
    UserName = models.CharField(
        max_length=20,
        null=False,
        verbose_name="اسم العميل",
        help_text="اكتب اسم العميل",
    )
    UserNum = models.CharField(
        max_length=8, verbose_name="رقم الهاتف", help_text="+رقم الهاتف 968"
    )
    Amount = models.IntegerField(
        default="00",
        verbose_name="السعر",
        validators=[MinValueValidator(0), MaxValueValidator(30)],
    )
    Time = models.DateTimeField(
        null=True, max_length=20, verbose_name="التاريخ و الوقت", default=datetime.now()
    )
    PymentWay = models.CharField(
        max_length=20,
        default="visa",
        verbose_name="طريقه الدفع",
        help_text="Visa او chash",
    )

    def __str__(self) -> str:
        return self.UserName

    class Meta:
        verbose_name = "Consumer"
