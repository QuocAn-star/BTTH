import scrapy
import pandas as pd

class DienMayXanhSpider(scrapy.Spider):
    name = "dienmayxanh"
    start_urls = ['https://www.dienmayxanh.com/']

    def parse(self, response):
        # Chọn các sản phẩm trong trang
        products = response.css('div.product-item')  # Thay đổi selector cho đúng

        for product in products:
            # Lấy thông tin cần thiết
            yield {
                'id': product.css('::attr(data-id)').get(),  # Chỉnh sửa selector cho đúng
                'name': product.css('h3.product-title::text').get(),
                'price': product.css('span.price::text').get(),
                'rating_average': product.css('span.rating-average::text').get(),
                'review_count': product.css('span.review-count::text').get(),
                'quantity_sold': product.css('span.quantity-sold::text').get(),
                'quantity_sold_1weeks': product.css('span.quantity-sold-1weeks::text').get(),
                'product_categories': product.css('span.product-categories::text').get(),
                'shop_categories': product.css('span.shop-categories::text').get(),
                'Name_Shop': product.css('span.name-shop::text').get(),
                'Year_Joined': product.css('span.year-joined::text').get(),
                'Followers': product.css('span.followers::text').get(),
                'Chat_Response': product.css('span.chat-response::text').get(),
                'Reviews': product.css('div.reviews::text').get(),
            }

        # Tiếp theo, kiểm tra xem có trang tiếp theo không và tiếp tục thu thập dữ liệu
        next_page = response.css('a.next-page::attr(href)').get()  # Chỉnh sửa selector cho đúng
        if next_page:
            yield response.follow(next_page, self.parse)

    def close(self, reason):
        # Xuất dữ liệu ra file Excel
        df = pd.DataFrame(self.crawler.stats.get_value('item_scraped_count'))  # Tạo DataFrame từ kết quả thu thập
        df.to_excel('dienmayxanh_products.xlsx', index=False)
