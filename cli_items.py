from scrapy import cmdline

if __name__ == '__main__':
    cmdline.execute("scrapy runspider website/spiders/items.py -o /data/tmp/vntrip/data.jl -t jsonlines".split())