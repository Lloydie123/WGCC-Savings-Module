# -*- coding: utf-8 -*-

from odoo import models, fields, api

class wgcc_savings(models.Model):
    _name = 'wgcc_savings.wgcc_savings'

    name = fields.Char(string="Name:")
    search = fields.Char(string="Search:")
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
    cash = fields.Char(string="Cash:")
    date_of_widthrawal = fields.Date(string='Date Of Widthrawal:')
    is_atm = fields.Boolean(string="ATM")
    release_date = fields.Date(string='Release Date')
    is_cheque = fields.Boolean(string="Check")
    cheque_information = fields.Char("Cheque Information: ")
    bank = fields.Char("Cheque Information: ")
    cheque_no = fields.Char("Cheque No: ")
    prepared_by = fields.Char("Prepared By: ")
    posted_by = fields.Char("Posted By: ")
    cancelled_by = fields.Char("Cancelled By: ")
    cancel_reason = fields.Char("Cancel Reason: ")
    
    
    