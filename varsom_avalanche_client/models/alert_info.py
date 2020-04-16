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


class AlertInfo(object):
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
        'language_field': 'int',
        'category_field': 'list[int]',
        'event_field': 'int',
        'response_type_field': 'list[int]',
        'urgency_field': 'int',
        'severity_field': 'int',
        'certainty_field': 'int',
        'event_code_field': 'list[AlertInfoEventCode]',
        'effective_field': 'datetime',
        'effective_field_specified': 'bool',
        'onset_field': 'datetime',
        'onset_field_specified': 'bool',
        'expires_field': 'datetime',
        'sender_name_field': 'int',
        'headline_field': 'str',
        'description_field': 'str',
        'instruction_field': 'str',
        'web_field': 'str',
        'contact_field': 'str',
        'parameter_field': 'list[AlertInfoParameter]',
        'resource_field': 'list[AlertInfoResource]',
        'area_field': 'list[AlertInfoArea]'
    }

    attribute_map = {
        'language_field': 'languageField',
        'category_field': 'categoryField',
        'event_field': 'eventField',
        'response_type_field': 'responseTypeField',
        'urgency_field': 'urgencyField',
        'severity_field': 'severityField',
        'certainty_field': 'certaintyField',
        'event_code_field': 'eventCodeField',
        'effective_field': 'effectiveField',
        'effective_field_specified': 'effectiveFieldSpecified',
        'onset_field': 'onsetField',
        'onset_field_specified': 'onsetFieldSpecified',
        'expires_field': 'expiresField',
        'sender_name_field': 'senderNameField',
        'headline_field': 'headlineField',
        'description_field': 'descriptionField',
        'instruction_field': 'instructionField',
        'web_field': 'webField',
        'contact_field': 'contactField',
        'parameter_field': 'parameterField',
        'resource_field': 'resourceField',
        'area_field': 'areaField'
    }

    def __init__(self, language_field=None, category_field=None, event_field=None, response_type_field=None, urgency_field=None, severity_field=None, certainty_field=None, event_code_field=None, effective_field=None, effective_field_specified=None, onset_field=None, onset_field_specified=None, expires_field=None, sender_name_field=None, headline_field=None, description_field=None, instruction_field=None, web_field=None, contact_field=None, parameter_field=None, resource_field=None, area_field=None):  # noqa: E501
        """AlertInfo - a model defined in Swagger"""  # noqa: E501
        self._language_field = None
        self._category_field = None
        self._event_field = None
        self._response_type_field = None
        self._urgency_field = None
        self._severity_field = None
        self._certainty_field = None
        self._event_code_field = None
        self._effective_field = None
        self._effective_field_specified = None
        self._onset_field = None
        self._onset_field_specified = None
        self._expires_field = None
        self._sender_name_field = None
        self._headline_field = None
        self._description_field = None
        self._instruction_field = None
        self._web_field = None
        self._contact_field = None
        self._parameter_field = None
        self._resource_field = None
        self._area_field = None
        self.discriminator = None
        if language_field is not None:
            self.language_field = language_field
        if category_field is not None:
            self.category_field = category_field
        if event_field is not None:
            self.event_field = event_field
        if response_type_field is not None:
            self.response_type_field = response_type_field
        if urgency_field is not None:
            self.urgency_field = urgency_field
        if severity_field is not None:
            self.severity_field = severity_field
        if certainty_field is not None:
            self.certainty_field = certainty_field
        if event_code_field is not None:
            self.event_code_field = event_code_field
        if effective_field is not None:
            self.effective_field = effective_field
        if effective_field_specified is not None:
            self.effective_field_specified = effective_field_specified
        if onset_field is not None:
            self.onset_field = onset_field
        if onset_field_specified is not None:
            self.onset_field_specified = onset_field_specified
        if expires_field is not None:
            self.expires_field = expires_field
        if sender_name_field is not None:
            self.sender_name_field = sender_name_field
        if headline_field is not None:
            self.headline_field = headline_field
        if description_field is not None:
            self.description_field = description_field
        if instruction_field is not None:
            self.instruction_field = instruction_field
        if web_field is not None:
            self.web_field = web_field
        if contact_field is not None:
            self.contact_field = contact_field
        if parameter_field is not None:
            self.parameter_field = parameter_field
        if resource_field is not None:
            self.resource_field = resource_field
        if area_field is not None:
            self.area_field = area_field

    @property
    def language_field(self):
        """Gets the language_field of this AlertInfo.  # noqa: E501


        :return: The language_field of this AlertInfo.  # noqa: E501
        :rtype: int
        """
        return self._language_field

    @language_field.setter
    def language_field(self, language_field):
        """Sets the language_field of this AlertInfo.


        :param language_field: The language_field of this AlertInfo.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1]  # noqa: E501
        if language_field not in allowed_values:
            raise ValueError(
                "Invalid value for `language_field` ({0}), must be one of {1}"  # noqa: E501
                .format(language_field, allowed_values)
            )

        self._language_field = language_field

    @property
    def category_field(self):
        """Gets the category_field of this AlertInfo.  # noqa: E501


        :return: The category_field of this AlertInfo.  # noqa: E501
        :rtype: list[int]
        """
        return self._category_field

    @category_field.setter
    def category_field(self, category_field):
        """Sets the category_field of this AlertInfo.


        :param category_field: The category_field of this AlertInfo.  # noqa: E501
        :type: list[int]
        """
        allowed_values = [0, 1]  # noqa: E501
        if not set(category_field).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `category_field` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(category_field) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._category_field = category_field

    @property
    def event_field(self):
        """Gets the event_field of this AlertInfo.  # noqa: E501


        :return: The event_field of this AlertInfo.  # noqa: E501
        :rtype: int
        """
        return self._event_field

    @event_field.setter
    def event_field(self, event_field):
        """Sets the event_field of this AlertInfo.


        :param event_field: The event_field of this AlertInfo.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35]  # noqa: E501
        if event_field not in allowed_values:
            raise ValueError(
                "Invalid value for `event_field` ({0}), must be one of {1}"  # noqa: E501
                .format(event_field, allowed_values)
            )

        self._event_field = event_field

    @property
    def response_type_field(self):
        """Gets the response_type_field of this AlertInfo.  # noqa: E501


        :return: The response_type_field of this AlertInfo.  # noqa: E501
        :rtype: list[int]
        """
        return self._response_type_field

    @response_type_field.setter
    def response_type_field(self, response_type_field):
        """Sets the response_type_field of this AlertInfo.


        :param response_type_field: The response_type_field of this AlertInfo.  # noqa: E501
        :type: list[int]
        """
        allowed_values = [0, 1, 2, 3, 4, 5, 6, 7, 8]  # noqa: E501
        if not set(response_type_field).issubset(set(allowed_values)):
            raise ValueError(
                "Invalid values for `response_type_field` [{0}], must be a subset of [{1}]"  # noqa: E501
                .format(", ".join(map(str, set(response_type_field) - set(allowed_values))),  # noqa: E501
                        ", ".join(map(str, allowed_values)))
            )

        self._response_type_field = response_type_field

    @property
    def urgency_field(self):
        """Gets the urgency_field of this AlertInfo.  # noqa: E501


        :return: The urgency_field of this AlertInfo.  # noqa: E501
        :rtype: int
        """
        return self._urgency_field

    @urgency_field.setter
    def urgency_field(self, urgency_field):
        """Sets the urgency_field of this AlertInfo.


        :param urgency_field: The urgency_field of this AlertInfo.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4]  # noqa: E501
        if urgency_field not in allowed_values:
            raise ValueError(
                "Invalid value for `urgency_field` ({0}), must be one of {1}"  # noqa: E501
                .format(urgency_field, allowed_values)
            )

        self._urgency_field = urgency_field

    @property
    def severity_field(self):
        """Gets the severity_field of this AlertInfo.  # noqa: E501


        :return: The severity_field of this AlertInfo.  # noqa: E501
        :rtype: int
        """
        return self._severity_field

    @severity_field.setter
    def severity_field(self, severity_field):
        """Sets the severity_field of this AlertInfo.


        :param severity_field: The severity_field of this AlertInfo.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4]  # noqa: E501
        if severity_field not in allowed_values:
            raise ValueError(
                "Invalid value for `severity_field` ({0}), must be one of {1}"  # noqa: E501
                .format(severity_field, allowed_values)
            )

        self._severity_field = severity_field

    @property
    def certainty_field(self):
        """Gets the certainty_field of this AlertInfo.  # noqa: E501


        :return: The certainty_field of this AlertInfo.  # noqa: E501
        :rtype: int
        """
        return self._certainty_field

    @certainty_field.setter
    def certainty_field(self, certainty_field):
        """Sets the certainty_field of this AlertInfo.


        :param certainty_field: The certainty_field of this AlertInfo.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4]  # noqa: E501
        if certainty_field not in allowed_values:
            raise ValueError(
                "Invalid value for `certainty_field` ({0}), must be one of {1}"  # noqa: E501
                .format(certainty_field, allowed_values)
            )

        self._certainty_field = certainty_field

    @property
    def event_code_field(self):
        """Gets the event_code_field of this AlertInfo.  # noqa: E501


        :return: The event_code_field of this AlertInfo.  # noqa: E501
        :rtype: list[AlertInfoEventCode]
        """
        return self._event_code_field

    @event_code_field.setter
    def event_code_field(self, event_code_field):
        """Sets the event_code_field of this AlertInfo.


        :param event_code_field: The event_code_field of this AlertInfo.  # noqa: E501
        :type: list[AlertInfoEventCode]
        """

        self._event_code_field = event_code_field

    @property
    def effective_field(self):
        """Gets the effective_field of this AlertInfo.  # noqa: E501


        :return: The effective_field of this AlertInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._effective_field

    @effective_field.setter
    def effective_field(self, effective_field):
        """Sets the effective_field of this AlertInfo.


        :param effective_field: The effective_field of this AlertInfo.  # noqa: E501
        :type: datetime
        """

        self._effective_field = effective_field

    @property
    def effective_field_specified(self):
        """Gets the effective_field_specified of this AlertInfo.  # noqa: E501


        :return: The effective_field_specified of this AlertInfo.  # noqa: E501
        :rtype: bool
        """
        return self._effective_field_specified

    @effective_field_specified.setter
    def effective_field_specified(self, effective_field_specified):
        """Sets the effective_field_specified of this AlertInfo.


        :param effective_field_specified: The effective_field_specified of this AlertInfo.  # noqa: E501
        :type: bool
        """

        self._effective_field_specified = effective_field_specified

    @property
    def onset_field(self):
        """Gets the onset_field of this AlertInfo.  # noqa: E501


        :return: The onset_field of this AlertInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._onset_field

    @onset_field.setter
    def onset_field(self, onset_field):
        """Sets the onset_field of this AlertInfo.


        :param onset_field: The onset_field of this AlertInfo.  # noqa: E501
        :type: datetime
        """

        self._onset_field = onset_field

    @property
    def onset_field_specified(self):
        """Gets the onset_field_specified of this AlertInfo.  # noqa: E501


        :return: The onset_field_specified of this AlertInfo.  # noqa: E501
        :rtype: bool
        """
        return self._onset_field_specified

    @onset_field_specified.setter
    def onset_field_specified(self, onset_field_specified):
        """Sets the onset_field_specified of this AlertInfo.


        :param onset_field_specified: The onset_field_specified of this AlertInfo.  # noqa: E501
        :type: bool
        """

        self._onset_field_specified = onset_field_specified

    @property
    def expires_field(self):
        """Gets the expires_field of this AlertInfo.  # noqa: E501


        :return: The expires_field of this AlertInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._expires_field

    @expires_field.setter
    def expires_field(self, expires_field):
        """Sets the expires_field of this AlertInfo.


        :param expires_field: The expires_field of this AlertInfo.  # noqa: E501
        :type: datetime
        """

        self._expires_field = expires_field

    @property
    def sender_name_field(self):
        """Gets the sender_name_field of this AlertInfo.  # noqa: E501


        :return: The sender_name_field of this AlertInfo.  # noqa: E501
        :rtype: int
        """
        return self._sender_name_field

    @sender_name_field.setter
    def sender_name_field(self, sender_name_field):
        """Sets the sender_name_field of this AlertInfo.


        :param sender_name_field: The sender_name_field of this AlertInfo.  # noqa: E501
        :type: int
        """
        allowed_values = [0, 1, 2, 3, 4]  # noqa: E501
        if sender_name_field not in allowed_values:
            raise ValueError(
                "Invalid value for `sender_name_field` ({0}), must be one of {1}"  # noqa: E501
                .format(sender_name_field, allowed_values)
            )

        self._sender_name_field = sender_name_field

    @property
    def headline_field(self):
        """Gets the headline_field of this AlertInfo.  # noqa: E501


        :return: The headline_field of this AlertInfo.  # noqa: E501
        :rtype: str
        """
        return self._headline_field

    @headline_field.setter
    def headline_field(self, headline_field):
        """Sets the headline_field of this AlertInfo.


        :param headline_field: The headline_field of this AlertInfo.  # noqa: E501
        :type: str
        """

        self._headline_field = headline_field

    @property
    def description_field(self):
        """Gets the description_field of this AlertInfo.  # noqa: E501


        :return: The description_field of this AlertInfo.  # noqa: E501
        :rtype: str
        """
        return self._description_field

    @description_field.setter
    def description_field(self, description_field):
        """Sets the description_field of this AlertInfo.


        :param description_field: The description_field of this AlertInfo.  # noqa: E501
        :type: str
        """

        self._description_field = description_field

    @property
    def instruction_field(self):
        """Gets the instruction_field of this AlertInfo.  # noqa: E501


        :return: The instruction_field of this AlertInfo.  # noqa: E501
        :rtype: str
        """
        return self._instruction_field

    @instruction_field.setter
    def instruction_field(self, instruction_field):
        """Sets the instruction_field of this AlertInfo.


        :param instruction_field: The instruction_field of this AlertInfo.  # noqa: E501
        :type: str
        """

        self._instruction_field = instruction_field

    @property
    def web_field(self):
        """Gets the web_field of this AlertInfo.  # noqa: E501


        :return: The web_field of this AlertInfo.  # noqa: E501
        :rtype: str
        """
        return self._web_field

    @web_field.setter
    def web_field(self, web_field):
        """Sets the web_field of this AlertInfo.


        :param web_field: The web_field of this AlertInfo.  # noqa: E501
        :type: str
        """

        self._web_field = web_field

    @property
    def contact_field(self):
        """Gets the contact_field of this AlertInfo.  # noqa: E501


        :return: The contact_field of this AlertInfo.  # noqa: E501
        :rtype: str
        """
        return self._contact_field

    @contact_field.setter
    def contact_field(self, contact_field):
        """Sets the contact_field of this AlertInfo.


        :param contact_field: The contact_field of this AlertInfo.  # noqa: E501
        :type: str
        """

        self._contact_field = contact_field

    @property
    def parameter_field(self):
        """Gets the parameter_field of this AlertInfo.  # noqa: E501


        :return: The parameter_field of this AlertInfo.  # noqa: E501
        :rtype: list[AlertInfoParameter]
        """
        return self._parameter_field

    @parameter_field.setter
    def parameter_field(self, parameter_field):
        """Sets the parameter_field of this AlertInfo.


        :param parameter_field: The parameter_field of this AlertInfo.  # noqa: E501
        :type: list[AlertInfoParameter]
        """

        self._parameter_field = parameter_field

    @property
    def resource_field(self):
        """Gets the resource_field of this AlertInfo.  # noqa: E501


        :return: The resource_field of this AlertInfo.  # noqa: E501
        :rtype: list[AlertInfoResource]
        """
        return self._resource_field

    @resource_field.setter
    def resource_field(self, resource_field):
        """Sets the resource_field of this AlertInfo.


        :param resource_field: The resource_field of this AlertInfo.  # noqa: E501
        :type: list[AlertInfoResource]
        """

        self._resource_field = resource_field

    @property
    def area_field(self):
        """Gets the area_field of this AlertInfo.  # noqa: E501


        :return: The area_field of this AlertInfo.  # noqa: E501
        :rtype: list[AlertInfoArea]
        """
        return self._area_field

    @area_field.setter
    def area_field(self, area_field):
        """Sets the area_field of this AlertInfo.


        :param area_field: The area_field of this AlertInfo.  # noqa: E501
        :type: list[AlertInfoArea]
        """

        self._area_field = area_field

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
        if issubclass(AlertInfo, dict):
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
        if not isinstance(other, AlertInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
