import pytest
from playwright.sync_api import Browser, Page, expect

from pages.invoice_details_page import InvoiceDetailsPage
from pages.login_page import LoginPage

HotelName = 'Rendezvous Hotel'
InvoiceNumber = '110'
InvoiceDate = '14/01/2018'
DueDate = '15/01/2018'
BookingCode = '0875'
Room = 'Superior Double'
CheckIn = '14/01/2018'
CheckOut = '15/01/2018'
TotalStayCount = '1'
TotalStayAmount = '$150'
DepositNow = 'USD $20.90'
TaxAndVAT = 'USD $19' #TODO - update value when UI is fixed
TotalAmount = 'USD $209' #TODO - update value when UI is fixed
CustomerDetails = {
    'name': 'JOHNY SMITH',
    'address': 'R2, AVENUE DU MAROC',
    'zip': '123456'
}

def test_TC003_invoice_details(browser: Browser):
    context = browser.new_context()
    page = context.new_page()
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login_as("demouser", "abc123")

    # Get new page after clicking a link
    with context.expect_page() as new_page_info:
        page.get_by_role("link", name="Invoice Details").first.click() # Opens a new tab

    invoice_details = new_page_info.value
    invoice_details_page = InvoiceDetailsPage(invoice_details)
    expect(invoice_details_page.page_heading('Invoice Details')).to_be_visible()
    expect(invoice_details_page.page_heading(HotelName)).to_be_visible()
    expect(invoice_details_page.invoice_number(InvoiceNumber)).to_be_visible()
    expect(invoice_details_page.invoice_date).to_have_text(f'Invoice Date: {InvoiceDate}')
    expect(invoice_details_page.due_date).to_have_text(f'Due Date: {DueDate}')

    #Booking Details
    expect(invoice_details_page.booking_details_value_in_row(0)).to_have_text(BookingCode)
    expect(invoice_details_page.booking_details_value_in_row(1)).to_have_text(Room)
    expect(invoice_details_page.booking_details_value_in_row(2)).to_have_text(TotalStayCount)
    expect(invoice_details_page.booking_details_value_in_row(3)).to_have_text(TotalStayAmount)
    expect(invoice_details_page.booking_details_value_in_row(4)).to_have_text(CheckIn)
    expect(invoice_details_page.booking_details_value_in_row(5)).to_have_text(CheckOut)

    #Customer Details
    expect(invoice_details.get_by_text(CustomerDetails['name'])).to_be_visible()
    expect(invoice_details.get_by_text(CustomerDetails['address'])).to_be_visible()
    expect(invoice_details.get_by_text(CustomerDetails['zip'])).to_be_visible()
    
    #Billing Details
    expect(invoice_details_page.billing_details_header).to_have_text(['Deposit Nowt', 'Tax&VAT', 'Total Amount']) #TODO - update value when UI is fixed
    expect(invoice_details_page.billing_details_values).to_have_text([DepositNow, TaxAndVAT, TotalAmount])
