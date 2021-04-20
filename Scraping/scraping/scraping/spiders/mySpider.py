import scrapy


class QuotesSpider(scrapy.Spider):
    name = "recipes"
    start_urls = [
        'https://minimalistbaker.com/recipe-index/',
    ]

# response.css(".entry-title::text").get()      title
#response.css(".wprm-recipe-prep_time-minutes::text").get()            TODO: All have hours too
#response.css(".wprm-recipe-cook_time-minutes::text").get()
#response.css(".wprm-recipe-total_time-minutes::text").get()

#.wprm-recipe-ingredient-amount
#.wprm-recipe-ingredient-unit
#.wprm-recipe-ingredient-name
#.wprm-recipe-ingredient-link

    def parse_recipe(self, response):
        replace_val = 0
        for i in range(0, len(response.css(".wprm-recipe-ingredient-amount::text").getall())):
            yield {
                'Name': response.css(".entry-title::text").get(),
                'Prep.Hour': int(response.css(".wprm-recipe-prep_time-hours::text").get() or replace_val),
                'Prep.Min': int(response.css(".wprm-recipe-prep_time-minutes::text").get() or replace_val),
                'Cook.Hour': int(response.css(".wprm-recipe-cook_time-hours::text").get() or replace_val),
                'Cook.Min': int(response.css(".wprm-recipe-cook_time-minutes::text").get() or replace_val),
                'Total.Hour': int(response.css(".wprm-recipe-total_time-hours::text").get() or replace_val),
                'Total.Min': int(response.css(".wprm-recipe-total_time-minutes::text").get() or replace_val),
                'Amount': response.css(".wprm-recipe-ingredient-amount::text").getall()[i],
                'Unit': response.css(".wprm-recipe-ingredient-unit::text").getall()[i],
                'Ingredient': response.css(".wprm-recipe-ingredient-name::text, "
                                           ".wprm-recipe-ingredient-name a::text").getall()[i],
            }

    def parse_dir_page(self, response):
        for recipe in response.css("h3.post-summary__title a::attr(href)").getall():
            yield response.follow(recipe, callback=self.parse_recipe)

    def parse(self, response):
        for page_num in range(1,72):
            page = 'https://minimalistbaker.com/recipe-index/?fwp_paged=' + str(page_num)
            yield response.follow(page, callback=self.parse_dir_page)

'''
    def parse(self, response):
        for recipe in response.css('liv.li-a'):
            yield {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        next_page = response.css('div.li-a a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)
            '''