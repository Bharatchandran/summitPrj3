from django import template
register = template.Library()

@register.filter(name='check_like_exists')
def check_like_exists(like_object, post):
     # get the user id
    post_id = int(post.id)
    return like_object.filter(post_id=post_id).exists()
