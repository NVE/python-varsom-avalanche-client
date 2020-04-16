# coding: utf-8

"""
    Snøskredvarsel API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v5.0.1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six


class MeasurementSubType(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'id': 'int',
        'name': 'str',
        'sort_order': 'int',
        'value': 'str'
    }

    attribute_map = {
        'id': 'Id',
        'name': 'Name',
        'sort_order': 'SortOrder',
        'value': 'Value'
    }

    def __init__(self, id=None, name=None, sort_order=None, value=None):  # noqa: E501
        """MeasurementSubType - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._name = None
        self._sort_order = None
        self._value = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if sort_order is not None:
            self.sort_order = sort_order
        if value is not None:
            self.value = value

    @property
    def id(self):
        """Gets the id of this MeasurementSubType.  # noqa: E501


        :return: The id of this MeasurementSubType.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this MeasurementSubType.


        :param id: The id of this MeasurementSubType.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def name(self):
        """Gets the name of this MeasurementSubType.  # noqa: E501


        :return: The name of this MeasurementSubType.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this MeasurementSubType.


        :param name: The name of this MeasurementSubType.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sort_order(self):
        """Gets the sort_order of this MeasurementSubType.  # noqa: E501


        :return: The sort_order of this MeasurementSubType.  # noqa: E501
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this MeasurementSubType.


        :param sort_order: The sort_order of this MeasurementSubType.  # noqa: E501
        :type: int
        """

        self._sort_order = sort_order

    @property
    def value(self):
        """Gets the value of this MeasurementSubType.  # noqa: E501


        :return: The value of this MeasurementSubType.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this MeasurementSubType.


        :param value: The value of this MeasurementSubType.  # noqa: E501
        :type: str
        """

        self._value = value

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(MeasurementSubType, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, MeasurementSubType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
