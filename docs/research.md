# Research

## Printing HTML

Reference article on printing HTML

```
https://medium.com/@Idan_Co/the-ultimate-print-html-template-with-header-footer-568f415f6d2a
```

Demo

```
https://plnkr.co/edit/lWk6Yd?preview
```

Print.js

```
https://printjs.crabbly.com/
```

### Idea

Create multiple print ready HTML templates utilizing `print.js` for the printing functionality.

## Django Reference model

[Model Documentation](https://docs.djangoproject.com/en/5.0/topics/db/models/)

```python
# Create your models here.
class Article(models.Model):
    '''
    Holds blog articles
    '''
    unique_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    author = models.ForeignKey(User, verbose_name='Author', on_delete=models.SET_NULL, blank=True, null=True)
    title = models.CharField(verbose_name='Title', max_length=100, unique=True)
    alt_title = models.CharField(verbose_name='Alt title (english)', max_length=100, unique=True, null=True, blank=True)
    content = RichTextUploadingField(verbose_name='Content')
    banner = models.ImageField(verbose_name='Banner',upload_to='banners/blogs', default='defaults/blog_default.webp', validators=[validate_image])
    created_at = models.DateTimeField(verbose_name='created_at', auto_now_add=True)
    slug = models.SlugField(verbose_name='slug', null=True, blank=True)
    tags = models.ManyToManyField('Tag', verbose_name='Tags', blank=True)

```