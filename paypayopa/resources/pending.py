from .base import Resource
from ..constants.url import URL
import datetime


class Pending(Resource):
    def __init__(self, client=None):
        super(Pending, self).__init__(client)
        self.base_url = URL.PENDING_PAYMENT

    def create_pending_payment(self, data={}, **kwargs):
        url = self.base_url
        if "requestedAt" not in data:
            data['requestedAt'] = int(datetime.datetime.now().timestamp())
        if "merchantPaymentId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for merchantPaymentId")
        if "userAuthorizationId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for userAuthorizationId")
        if "amount" not in data["amount"]:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for amount")
        if type(data["amount"]["amount"]) != int:
            raise ValueError("\x1b[31m Amount should be of type integer"
                             " \x1b[0m")
        if "currency" not in data["amount"]:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for currency")
        return self.post_url(url, data, **kwargs)

    def get_payment_details(self, id, **kwargs):
        url = "{}/{}".format(self.base_url, id)
        if id is None:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for merchantPaymentId")
        return self.fetch(None, url, **kwargs)

    def cancel_payment(self, id, **kwargs):
        url = "{}/{}".format(self.base_url, id)
        if id is None:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for merchantPaymentId")
        return self.delete(None, url, **kwargs)

    def refund_payment(self, data={}, **kwargs):
        url = "{}/{}".format(self.base_url, 'refunds')
        if "requestedAt" not in data:
            data['requestedAt'] = datetime.datetime.now().second
        if "merchantPaymentId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for merchantPaymentId")
        if "paymentId" not in data:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for userAuthorizationId")
        if "amount" not in data["amount"]:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS "
                             "\x1b[0m for amount")
        if type(data["amount"]["amount"]) != int:
            raise ValueError("\x1b[31m Amount should be of type integer"
                             " \x1b[0m")
        if "currency" not in data["amount"]:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for currency")
        return self.post_url(url, data, **kwargs)

    def refund_details(self, id=None, **kwargs):
        if id is None:
            raise ValueError("\x1b[31m MISSING REQUEST PARAMS"
                             " \x1b[0m for merchantRefundId")
        url = "{}/{}".format(self.base_url, id)
        return self.fetch(None, url, **kwargs)