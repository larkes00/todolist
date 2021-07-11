from todolist.models import List


class DataMixin:
    def get_user_context(self, **kwargs):
        context = kwargs
        context["lists"] = List.objects.filter(owner=kwargs["user"])
        return context
