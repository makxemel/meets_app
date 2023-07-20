from PIL import Image
import app.models
from django.conf import settings
from django.core.mail import send_mass_mail


def watermark_avatar_service(image_path, watermark_image_path='media/watermark.png'):
    base_image = Image.open(image_path)
    watermark = Image.open(watermark_image_path)

    base_image.paste(watermark, (0, 0))
    base_image.show()
    base_image.save(image_path)


def send_match_letter_to_email(data):
    messages = []

    for (key, value) in data.items():
        message = (
            'Match in MEETS APP!',
            f'«Вы понравились {value[0]}! Почта участника: {value[1]}»',
            settings.EMAIL_HOST_USER,
            [key, ]
        )
        messages.append(message)

    try:
        send_mass_mail(tuple(messages))
    except:
        print("Mail Sending Failed!")
        return False

    return True


def check_match(user_from_id, user_to_id):
    user_from = app.models.User.objects.get(pk=user_from_id)
    user_to = app.models.User.objects.get(pk=user_to_id)

    # collect data for send emails
    data = {
        user_from.email: [user_to.first_name, user_to.email],
        user_to.email: [user_from.first_name, user_from.email]
    }

    if app.models.Likes.objects.filter(user=user_to, user_like=user_from).exists() and data:
        send_match_letter_to_email(data)
        if send_match_letter_to_email:
            print('****************************MATCH EMAIL SENDED')
    else:
        print('----------------------------NO MATCH')


def like(user_from_id, user_to_id):
    user_from = app.models.User.objects.get(pk=user_from_id)
    user_to = app.models.User.objects.get(pk=user_to_id)

    likes = app.models.Likes.objects.get(user=user_from)
    likes.user_like.add(user_to)

    print('++++++++++++++++++++++++++++++USER LIKED')


def like_and_check_match(user_from_id, user_to_id):
    like(user_from_id, user_to_id)
    check_match(user_from_id, user_to_id)

