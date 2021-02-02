BOT_NAME = 'bankpozitif'
SPIDER_MODULES = ['bankpozitif.spiders']
NEWSPIDER_MODULE = 'bankpozitif.spiders'
LOG_LEVEL = 'WARNING'
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
   'bankpozitif.pipelines.DatabasePipeline': 300,
}
