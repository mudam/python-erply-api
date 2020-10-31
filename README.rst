Erply InventoryAPI Python library
=================================

Please note this is API is currently work in progress and might change in future.

Build Status
============
.. image:: https://travis-ci.org/plaes/python-erply-api.svg?branch=master
    :target: https://travis-ci.org/plaes/python-erply-api

Usage
=====
.. code:: python

    from erply_api import Erply, ErplyAuth

    ERPLY_CUSTOMER_CODE = "eng"
    ERPLY_USERNAME = "demo"
    ERPLY_PASSWORD = "demouser"

    auth = ErplyAuth(ERPLY_CUSTOMER_CODE, ERPLY_USERNAME, ERPLY_PASSWORD)
    erply = Erply(auth)
    """ Some results such as sales reports can return different results
    depending on Erply account settings.
    You should fetch configuration data before trying to read the returned data.

    All parameters listed `https://learn-api.erply.com/requests/getconfparameters`
    are stored in 'erply.conf' dictionary throughout the object's lifecycle.
    Use `erply.fetch_config()` to initialize them.

    Note that Erply API uses configured CSV separator inconsistently. Apparently
    the only place it has effect is getSalesReport.

    Best solution it to handle CSV parsing yourself with appropriate delimiter, 
    and not to rely on the inbuilt `records` property.
    """
    erply.fetch_config()
    response = erply.getProducts()
    print (response.total)
    # Iterate over automatically paginated results
    for page in response:
        for product in page:
            print (product)

    # Example of reading sales reports (assuming `fetch_config()` has been called)

    response = erply.getSalesReport(**arguments)
    output = csv.reader(open(response.url,"rb"), delimiter=erply.conf['csv_field_separator'])