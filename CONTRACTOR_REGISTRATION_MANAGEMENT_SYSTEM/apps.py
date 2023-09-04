from django.apps import AppConfig as DjangoAppConfig

from datetime import datetime
from dateutil.tz import gettz

from edc_base.apps import AppConfig as BaseEdcBaseAppConfig


class AppConfig(DjangoAppConfig):
    name = 'CONTRACTOR_REGISTRATION_MANAGEMENT_SYSTEM'
    verbose_name = 'CONTRACTOR REGISTRATION MANAGEMENT SYSTEM'


class EdcBaseAppConfig(BaseEdcBaseAppConfig):
    project_name = 'CONTRACTOR REGISTRATION MANAGEMENT SYSTEM'
    institution = 'Triallav Holdings'
    disclaimer = 'For Triallav Holdings & it\'s Customers use only.'