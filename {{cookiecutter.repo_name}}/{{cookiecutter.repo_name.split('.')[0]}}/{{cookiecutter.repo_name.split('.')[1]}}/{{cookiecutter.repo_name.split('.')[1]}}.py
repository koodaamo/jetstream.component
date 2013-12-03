"""
Implement a Jetstream {{component_type}}Component
"""


from jetstream.base import {{component_type}}Component

# Here's the component boilerplate. It inherits from a Jetstream
# base {{component_type}} component, so is already runnable:
# Your can add it to your Jetstream configuration and try it out!

class {{component_name}}{{component_type}}Component({{component_type}}Component):
   "a {{component_type}}Component class"


# Here's a simple example of a dummy Input component that can also
# act as a pass-through component if it's given a stream

fro jetstream.base import InputComponent

class InputComponent(InputComponent):
   "an example Input component"

   # If the component does not need to be configured,
   # __init__ can be removed since the base class
   # sets _stream and _config

   def __init__(self, stream, config):
      "configure the component"
      # use a static dummy data source
      self._stream = stream or ({"key1":"value1"}, {"key2":"value"})
      self._config = config

   # Implementing __iter__ is almost always necessary

   def __iter__(self):
      "produce the result"

      # this is where the component produces data records, or inspects or modifies
      # them, or writes them out, depending on the component type

      # this is an Input component so we produce data (dicts)
      for record in self._stream:
         result = record
         yield result
