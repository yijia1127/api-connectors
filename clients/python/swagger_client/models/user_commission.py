# coding: utf-8

"""
Copyright 2015 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class UserCommission(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        UserCommission - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'maker_fee': 'str',
            'taker_fee': 'str',
            'insurance_fee': 'str'
        }

        self.attribute_map = {
            'maker_fee': 'makerFee',
            'taker_fee': 'takerFee',
            'insurance_fee': 'insuranceFee'
        }

        self._maker_fee = None
        self._taker_fee = None
        self._insurance_fee = None

    @property
    def maker_fee(self):
        """
        Gets the maker_fee of this UserCommission.


        :return: The maker_fee of this UserCommission.
        :rtype: str
        """
        return self._maker_fee

    @maker_fee.setter
    def maker_fee(self, maker_fee):
        """
        Sets the maker_fee of this UserCommission.


        :param maker_fee: The maker_fee of this UserCommission.
        :type: str
        """
        self._maker_fee = maker_fee

    @property
    def taker_fee(self):
        """
        Gets the taker_fee of this UserCommission.


        :return: The taker_fee of this UserCommission.
        :rtype: str
        """
        return self._taker_fee

    @taker_fee.setter
    def taker_fee(self, taker_fee):
        """
        Sets the taker_fee of this UserCommission.


        :param taker_fee: The taker_fee of this UserCommission.
        :type: str
        """
        self._taker_fee = taker_fee

    @property
    def insurance_fee(self):
        """
        Gets the insurance_fee of this UserCommission.


        :return: The insurance_fee of this UserCommission.
        :rtype: str
        """
        return self._insurance_fee

    @insurance_fee.setter
    def insurance_fee(self, insurance_fee):
        """
        Sets the insurance_fee of this UserCommission.


        :param insurance_fee: The insurance_fee of this UserCommission.
        :type: str
        """
        self._insurance_fee = insurance_fee

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other): 
        """
        Returns true if both objects are equal
        """
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """ 
        Returns true if both objects are not equal
        """
        return not self == other
