from django.db import models
from isbn_field import ISBNField
from phonenumber_field.modelfields import PhoneNumberField


class Author(models.Model):
    first_name = models.CharField(max_length=50, blank=False, null=False)
    last_name = models.CharField(max_length=50, blank=False, null=False)
    email = models.EmailField(blank=True, null=True)
    birthday = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Authors"
    
    def __str__(self):
        return f"{self.last_name}, {self.first_name}"


class Publisher(models.Model):
    name = models.CharField(max_length=100, blank=False, null=False, unique=True)
    address = models.CharField(max_length=100, blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "Publishers"

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=255, blank=True)
    isbn = ISBNField(clean_isbn=True, unique=True) 
    pub_date = models.DateField(blank=True, null=True)
    visibility = models.BooleanField(default=True)
    #
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, null=True, blank=True, default=None, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = "Books"

    def __str__(self):
        return self.title

    @property
    def author_name(self):
        return str(self.author)

    @property
    def publisher_name(self):
        return self.publisher.name
