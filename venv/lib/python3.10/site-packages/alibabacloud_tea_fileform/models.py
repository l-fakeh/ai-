from Tea.model import TeaModel


class FileField(TeaModel):
    def __init__(self, filename=None, content_type=None, content=None):
        self.filename = filename
        self.content_type = content_type
        self.content = content

    def validate(self):
        self.validate_required(self.filename, 'filename')
        self.validate_required(self.content_type, 'content_type')
        self.validate_required(self.content, 'content')

    def to_map(self):
        result = {}
        result['filename'] = self.filename
        result['contentType'] = self.content_type
        result['content'] = self.content
        return result

    def from_map(self, map={}):
        self.filename = map.get('filename')
        self.content_type = map.get('contentType')
        self.content = map.get('content')
        return self
