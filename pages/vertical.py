class verticals:
    def __init__(self,page):
        self.page = page 

        #Vertical:
        self.vertical = page.locator('(//a[text()="Verticals"])[1]')

        #Trading:
        self.vrt = page.locator('//strong[text()="Trading"]')
        self.vrt2 = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-mobile-app-development-company"])[1]')
        self.vrt3 = page.locator('(//a[@href="https://www.tranktechnologies.com/paper-trading-app-development-company"])[1]')
        self.vrt4 = page.locator('(//a[@href="https://www.tranktechnologies.com/cfd-trading-app-development-company"])[1]')
        self.vrt5 = page.locator('(//a[@href="https://www.tranktechnologies.com/stock-trading-development-in-massachusetts"])[1]')
        self.vrt6 = page.locator('(//a[@href="https://www.tranktechnologies.com/algo-trading-app-development-company"])[1]')
        self.vrt7 = page.locator('(//a[@href="https://www.tranktechnologies.com/custom-trading-software-development-company"])[1]')
        self.vrt8 = page.locator('(//a[@href="https://www.tranktechnologies.com/webportal-trading-development"])[1]')

        self.trading_list = [self.vrt2,self.vrt3,self.vrt4,self.vrt5,self.vrt6,self.vrt7,self.vrt8]

        #RetailEcomers:
        #self.rtl = page.locator('//strong[text()="Retail and Ecommerce"]')
        self.rtl = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[1]')
        self.rtl1 = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-web-development-company"])[2]')
        self.rtl2 = page.locator('(//a[@href="https://www.tranktechnologies.com/ecommerce-app-development"])[1]')

        self.RetailEcomers_list = [self.rtl1, self.rtl2]

        #Healthcare:
        self.hlc = page.locator('//strong[text()="Healthcare"]')
        self.hlc1 = page.locator('(//a[@href="https://www.tranktechnologies.com/diet-and-nutrition-app-developement"])[1]')
        self.hlc2 = page.locator('(//a[@href="https://www.tranktechnologies.com/health-tracking-app"])[1]')

        self.Healthcare_list = [self.hlc1, self.hlc2]

        #Fintech
        self.fint = page.locator('//strong[text()="Fintech"]')
        self.fint1 = page.locator('(//a[@href="https://www.tranktechnologies.com/pos-software-development-company"])[1]')
        self.fint2 = page.locator('(//a[@href="https://www.tranktechnologies.com/cryptocurrency-mobile-app-development-company"])[1]')

        self.Fintech_list = [self.fint1, self.fint2]

    def click_trading_option(self):
        for i in self.trading_list:
            self.vertical.hover()
            self.vrt.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def click_RetailEcomers_option(self):
        for i in self.RetailEcomers_list:
            self.vertical.hover()
            self.rtl.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def click_Healthcare_option(self):
        for i in self.Healthcare_list:
            self.vertical.hover()
            self.hlc.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def click_Fintech_option(self):
        for i in self.Fintech_list:
            self.vertical.hover()
            self.fint.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()
                


        