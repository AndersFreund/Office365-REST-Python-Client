from office365.directory.directory_object import DirectoryObject
from office365.onedrive.drive import Drive
from office365.outlookservices.contact_collection import ContactCollection
from office365.outlookservices.event_collection import EventCollection
from office365.outlookservices.message_collection import MessageCollection
from office365.runtime.client_query import ClientQuery
from office365.runtime.resource_path_entity import ResourcePathEntity
from office365.runtime.utilities.http_method import HttpMethod


class User(DirectoryObject):
    """A user in the system."""

    @property
    def drive(self):
        """Retrieve the properties and relationships of a Drive resource."""
        if self.is_property_available('drive'):
            return self.properties['drive']
        else:
            return Drive(self.context, ResourcePathEntity(self.context, self.resource_path, "drive"))

    @property
    def contacts(self):
        """Get a contact collection from the default Contacts folder of the signed-in user (.../me/contacts),
        or from the specified contact folder."""
        if self.is_property_available('contacts'):
            return self.properties['contacts']
        else:
            return ContactCollection(self.context, ResourcePathEntity(self, self._resource_path, "contacts"))

    @property
    def events(self):
        """Get an event collection or an event."""
        if self.is_property_available('events'):
            return self.properties['events']
        else:
            return EventCollection(self.context, ResourcePathEntity(self, self._resource_path, "events"))

    @property
    def messages(self):
        """Get an event collection or an event."""
        if self.is_property_available('messages'):
            return self.properties['messages']
        else:
            return MessageCollection(self.context, ResourcePathEntity(self, self._resource_path, "messages"))

    def send_mail(self, message):
        """Send a new message on the fly"""
        url = self.resource_url + "/sendmail"
        qry = ClientQuery(url, HttpMethod.Post, message)
        self.context.add_query(qry)
