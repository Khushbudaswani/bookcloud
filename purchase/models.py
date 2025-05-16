
from django.db import models

class Purchase(models.Model):
    BOOK_CHOICES = [
        ('book1', 'Harry Potter'),
        ('book2', 'Atomic Habits'),
        ('book3', '1984 by George Orwell'),
        ('book4', 'Deep Work'),
    ]

    book = models.CharField(max_length=100, choices=BOOK_CHOICES)
    quantity = models.PositiveIntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Optional: timestamp

    def __str__(self):
        return f"{self.name} ordered {self.quantity}x {self.get_book_display()}"

