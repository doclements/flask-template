
from views.main import main,   index
from views.service import service, services, add_service, edit_service, delete_service
from views.admin import admin, ad_index

routes = [
    ((main, ''),
        ('/', index)
    ),
    ((service, '/services'),
        ('/', services),
        ('/add/', add_service),
        ('/add/<service_id>', add_service),
        ('/edit/<service_id>',edit_service),
        ('/delete/<service_id>', delete_service)
    ),
    ((admin, '/admin'),
        ('/', ad_index)
    )
]


##maybe try overloading add such that without id it uses the get and with it uses the post??