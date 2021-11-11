import sys

from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment


class PayPalClient:
    def __init__(self):
        self.client_id = "AYY-9FkCxhGzEN9aRhg6XC2iIRElPge4oi_bpYaNh3WcfpZGZXYrJodxzsBn26Z_G8Dt76yv41xHgVcv"
        self.client_secret = "EGdHBUxx0YScUEYfoT7kJGVhzFUn32Utl4BpERGqLnJJEw_mV6iHqK4qC8QkdRppMy1EQ9a0TZz3fyfD"
        self.environment = SandboxEnvironment(client_id=self.client_id, client_secret=self.client_secret)
        self.client = PayPalHttpClient(self.environment)
