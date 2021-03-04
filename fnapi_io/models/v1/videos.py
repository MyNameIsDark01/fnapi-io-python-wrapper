class VideosV1:
    def __init__(self, data):
        self.type: str = data.get('type')
        self.url: str = data.get('url')
