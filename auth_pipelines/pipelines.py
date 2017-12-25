# from requests import request, HTTPError
# from django.contrib.auth.models import User


def save_profile(backend, user, is_new, response, *args, **kwargs):

    if backend.name == 'facebook' and is_new:
        # url = 'http://graph.facebook.com/{0}/picture'.format(response['id'])
        user.username = response['id']
        user.save()
        # try:
        # response = request('GET', url, params={'type': 'large'})
        # with open("/home/roshan/Desktop/socialuser.jpg", 'wb') as f:
        #    f.write(response.content)

        # response.raise_for_status()
        # except HTTPError:
        #    pass

    # newuser = User.objects.get(username=str(response['id']))
    # newuser.profile.logout = 1
    # newuser.profile.save()
