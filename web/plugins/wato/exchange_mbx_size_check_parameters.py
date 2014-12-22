#!/usr/bin/python
# -*- encoding: utf-8; py-indent-offset: 4 -*-
# 2014 Marius Pana mp@sphs.ro


register_check_parameters(
    subgroup_applications,
    "exchange_user_mbx_size",
    _("MS Exchange User Mailbox Size"),
    Tuple(
      title = _('Maximum Mailbox Size'),
          elements = [
             Integer(title = _("Warning if above"), default_value = 1500 ),
             Integer(title = _("Critical if above"), default_value = 2000 ),
          ]
    ),
    None,
    None,
)

