from rest_framework import status
from rest_framework.response import Response
from rest_framework_mongoengine import viewsets


class BaseViewset(viewsets.ModelViewSet):
    def destroy(self, _, *args, **kwargs):
        _, _ = args, kwargs  # ruff :variables no utilizadas
        model = self.get_object()
        model.is_active = False
        model.save()

        model_name = model._cls
        return Response(
            {"detail": f"{model_name} deleted."}, status=status.HTTP_204_NO_CONTENT
        )
