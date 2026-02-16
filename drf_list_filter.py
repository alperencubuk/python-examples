from rest_framework.filters import BaseFilterBackend


class ListFilterBackend(BaseFilterBackend):
    """
    DRF-compatible filter backend for Python lists.

    Supported lookups:
        field=value
        field__contains=value
        field__icontains=value
        field__in=1,2,3

    Ordering:
        ?ordering=field
        ?ordering=-field
    """

    RESERVED_PARAMS = {"page", "page_size", "ordering"}

    def filter_queryset(self, request, queryset, view):
        if not isinstance(queryset, list):
            return queryset

        params = request.query_params
        data = queryset

        for raw_key, value in params.items():
            if raw_key in self.RESERVED_PARAMS:
                continue

            if "__" in raw_key:
                field, lookup = raw_key.split("__", 1)
            else:
                field, lookup = raw_key, "exact"

            data = self.apply_filter(data, field, lookup, value)

        ordering = params.get("ordering")
        if ordering:
            reverse = ordering.startswith("-")
            field = ordering.lstrip("-")
            data = sorted(
                data,
                key=lambda x: x.get(field),
                reverse=reverse,
            )

        return data

    @staticmethod
    def apply_filter(data, field, lookup, value):
        if lookup == "exact":
            return [item for item in data if str(item.get(field)) == value]

        if lookup == "contains":
            return [item for item in data if value in str(item.get(field, ""))]

        if lookup == "icontains":
            value_lower = value.lower()
            return [item for item in data if value_lower in str(item.get(field, "")).lower()]

        if lookup == "in":
            values = value.split(",")
            return [item for item in data if str(item.get(field)) in values]

        return data
