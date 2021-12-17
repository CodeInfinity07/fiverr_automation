from plyer.utils import platform
from plyer import notification

notification.notify(
    title='Here is the title',
    message='Here is the message',
    app_name='Here is the application name',
    app_icon='path/to/the/icon.' + ('ico' if platform == 'win' else 'png')
)
