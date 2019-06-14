from datetime import datetime


class Post(object):
    def __init__(self, text, timestamp=datetime.now()):
        self.text = text
        self.timestamp = timestamp
        self.user = None

    def set_user(self, user):
        self.user = user

    def __lt__(self, other):
        return self.timestamp < other.timestamp


class TextPost(Post):
    def __init__(self, text, timestamp=datetime.now()):
        try:
            super().__init__(text, timestamp)
        except:
            super(TextPost, self).__init__(text, timestamp)

    def __str__(self):
        return '@{} {}: "{}"\n\t{}'.format(
            self.user.first_name,
            self.user.last_name,
            self.text,
            datetime.strftime(self.timestamp, "%A, %b %d, %Y")
        )


class PicturePost(Post):
    def __init__(self, text, image_url, timestamp=datetime.now()):
        try:
            super().__init__(text, timestamp)
        except:
            super(PicturePost, self).__init__(text, timestamp)
        self.image_url = image_url

    def __str__(self):
        return '@{} {}: "{}"\n\t{}\n\t{}'.format(
            self.user.first_name,
            self.user.last_name,
            self.text,
            self.image_url,
            datetime.strftime(self.timestamp, "%A, %b %d, %Y")
        )


class CheckInPost(Post):
    def __init__(self, text, latitude, longitude, timestamp=datetime.now()):
        try:
            super().__init__(text, timestamp)
        except:
            super(CheckInPost, self).__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return '@{} Checked In: "{}"\n\t{}, {}\n\t{}'.format(
            self.user.first_name,
            self.text,
            self.latitude,
            self.longitude,
            datetime.strftime(self.timestamp, "%A, %b %d, %Y")
        )
