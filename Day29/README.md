This is Day 29 of learning Python

Topic: Customizing Attribute Access
Summary: The\_\_\getattr\_\_() is executed when an attempt to reference any attribute outside of an object's namespace\*\* is made. It takes a name parameter and implements custom functionality, rather than raising an AttributeError.

Summary: The \_\_\setattr\_\_() is a magic method that is executed when a (new or existing) attribute is set or updated. It includes attributes set using \_\_\init\_\_() and takes name of attribute and value.

Topic: Custom Iterators
Summary: Iterators are classes that allow for a collection of objects or data stream to be traversed, and return one item at a time.
Additional Info: Iterator protocol. For a class to be considered as iterator, it must defined both \_\_\iter\_\_() and \_\_\next\_\_().
The \_\_\iter\_\_() method returns an iterator - a reference to itself (self).
The \_\_\next\_\_() returns value in the collection or data stream. This is where iteration, transformation, and generation takes place.
