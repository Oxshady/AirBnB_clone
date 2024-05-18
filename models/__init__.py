"""This code snippet is importing the `FileStorage`
class from the `file_storage` module within the
 `engine` package. It then creates an instance
 of the `FileStorage` class and calls its `reload()`
 method. This code is likely used to initialize and
 reload a file storage system for data storage and
 retrieval."""

from .engine import file_storage

storage = file_storage.FileStorage()
storage.reload()
