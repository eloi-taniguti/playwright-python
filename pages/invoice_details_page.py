from playwright.sync_api import Page, Locator, expect

class InvoiceDetailsPage:
    def __init__(self, page: Page):
        self.page = page
        self.invoice_date: Locator = page.locator('section').get_by_role('listitem').first
        self.due_date: Locator = page.locator('section').get_by_role('listitem').nth(1)
        self.billing_details_header: Locator = page.get_by_role('table').nth(1).get_by_role('row').nth(0).get_by_role('cell')
        self.billing_details_values: Locator = page.get_by_role('table').nth(1).get_by_role('row').nth(1).get_by_role('cell')

    def page_heading(self, value: str):
        return self.page.get_by_role('heading', name=value)
    
    def invoice_number(self, value: str):
        return self.page.get_by_role('heading', name=f'Invoice #{value} details')
    
    def booking_details_value_in_row(self, row: int):
        return self.page.get_by_role('table').first.get_by_role('row').nth(row).get_by_role('cell').nth(1)
