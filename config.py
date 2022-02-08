# Qtile Config File
# http://www.qtile.org/

# Antonio Sarosi
# https://youtube.com/c/antoniosarosi
# https://github.com/antoniosarosi/dotfiles


from libqtile import hook

from settings.keys import mod, keys
from settings.groups import groups
from settings.layouts import layouts, floating_layout
from settings.widgets import widget_defaults, extension_defaults
from settings.screens import screens
from settings.mouse import mouse
from settings.path import qtile_path
from peewee import *

from os import path
import subprocess

DATABASE = '/home/lescobarvx/.config/qtile/infodevices.db'
database = SqliteDatabase(DATABASE)


class BaseModel(Model):
    class Meta:
        database = database


class Devices(BaseModel):
    name = CharField()
    macaddress = CharField(unique=True)


class InfoDevices(BaseModel):
    device_id = ForeignKeyField(Devices, backref='infodevice_id')
    join_date = DateTimeField()


def create_tables():
    with database:
        database.create_tables([Devices, InfoDevices])


@hook.subscribe.startup_once
def autostart():
    subprocess.call([path.join(qtile_path, 'autostart.sh')])

@hook.subscribe.startup
def autostart_ever():
    create_tables()

main = None
dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = False
# cursor_warp = True
auto_fullscreen = True
focus_on_window_activation = 'urgent'
# wmname = 'LG3D'
