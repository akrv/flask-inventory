# project/vendor/forms.py


from flask_wtf import Form
from wtforms import TextField, SelectField, IntegerField, DateField
from wtforms.validators import DataRequired, Optional
from project.models import Vendor, PurchaseOrder, LineItem, Component, Borrow
STATE_ABBREV = ('AL', 'AK', 'AZ', 'AR', 'CA', 'CO', 'CT', 'DE', 'FL', 'GA',
                'HI', 'ID', 'IL', 'IN', 'IO', 'KS', 'KY', 'LA', 'ME', 'MD',
                'MA', 'MI', 'MN', 'MS', 'MO', 'MT', 'NE', 'NV', 'NH', 'NJ',
                'NM', 'NY', 'NC', 'ND', 'OH', 'OK', 'OR', 'PA', 'RI', 'SC',
                'SD', 'TN', 'TX', 'UT', 'VT', 'VA', 'WA', 'WV', 'WI', 'WY')

STATUS_AVL = ('Returned','Borrowed','Available')


class VendorCreateForm(Form):
    name = TextField('Company', validators=[DataRequired()])
    contact = TextField('Contact')
    line1 = TextField('Address 1')
    line2 = TextField('Address 2')
    line3 = TextField('Address 3')
    city = TextField('City')
    state = SelectField('State',
                        choices=[(state, state) for state in STATE_ABBREV])
    zipcode = TextField('Zipcode')
    phone = TextField('Phone')
    website = TextField('Website')


class PurchaseOrderForm(Form):
    item = SelectField('Item Id', choices=[(str('(')+str(item.id)+str(')  ')+str(item.name),
                                            str('(')+str(item.id)+str(')  ')+str(item.name))
                                            for item in Component.query.all()],validators=[DataRequired()])
    quantity = IntegerField('Quantity', validators=[DataRequired()])
    vendor_id = SelectField('Vendor ID', choices=[(str('(')+str(vendor.id)+str(')  ')+str(vendor.name),
                                                    str('(')+str(vendor.id)+str(')  ')+str(vendor.name))
                                                    for vendor in Vendor.query.all()],validators=[DataRequired()])
    unit_price = TextField('Unit Price', validators=[DataRequired()])

class BorrowForm(Form):

    quantity = IntegerField('Quantity', validators=[DataRequired()])
    borrowed_by = SelectField('State',
                        choices=[(state, state) for state in STATE_ABBREV])
    borrowed_to = SelectField('State',
                        choices=[(state, state) for state in STATE_ABBREV])
    reason = TextField('Reason')
    current_status = SelectField('Status',
                        choices=[(status, status) for status in STATUS_AVL])

    borrowed_on = DateField('Borrowed date', format='%m/%d/%Y', validators=[Optional()])
    returned_on = DateField('Return date', format='%m/%d/%Y', validators=[Optional()])

class ComponentCreateForm(Form):
    name = TextField('Name', validators=[DataRequired()])
