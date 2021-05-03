from office365.runtime.client_value import ClientValue


class ResourcePath(ClientValue):

    def __init__(self, decoded_url):
        super(ResourcePath, self).__init__()
        self.DecodedUrl = decoded_url
