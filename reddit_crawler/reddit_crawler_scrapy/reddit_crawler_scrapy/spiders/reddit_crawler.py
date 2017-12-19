# -*- coding: utf-8 -*-
import scrapy

# scrapy crawl reddit -a subreddit=leagueoflegends -a pages=3 -s LOG_FILE=filename

class RedditSpider(scrapy.Spider):
    name = 'reddit'
    allowed_domains = ["reddit.com"]

    def __init__(self, subreddit=None, pages=None, *args, **kwargs):
        super(RedditSpider, self).__init__(*args, **kwargs)
        self.start_urls = ['https://www.reddit.com/r/%s/new/' % subreddit]
        self.pages = int(pages)
        self.page_count = 0

    def parse(self, response):

        # Extracting the content using css selectors
        titles = response.css('.title.may-blank::text').extract()
        # votes = response.css('.score.unvoted::text').extract()
        # times = response.css('time::attr(title)').extract()
        # comments = response.css('.comments::text').extract()
        submission_id = response.css('.title.may-blank').xpath('@data-outbound-url').extract()
        # submission_id = submission_id[24:33]

        # Give the extracted content row wise
        # for item in zip(titles, votes, times, comments, titles_full):
        for item in zip(titles, submission_id):
            # create a dictionary to store the scraped info
            scraped_info = {
                'title': item[0],
                'submission_id': item[1][23:32]
                # 'vote': item[2],
                # 'created_at': item[3],
                # 'comments': item[4]
            }

            # yield or give the scraped info to scrapy
            yield scraped_info

        if (self.pages > 1) and (self.page_count < self.pages):
            self.page_count += 1
            next_page = response.css('span.next-button a::attr(href)').extract_first()
            if next_page is not None:
                print("next page ... " + next_page)
                yield response.follow(next_page, callback=self.parse)

            if next_page is None:
                print("no more pages ... lol")