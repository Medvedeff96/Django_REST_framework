from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'


GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('вариатор', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)


DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)


class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    model = models.CharField(max_length=50)
    year = models.IntegerField()
    color = models.CharField(max_length=50)
    mileage = models.CharField(max_length=50)
    volume = models.CharField(max_length=50)
    body_type = models.CharField(max_length=9, choices=BODY_TYPE_CHOICES, null=True, blank=True)
    drive_unit = models.CharField(max_length=5, choices=DRIVE_UNIT_CHOICES, null=True, blank=True)
    gearbox = models.CharField(max_length=9, choices=GEARBOX_CHOICES, null=True, blank=True)
    fuel_type = models.CharField(max_length=8, choices=FUEL_TYPE_CHOICES, null=True, blank=True)
    price = models.IntegerField()
    image = models.ImageField()
    pass

    def __str__(self):
        return f'{self.model} {self.year} {self.price}'



class Sale(models.Model):
    id = models.IntegerField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    pass  # реализуйте модель

    def __str__(self):
        return f'{self.client} {self.car.model} {self.created_at}'
