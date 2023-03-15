# -*- coding: utf-8 -*-

from odoo import models, fields, api

class wgcc_savings(models.Model):
    _name = 'wgcc_savings.wgcc_savings'
    
    employee_id = fields.Many2one('hr.employee', string="Employee ID No.")
    name = fields.Char(string="Name:")
    search_field = fields.Char(string="Search:")
    deposit_amount = fields.Float(string='Deposit Amount', digits=(10, 2))

    deposit_date = fields.Date(string='Deposit Date')
    Company = fields.Char("Company:")
    current_balance_before_widthrawal = fields.Float(string='Current Balance Before Widthrawal: ', digits=(10, 2))
    last_date_of_widthrawal = fields.Date(string='Last Date Of Widthrawal')
    saving_deposit_deduction = fields.Float(string='Savings Deposit Deduction')
    withdrawable_balance = fields.Float(string='Withdrawable Balance', digits=(10, 2))
    account_number = fields.Char(string="Account Number:")
    bank_code = fields.Char(string="Bank Code:")
    withdrawable_mode = fields.Char(string="Widthrawal Mode:")
    amount_to_be_widthrawn = fields.Float(string='Amount to be withdrawn: ', digits=(10, 2))
    withdrawal_slip_no = fields.Integer(string='Withdrawal Slip No.')
    cash = fields.Char(string="(Words)")
    date_of_widthrawal = fields.Date(string='Date Of Widthrawal:')
    is_atm = fields.Boolean(string="ATM")
    release_date = fields.Date(string='Release Date')
    is_cheque = fields.Boolean(string="Check")
    cheque_information = fields.Char("Cheque Information: ")
    bank = fields.Char("Bank: ")
    cheque_no = fields.Char("Cheque No: ")
    prepared_by = fields.Char()
    posted_by = fields.Char()
    cancelled_by = fields.Char()
    cancel_reason = fields.Char()
    
    status= fields.Selection([
        ('draft', 'Draft'),
        ('released', 'Released'),
        ('cancelled', 'Cancelled'),
        
    ], string='Status', readonly="True", default="draft")
    
    
    