# Copyright 2022 Marcin Żurawski
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).
from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.logged_query(
        env.cr,
        """
        UPDATE res_partner SET state_id = (SELECT id from res_country_state WHERE name='wielkopolskie') WHERE id=671 or id=670
        """
    )
    openupgrade.logged_query(
        env.cr,
        """
        DELETE FROM res_country_state where name='Wielkopolskie';
        """
    )
