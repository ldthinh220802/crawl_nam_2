# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class RCommentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    R_url = scrapy.Field()
    R_reviewer_name = scrapy.Field()
    R_comment_date = scrapy.Field()
    R_reviewer_address = scrapy.Field()
    R_reviewer_contribution = scrapy.Field()
    R_reviewer_helpfuvote = scrapy.Field()
    comment_rating_sum = scrapy.Field()
    R_title_comment = scrapy.Field()
    R_content_comment = scrapy.Field()
    R_reviewer_staydate = scrapy.Field()
    R_smart_device = scrapy.Field()
    R_reviewer_gt = scrapy.Field()
    R_reviewer_dv = scrapy.Field()
    R_reviewer_da = scrapy.Field()
    pass
