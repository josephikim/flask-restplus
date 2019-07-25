from flask_restplus import Api
from .ns_cats import api as cats
# from .namespace2 import api as ns2
# # ...
# from .namespaceX import api as nsX

api = Api(
    title='My Title',
    version='1.0',
    description='A description',
    # All API metadatas
)

api.add_namespace(cats, path='/cats')
# api.add_namespace(ns2, path='/prefix/of/ns2')
# # ...
# api.add_namespace(nsX, path='/prefix/of/nsX')