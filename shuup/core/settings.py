# -*- coding: utf-8 -*-
# This file is part of Shuup.
#
# Copyright (c) 2012-2017, Shoop Commerce Ltd. All rights reserved.
#
# This source code is licensed under the OSL-3.0 license found in the
# LICENSE file in the root directory of this source tree.
from __future__ import unicode_literals

"""
Settings of Shuup Core.

See :ref:`apps-settings` (in :obj:`shuup.apps`) for general information
about the Shuup settings system.  Especially, when inventing settings of
your own, the :ref:`apps-naming-settings` section is an important read.
"""


#: The home currency for the Shuup installation. All monetary values
#: are implicitly in this currency unless somehow otherwise specified.
SHUUP_HOME_CURRENCY = "EUR"

#: The home country code (ISO 3166-1 alpha 2) for the Shuup installation.
#: Among other things, addresses that would be printed with this country
#: visible are printed with no country.
SHUUP_ADDRESS_HOME_COUNTRY = None

#: Whether or not anonymous orders (without a ``creator`` user)
#: are allowed.
SHUUP_ALLOW_ANONYMOUS_ORDERS = True

#: Which method is used to calculate order identifiers ("order numbers").
#: May be either the string "id", a callable or a spec string pointing
#: to a callable that must return a string given an ``order``.
SHUUP_ORDER_IDENTIFIER_METHOD = "id"

#: Which method is used by default to calculate order reference numbers.
#:
#: May be a spec string pointing to a callable that must return a string
#: given an Order, or one of the following built-in generators.
#:
#: ``unique``
#:    Unique reference number based on time and the order ID.
#:    The reference number has the Finnish bank reference check digit
#:    appended, making the reference number valid for Finnish bank transfers.
#: ``running``
#:    Ascending reference number. The length of the reference number will be
#:    ``SHUUP_REFERENCE_NUMBER_LENGTH`` + 1 (for the check digit described below).
#:    ``SHUUP_REFERENCE_NUMBER_PREFIX`` is prepended, if set.
#:    The reference number has the Finnish bank reference check digit
#:    appended, making the reference number valid for Finnish bank transfers.
#: ``shop_running``
#:    As ``running``, but with the shop ID prepended.
SHUUP_REFERENCE_NUMBER_METHOD = "unique"

#: The default length of reference numbers generated by certain reference number generators.
SHUUP_REFERENCE_NUMBER_LENGTH = 17

#: An arbitrary (numeric) default prefix for certain reference number generators.
SHUUP_REFERENCE_NUMBER_PREFIX = ""

#: The identifier of the pricing module to use for pricing products.
#:
#: Determines how product prices are calculated.  See
#: :obj:`shuup.core.pricing` for details.
SHUUP_PRICING_MODULE = "customer_group_pricing"

#: List of identifiers of discount modules to use.
#:
#: Each discount module may change the price of a product.  See
#: `shuup.core.pricing.DiscountModule` for details.
SHUUP_DISCOUNT_MODULES = ["catalog_campaigns", "customer_group_discount"]

#: List of identifiers of order source modifier modules.
#:
#: See `shuup.core.order_creator.OrderSourceModifierModule` for details.
SHUUP_ORDER_SOURCE_MODIFIER_MODULES = ["basket_campaigns"]

#: The identifier of the tax module to use for determining taxes of products and order lines.
#:
#: Determines taxing rules for products, shipping/payment methods and
#: other order lines.  See :obj:`shuup.core.taxing` for details.
SHUUP_TAX_MODULE = "default_tax"

#: Whether product attributes are enabled.  For installations not requiring attributes,
#: disabling this may confer a small performance increase.
SHUUP_ENABLE_ATTRIBUTES = True

#: Whether multiple shops are expected to be enabled in this installation.
#: Enabling or disabling this flag does not make it (im)possible to set up multiple shops,
#: but having it disabled may confer a small performance increase.
SHUUP_ENABLE_MULTIPLE_SHOPS = False

#: Whether multiple suppliers are enabled in this installation.
#: Enabling this flag allows supplier creation from admin.
SHUUP_ENABLE_MULTIPLE_SUPPLIERS = False

#: Indicates whether Shuup should restrict Contact access per Shop
#:
#: This is useful when multi-shop is in use and the contact shouldn't
#: be visible by other shops.
#:
#: The contact will be visible for shops in which user registered or
#: placed an order.
SHUUP_MANAGE_CONTACTS_PER_SHOP = False

#: A list of order labels (2-tuples of internal identifier / visible name).
#:
#: Order labels serve as a simple taxonomy layer for easy "tagging" of orders even within
#: a single Shop.  For instance, an installation could define ``"default"`` and ``"internal"``
#: order labels, which are then usable in reports, admin filtering, etc.
SHUUP_ORDER_LABELS = [
    ("default", "Default"),
]

#: The order label (see ``SHUUP_ORDER_LABELS``) to apply to orders by default.
#: This should naturally be one of the keys in ``SHUUP_ORDER_LABELS``.
SHUUP_DEFAULT_ORDER_LABEL = "default"

#: A list of "known keys" within the ``Order.payment_data`` property bag.
#:
#: The format of this setting is a list of 2-tuples of dict key / visible name,
#: for example ``[("ssn", "Social Security Number")]``.
#:
#: For installations where customizations may save some human-readable, possibly important
#: information in ``payment_data``, this setting may be used to make this data easily visible
#: in the administration backend.
SHUUP_ORDER_KNOWN_PAYMENT_DATA_KEYS = []

#: A list of "known keys" within the ``Order.shipping_data`` property bag.
#:
#: The format of this setting is a list of 2-tuples of dict key / visible name,
#: for example ``[("shipping_instruction", "Special Shipping Instructions")]``.
#:
#: For installations where customizations may save some human-readable, possibly important
#: information in ``shipping_data``, this setting may be used to make this data easily visible
#: in the administration backend.
SHUUP_ORDER_KNOWN_SHIPPING_DATA_KEYS = []

#: A list of "known keys" within the ``Order.extra_data`` property bag.
#:
#: The format of this setting is a list of 2-tuples of dict key / visible name,
#: for example ``[("wrapping_color", "Wrapping Paper Color")]``.
#:
#: For installations where customizations may save some human-readable, possibly important
#: information in ``extra_data``, this setting may be used to make this data easily visible
#: in the administration backend.
SHUUP_ORDER_KNOWN_EXTRA_DATA_KEYS = []

#: A flag to enable/disable the telemetry system
SHUUP_TELEMETRY_ENABLED = True

#: The host URL for Shuup's telemetry (statistics) system
SHUUP_TELEMETRY_HOST_URL = "https://telemetry.shuup.com"

#: The submission URL for Shuup's telemetry (statistics) system
SHUUP_TELEMETRY_URL = "%s/collect/" % SHUUP_TELEMETRY_HOST_URL

#: The URL to fetch the Shuup installation support id
SHUUP_SUPPORT_ID_URL = "%s/support-id" % SHUUP_TELEMETRY_HOST_URL

#: Default cache duration for various caches in seconds
SHUUP_DEFAULT_CACHE_DURATION = 60 * 30

#: Overrides for default cache durations by key namespace.
#: These override possible defaults in `shuup.core.cache.impl.DEFAULT_CACHE_DURATIONS`.
SHUUP_CACHE_DURATIONS = {}

#: Whether taxes should be calculated automatically in TaxModule
SHUUP_CALCULATE_TAXES_AUTOMATICALLY_IF_POSSIBLE = True

#: Spec which defines an address formatter used to
#: format output string of an Address model instances
SHUUP_ADDRESS_FORMATTER_SPEC = (
    "shuup.core.utils.formatters:DefaultAddressFormatter")

#: Spec which defines an default address model form
SHUUP_ADDRESS_MODEL_FORM = (
    "shuup.core.utils.forms.MutableAddressForm")

#: A dictionary defining properties to override the default field properties of the
#: checkout address form and also the Address API.
#:  Should map the field name (as a string) to a dictionary containing the overriding
#:  Django form field properties, as in the following
#: example which makes the postal code a required field:
#:
#: SHUUP_ADDRESS_FIELD_PROPERTIES = {
#:    "postal_code": {"required": True}
#: }
#:
#: Some of the Django form field properties will not affect Address API.
#: The valid set of properties are those defined by the Serializer fields core arguments
#: like read_only, required, allow_null, etc. See the Django Rest Framework documentation
#: for more properties.
#:
#: It should be noted, however, that overriding some settings (such as making a
#: required field non-required) could create other validation issues.
SHUUP_ADDRESS_FIELD_PROPERTIES = {}

#: Indicates maximum days for daily data included to one telemetry request
SHUUP_MAX_DAYS_IN_TELEMETRY = 180

#: Spec which defines if shop product categories
#: will be automatically populated on save or
#: when the shop_product categories change.
#:
#: Example A:
#: shop_product.categories = []
#: shop_product.primary_category = "A"
#: shop_product.save()
#: => "A" will be added to categories
#:
#: Example B:
#: shop_product.primary_category = None
#: shop_product.categories = ["A", "B"]
#: => "A" will be made the shop_product.primary_category
SHUUP_AUTO_SHOP_PRODUCT_CATEGORIES = True

#: Spec which defines a list of handlers of page errors
#: overwriting Django's default error handlers configured in urls.py (if some).
#:
#: Shuup will iterate over all handlers in order to determinate
#: if some can handle the error. In case of no handler can
#: do the job, a blank response will be returned.
#:
#: A handler must be a subclass of `shuup.core.error_handling.ErrorPageHandler`.
#:
#: If no handler is set (blank), Shuup will use default Django's handlers.
#:
SHUUP_ERROR_PAGE_HANDLERS_SPEC = []

#: Spec which defines shop product supplier strategy
#: Used to determine how the supplier is selected for source line and orderability checks.
#:
#: This spec defines class which should implement `get_supplier`-method for which
#: the current shop product with customer, quantity and shipping address is passed as kwargs.
SHUUP_SHOP_PRODUCT_SUPPLIERS_STRATEGY = (
    "shuup.core.suppliers.FirstSupplierStrategy")

#: Spec which provides the current shop for a given request and set of parameters.
SHUUP_REQUEST_SHOP_PROVIDER_SPEC = (
    "shuup.core.shop_provider.DefaultShopProvider")
