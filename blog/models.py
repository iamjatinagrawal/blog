import uuid

from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

User = get_user_model()

#Base Model
class BaseModel(models.Model):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, editable=False
    )
    created_by = models.ForeignKey(User, null=True, blank=True, on_delete=models.PROTECT)
    last_modified_by = models.ForeignKey(
        User, null=True, blank=True, on_delete=models.CASCADE, related_name="%(app_label)s_%(class)s_related"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)


#Category Model
class Category(BaseModel):
    name = models.CharField(max_length=50, null=False, blank=False)

    class Meta:
        db_table = 'CategoryModel'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


#Post Model
class Post(BaseModel):
    title = models.CharField(max_length=150, null=False, blank=False)
    short_description = models.CharField(max_length=250, null=True, blank=True)
    # index_image = models.ImageField(null=True, blank=True, upload_to='blog/index_image/')
    index_image = models.URLField(max_length=500,null=True, blank=True)
    category = models.ManyToManyField(Category, blank=False)
    content = RichTextField(null=True, blank=True)

    class Meta:
        db_table = 'PostModel'
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title

    # def get_absolute_url(self):
    #     return reverse("post_detail",kwargs={'pk':self.pk})



class ContactFormModel(BaseModel):
    full_name = models.CharField(max_length=250, null=False, blank=False)
    email = models.EmailField()
    subject = models.CharField(max_length=250, null=False, blank=False)
    message = models.TextField(max_length=1000, null=False, blank=False)

    def __str__(self):
        return self.full_name
    
    class Meta:
        db_table = 'ContactFormModel'
        verbose_name = 'Contact Form'
        verbose_name_plural = 'Contact Forms' 








