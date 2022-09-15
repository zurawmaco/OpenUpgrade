# Copyright 2020 Payam Yasaie <https://www.tashilgostar.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.logged_query(
        env.cr, """
        DELETE FROM ir_act_window_view 
        WHERE act_window_id=380 and view_mode='tree'"""
    )
    openupgrade.set_xml_ids_noupdate_value(
        env,
        "hr_timesheet",
        [
            "group_timesheet_manager",
        ],
        False,
    )
