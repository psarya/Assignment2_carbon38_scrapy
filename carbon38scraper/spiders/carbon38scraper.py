import scrapy

class Carbon38Spider(scrapy.Spider):
    name = 'carbon38'
    start_urls = ['https://www.carbon38.com/shop-all-activewear/tops']

    def parse(self, response):
        products = response.css('div.ProductItem__Wrapper')

        for product in products:
            yield {
                'breadcrumbs': product.css('ul.HorizontalList::text').getall(),
                'image_url': product.css('div a').attrib['href'],
                'brand': product.css('h3.ProductItem__Designer::text').get(),
                'product_name': product.css('h2 a::text').get(),
                'price':  product.css('span.ProductItem__Price::text').get(),
                'reviews': product.css('div.yotpo-sr-bottom-line-right-panel::text').get(),
                'colour': product.css('div.ProductItem__ColorSwatchItem::text').get(),
                'sizes': product.css('div a.add-size-to-cart::text').get(),
                'description': product.css('div.Faq__AnswerWrapper::text').get(),
                'sku': product.css('div.ProductItem__SKU::text').get(),
                'product_id': product.css('div.ProductItem__ID::text').get(),
        }
        next_page = response.css('a.Pagination__NavItem.Link.Link--primary').attr['href']
        if next_page is not None:
            yield  response.follow(next_page, callback=self.parse)