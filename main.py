#!/usr/bin/env python
# -*- coding:utf-8 -*-
from jd_assistant import Assistant

if __name__ == '__main__':
    """
    重要提示：此处为示例代码之一，请移步下面的链接查看使用教程👇
    https://github.com/tychxn/jd-assistant/wiki/1.-%E4%BA%AC%E4%B8%9C%E6%8A%A2%E8%B4%AD%E5%8A%A9%E6%89%8B%E7%94%A8%E6%B3%95
    """

    sku_ids = '100012043978'  # 茅台商品id
    area = '19_1609_41655_41710'  # 区域id
    asst = Assistant()  # 初始化
    asst.login_by_QRcode()  # 扫码登陆
    # asst.clear_cart() # 清空购物车（可选）
    # asst.add_item_to_cart(sku_ids='100016117840')  # 根据商品id添加购物车（可选）
    # asst.submit_order_by_time(buy_time='2020-11-10 20:59:59.700', retry=4, interval= 0.5) #普通订单可用
    # asst.exec_seckill_by_time(sku_ids =sku_ids,buy_time='2020-11-10 23:59:59.700', retry=5, interval= 0.5)  # 定时提交秒杀订单
    asst.exec_reserve_seckill_by_time(sku_id ='100016117840',buy_time='2020-11-11 07:59:59.975', retry=4, interval= 0.2) #该秒杀会放入购物车
    # asst.buy_item_in_stock(sku_ids=sku_ids, area=area, wait_all=False, stock_interval=5)  # 根据商品是否有货自动下单
    # 6个参数：
    # sku_ids: 商品id。可以设置多个商品，也可以带数量，如：'1234' 或 '1234,5678' 或 '1234:2' 或 '1234:2,5678:3'
    # area: 地区id
    # wait_all: 是否等所有商品都有货才一起下单，可选参数，默认False
    # stock_interval: 查询库存时间间隔，可选参数，默认3秒
    # submit_retry: 提交订单失败后重试次数，可选参数，默认3次
    # submit_interval: 提交订单失败后重试时间间隔，可选参数，默认5秒
