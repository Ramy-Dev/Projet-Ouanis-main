# services.py
from django.conf import settings
import requests
from django.core.mail import send_mail
from django.utils.html import strip_tags
from django.utils import timezone
from django.template.loader import render_to_string
import json
import logging
logger = logging.getLogger(__name__)

class LemonSqueezyService:
    def create_payment_link(self, email, amount, demande_id):
        url = 'https://api.lemonsqueezy.com/v1/checkouts'
        headers = {
            'Authorization': f'Bearer {settings.LEMON_SQUEEZY_API_KEY}',
            'Accept': 'application/vnd.api+json',
            'Content-Type': 'application/vnd.api+json',
        }
        data = {
            "data": {
                "type": "checkouts",
                "attributes": {
                    "custom_price": amount * 100,
                    "checkout_data": {
                        "custom": {
                            "demande_id": str(demande_id)
                        }
                    },
                    "expires_at": (timezone.now() + timezone.timedelta(days=1)).isoformat(),  # Optional expiration time
                },
                "relationships": {
                    "store": {
                        "data": {
                            "type": "stores",
                            "id": "94304"
                        }
                    },
                    "variant": {
                        "data": {
                            "type": "variants",
                            "id": "420304"
                        }
                    }
                }
            }
        }
        try:
            response = requests.post(url, headers=headers, json=data)
            response.raise_for_status()
            return response.json().get('data').get('attributes').get('url')
        except requests.RequestException as e:
            logger.error(f"Request failed: URL={url}, Headers={json.dumps(headers)}, Data={json.dumps(data)}")
            logger.error(f"Response: Status Code={response.status_code}, Content={response.content}")
            return None

class EmailService:
    def send_confirmation_email(self, user, annonce, total_price, payment_link):
        html_message = render_to_string('emails/payment_confirmation.html', {
            'user': user,
            'annonce': annonce,
            'total_price': total_price,
            'payment_link': payment_link,
            'year': timezone.now().year,
        })
        plain_message = strip_tags(html_message)
        send_mail(
            'Payment Confirmation',
            plain_message,
            settings.DEFAULT_FROM_EMAIL,
            [user.email],
            html_message=html_message,
            fail_silently=False,
        )