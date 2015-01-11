#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# 2014 Marius Pana mp@sphs.ro

#register_check_parameters(
#    subgroup_applications,
#    "exchange_user_mbx_size",
#    _("MS Exchange User Mailbox Size"),
#    Dictionary(
#        elements = [
#            ("Maximum Mailbox Size",
#                Integer(
#                    title = _("Warning if above"),
#                    unit = _("MB"),
#                    default_value = 1500
#                ),
#                Integer(
#                    title = _("Critical if above"),
#                    unit = _("MB"),
#                    default_value = 2000
#                ),
#            ),
#	]
#    ),
#    None,
#    "dict"
#)

# -- another attempt -- #

register_check_parameters(
    subgroup_applications,
    "exchange_user_mbx_size",
    _("MS Exchange User Mailbox Size"),
    Dictionary(
        elements = [
        ("levels",
          Tuple(
            title = _("Maximum Exchange Mailbox Size"),
            elements = [
                Integer(title = _("Warning if larger than"), default_value = 1500),
                Integer(title = _("Critical if larger than"), default_value = 2000)
            ]
          )
        )]
    ),
    None,
    None
)
