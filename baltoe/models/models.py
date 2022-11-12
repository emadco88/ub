from odoo import api, fields, models


class Customers(models.Model):
    _name = 'baltoe_customer'

    name = fields.Char()
    commercial_reg = fields.Char()
    tax_no = fields.Char()
    nid = fields.Char()
    address = fields.Char()
    description = fields.Text()
    first_deal_date = fields.Date()
    company = fields.Selection(selection=[('upper', 'Upper Medic'), ('baltoe', 'Baltoe'), ('common', 'Common'), ], )

    eval = fields.Integer()

    att_files = fields.Binary(string="Attachments", )


class Services(models.Model):
    _name = 'baltoe_service'
    _description = 'Services'

    name = fields.Char()
    service_type = fields.Selection(selection=[('one', 'One Time'), ('subs', 'Subscription'), ])
    cost = fields.Float()
    price = fields.Float()


class Contracts(models.Model):
    _name = 'baltoe_contract'
    _description = 'Contracts'

    name = fields.Char()
    company = fields.Selection(selection=[('upper', 'Upper Medic'), ('baltoe', 'Baltoe'), ])
    customer_id = fields.Many2one('baltoe_customer')
    contract_type = fields.Selection(selection=[('one', 'One Time'), ('subs', 'Subscription'), ])
    service_id = fields.Many2one('baltoe_service')
    estimated_cost = fields.Float()
    total_price = fields.Float()
    downpayment = fields.Float()
    installment = fields.Float()
    periodicity = fields.Integer()
    start = fields.Date()
    end = fields.Date()
    creator_id = fields.Many2one('baltoe_employee')
    att_files = fields.Binary()
    status = fields.Selection(selection=[('active', 'Active'), ('inactivated', 'Inactivated'),
                                         ('terminated', 'Terminated'), ('expired', 'Expired')])


class Department(models.Model):
    _name = 'baltoe_department'
    _description = 'Department'

    name = fields.Char()


class Job(models.Model):
    _name = 'baltoe_job'
    _description = 'Jobs'
    name = fields.Char()


class Employees(models.Model):
    _name = 'baltoe_employee'
    _description = 'Employees'

    name = fields.Char()
    user_id = fields.Many2one('res.users')
    birthdate = fields.Date()
    qualification = fields.Char()
    job_id = fields.Many2one('baltoe_job')
    department_id = fields.Many2one('baltoe_department')
    company = fields.Selection(selection=[('upper', 'Upper Medic'), ('baltoe', 'Baltoe'), ('common', 'Common'), ], )
    working_type = fields.Selection(selection=[('full', 'Full Time'), ('part', 'Part Time'), ('free', 'Freelance'), ], )
    hour_price = fields.Float()
    hiring_date = fields.Date()


class Doctype(models.Model):
    _name = 'baltoe_doctype'
    _description = 'Document Types'
    name = fields.Char()


class AccGuide(models.Model):
    _name = 'baltoe_accguide'
    _description = 'AccGuide'

    name = fields.Char()
    is_company_account = fields.Boolean()
    has_costcenter = fields.Boolean()
    required_costcenter = fields.Boolean()
    parent_id = fields.Many2one('baltoe_accguide')


class Income(models.Model):
    _name = 'baltoe_income'
    _description = 'Income'

    creation_date = fields.Date()
    due_date = fields.Date()
    contract_id = fields.Many2one('baltoe_contract')
    customer_id = fields.Many2one(related='contract_id.customer_id')
    service_id = fields.Many2one('baltoe_service')
    creator_id = fields.Many2one('baltoe_employee')
    settlement_status = fields.Boolean()
    settlement_date = fields.Date()
    collected_value = fields.Float()
    bill_value = fields.Float()
    attach = fields.Binary()
    company_account_id = fields.Many2one('baltoe_accguide')
    doctype = fields.Many2one('baltoe_doctype')
    company = fields.Selection(selection=[('upper', 'Upper Medic'), ('baltoe', 'Baltoe')], )
    active = fields.Boolean(default=True)


class CostCenter(models.Model):
    _name = 'baltoe_costcenter'
    _description = 'CostCenter'

    name = fields.Char()
    nick_name = fields.Char()
    id_no = fields.Char()


class JE(models.Model):
    _name = 'baltoe_je'
    _description = 'JE'
    _rec_name = 'explain'
    explain = fields.Char('explain')
    out_value = fields.Float()
    in_value = fields.Float()
    costcenter_id = fields.Many2one('baltoe_costcenter')
    creation_date = fields.Date()
    due_date = fields.Date()
    contract_id = fields.Many2one('baltoe_contract')
    customer_id = fields.Many2one(related='contract_id.customer_id')
    service_id = fields.Many2one('baltoe_service')
    creator_id = fields.Many2one('baltoe_employee')
    company = fields.Selection(selection=[('upper', 'Upper Medic'), ('baltoe', 'Baltoe'), ('common', 'Common'), ], )
    doctype = fields.Many2one('baltoe_doctype')
    company_account_id = fields.Many2one('baltoe_accguide')
    on_account = fields.Many2one('baltoe_accguide')
    att_files = fields.Binary(string="Attachments", )
    active = fields.Boolean(default=True)
