from __future__ import unicode_literals, absolute_import

from django.utils.translation import ugettext_lazy as _

from temba.channels.types.twilio_messaging_service.views import ClaimView
from temba.channels.views import TWILIO_SUPPORTED_COUNTRIES_CONFIG
from temba.contacts.models import TEL_SCHEME
from temba.utils.timezones import timezone_to_country_code
from ...models import Channel, ChannelType


class TwilioMessagingServiceType(ChannelType):
    """
    An Twilio Messaging Service channel
    """

    code = 'TMS'
    category = ChannelType.Category.PHONE

    name = "Twilio Messaging Service"
    slug = "twilio_messaging_service"
    icon = "icon-channel-twilio"

    claim_blurb = _("""You can connect a messaging service from your Twilio account to benefit from <a href="https://www.twilio.com/copilot">Twilio Copilot features</a></br>""")
    claim_view = ClaimView

    schemes = [TEL_SCHEME]
    max_length = 1600

    attachment_support = True

    def is_recommended_to(self, user):
        org = user.get_org()
        countrycode = timezone_to_country_code(org.timezone)
        return countrycode in TWILIO_SUPPORTED_COUNTRIES_CONFIG

    def send(self, channel, msg, text):
        # use regular Twilio channel sending
        return Channel.get_type_from_code('T').send(channel, msg, text)
