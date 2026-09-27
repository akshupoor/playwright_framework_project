class Blogs:
    def __init__(self,page):
        self.page = page 

        #Technologies:
        self.blg = page.locator('(//a[@href="https://www.tranktechnologies.com/blog/"])[1]')


        #Trading:
        self.blog2 = page.locator('(//a[text()="App Development"])[1]')
        self.blog3 = page.locator('(//a[text()="Web Development"])[1]')
        #self.blog4 = page.locator('(//a[text()="Software Development"])[1]')
        self.blog5 = page.locator('(//a[text()="Digital Marketing"])[1]')
        self.blog6 = page.locator('(//a[text()="Email Marketing"])[1]')
        self.blog7 = page.locator('(//a[text()="Artificial Intelligence"])[2]')  
        self.blog8 = page.locator('(//a[text()="UI UX Design"])[1]')  

              

        self.blog_list = [self.blog2,self.blog3,self.blog5,self.blog6,self.blog7,self.blog8]

    def click_blog_option(self):
        for i in self.blog_list:
            self.blg.hover()
            #i.wait_for(state="visible", timeout=5000) 
            #self.blog.hover()
            i.click()
            self.page.wait_for_load_state("load")
            self.page.go_back()