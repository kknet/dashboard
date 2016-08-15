# coding=utf-8
#
# Copyright 2016 timercrack
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
from djchoices import DjangoChoices, C

CFFEX_QUOTE_FORMAT = 'http://stock2.finance.sina.com.cn/futures/api/json.php/CffexFuturesService.getCffexFuturesDailyKLine?symbol={}'
"""
[["2016-01-18","2734.6","2816.8","2714.4","2743","194"], ...
"""

OTHER_QUOTE_FORMAT = 'http://stock.finance.sina.com.cn/futures/api/json.php/InnerFuturesService.getInnerFuturesDailyKLine?symbol={}'

"""
[{date:"2016-01-18",open:"1530.000",high:"1558.000",low:"1530.000",close:"1556.000",volume:"166234"}, ...
"""


class ContractType(DjangoChoices):
    STOCK = C(label='股票')
    FUTURE = C(label='期货')
    OPTION = C(label='期权')


class ExchangeType(DjangoChoices):
    SHFE = C(value='SHFE', label='上期所')
    DCE = C(value='DCE', label='大商所')
    CZCE = C(value='CZCE', label='郑商所')
    CFFEX = C(value='CFFEX', label='中金所')


class AddressType(DjangoChoices):
    TRADE = C(label='交易')
    MARKET = C(label='行情')


class OperatorType(DjangoChoices):
    TELECOM = C(label='电信')
    UNICOM = C(label='联通')


class DirectionType(DjangoChoices):
    LONG = C(label='多')
    SHORT = C(label='空')


class OffsetFlag(DjangoChoices):
    BUY = C(label='买开')
    SELL = C(label='卖平')
    SELL_SHORT = C(label='卖开')
    BUY_COVER = C(label='买平')


class OrderStatus(DjangoChoices):
    AllTraded = C(value='0', label='全部成交')
    PartTradedQueueing = C(value='1', label='部分成交还在队列中')
    PartTradedNotQueueing = C(value='2', label='部分成交不在队列中')
    NoTradeQueueing = C(value='3', label='未成交还在队列中')
    NoTradeNotQueueing = C(value='4', label='未成交不在队列中')
    Canceled = C(value='5', label='撤单')
    Unknown = C(value='a', label='未知')
    NotTouched = C(value='b', label='尚未触发')
    Touched = C(value='c', label='已触发')