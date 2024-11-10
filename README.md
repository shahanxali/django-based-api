# Django Based Api, Basic

## When you run this Django project locally, the following will occur:

  API Endpoints:
      List/Create: GET /api/ and POST /api/ to retrieve a list of apimodel instances or create a new one.
      Retrieve/Update/Delete: GET /api/{id}/, PUT /api/{id}/, PATCH /api/{id}/, and DELETE /api/{id}/ for operations on a specific instance identified by {id}.

  Browsable API:
      Navigating to /api/ in your browser will display a browsable interface provided by DRF, allowing you to interact with the API endpoints directly.

  Authentication:
      Accessing /api-auth/ will provide login and logout interfaces if authentication is enabled, facilitating secure access to the API.
