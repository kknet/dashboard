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
from django.contrib import admin

from .forms import BrokerForm
from .models import *


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('name', 'url')


@admin.register(Broker)
class BrokerAdmin(admin.ModelAdmin):
    list_display = ('name', 'contract_type', 'trade_address', 'market_address', 'identify', 'username')
    form = BrokerForm


@admin.register(Strategy)
class StrategyAdmin(admin.ModelAdmin):
    list_display = ('name', 'broker')


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('instrument', 'price', 'direction', 'offset_flag', 'status', 'send_time', 'update_time')


@admin.register(Instrument)
class InstrumentAdmin(admin.ModelAdmin):
    list_display = ('exchange', 'name', 'product_code', 'all_inst', 'main_code', 'last_main', 'change_time')


@admin.register(DailyBar)
class DailyBarAdmin(admin.ModelAdmin):
    list_display = ('code', 'time', 'open', 'high', 'low', 'close', 'volume')


@admin.register(Trade)
class TradeAdmin(admin.ModelAdmin):
    list_display = ('strategy', 'instrument', 'shares', 'direction', 'open_time', 'close_time', 'avg_entry_price', 'avg_exit_price', 'profit')