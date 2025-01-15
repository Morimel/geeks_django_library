from django.db import models

class Books(models.Model):
    GENRE_CHOICES = (
        ('Ужасы', 'Ужасы'),
        ('Комедия', 'Комедия'),
        ('Романтика', 'Романтика'),
    )
    image = models.ImageField(upload_to='books/', verbose_name='загрузите фото')
    title = models.CharField(max_length=100, verbose_name='укажите название фильма')
    description = models.TextField(verbose_name='напишите описание', blank=True, null=True)
    price = models.PositiveIntegerField(verbose_name='укажите цену', default=400)
    created_at = models.DateTimeField(auto_now_add=True)
    genre_choices = models.CharField(max_length=100, choices=GENRE_CHOICES, verbose_name='выберите жанр', default='Комедия')
    director_email = models.EmailField(default='example@gmail.com', verbose_name='укажите email автора')
    director = models.CharField(max_length=100, verbose_name='укажите режиссера', null=True)
    trailer = models.URLField(verbose_name='вставьте ссылку с YouTube', default='https://example.com/trailer')
    
    class Meta:
        verbose_name = 'Книга'
        verbose_name_plural = 'Книги'
        
    def __str__(self):
        return f'{self.title}'
    
    
    
class Reviews(models.Model):
    STARS = (
        ('⭐', '⭐'),
        ('⭐⭐', '⭐⭐'),
        ('⭐⭐⭐', '⭐⭐⭐'),
        ('⭐⭐⭐⭐', '⭐⭐⭐⭐'),
        ('⭐⭐⭐⭐⭐', '⭐⭐⭐⭐⭐'),
    )
    reviews_choice = models.ForeignKey(Books, on_delete=models.CASCADE, related_name='books')
    created_at = models.DateField(auto_now_add=True)
    comment = models.TextField()
    stars = models.CharField(max_length=100, choices=STARS, default='⭐⭐⭐⭐⭐')
    
    def __str__(self):
        return f'{self.comment}-{self.stars}'