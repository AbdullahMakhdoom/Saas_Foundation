import helpers

from django.core.management.base import BaseCommand 
from django.conf import settings
from typing import Any

STATICFILE_VENDOR_DIR = getattr(settings, 'STATICFILE_VENDOR_DIR')

VENDOR_STATICFILES = {
    "saas-theme.min.css": "https://raw.githubusercontent.com/codingforentrepreneurs/SaaS-Foundations/main/src/staticfiles/theme/saas-theme.min.css",
    "flowbite.min.css": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.css",
    "flowbite.min.js": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js",
    "flowbite.min.js.map": "https://cdnjs.cloudflare.com/ajax/libs/flowbite/2.3.0/flowbite.min.js.map"
}

class Command(BaseCommand):

    def handle(self, *args: Any, **kwargs: Any):
        
        self.stdout.write(f"Downloading vendor staticfiles...")
        completed_urls = []

        for filename, url in VENDOR_STATICFILES.items():
            out_path = STATICFILE_VENDOR_DIR / filename
            self.stdout.write(f"Downloading {filename} from {url}")

            df_success = helpers.download_to_local(url, out_path) 
            if df_success:
                completed_urls.append(url)
            else:
                self.stdout.write(f"Failed to download {filename} to {out_path}")

            
        if set(completed_urls) == set(VENDOR_STATICFILES.values()):
            self.stdout.write(self.style.SUCCESS(f"Downloaded all vendor staticfiles."))
        else:   
            self.stdout.write(self.style.WARNING(f"Failed to download all vendor staticfiles."))

        