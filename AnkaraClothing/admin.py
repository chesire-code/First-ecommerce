from django.contrib import admin
from .models import (smartphone,
                     earphones,
                     bt_speaker,
                     cover,
                     USB_drive,
                     charger,
                     offer,
                     bestseller,
                     )


admin.site.register(charger)
admin.site.register(cover)
admin.site.register(USB_drive)
admin.site.register(earphones)
admin.site.register(bt_speaker)
admin.site.register(smartphone)
admin.site.register(offer)
admin.site.register(bestseller)

