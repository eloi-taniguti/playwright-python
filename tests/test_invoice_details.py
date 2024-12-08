import pytest
from playwright.sync_api import Browser, Page, expect

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
TaxAndVAT = 'USD $19.00'
TotalAmount = 'USD $209.00'
CustomerDetails = {
    'name': 'JOHNY SMITH',
    'address': 'R2, AVENUE DU MAROC',
    'zip': '123456'
}

def test_TC003_invoice_details(page: Page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login_as("demouser", "abc123")

    # Get new page after clicking a link
    with page.expect_popup() as new_page_info:
        page.get_by_role("link", name="Invoice Details").first.click() # Opens a new tab
    invoice_details_page = new_page_info.value

    expect(invoice_details_page.get_by_role('heading', name='Invoice Details')).to_be_visible()
    expect(invoice_details_page.get_by_role('heading', name=HotelName)).to_be_visible()
    expect(invoice_details_page.get_by_role('heading', name=f'Invoice #{InvoiceNumber} details')).to_be_visible()
    expect(invoice_details_page.locator('section').get_by_role('listitem').first).to_have_text(f'Invoice Date: {InvoiceDate}')
    expect(invoice_details_page.locator('section').get_by_role('listitem').nth(1)).to_have_text(f'Due Date: {DueDate}')

    #Booking Details
    expect(invoice_details_page.get_by_role('table').first.get_by_role('row').nth(0).get_by_role('cell').nth(1)).to_have_text(BookingCode)
    expect(invoice_details_page.get_by_role('table').first.get_by_role('row').nth(1).get_by_role('cell').nth(1)).to_have_text(Room)
    expect(invoice_details_page.get_by_role('table').first.get_by_role('row').nth(2).get_by_role('cell').nth(1)).to_have_text(TotalStayCount)
    expect(invoice_details_page.get_by_role('table').first.get_by_role('row').nth(3).get_by_role('cell').nth(1)).to_have_text(TotalStayAmount)
    expect(invoice_details_page.get_by_role('table').first.get_by_role('row').nth(4).get_by_role('cell').nth(1)).to_have_text(CheckIn)
    expect(invoice_details_page.get_by_role('table').first.get_by_role('row').nth(5).get_by_role('cell').nth(1)).to_have_text(CheckOut)

    #Customer Details
    expect(invoice_details_page.get_by_role('heading', name='Customer Details')).to_be_visible()
    expect(invoice_details_page.get_by_text(CustomerDetails['name'])).to_be_visible()
    expect(invoice_details_page.get_by_text(CustomerDetails['address'])).to_be_visible()
    expect(invoice_details_page.get_by_text(CustomerDetails['zip'])).to_be_visible()
    
    #Billing Details
    expect(invoice_details_page.get_by_role('table').nth(1).get_by_role('row').nth(1).get_by_role('cell').nth(0)).to_have_text(DepositNow)
    expect(invoice_details_page.get_by_role('table').nth(1).get_by_role('row').nth(1).get_by_role('cell').nth(1)).to_have_text(TaxAndVAT)
    expect(invoice_details_page.get_by_role('table').nth(1).get_by_role('row').nth(1).get_by_role('cell').nth(2)).to_have_text(TotalAmount)
