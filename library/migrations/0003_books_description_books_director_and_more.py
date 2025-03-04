# Generated by Django 4.2.17 on 2025-01-13 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_remove_books_description_remove_books_director_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='books',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='напишите описание'),
        ),
        migrations.AddField(
            model_name='books',
            name='director',
            field=models.CharField(max_length=100, null=True, verbose_name='укажите режиссера'),
        ),
        migrations.AddField(
            model_name='books',
            name='director_email',
            field=models.EmailField(default='example@gmail.com', max_length=254, verbose_name='укажите email автора'),
        ),
        migrations.AddField(
            model_name='books',
            name='genre_choices',
            field=models.CharField(choices=[('Ужасы', 'Ужасы'), ('Комедия', 'Комедия'), ('Романтика', 'Романтика')], default='Комедия', max_length=100, verbose_name='выберите жанр'),
        ),
        migrations.AddField(
            model_name='books',
            name='price',
            field=models.PositiveIntegerField(default=400, verbose_name='укажите цену'),
        ),
        migrations.AddField(
            model_name='books',
            name='trailer',
            field=models.URLField(default='https://example.com/trailer', verbose_name='вставьте ссылку с YouTube'),
        ),
    ]
