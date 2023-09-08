# coding: utf-8

"""
    flyteidl/service/admin.proto

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: version not set
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from flyteadmin.models.protobuf_list_value import ProtobufListValue  # noqa: F401,E501
from flyteadmin.models.protobuf_null_value import ProtobufNullValue  # noqa: F401,E501
from flyteadmin.models.protobuf_struct import ProtobufStruct  # noqa: F401,E501


class ProtobufValue(object):
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
        'null_value': 'ProtobufNullValue',
        'number_value': 'float',
        'string_value': 'str',
        'bool_value': 'bool',
        'struct_value': 'ProtobufStruct',
        'list_value': 'ProtobufListValue'
    }

    attribute_map = {
        'null_value': 'null_value',
        'number_value': 'number_value',
        'string_value': 'string_value',
        'bool_value': 'bool_value',
        'struct_value': 'struct_value',
        'list_value': 'list_value'
    }

    def __init__(self, null_value=None, number_value=None, string_value=None, bool_value=None, struct_value=None, list_value=None):  # noqa: E501
        """ProtobufValue - a model defined in Swagger"""  # noqa: E501

        self._null_value = None
        self._number_value = None
        self._string_value = None
        self._bool_value = None
        self._struct_value = None
        self._list_value = None
        self.discriminator = None

        if null_value is not None:
            self.null_value = null_value
        if number_value is not None:
            self.number_value = number_value
        if string_value is not None:
            self.string_value = string_value
        if bool_value is not None:
            self.bool_value = bool_value
        if struct_value is not None:
            self.struct_value = struct_value
        if list_value is not None:
            self.list_value = list_value

    @property
    def null_value(self):
        """Gets the null_value of this ProtobufValue.  # noqa: E501

        Represents a null value.  # noqa: E501

        :return: The null_value of this ProtobufValue.  # noqa: E501
        :rtype: ProtobufNullValue
        """
        return self._null_value

    @null_value.setter
    def null_value(self, null_value):
        """Sets the null_value of this ProtobufValue.

        Represents a null value.  # noqa: E501

        :param null_value: The null_value of this ProtobufValue.  # noqa: E501
        :type: ProtobufNullValue
        """

        self._null_value = null_value

    @property
    def number_value(self):
        """Gets the number_value of this ProtobufValue.  # noqa: E501

        Represents a double value.  # noqa: E501

        :return: The number_value of this ProtobufValue.  # noqa: E501
        :rtype: float
        """
        return self._number_value

    @number_value.setter
    def number_value(self, number_value):
        """Sets the number_value of this ProtobufValue.

        Represents a double value.  # noqa: E501

        :param number_value: The number_value of this ProtobufValue.  # noqa: E501
        :type: float
        """

        self._number_value = number_value

    @property
    def string_value(self):
        """Gets the string_value of this ProtobufValue.  # noqa: E501

        Represents a string value.  # noqa: E501

        :return: The string_value of this ProtobufValue.  # noqa: E501
        :rtype: str
        """
        return self._string_value

    @string_value.setter
    def string_value(self, string_value):
        """Sets the string_value of this ProtobufValue.

        Represents a string value.  # noqa: E501

        :param string_value: The string_value of this ProtobufValue.  # noqa: E501
        :type: str
        """

        self._string_value = string_value

    @property
    def bool_value(self):
        """Gets the bool_value of this ProtobufValue.  # noqa: E501

        Represents a boolean value.  # noqa: E501

        :return: The bool_value of this ProtobufValue.  # noqa: E501
        :rtype: bool
        """
        return self._bool_value

    @bool_value.setter
    def bool_value(self, bool_value):
        """Sets the bool_value of this ProtobufValue.

        Represents a boolean value.  # noqa: E501

        :param bool_value: The bool_value of this ProtobufValue.  # noqa: E501
        :type: bool
        """

        self._bool_value = bool_value

    @property
    def struct_value(self):
        """Gets the struct_value of this ProtobufValue.  # noqa: E501

        Represents a structured value.  # noqa: E501

        :return: The struct_value of this ProtobufValue.  # noqa: E501
        :rtype: ProtobufStruct
        """
        return self._struct_value

    @struct_value.setter
    def struct_value(self, struct_value):
        """Sets the struct_value of this ProtobufValue.

        Represents a structured value.  # noqa: E501

        :param struct_value: The struct_value of this ProtobufValue.  # noqa: E501
        :type: ProtobufStruct
        """

        self._struct_value = struct_value

    @property
    def list_value(self):
        """Gets the list_value of this ProtobufValue.  # noqa: E501

        Represents a repeated `Value`.  # noqa: E501

        :return: The list_value of this ProtobufValue.  # noqa: E501
        :rtype: ProtobufListValue
        """
        return self._list_value

    @list_value.setter
    def list_value(self, list_value):
        """Sets the list_value of this ProtobufValue.

        Represents a repeated `Value`.  # noqa: E501

        :param list_value: The list_value of this ProtobufValue.  # noqa: E501
        :type: ProtobufListValue
        """

        self._list_value = list_value

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
        if issubclass(ProtobufValue, dict):
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
        if not isinstance(other, ProtobufValue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other