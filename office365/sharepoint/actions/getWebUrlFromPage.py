from office365.runtime.client_result import ClientResult
from office365.runtime.queries.service_operation_query import ServiceOperationQuery


class GetWebUrlFromPageUrlQuery(ServiceOperationQuery):

    def __init__(self, context, page_full_url):
        result = ClientResult(context)
        payload = {
            "pageFullUrl": page_full_url
        }
        super(GetWebUrlFromPageUrlQuery, self).__init__(context.web, "GetWebUrlFromPageUrl", None, payload, None, result)
        self.static = True
