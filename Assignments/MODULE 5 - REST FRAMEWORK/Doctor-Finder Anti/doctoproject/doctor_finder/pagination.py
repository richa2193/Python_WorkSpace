from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class DoctorPagination(PageNumberPagination):
    """Custom pagination for the Doctor API.

    - Uses a default page size of **5** records.
    - Allows the client to request a different page size via the
      ``page_size`` query parameter (capped at ``max_page_size``).
    - Returns a JSON response containing the required keys:
        ``count``, ``next``, ``previous`` and ``results``.
    """

    page_size = 5
    page_size_query_param = "page_size"
    max_page_size = 100

    def get_paginated_response(self, data):
        return Response({
            "count": self.page.paginator.count,
            "next": self.get_next_link(),
            "previous": self.get_previous_link(),
            "results": data,
        })
