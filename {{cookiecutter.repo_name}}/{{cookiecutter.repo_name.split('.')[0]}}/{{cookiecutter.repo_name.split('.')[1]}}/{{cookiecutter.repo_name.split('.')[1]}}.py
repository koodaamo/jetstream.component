"""
Implement a Jetstream {{cookiecutter.component_type}} component
"""

from jetstream.base import {{cookiecutter.component_type}}Component

# Here's your component boilerplate. It inherits from a Jetstream
# base {{cookiecutter.component_type}} component, so is already runnable:
# Your can add it to your Jetstream configuration and try it out!

class {{cookiecutter.component_klass}}({{cookiecutter.component_type}}Component):
   "a {{cookiecutter.component_type}}Component class"


# Here's a simple example of a dummy Input component

from jetstream.base import InputComponent

class InputComponent(InputComponent):
   "an example Input component"

   # If the component does not need to be configured,
   # __init__ can be removed since the base class
   # sets _stream and _config

   def __init__(self, stream, config):
      "configure the component"
      # use a static dummy data source
      self._stream = ({"key1":"value1"}, {"key2":"value"})
      self._config = config

   def __iter__(self):
      "produce the result"

      # this is where the component produces data records, or inspects or modifies
      # them, or writes them out, depending on the component type

      # this is an Input component so we produce data (dicts)
      for record in self._stream:
         result = record
         yield result
