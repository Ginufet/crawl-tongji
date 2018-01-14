# Introduction

为软件工程课程项目编写的爬虫，目的是爬取同济大学财务处的信息，为项目扩充知识库。

# Get start

## Item list

1. FaqItem
   - name: faq
   - fields_to_export: FIELDS_TO_EXPORT_FAQ
2. DownloadsItem
   - name: downloads
   - fields_to_export: FIELDS_TO_EXPORT_DOWNLOADS

## Start

1. 选择一个要爬取的Item

2. 修改 *my_csv_exporter.py* 中的 fields_to_export 为Item对应的 fields_to_export

3. 在项目代码根目录 *tjcwc* 下打开shell，使用命令

```shell
scrapy crawl item-name -o filename.csv
```

## Example

以爬取FaqItem为例：

1. 修改 *my_csv_exporter.py* 文件中的 fields_to_export 为

```python
fields_to_export = settings.get('FIELDS_TO_EXPORT_FAQ', [])
```

2. 在项目代码根目录 *tjcwc* 下打开shell，使用命令

```shell
scrapy crawl faq -o faq_item.csv
```

3. 爬取结果会被保存在 *tjcwc/faq_item.csv* 中



