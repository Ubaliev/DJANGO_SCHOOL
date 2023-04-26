from rest_framework.routers import DefaultRouter as DR

from mainapp.views import (
    SchoolView,
)
router = DR()

from mainapp.views import (
    ClasView,
)
router = DR()

from mainapp.views import (
    StudentView,
)
router = DR()

router.register('school', SchoolView)


router.register('Clas', ClasView)


router.register('Student', StudentView)

urlpatterns = []

urlpatterns += router.urls

