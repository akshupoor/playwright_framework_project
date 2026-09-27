class Technologies:
    def __init__(self,page):
        self.page = page 

        #Technologies:
        self.techno = page.locator('(//a[text()="Technologies"])[1]')


        #Trading:
        self.tech = page.locator('//strong[text()="eCommerce Development"]')
        self.tech1 = page.locator('(//a[@href="https://www.tranktechnologies.com/magento-development"])[1]')
        self.tech2 = page.locator('(//a[@href="https://www.tranktechnologies.com/opencart-development"])[1]')
        self.tech3 = page.locator('(//a[@href="https://www.tranktechnologies.com/codeigniter-development"])[1]')
        self.tech4 = page.locator('(//a[@href="https://www.tranktechnologies.com/wordpress-development"])[1]')
        self.tech5 = page.locator('(//a[@href="https://www.tranktechnologies.com/big-commerce"])[1]')
        self.tech6 = page.locator('(//a[@href="https://www.tranktechnologies.com/shopify-development"])[1]')
        self.tech7 = page.locator('(//a[@href="https://www.tranktechnologies.com/cs-cart-development"])[1]')
        self.tech8 = page.locator('(//a[@href="https://www.tranktechnologies.com/node-js-development"])[1]')
        self.tech9 = page.locator('(//a[@href="https://www.tranktechnologies.com/laravel-development"])[1]')
        self.tech10 = page.locator('(//a[@href="https://www.tranktechnologies.com/prestashop-development"])[1]')
        self.tech11 = page.locator('(//a[@href="https://www.tranktechnologies.com/wix-development"])[1]')
        self.tech12 = page.locator('(//a[@href="https://www.tranktechnologies.com/joomla-development"])[1]')
        self.tech13 = page.locator('(//a[@href="https://www.tranktechnologies.com/express-js-development"])[1]')

        self.technologies_list = [self.tech1,self.tech2,self.tech3,self.tech4,self.tech5,self.tech6,self.tech8,self.tech9,self.tech10,self.tech11,self.tech12,self.tech13,]

        #Mobile App Development:
        self.mad = page.locator('//strong[text()="Mobile App Development"]')
        self.mad1 = page.locator('(//a[@href="https://www.tranktechnologies.com/react-native-mobile-app-development"])[1]')
        self.mad2 = page.locator('(//a[@href="https://www.tranktechnologies.com/enterprise-mobile-app-development"])[1]')
        self.mad3 = page.locator('(//a[@href="https://www.tranktechnologies.com/xamarin-mobile-app-development"])[1]')
        self.mad4 = page.locator('(//a[@href="https://www.tranktechnologies.com/kotlin-mobile-app-development"])[1]')
        self.mad5 = page.locator('(//a[@href="https://www.tranktechnologies.com/flutter-mobile-app-development"])[1]')
        self.mad6 = page.locator('(//a[@href="https://www.tranktechnologies.com/appointment-booking-development"])[1]')


        self.Mobile_App_Development_List = [self.mad1, self.mad2,self.mad3,self.mad4,self.mad5,self.mad6]

        #Artificial Intelligence:
        self.arti = page.locator('//strong[text()="Artificial Intelligence"]')

        
    def click_ecom_option(self):
        for i in self.technologies_list:
            self.techno.hover()
            self.tech.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def click_Mobappdev_option(self):
        for i in self.Mobile_App_Development_List:
            self.techno.hover()
            self.mad.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()

    def click_artificial_option(self):
            self.techno.hover()
            self.arti.hover()
            self.arti.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()



        