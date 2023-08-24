from django import template
register = template.Library()

@register.filter(name='check_membership_exists')
def check_membership_exists(member_object, group):
     # get the user id
    group_id = int(group.id)
    return member_object.filter(group_id=group_id).exists()
