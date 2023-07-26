from django.db import models
from django.urls import reverse

class User(models.Model):
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    password = models.CharField(max_length=255)
    firts_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    is_staff = models.BooleanField()
    is_usersupper = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return self.username

class UserProfile(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    is_active = models.BooleanField(default= True)
    activation_token = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.user.username} - {self.is_active}"

class Tour(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    average_rating = models.DecimalField(max_digits=5, decimal_places=2)
  

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('tour-detail', args=[str(self.id)])

    def __str__(self):
        return self.name
    class Tour(models.Model):
        id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    average_rating = models.DecimalField(max_digits=5, decimal_places=2)
  

    def get_absolute_url(self):
        """Returns the url to access a particular book instance."""
        return reverse('tour-detail', args=[str(self.id)])

    def __str__(self):
        return self.name

    def calculate_stars(self):
        avg_rating = self.average_rating
        if avg_rating >= 4.5:
            return "★★★★★"
        elif avg_rating >= 3.5:
            return "★★★★☆"
        elif avg_rating >= 2.5:
            return "★★★☆☆"
        elif avg_rating >= 1.5:
            return "★★☆☆☆"
        else:
            return "★☆☆☆☆"
        

class Image(models.Model):
    id = models.IntegerField(primary_key=True)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='tour_images/')

    def __str__(self):
        return f"Image {self.id} for Tour {self.tour.name}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    status = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add= True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    number_of_people = models.CharField(max_length=255)
    departure_date = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username} - {self.tour.name} - {self.status}"

class Rating(models.Model):
    id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    rating = models.IntegerField()
    content = models.TextField()
    create_time = models.DateTimeField(auto_now_add= True)

    def __str__(self):
        return f"{self.user.username} - {self.tour.name} - {self.rating}"
