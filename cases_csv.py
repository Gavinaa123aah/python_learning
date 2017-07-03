# Copyright (c) 2016 App Annie Inc. All rights reserved.
from tests.quick_smoke.smoke_utils import get_env_var

env_var = get_env_var()
debug_csv_cases = [

]

csv_cases = [
    # =============  App compare overview dashboard  ============================
    # -------------  App breakdown  -----------------------
    {'name': '[AN] AppComparator - OverviewDashboard - AppBreakdown - All',
     'url': '#{https}/ajax/comparator/export/?group_id=#{groupId}&'
            'breakdown=product&countries=US&start_date=%s&end_date=%s&chart_type=all&with_ad=f' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,Overview dashboard', 'Breakdown,App',
               'Countries,United States']},
    {'name': '[AN] AppComparator - OverviewDashboard - AppBreakdown - All - Filter by platform',
     'url': '#{https}/ajax/comparator/export/?group_id=#{groupId}&'
            'platform=ios&'
            'breakdown=product&countries=US&start_date=%s&end_date=%s&chart_type=all&with_ad=f' %
            (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,Overview dashboard', 'Breakdown,App',
               'Countries,United States']},
    # -------------  Country breakdown  -----------------------
    {'name': '[AN] AppComparator - OverviewDashboard - CountryBreakdown - All',
     'url': '#{https}/ajax/comparator/export/?group_id=#{groupId}&'
            'breakdown=country&countries=US&start_date=%s&end_date=%s&chart_type=all&with_ad=f' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,Overview dashboard', 'Breakdown,Country',
               'Countries,United States']},
    # -------------  Platform breakdown  -----------------------
    {'name': '[AN] AppComparator - OverviewDashboard - PlatformBreakdown - All',
     'url': '#{https}/ajax/comparator/export/?group_id=#{groupId}&'
            'breakdown=platform&countries=US&start_date=%s&end_date=%s&chart_type=all&with_ad=f' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,Overview dashboard', 'Breakdown,Platform',
               'Countries,United States']},
    # -------------  Publisher breakdown  -----------------------
    {'name': '[AN] AppComparator - OverviewDashboard - PublisherBreakdown - All',
     'url': '#{https}/ajax/comparator/export/?group_id=#{groupId}&'
            'breakdown=publisher&countries=US&start_date=%s&end_date=%s&chart_type=all&with_ad=f' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,Overview dashboard', 'Breakdown,Publisher',
               'Countries,United States']},
    # =============  App compare Download dashboard  ============================
    # -------------  App breakdown  -----------------------
    {'name': '[AN] AppComparator - DownloadDashboard - AppBreakdown - All',
     'url': '#{https}/ajax/comparator/downloads/export/?group_id=#{groupId}&'
            'breakdown=product&countries=US&start_date=%s&end_date=%s&chart_type=all&with_ad=f' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,Downloads dashboard', 'Breakdown,App',
               'Countries,United States']},
    # -------------  Country breakdown  -----------------------
    {'name': '[AN] AppComparator - DownloadDashboard - CountryBreakdown - All',
     'url': '#{https}/ajax/comparator/downloads/export/?group_id=#{groupId}&'
            'breakdown=country&countries=US&start_date=%s&end_date=%s&chart_type=all&with_ad=f' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,Downloads dashboard', 'Breakdown,Country',
               'Countries,United States']},
    # -------------  Platform breakdown  -----------------------
    {'name': '[AN] AppComparator - DownloadDashboard - PlatformBreakdown - All',
     'url': '#{https}/ajax/comparator/downloads/export/?group_id=#{groupId}&'
            'breakdown=platform&countries=US&start_date=%s&end_date=%s&chart_type=all&with_ad=f' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,Downloads dashboard', 'Breakdown,Platform',
               'Countries,United States']},
    # -------------  Publisher breakdown  -----------------------
    {'name': '[AN] AppComparator - DownloadDashboard - PublisherBreakdown - All',
     'url': '#{https}/ajax/comparator/downloads/export/?group_id=#{groupId}&'
            'breakdown=publisher&countries=US&start_date=%s&end_date=%s&chart_type=all&with_ad=f' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,Downloads dashboard', 'Breakdown,Publisher',
               'Countries,United States']},
    # =============  App compare Revenue dashboard  ============================  <>
    # -------------  App breakdown  -----------------------
    {'name': '[AN] AppComparator - RevenueDashboard - AppBreakdown - All',
     'url': '#{https}/ajax/comparator/revenue/export/?group_id=#{groupId}&'
            'breakdown=product&countries=US&start_date=%s&end_date=%s&chart_type=all&with_ad=f' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,Revenue dashboard', 'Breakdown,App',
               'Countries,United States']},
    # -------------  Country breakdown  -----------------------
    {'name': '[AN] AppComparator - RevenueDashboard - CountryBreakdown - All',
     'url': '#{https}/ajax/comparator/revenue/export/?group_id=#{groupId}&'
            'breakdown=country&countries=US&start_date=%s&end_date=%s&chart_type=all&with_ad=f' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,Revenue dashboard', 'Breakdown,Country',
               'Countries,United States']},
    # -------------  Platform breakdown  -----------------------
    {'name': '[AN] AppComparator - RevenueDashboard - PlatformBreakdown - All',
     'url': '#{https}/ajax/comparator/revenue/export/?group_id=#{groupId}&'
            'breakdown=platform&countries=US&start_date=%s&end_date=%s&chart_type=all&with_ad=f' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,Revenue dashboard', 'Breakdown,Platform',
               'Countries,United States']},
    # -------------  Publisher breakdown  -----------------------
    {'name': '[AN] AppComparator - RevenueDashboard - PublisherBreakdown - All',
     'url': '#{https}/ajax/comparator/revenue/export/?group_id=#{groupId}&'
            'breakdown=publisher&countries=US&start_date=%s&end_date=%s&chart_type=all&with_ad=f' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,Revenue dashboard', 'Breakdown,Publisher',
               'Countries,United States']},
    # =============  App compare Usage dashboard  ================
    # -------------  App breakdown  ------------------
    {'name': '[AN] AppComparator - UsageDashboard - AppBreakdown - All',
     'url': '#{https}/ajax/comparator/itc-usage/export/?group_id=#{groupId}&'
            'breakdown=product_id&countries=US&devices=iPhone&'
            'start_date=2016-06-23&end_date=2016-07-22&with_ad=f',
     'check': ['Report,ITC Usage', 'Breakdown,App', 'Countries,United States', 'Devices,iPhone',
               'Metric,All']},
    # -------------  Country breakdown  ----------------
    {'name': '[AN] AppComparator - UsageDashboard - CountryBreakdown - All',
     'url': '#{https}/ajax/comparator/itc-usage/export/?group_id=#{groupId}&'
            'breakdown=country&countries=ALL&devices=All+Devices&'
            'start_date=2016-06-23&end_date=2016-07-22&with_ad=f',
     'check': ['Report,ITC Usage', 'Breakdown,Country', 'Countries,All Countries', 'Devices,All Devices',
               'Metric,All']},
    # -------------  Platform breakdown  ---------------
    {'name': '[AN] AppComparator - UsageDashboard - PlatformBreakdown - All',
     'url': '#{https}/ajax/comparator/itc-usage/export/?group_id=#{groupId}&'
            'breakdown=platform&countries=US&devices=iPhone&'
            'start_date=2016-06-23&end_date=2016-07-22&with_ad=f',
     'check': ['Report,ITC Usage', 'Breakdown,Platform', 'Countries,United States', 'Devices,iPhone',
               'Metric,All']},
    # -------------  Publisher breakdown  ------------------
    {'name': '[AN] AppComparator - UsageDashboard - PublisherBreakdown - All',
     'url': '#{https}/ajax/comparator/itc-usage/export/?group_id=#{groupId}&'
            'breakdown=publisher&countries=ALL&devices=All+Devices&'
            'start_date=2016-06-23&end_date=2016-07-22&with_ad=f',
     'check': ['Report,ITC Usage', 'Breakdown,Publisher', 'Countries,All Countries', 'Devices,All Devices',
               'Metric,All']},
    # =============  Store Dashboard  ============================
    # -------------  ITC  -----------------------

    {'name': '[AN] itc overview all',
     'url': '#{https}/dashboard/#{itcAccountId}/overview/export/?breakdown=product'
            '&start_date=%s&end_date=%s'
            '&chart_type=all&with_ad=t' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,Overview dashboard', 'Account,#{csvItcAccount}',
               'Breakdown,App']},
    # -------------  Google Play  -----------------------

    {'name': '[ADV] gp overview all',
     'url': '#{https}/dashboard/#{gpAccountId}/overview/export/?breakdown=product'
            '&start_date=%s&end_date=%s'
            '&chart_type=all&with_ad=t' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,Overview dashboard', 'Account,#{csvGpAccount}',
               'Breakdown,App']},
    # -------------  Amazon  ----------------------- amzAccountId #{csvAmzAccount}

    {'name': '[AN] amz overview all',
     'url': '#{https}/dashboard/#{amzAccountId}/overview/export/?breakdown=product'
            '&start_date=%s&end_date=%s'
            '&chart_type=all&with_ad=t' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,Overview dashboard', 'Account,#{csvAmzAccount}',
               'Breakdown,App']},
    # -------------  Windows Phone  ----------------------- wpAccountId #{csvWpAccount}

    {'name': '[AN] windowsphone overview all',
     'url': '#{https}/dashboard/#{wpAccountId}/overview/export/?breakdown=product'
            '&start_date=%s&end_date=%s'
            '&chart_type=all&with_ad=t' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,Overview dashboard', 'Account,#{csvWpAccount}',
               'Breakdown,App']},
    # =============  Advertising Dashboard  ============================
    # -------------  Ad Revenue  -----------------------
    {'name': '[ADV] AdRevenue-Country-Ad Revenue',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=revenue&data_break_down=country'
            '&ad_account_id=#{adRevenueAccount}',
     'check': ['Report,Ad Revenue', 'Breakdown,Country', 'Ad Platform,#{adRevenuePlatform}']},
    {'name': '[ADV] AdRevenue-Country-eCPM',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=eCPM&data_break_down=country&c=US',
     'check': ['Report,eCPM', 'Breakdown,Country', 'Country,United States']},
    {'name': '[ADV] AdRevenue-Country-eCPC',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=eCPC&data_break_down=country',
     'check': ['Report,eCPC', 'Breakdown,Country']},
    {'name': '[ADV] AdRevenue-Country-Impressions',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=impressions&data_break_down=country',
     'check': ['Report,Impressions', 'Breakdown,Country']},
    {'name': '[ADV] AdRevenue-Country-Clicks',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=clicks&data_break_down=country',
     'check': ['Report,Clicks', 'Breakdown,Country']},
    {'name': '[ADV] AdRevenue-App-Ad Revenue',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=revenue&data_break_down=app',
     'check': ['Report,Ad Revenue', 'Breakdown,App']},
    {'name': '[ADV] AdRevenue-App-eCPM',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=eCPM&data_break_down=app',
     'check': ['Report,eCPM', 'Breakdown,App']},
    {'name': '[ADV] AdRevenue-App-eCPC',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=eCPC&data_break_down=app',
     'check': ['Report,eCPC', 'Breakdown,App']},
    {'name': '[ADV] AdRevenue-App-Impressions',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=impressions&data_break_down=app',
     'check': ['Report,Impressions', 'Breakdown,App']},
    {'name': '[ADV] AdRevenue-App-Clicks',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=clicks&data_break_down=app',
     'check': ['Report,Clicks', 'Breakdown,App']},
    {'name': '[ADV] AdRevenue-Ad Platform-Ad Revenue',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=revenue&data_break_down=ad_account',
     'check': ['Report,Ad Revenue', 'Breakdown,Ad Platform']},
    {'name': '[ADV] AdRevenue-Ad Platform-eCPM',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=eCPM&data_break_down=ad_account',
     'check': ['Report,eCPM', 'Breakdown,Ad Platform']},
    {'name': '[ADV] AdRevenue-Ad Platform-eCPC',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=eCPC&data_break_down=ad_account',
     'check': ['Report,eCPC', 'Breakdown,Ad Platform']},
    {'name': '[ADV] AdRevenue-Ad Platform-Impressions',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=impressions&data_break_down=ad_account',
     'check': ['Report,Impressions', 'Breakdown,Ad Platform']},
    {'name': '[ADV] AdRevenue-Ad Platform-Clicks',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=clicks&data_break_down=ad_account',
     'check': ['Report,Clicks', 'Breakdown,Ad Platform']},
    {'name': '[ADV] AdRevenue-Ad Platform-Fill Rate',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=fillrate&data_break_down=ad_account',
     'check': ['Report,Fill Rate', 'Breakdown,Ad Platform']},
    {'name': '[ADV] AdRevenue-Site-Ad Revenue',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=revenue&data_break_down=ad_item',
     'check': ['Report,Ad Revenue', 'Breakdown,Site']},
    {'name': '[ADV] AdRevenue-Site-eCPM',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=eCPM&data_break_down=ad_item',
     'check': ['Report,eCPM', 'Breakdown,Site']},
    {'name': '[ADV] AdRevenue-Site-eCPC',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=eCPC&data_break_down=ad_item',
     'check': ['Report,eCPC', 'Breakdown,Site']},
    {'name': '[ADV] AdRevenue-Site-Impressions',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=impressions&data_break_down=ad_item',
     'check': ['Report,Impressions', 'Breakdown,Site']},
    {'name': '[ADV] AdRevenue-Site-Clicks',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=clicks&data_break_down=ad_item',
     'check': ['Report,Clicks', 'Breakdown,Site']},
    {'name': '[ADV] AdRevenue-Site-Fill Rate',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=fillrate&data_break_down=ad_item',
     'check': ['Report,Fill Rate', 'Breakdown,Site']},
    {'name': '[ADV] AdRevenue-Store-Ad Revenue',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=revenue&data_break_down=store',
     'check': ['Report,Ad Revenue', 'Breakdown,Store']},
    {'name': '[ADV] AdRevenue-Store-eCPM',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=eCPM&data_break_down=store',
     'check': ['Report,eCPM', 'Breakdown,Store']},
    {'name': '[ADV] AdRevenue-Store-eCPC',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=eCPC&data_break_down=store',
     'check': ['Report,eCPC', 'Breakdown,Store']},
    {'name': '[ADV] AdRevenue-Store-Impressions',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=impressions&data_break_down=store',
     'check': ['Report,Impressions', 'Breakdown,Store']},
    {'name': '[ADV] AdRevenue-Store-Clicks',
     'url': '#{https}/ad_dashboard/ad_revenue/export/?chart_type=clicks&data_break_down=store',
     'check': ['Report,Clicks', 'Breakdown,Store']},
    # -------------  Ad Expense  -----------------------
    {'name': '[ADV] AdExpense-Country-Ad Expense',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=expense&data_break_down=country'
            '&ad_account_id=#{adRevenueAccount}',
     'check': ['Report,Ad Expense', 'Breakdown,Country', 'Ad Platform,#{adRevenuePlatform}']},
    {'name': '[ADV] AdExpense-Country-Ad Expense-SearchAds',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=expense&data_break_down=country'
            '&ad_account_id=#{adSearchAccount}',
     'check': ['Report,Ad Expense', 'Breakdown,Country', 'Ad Platform,#{adSearchPlatform}']},
    {'name': '[ADV] AdExpense-Country-Installs',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=installs&data_break_down=country&c=US',
     'check': ['Report,Installs', 'Breakdown,Country', 'Country,United States']},
    {'name': '[ADV] AdExpense-Country-eCPI',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=eCPI&data_break_down=country',
     'check': ['Report,eCPI', 'Breakdown,Country']},
    {'name': '[ADV] AdExpense-Country-eCPI-SearchAds',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=eCPI&data_break_down=country'
            '&ad_account_id=#{adSearchAccount}',
     'check': ['Report,eCPI', 'Breakdown,Country', 'Ad Platform,#{adSearchPlatform}']},
    {'name': '[ADV] AdExpense-App-Ad Expense',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=expense&data_break_down=app',
     'check': ['Report,Ad Expense', 'Breakdown,App']},
    {'name': '[ADV] AdExpense-App-Installs',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=installs&data_break_down=app',
     'check': ['Report,Installs', 'Breakdown,App']},
    {'name': '[ADV] AdExpense-App-Installs-SearchAds',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=installs&data_break_down=app'
            '&ad_account_id=#{adSearchAccount}',
     'check': ['Report,Installs', 'Breakdown,App', 'Ad Platform,#{adSearchPlatform}']},
    {'name': '[ADV] AdExpense-App-eCPI',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=eCPI&data_break_down=app',
     'check': ['Report,eCPI', 'Breakdown,App']},
    {'name': '[ADV] AdExpense-Ad Platform-Ad Expense',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=expense&data_break_down=ad_account',
     'check': ['Report,Ad Expense', 'Breakdown,Ad Platform']},
    {'name': '[ADV] AdExpense-Ad Platform-Impressions',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=impressions&data_break_down=ad_account',
     'check': ['Report,Impressions', 'Breakdown,Ad Platform']},
    {'name': '[ADV] AdExpense-Ad Platform-Impressions-SearchAds',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=impressions&data_break_down=ad_account'
            '&ad_account_id=#{adSearchAccount}',
     'check': ['Report,Impressions', 'Breakdown,Ad Platform', 'Ad Platform,#{adSearchPlatform}']},
    {'name': '[ADV] AdExpense-Ad Platform-Clicks',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=clicks&data_break_down=ad_account',
     'check': ['Report,Clicks', 'Breakdown,Ad Platform']},
    {'name': '[ADV] AdExpense-Ad Platform-Installs',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=installs&data_break_down=ad_account',
     'check': ['Report,Installs', 'Breakdown,Ad Platform']},
    {'name': '[ADV] AdExpense-Ad Platform-CTR',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=CTR&data_break_down=ad_account',
     'check': ['Report,CTR', 'Breakdown,Ad Platform']},
    {'name': '[ADV] AdExpense-Ad Platform-CTR-SearchAds',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=CTR&data_break_down=ad_account'
            '&ad_account_id=#{adSearchAccount}',
     'check': ['Report,CTR', 'Breakdown,Ad Platform', 'Ad Platform,#{adSearchPlatform}']},
    {'name': '[ADV] AdExpense-Ad Platform-CVR',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=CVR&data_break_down=ad_account',
     'check': ['Report,CVR', 'Breakdown,Ad Platform']},
    {'name': '[ADV] AdExpense-Ad Platform-eCPI',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=eCPI&data_break_down=ad_account',
     'check': ['Report,eCPI', 'Breakdown,Ad Platform']},
    {'name': '[ADV] AdExpense-Campaign-Ad Expense',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=expense&data_break_down=ad_item',
     'check': ['Report,Ad Expense', 'Breakdown,Campaign']},
    {'name': '[ADV] AdExpense-Campaign-Impressions',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=impressions&data_break_down=ad_item',
     'check': ['Report,Impressions', 'Breakdown,Campaign']},
    {'name': '[ADV] AdExpense-Campaign-Clicks',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=clicks&data_break_down=ad_item',
     'check': ['Report,Clicks', 'Breakdown,Campaign']},
    {'name': '[ADV] AdExpense-Campaign-Clicks-SearchAds',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=clicks&data_break_down=ad_item'
            '&ad_account_id=#{adSearchAccount}',
     'check': ['Report,Clicks', 'Breakdown,Campaign', 'Ad Platform,#{adSearchPlatform}']},
    {'name': '[ADV] AdExpense-Campaign-Installs',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=installs&data_break_down=ad_item',
     'check': ['Report,Installs', 'Breakdown,Campaign']},
    {'name': '[ADV] AdExpense-Campaign-CTR',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=CTR&data_break_down=ad_item',
     'check': ['Report,CTR', 'Breakdown,Campaign']},
    {'name': '[ADV] AdExpense-Campaign-CVR',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=CVR&data_break_down=ad_item',
     'check': ['Report,CVR', 'Breakdown,Campaign']},
    {'name': '[ADV] AdExpense-Campaign-CVR-SearchAds',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=CVR&data_break_down=ad_item'
            '&ad_account_id=#{adSearchAccount}',
     'check': ['Report,CVR', 'Breakdown,Campaign', 'Ad Platform,#{adSearchPlatform}']},
    {'name': '[ADV] AdExpense-Campaign-eCPI',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=eCPI&data_break_down=ad_item',
     'check': ['Report,eCPI', 'Breakdown,Campaign']},
    {'name': '[ADV] AdExpense-Store-Ad Expense',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=expense&data_break_down=store',
     'check': ['Report,Ad Expense', 'Breakdown,App Store']},
    {'name': '[ADV] AdExpense-Store-Installs',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=installs&data_break_down=store',
     'check': ['Report,Installs', 'Breakdown,App Store']},
    {'name': '[ADV] AdExpense-Store-eCPI',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=eCPI&data_break_down=store',
     'check': ['Report,eCPI', 'Breakdown,App Store']},
    {'name': '[ADV] AdExpense-Store-eCPI-SearchAds',
     'url': '#{https}/ad_dashboard/ad_expense/export/?chart_type=eCPI&data_break_down=store'
            '&ad_account_id=#{adSearchAccount}',
     'check': ['Report,eCPI', 'Breakdown,App Store', 'Ad Platform,#{adSearchPlatform}']},

    # =============  Intelligence TopChart  ============================
    # smoketesting@appannie.com has no INT topchart csv donwload permission
    # ['Intelligence-iPhone Top Publishers']
    # ['Intelligence-iPhone Top Apps']

    # =============  ITC Single App  ============================
    # -------------  Download  -----------------------
    {'name': '[AN] ITC-Download-Source',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/downloads/export/'
            '?breakdown=source&countries=US'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Source', 'Countries,United States']},
    {'name': '[AN] ITC-Download-Country-Download',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/downloads/export/?breakdown=country'
            '&chart_type=downloads'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Data,Downloads']},
    {'name': '[AN] ITC-Download-Country-Promotions',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/downloads/export/?breakdown=country'
            '&chart_type=promotions'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Data,Promotions']},
    {'name': '[AN] ITC-Download-Country-Refunds',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/downloads/export/?breakdown=country'
            '&chart_type=refunds'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Data,Refunds']},
    {'name': '[AN] ITC-Download-Country-Updates',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/downloads/export/?breakdown=country'
            '&chart_type=updates'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Data,Updates']},
    {'name': '[AN] ITC-Download-Country-All',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/downloads/export/?breakdown=country'
            '&countries=ALL'
            '&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Countries,All Countries']},
    {'name': '[AN] ITC-Download-Source-All',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/downloads/export/?breakdown=source'
            '&countries=ALL&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Source', 'Countries,All Countries']},
    {'name': '[AN] AppleTV-Download-Source',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/downloads/export/'
            '?breakdown=source&countries=US'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Source', 'Countries,United States']},
    {'name': '[AN] AppleTVDownload-Country-Download',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/downloads/export/'
            '?breakdown=country&chart_type=downloads'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Data,Downloads']},
    {'name': '[AN] AppleTV-Download-Country-Promotions',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/downloads/export/'
            '?breakdown=country&chart_type=promotions'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Data,Promotions']},
    {'name': '[AN] AppleTV-Download-Country-Refunds',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/downloads/export/'
            '?breakdown=country&chart_type=refunds&start_date=%s&end_date=%s' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Data,Refunds']},
    {'name': '[AN] AppleTV-Download-Country-Updates',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/downloads/export/'
            '?breakdown=country&chart_type=updates'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Data,Updates']},
    {'name': '[AN] AppleTV-Download-Country-All',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/downloads/export/'
            '?breakdown=country&countries=ALL&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Countries,All Countries']},
    {'name': '[AN] AppleTV-Download-Source-All',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/downloads/export/'
            '?breakdown=source&countries=ALL&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Source', 'Countries,All Countries']},
    # -------------  Revenue  -----------------------
    {'name': '[AN] ITC-Revenue-Source',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/revenue/export/?breakdown=country'
            '&chart_type=sales_revenue&c=US'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,Sales Revenue']},
    {'name': '[AN] ITC-Revenue-Country-Total Revenue',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/revenue/export/?breakdown=country'
            '&chart_type=total_revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,Total Revenue']},
    {'name': '[AN] ITC-Revenue-Country-Sales Revenue',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/revenue/export/?breakdown=country'
            '&chart_type=sales_revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,Sales Revenue']},
    {'name': '[AN] ITC-Revenue-Country-Iap Revenue',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/revenue/export/?breakdown=country'
            '&chart_type=iap_revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,IAP Revenue']},
    {'name': '[AN] ITC-Revenue-Country-Ad Revenue',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/revenue/export/?breakdown=country'
            '&chart_type=ad_revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,Ad Revenue']},
    {'name': '[AN] ITC-Revenue-Country-All',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/revenue/export/?breakdown=country'
            '&countries=ALL&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Countries,All Countries']},
    {'name': '[AN] ITC-Revenue-Source-All',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/revenue/export/?breakdown=source'
            '&countries=ALL&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date2'], env_var['end_date2']),
     'check': ['Report,App Revenue', 'Breakdown,Source', 'Countries,All Countries']},
    {'name': '[AN] AppleTV-Revenue-Source',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/revenue/export/'
            '?breakdown=country&chart_type=sales_revenue&c=US'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,Sales Revenue']},
    {'name': '[AN] AppleTV-Revenue-Country-Total Revenue',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/revenue/export/'
            '?breakdown=country&chart_type=total_revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,Total Revenue']},
    {'name': '[AN] AppleTV-Revenue-Country-Sales Revenue',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/revenue/export/'
            '?breakdown=country&chart_type=sales_revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,Sales Revenue']},
    {'name': '[AN] AppleTV-Revenue-Country-Iap Revenue',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/revenue/export/'
            '?breakdown=country&chart_type=iap_revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,IAP Revenue']},
    {'name': '[AN] AppleTV-Revenue-Country-Ad Revenue',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/revenue/export/'
            '?breakdown=country&chart_type=ad_revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,Ad Revenue']},
    {'name': '[AN] AppleTV-Revenue-Country-All',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/revenue/export/'
            '?breakdown=country&countries=ALL&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Countries,All Countries']},
    {'name': '[AN] AppleTV-Revenue-Source-All',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/revenue/export/'
            '?breakdown=source&countries=ALL&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Source', 'Countries,All Countries']},
    # -------------  IAP  -----------------------
    {'name': '[AN] ITC-IAP-IAP Items-IAP Revenue',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/iap/export/'
            '?breakdown=ipp&chart_type=revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Data,IAP Revenue']},
    {'name': '[AN] ITC-IAP-IAP Items-IAP Units',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/iap/export/'
            '?breakdown=ipp&chart_type=units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Data,IAP Units']},
    {'name': '[AN] ITC-IAP-IAP Items-Promotions',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/iap/export/'
            '?breakdown=ipp&chart_type=promotion_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Data,Promotions']},
    {'name': '[AN] ITC-IAP-IAP Items-Refunds',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/iap/export/'
            '?breakdown=ipp&chart_type=refund_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Data,Refunds']},
    {'name': '[AN] ITC-IAP-IAP Items-New Subscriptions',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/iap/export/'
            '?breakdown=ipp&chart_type=subscription_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Data,New Subscriptions']},
    {'name': '[AN] ITC-IAP-IAP Items-Renewal Units',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/iap/export/'
            '?breakdown=ipp&chart_type=renewal_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Data,Subscription Renewals']},
    {'name': '[AN] ITC-IAP-Country-IAP Revenue',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/iap/export/'
            '?breakdown=country&chart_type=revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Data,IAP Revenue']},
    {'name': '[AN] ITC-IAP-Country-IAP Units',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/iap/export/'
            '?breakdown=country&chart_type=units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Data,IAP Units']},
    {'name': '[AN] ITC-IAP-Country-Promotions',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/iap/export/'
            '?breakdown=country&chart_type=promotion_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Data,Promotions']},
    {'name': '[AN] ITC-IAP-Country-Refunds',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/iap/export/'
            '?breakdown=country&chart_type=refund_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Data,Refunds']},
    {'name': '[AN] ITC-IAP-Country-New Subscriptions',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/iap/export/'
            '?breakdown=country&chart_type=subscription_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Data,New Subscriptions']},
    {'name': '[AN] ITC-IAP-Country-Subscription Renewals',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/iap/export/'
            '?breakdown=country&chart_type=renewal_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Data,Subscription Renewals']},
    {'name': '[AN] ITC-IAP-Type-IAP Revenue',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/iap/export/?breakdown=type&chart_type=revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Type', 'Data,IAP Revenue']},
    {'name': '[AN] ITC-IAP-Type-IAP Units',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/iap/export/?breakdown=type&chart_type=units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Type', 'Data,IAP Units']},
    {'name': '[AN] ITC-IAP-Type-Promotions',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/iap/export/'
            '?breakdown=type&chart_type=promotion_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Type', 'Data,Promotions']},
    {'name': '[AN] ITC-IAP-Type-Refunds',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/iap/export/'
            '?breakdown=type&chart_type=refund_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Type', 'Data,Refunds']},
    {'name': '[AN] ITC-IAP-IAP Items-All',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/iap/export/?breakdown=ipp&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items',
               'IAP Items,Date,IAP Revenue,IAP Units,Promotions,Refunds,New Subscriptions,Subscription Renewals']},
    {'name': '[AN] ITC-IAP-Country-All',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/iap/export/?breakdown=country&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country',
               'Country,Date,IAP Revenue,IAP Units,Promotions,Refunds,New Subscriptions,Subscription Renewals']},
    {'name': '[AN] ITC-IAP-Type-All',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/iap/export/?breakdown=type&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Type',
               'Type,Date,IAP Revenue,IAP Units,Promotions,Refunds']},
    {'name': '[AN] AppleTV-IAP-IAP Items-IAP Revenue',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/iap/export/'
            '?breakdown=ipp&chart_type=revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Data,IAP Revenue']},
    {'name': '[AN] AppleTV-IAP-IAP Items-IAP Units',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/iap/export/'
            '?breakdown=ipp&chart_type=units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Data,IAP Units']},
    {'name': '[AN] AppleTV-IAP-IAP Items-Promotions',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/iap/export/'
            '?breakdown=ipp&chart_type=promotion_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Data,Promotions']},
    {'name': '[AN] AppleTV-IAP-IAP Items-Refunds',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/iap/export/'
            '?breakdown=ipp&chart_type=refund_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Data,Refunds']},
    {'name': '[AN] AppleTV-IAP-IAP Items-New Subscriptions',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/iap/export/'
            '?breakdown=ipp&chart_type=subscription_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Data,New Subscriptions']},
    {'name': '[AN] AppleTV-IAP-IAP Items-Renewal Units',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/iap/export/'
            '?breakdown=ipp&chart_type=renewal_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Data,Subscription Renewals']},
    {'name': '[AN] AppleTV-IAP-Country-IAP Revenue',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/iap/export/'
            '?breakdown=country&chart_type=revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Data,IAP Revenue']},
    {'name': '[AN] AppleTV-IAP-Country-IAP Units',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/iap/export/'
            '?breakdown=country&chart_type=units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Data,IAP Units']},
    {'name': '[AN] AppleTV-IAP-Country-Promotions',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/iap/export/'
            '?breakdown=country&chart_type=promotion_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Data,Promotions']},
    {'name': '[AN] AppleTV-IAP-Country-Refunds',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/iap/export/'
            '?breakdown=country&chart_type=refund_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Data,Refunds']},
    {'name': '[AN] AppleTV-IAP-Country-New Subscriptions',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/iap/export/'
            '?breakdown=country&chart_type=subscription_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Data,New Subscriptions']},
    {'name': '[AN] AppleTV-IAP-Country-Subscription Renewals',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/iap/export/'
            '?breakdown=country&chart_type=renewal_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Data,Subscription Renewals']},
    {'name': '[AN] AppleTV-IAP-Type-IAP Revenue',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/iap/export/'
            '?breakdown=type&chart_type=revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Type', 'Data,IAP Revenue']},
    {'name': '[AN] AppleTV-IAP-Type-IAP Units',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/iap/export/?breakdown=type&chart_type=units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Type', 'Data,IAP Units']},
    {'name': '[AN] AppleTV-IAP-Type-Promotions',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/iap/export/'
            '?breakdown=type&chart_type=promotion_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Type', 'Data,Promotions']},
    {'name': '[AN] AppleTV-IAP-Type-Refunds',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/iap/export/'
            '?breakdown=type&chart_type=refund_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Type', 'Data,Refunds']},
    {'name': '[AN] AppleTV-IAP-IAP Items-All',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/iap/export/?breakdown=ipp&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items',
               'IAP Items,Date,IAP Revenue,IAP Units,Promotions,Refunds,New Subscriptions,Subscription Renewals']},
    {'name': '[AN] AppleTV-IAP-Country-All',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/iap/export/?breakdown=country&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country',
               'Country,Date,IAP Revenue,IAP Units,Promotions,Refunds,New Subscriptions,Subscription Renewals']},
    {'name': '[AN] AppleTV-IAP-Type-All',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/iap/export/?breakdown=type&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Type',
               'Type,Date,IAP Revenue,IAP Units,Promotions,Refunds']},
    # -----------ITC Analytics Store Views -------------
    {'name': '[AN] ITCAnalytics-StoreViews-Country-AppStoreViews',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/storeviews/export/?breakdown=country'
            '&chart_type=app_store_views'
            '&countries=ALL&devices=All+Devices&start_date=2016-03-29&end_date=2016-04-27',
     'check': ['Report,Store Views', 'Breakdown,Country', 'Countries,All Countries', 'Devices,All Devices',
               'Metrics,Store Page Views']},
    {'name': '[AN] ITCAnalytics-StoreViews-Country-AppStoreViews-US-iPhone',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/storeviews/export/?breakdown=country'
            '&chart_type=app_store_views'
            '&countries=US&devices=iPhone&start_date=2016-03-29&end_date=2016-04-27',
     'check': ['Report,Store Views', 'Breakdown,Country', 'Countries,United States', 'Devices,iPhone',
               'Metrics,Store Page Views']},
    {'name': '[AN] ITCAnalytics-StoreViews-Country-Downloads',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/storeviews/export/?breakdown=country'
            '&chart_type=downloads'
            '&countries=ALL&devices=All+Devices&start_date=2016-03-29&end_date=2016-04-27',
     'check': ['Report,Store Views', 'Breakdown,Country', 'Countries,All Countries', 'Devices,All Devices',
               'Metrics,Downloads']},
    {'name': '[AN] ITCAnalytics-StoreViews-Country-ConversionRate',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/storeviews/export/?breakdown=country'
            '&chart_type=downloads_per_views&countries=ALL&devices=All+Devices'
            '&start_date=2016-03-29&end_date=2016-04-27',
     'check': ['Report,Store Views', 'Breakdown,Country', 'Countries,All Countries', 'Devices,All Devices',
               'Metrics,Conversion Rate']},
    {'name': '[AN] ITCAnalytics-StoreViews-Country-All',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/storeviews/export/?breakdown=country'
            '&chart_type=all'
            '&countries=ALL&devices=All+Devices&start_date=2016-03-29&end_date=2016-04-27',
     'check': ['Report,Store Views', 'Breakdown,Country', 'Countries,All Countries', 'Devices,All Devices',
               'Metrics,All']},
    {'name': '[AN] ITCAnalytics-StoreViews-Country-All-US',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/storeviews/export/?breakdown=country'
            '&chart_type=all'
            '&countries=US&devices=All+Devices&start_date=2016-03-29&end_date=2016-04-27',
     'check': ['Report,Store Views', 'Breakdown,Country', 'Countries,United States', 'Devices,All Devices',
               'Metrics,All']},
    {'name': '[AN] ITCAnalytics-StoreViews-Country-All-iPhone',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/storeviews/export/?breakdown=country'
            '&chart_type=all'
            '&countries=ALL&devices=iPhone&start_date=2016-03-29&end_date=2016-04-27',
     'check': ['Report,Store Views', 'Breakdown,Country', 'Countries,All Countries', 'Devices,iPhone',
               'Metrics,All']},
    {'name': '[AN] ITCAnalytics-StoreViews-Device-AppStoreViews-US',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/storeviews/export/?breakdown=device'
            '&chart_type=app_store_views'
            '&countries=US&devices=All+Devices&start_date=2016-03-29&end_date=2016-04-27',
     'check': ['Report,Store Views', 'Breakdown,Device', 'Countries,United States', 'Devices,All Devices',
               'Metrics,Store Page Views']},
    {'name': '[AN] ITCAnalytics-StoreViews-Device-AppStoreViews-US-iPhone',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/storeviews/export/?breakdown=device'
            '&chart_type=app_store_views'
            '&countries=US&devices=iPhone&start_date=2016-03-29&end_date=2016-04-27',
     'check': ['Report,Store Views', 'Breakdown,Device', 'Countries,United States', 'Devices,iPhone',
               'Metrics,Store Page Views']},
    {'name': '[AN] ITCAnalytics-StoreViews-Device-AppStoreViews',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/storeviews/export/?breakdown=device'
            '&chart_type=app_store_views'
            '&countries=ALL&devices=All+Devices&start_date=2016-03-29&end_date=2016-04-27',
     'check': ['Report,Store Views', 'Breakdown,Device', 'Countries,All Countries', 'Devices,All Devices',
               'Metrics,Store Page Views']},
    {'name': '[AN] ITCAnalytics-StoreViews-Device-Downloads-iPhone',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/storeviews/export/?breakdown=device'
            '&chart_type=downloads'
            '&countries=ALL&devices=iPhone&start_date=2016-03-29&end_date=2016-04-27',
     'check': ['Report,Store Views', 'Breakdown,Device', 'Countries,All Countries', 'Devices,iPhone',
               'Metrics,Downloads']},
    {'name': '[AN] ITCAnalytics-StoreViews-Device-ConversionRate-US-iPhone',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/storeviews/export/?breakdown=device'
            '&chart_type=downloads_per_views'
            '&countries=US&devices=iPhone&start_date=2016-03-29&end_date=2016-04-27',
     'check': ['Report,Store Views', 'Breakdown,Device', 'Countries,United States', 'Devices,iPhone',
               'Metrics,Conversion Rate']},
    {'name': '[AN] ITCAnalytics-StoreViews-Device-All',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/storeviews/export/?breakdown=device'
            '&chart_type=all'
            '&countries=ALL&devices=All+Devices&start_date=2016-03-29&end_date=2016-04-27',
     'check': ['Report,Store Views', 'Breakdown,Device', 'Countries,All Countries', 'Devices,All Devices',
               'Metrics,All']},
    {'name': '[AN] ITCAnalytics-StoreViews-Device-All-US-iPhone',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/storeviews/export/?breakdown=device'
            '&chart_type=all'
            '&countries=US&devices=iPhone&start_date=2016-03-29&end_date=2016-04-27',
     'check': ['Report,Store Views', 'Breakdown,Device', 'Countries,United States', 'Devices,iPhone',
               'Metrics,All']},

    # ----------- ITC Analytics Paying Users -------------
    {'name': '[AN] ITCAnalytics-PayingUsers-Country-PayingUsers',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/payingusers/export/?breakdown=country'
            '&chart_type=paying_users'
            '&countries=ALL&devices=All+Devices&start_date=2016-05-06&end_date=2016-06-04',
     'check': ['Report,Paying Users', 'Breakdown,Country', 'Countries,All Countries', 'Devices,All Devices',
               'Metrics,Paying Users']},
    {'name': '[AN] ITCAnalytics-PayingUsers-Country-DailyActiveDevices',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/payingusers/export/?breakdown=country'
            '&chart_type=active_devices'
            '&countries=ALL&devices=All+Devices&start_date=2016-05-06&end_date=2016-06-04',
     'check': ['Report,Paying Users', 'Breakdown,Country', 'Countries,All Countries', 'Devices,All Devices',
               'Metrics,Daily Active Devices']},
    {'name': '[AN] ITCAnalytics-PayingUsers-Country-PayingUsersPerActiveDevices',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/payingusers/export/?breakdown=country'
            '&chart_type=users_per_devices'
            '&countries=ALL&devices=All+Devices&start_date=2016-05-06&end_date=2016-06-04',
     'check': ['Report,Paying Users', 'Breakdown,Country', 'Countries,All Countries', 'Devices,All Devices',
               'Metrics,Paying Users/Active Devices']},
    {'name': '[AN] ITCAnalytics-PayingUsers-Country-All',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/payingusers/export/?breakdown=country'
            '&chart_type=all'
            '&countries=ALL&devices=All+Devices&start_date=2016-05-06&end_date=2016-06-04',
     'check': ['Report,Paying Users', 'Breakdown,Country', 'Countries,All Countries', 'Devices,All Devices',
               'Metrics,All']},
    {'name': '[AN] ITCAnalytics-PayingUsers-Country-All-US',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/payingusers/export/?breakdown=country'
            '&chart_type=all'
            '&countries=US&devices=All+Devices&start_date=2016-05-06&end_date=2016-06-04',
     'check': ['Report,Paying Users', 'Breakdown,Country', 'Countries,United States', 'Devices,All Devices',
               'Metrics,All']},
    {'name': '[AN] ITCAnalytics-PayingUsers-Country-All-iPhone',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/payingusers/export/?breakdown=country'
            '&chart_type=all'
            '&countries=ALL&devices=iPhone&start_date=2016-05-06&end_date=2016-06-04',
     'check': ['Report,Paying Users', 'Breakdown,Country', 'Countries,All Countries', 'Devices,iPhone',
               'Metrics,All']},
    {'name': '[AN] ITCAnalytics-PayingUsers-Device-PayingUsers-US',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/payingusers/export/?breakdown=device'
            '&chart_type=paying_users'
            '&countries=US&devices=All+Devices&start_date=2016-05-06&end_date=2016-06-04',
     'check': ['Report,Paying Users', 'Breakdown,Device', 'Countries,United States', 'Devices,All Devices',
               'Metrics,Paying Users']},
    {'name': '[AN] ITCAnalytics-PayingUsers-Device-DailyActiveDevices-iPhone',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/payingusers/export/?breakdown=device'
            '&chart_type=active_devices'
            '&countries=ALL&devices=iPhone&start_date=2016-05-06&end_date=2016-06-04',
     'check': ['Report,Paying Users', 'Breakdown,Device', 'Countries,All Countries', 'Devices,iPhone',
               'Metrics,Daily Active Devices']},
    {'name': '[AN] ITCAnalytics-PayingUsers-Device-PayingUsersPerActiveDevices-US-iPhone',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/payingusers/export/?breakdown=device'
            '&chart_type=users_per_devices'
            '&countries=US&devices=iPhone&start_date=2016-05-06&end_date=2016-06-04',
     'check': ['Report,Paying Users', 'Breakdown,Device', 'Countries,United States', 'Devices,iPhone',
               'Metrics,Paying Users/Active Devices']},
    {'name': '[AN] ITCAnalytics-PayingUsers-Device-All',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/payingusers/export/?breakdown=device'
            '&chart_type=all'
            '&countries=ALL&devices=All+Devices&start_date=2016-05-06&end_date=2016-06-04',
     'check': ['Report,Paying Users', 'Breakdown,Device', 'Countries,All Countries', 'Devices,All Devices',
               'Metrics,All']},
    {'name': '[AN] ITCAnalytics-PayingUsers-Device-All-US-iPhone',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/payingusers/export/?breakdown=device'
            '&chart_type=all'
            '&countries=US&devices=iPhone&start_date=2016-05-06&end_date=2016-06-04',
     'check': ['Report,Paying Users', 'Breakdown,Device', 'Countries,United States', 'Devices,iPhone',
               'Metrics,All']},
    # ----------- ITC Analytics Usage -------------
    {'name': '[AN] ITCAnalytics-Usage-Country-DAD',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/itc-usage/export/?breakdown=country'
            '&chart_type=active_devices'
            '&countries=ALL&devices=All+Devices&start_date=2016-04-30&end_date=2016-05-29',
     'check': ['Report,Usage', 'Breakdown,Country', 'Countries,All Countries', 'Devices,All Devices',
               'Metrics,DAD']},
    {'name': '[AN] ITCAnalytics-Usage-Country-30DayActive',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/itc-usage/export/?breakdown=country'
            '&chart_type=active_last_30_days'
            '&countries=ALL&devices=All+Devices&start_date=2016-04-30&end_date=2016-05-29',
     'check': ['Report,Usage', 'Breakdown,Country', 'Countries,All Countries', 'Devices,All Devices',
               'Metrics,30 Day Active']},
    {'name': '[AN] ITCAnalytics-Usage-Country-DADPer30DayActive',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/itc-usage/export/?breakdown=country'
            '&chart_type=dad_per_30d_active'
            '&countries=ALL&devices=All+Devices&start_date=2016-04-30&end_date=2016-05-29',
     'check': ['Report,Usage', 'Breakdown,Country', 'Countries,All Countries', 'Devices,All Devices',
               'Metrics,DAD / 30 Day Active']},
    {'name': '[AN] ITCAnalytics-Usage-Country-Sessions',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/itc-usage/export/?breakdown=country'
            '&chart_type=sessions'
            '&countries=ALL&devices=All+Devices&start_date=2016-04-30&end_date=2016-05-29',
     'check': ['Report,Usage', 'Breakdown,Country', 'Countries,All Countries', 'Devices,All Devices',
               'Metrics,Total Sessions']},
    {'name': '[AN] ITCAnalytics-Usage-Country-SessionsPerDevicePerDay',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/itc-usage/export/?breakdown=country'
            '&chart_type=sessions_per_device_per_day'
            '&countries=ALL&devices=All+Devices&start_date=2016-04-30&end_date=2016-05-29',
     'check': ['Report,Usage', 'Breakdown,Country', 'Countries,All Countries', 'Devices,All Devices',
               'Metrics,Sessions / Device / Day']},
    {'name': '[AN] ITCAnalytics-Usage-Country-All',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/itc-usage/export/?breakdown=country'
            '&chart_type=all'
            '&countries=ALL&devices=All+Devices&start_date=2016-04-30&end_date=2016-05-29',
     'check': ['Report,Usage', 'Breakdown,Country', 'Countries,All Countries', 'Devices,All Devices',
               'Metrics,All']},
    {'name': '[AN] ITCAnalytics-Usage-Country-All-US-iPhone',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/itc-usage/export/?breakdown=country'
            '&chart_type=all'
            '&countries=US&devices=iPhone&start_date=2016-04-30&end_date=2016-05-29',
     'check': ['Report,Usage', 'Breakdown,Country', 'Countries,United States', 'Devices,iPhone',
               'Metrics,All']},
    {'name': '[AN] ITCAnalytics-Usage-Device-DAD-US-iPhone',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/itc-usage/export/?breakdown=device'
            '&chart_type=active_devices'
            '&countries=US&devices=iPhone&start_date=2016-04-30&end_date=2016-05-29',
     'check': ['Report,Usage', 'Breakdown,Device', 'Countries,United States', 'Devices,iPhone',
               'Metrics,DAD']},
    {'name': '[AN] ITCAnalytics-Usage-Device-30DayActive-US-iPhone',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/itc-usage/export/?breakdown=device'
            '&chart_type=active_last_30_days'
            '&countries=US&devices=iPhone&start_date=2016-04-30&end_date=2016-05-29',
     'check': ['Report,Usage', 'Breakdown,Device', 'Countries,United States', 'Devices,iPhone',
               'Metrics,30 Day Active']},
    {'name': '[AN] ITCAnalytics-Usage-Device-DADPer30DayActive-US-iPhone',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/itc-usage/export/?breakdown=device'
            '&chart_type=dad_per_30d_active'
            '&countries=US&devices=iPhone&start_date=2016-04-30&end_date=2016-05-29',
     'check': ['Report,Usage', 'Breakdown,Device', 'Countries,United States', 'Devices,iPhone',
               'Metrics,DAD / 30 Day Active']},
    {'name': '[AN] ITCAnalytics-Usage-Device-Sessions-US-iPhone',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/itc-usage/export/?breakdown=device'
            '&chart_type=sessions'
            '&countries=US&devices=iPhone&start_date=2016-04-30&end_date=2016-05-29',
     'check': ['Report,Usage', 'Breakdown,Device', 'Countries,United States', 'Devices,iPhone',
               'Metrics,Total Sessions']},
    {'name': '[AN] ITCAnalytics-Usage-Device-SessionsPerDevicePerDay-US-iPhone',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/itc-usage/export/?breakdown=device'
            '&chart_type=sessions_per_device_per_day'
            '&countries=US&devices=iPhone&start_date=2016-04-30&end_date=2016-05-29',
     'check': ['Report,Usage', 'Breakdown,Device', 'Countries,United States', 'Devices,iPhone',
               'Metrics,Sessions / Device / Day']},
    {'name': '[AN] ITCAnalytics-Usage-Device-All',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/itc-usage/export/?breakdown=device'
            '&chart_type=all'
            '&countries=ALL&devices=All+Devices&start_date=2016-04-30&end_date=2016-05-29',
     'check': ['Report,Usage', 'Breakdown,Device', 'Countries,All Countries', 'Devices,All Devices',
               'Metrics,All']},
    {'name': '[AN] ITCAnalytics-Usage-Device-All-US-iPhone',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/itc-usage/export/?breakdown=device'
            '&chart_type=all'
            '&countries=US&devices=iPhone&start_date=2016-04-30&end_date=2016-05-29',
     'check': ['Report,Usage', 'Breakdown,Device', 'Countries,United States', 'Devices,iPhone',
               'Metrics,All']},
    # -------------  AD Revenue  -----------------------
    {'name': '[ADV] ITCAdRevenue-Country-Ad Revenue',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/ad_revenue/export/?chart_type=revenue'
            '&data_break_down=country'
            '&start_date=2016-01-01&end_date=2016-01-02',
     'check': ['Report,Ad Revenue', 'Breakdown,Country']},
    {'name': '[ADV] ITCAdRevenue-Ad Platform-Ad Revenue',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/ad_revenue/export/?chart_type=revenue'
            '&data_break_down=ad_account'
            '&start_date=2016-01-01&end_date=2016-01-02',
     'check': ['Report,Ad Revenue', 'Breakdown,Ad Platform']},
    {'name': '[ADV] ITCAdRevenue-Site-Ad Revenue',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/ad_revenue/export/?chart_type=revenue&'
            'data_break_down=ad_item'
            '&start_date=2016-01-01&end_date=2016-01-02',
     'check': ['Report,Ad Revenue', 'Breakdown,Site']},
    # -------------  AD Expense  -----------------------
    {'name': '[ADV] ITCAdExpense-Country-Ad Expense',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/ad_expense/export/?chart_type=expense'
            '&data_break_down=country'
            '&start_date=2016-01-01&end_date=2016-01-02',
     'check': ['Report,Ad Expense', 'Breakdown,Country']},
    {'name': '[ADV] ITCAdExpense-Country-Ad Expense-SearchAds',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp4}/ad_expense/export/?chart_type=expense'
            '&data_break_down=country'
            '&start_date=2016-12-09&end_date=2016-12-10',
     'check': ['Report,Ad Expense', 'Breakdown,Country']},
    {'name': '[ADV] ITCAdExpense-Ad Platform-Ad Expense',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/ad_expense/export/?chart_type=expense'
            '&data_break_down=ad_account'
            '&start_date=2016-01-01&end_date=2016-01-02',
     'check': ['Report,Ad Expense', 'Breakdown,Ad Platform']},
    {'name': '[ADV] ITCAdExpense-Ad Platform-Ad Expense-SearchAds',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp4}/ad_expense/export/?chart_type=expense'
            '&data_break_down=ad_account'
            '&start_date=2016-12-09&end_date=2016-12-10',
     'check': ['Report,Ad Expense', 'Breakdown,Ad Platform']},
    {'name': '[ADV] ITCAdExpense-Campaign-Ad Expense',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/ad_expense/export/?chart_type=expense'
            '&data_break_down=ad_item'
            '&start_date=2016-01-01&end_date=2016-01-02',
     'check': ['Report,Ad Expense', 'Breakdown,Campaign']},
    {'name': '[ADV] ITCAdExpense-Campaign-Ad Expense-SearchAds',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp4}/ad_expense/export/?chart_type=expense'
            '&data_break_down=ad_item'
            '&start_date=2016-12-09&end_date=2016-12-10',
     'check': ['Report,Ad Expense', 'Breakdown,Campaign']},
    # =============  GP Single App  ============================
    # -------------  Download  -----------------------
    {'name': '[AN] GP-Download-Source',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/downloads/export/?breakdown=source&countries=US'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Source', 'Countries,United States']},
    {'name': '[AN] GP-Download-Country-Download',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/downloads/export/?breakdown=country'
            '&chart_type=downloads&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Data,Downloads']},
    {'name': '[AN] GP-Download-Country-Refunds',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/downloads/export/?breakdown=country'
            '&chart_type=refunds&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Data,Refunds']},
    {'name': '[AN] GP-Download-Country-All',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/downloads/export/?breakdown=country'
            '&chart_type=all&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Country,Date,Downloads,Refunds']},
    {'name': '[AN] GP-Download-Source-All',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/downloads/export/?breakdown=source'
            '&chart_type=all&start_date=%s&end_date=%s' % (env_var['start_date6'], env_var['end_date6']),
     'check': ['Report,App Downloads', 'Breakdown,Source', 'Date,Downloads']},
    # -------------  Revenue  -----------------------
    {'name': '[AN] GP-Revenue-Source',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/revenue/export/?breakdown=country'
            '&chart_type=sales_revenue&countries=US&start_date=%s&end_date=%s' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,Sales Revenue']},
    {'name': '[AN] GP-Revenue-Country-Total Revenue',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/revenue/export/?breakdown=country'
            '&chart_type=total_revenue&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,Total Revenue']},
    {'name': '[AN] GP-Revenue-Country-Sales Revenue',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/revenue/export/?breakdown=country'
            '&chart_type=sales_revenue&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,Sales Revenue']},
    {'name': '[AN] GP-Revenue-Country-Iap Revenue',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/revenue/export/?breakdown=country'
            '&chart_type=iap_revenue&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,IAP Revenue']},
    {'name': '[ADV] GP-Revenue-Country-Ad Revenue',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/revenue/export/?breakdown=country'
            '&chart_type=ad_revenue&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,Ad Revenue']},
    {'name': '[AN] GP-Revenue-Country-All',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/revenue/export/?breakdown=country&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country',
               'Country,Date,Total Revenue,Sales Revenue,IAP Revenue,Ad Revenue']},
    {'name': '[AN] GP-Revenue-Source-All',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/revenue/export/?breakdown=source&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date6'], env_var['end_date6']),
     'check': ['Report,App Revenue', 'Breakdown,Source', '#{gpCsvColumns}']},
    # -------------  IAP  -----------------------
    {'name': '[AN] GP-IAP-IAP Items-IAP Revenue',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/iap/export/?breakdown=ipp&chart_type=revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Data,IAP Revenue']},
    {'name': '[AN] GP-IAP-IAP Items-IAP Units',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/iap/export/?breakdown=ipp&chart_type=units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Data,IAP Units']},
    {'name': '[AN] GP-IAP-IAP Items-Refunds',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/iap/export/'
            '?breakdown=ipp&chart_type=refund_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Data,Refunds']},
    {'name': '[AN] GP-IAP-Country-IAP Revenue',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/iap/export/?breakdown=country&chart_type=revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Data,IAP Revenue']},
    {'name': '[AN] GP-IAP-Country-IAP Units',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/iap/export/?breakdown=country&chart_type=units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Data,IAP Units']},
    {'name': '[AN] GP-IAP-Country-Refunds',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/iap/export/'
            '?breakdown=country&chart_type=refund_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Data,Refunds']},
    {'name': '[AN] GP-IAP-Country-All',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/iap/export/?breakdown=country&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Country,Date,IAP Revenue,IAP Units,Refunds']},
    {'name': '[ADV] GP-IAP-IAP Items-All',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/iap/export/?breakdown=ipp&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'IAP Items,Date,IAP Revenue,IAP Units,Refunds']},
    # -------------  Store Views  ----------------------
    {'name': '[AN] GP-StoreViews-All',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/storeviews/export/?countries=ALL&chart_type=all'
            '&start_date=2016-07-26&end_date=2016-08-25',
     'check': ['Report,Store Views', 'Breakdown,Country', 'Countries,All Countries', 'Metrics,All']},
    {'name': '[AN] GP-StoreViews-All-US',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/storeviews/export/?countries=US&chart_type=all'
            '&start_date=2016-07-26&end_date=2016-08-25',
     'check': ['Report,Store Views', 'Breakdown,Country', 'Countries,United States', 'Metrics,All']},
    # -------------  AD Revenue  -----------------------
    {'name': '[ADV] GPAdRevenue-Country-Ad Revenue',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/ad_revenue/export/?'
            'chart_type=revenue&data_break_down=country&start_date=2016-01-01&end_date=2016-01-02',
     'check': ['Report,Ad Revenue', 'Breakdown,Country']},
    {'name': '[ADV] GPAdRevenue-Ad Platform-Ad Revenue',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/ad_revenue/export/?chart_type=revenue'
            '&data_break_down=ad_account&start_date=2016-01-01&end_date=2016-01-02',
     'check': ['Report,Ad Revenue', 'Breakdown,Ad Platform']},
    {'name': '[ADV] GPAdRevenue-Site-Ad Revenue',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/ad_revenue/export/?chart_type=revenue'
            '&data_break_down=ad_item&start_date=2016-01-01&end_date=2016-01-02',
     'check': ['Report,Ad Revenue', 'Breakdown,Site']},
    # -------------  AD Expense  -----------------------
    {'name': '[ADV] GPAdExpense-Country-Ad Expense',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/ad_expense/export/?chart_type=expense'
            '&data_break_down=country&start_date=2016-01-01&end_date=2016-01-02',
     'check': ['Report,Ad Expense', 'Breakdown,Country']},
    {'name': '[ADV] GPAdExpense-Ad Platform-Ad Expense',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/ad_expense/export/?chart_type=expense'
            '&data_break_down=ad_account&start_date=2016-01-01&end_date=2016-01-02',
     'check': ['Report,Ad Expense', 'Breakdown,Ad Platform']},
    {'name': '[ADV] GPAdExpense-Campaign-Ad Expense',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/ad_expense/export/?chart_type=expense'
            '&data_break_down=ad_item&start_date=2016-01-01&end_date=2016-01-02',
     'check': ['Report,Ad Expense', 'Breakdown,Campaign']},
    # =============  AMZ Single App  ============================
    # -------------  Download  -----------------------
    {'name': '[AN] AMZ-Download-Source',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/downloads/export/'
            '?breakdown=source&countries=US'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Source', 'Countries,United States']},
    {'name': '[AN] AMZ-Download-Country-Download',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/downloads/export/?breakdown=country'
            '&chart_type=downloads&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Data,Downloads']},
    {'name': '[AN] AMZ-Download-Country-Refunds',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/downloads/export/?breakdown=country'
            '&chart_type=refunds&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Data,Refunds']},
    {'name': '[AN] AMZ-Download-Country-All',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/downloads/export/?breakdown=country'
            '&chart_type=all&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Country,Date,Downloads,Refunds']},
    {'name': '[AN] AMZ-Download-Source-All',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/downloads/export/?breakdown=source'
            '&chart_type=all&start_date=%s&end_date=%s' % (env_var['start_date6'], env_var['end_date6']),
     'check': ['Report,App Downloads', 'Breakdown,Source', 'Date,Downloads']},
    # -------------  Revenue  -----------------------
    {'name': '[AN] AMZ-Revenue-Source',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/revenue/export/?breakdown=country'
            '&chart_type=sales_revenue&c=US&start_date=%s&end_date=%s' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,Sales Revenue']},
    {'name': '[AN] AMZ-Revenue-Country-Total Revenue',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/revenue/export/'
            '?breakdown=country&chart_type=total_revenue&start_date=%s&end_date=%s' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,Total Revenue']},
    {'name': '[AN] AMZ-Revenue-Country-Sales Revenue',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/revenue/export/'
            '?breakdown=country&chart_type=sales_revenue&start_date=%s&end_date=%s' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,Sales Revenue']},
    {'name': '[AN] AMZ-Revenue-Country-Iap Revenue',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/revenue/export/'
            '?breakdown=country&chart_type=iap_revenue&start_date=%s&end_date=%s' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,IAP Revenue']},
    {'name': '[ADV] AMZ-Revenue-Country-Ad Revenue',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/revenue/export/'
            '?breakdown=country&chart_type=ad_revenue&start_date=%s&end_date=%s' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,Ad Revenue']},
    {'name': '[AN] AMZ-Revenue-Country-All',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/revenue/export/'
            '?breakdown=country&chart_type=all&start_date=%s&end_date=%s' % (
                env_var['start_date2'], env_var['end_date2']),
     'check': ['Report,App Revenue', 'Breakdown,Country',
               'Country,Date,Total Revenue,Sales Revenue,IAP Revenue,Ad Revenue']},
    {'name': '[AN] AMZ-Revenue-Source-All',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/revenue/export/'
            '?breakdown=source&chart_type=all&start_date=%s&end_date=%s' % (
                env_var['start_date6'], env_var['end_date6']),
     'check': ['Report,App Revenue', 'Breakdown,Source', '#{amzCsvColumns}']},
    # -------------  IAP  -----------------------
    {'name': '[AN] AMZ-IAP-IAP Items-IAP Revenue',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/iap/export/?breakdown=ipp&chart_type=revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Data,IAP Revenue']},
    {'name': '[AN] AMZ-IAP-IAP Items-IAP Units',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/iap/export/?breakdown=ipp&chart_type=units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Data,IAP Units']},
    {'name': '[AN] AMZ-IAP-IAP Items-Refunds',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/iap/export/'
            '?breakdown=ipp&chart_type=refund_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Data,Refunds']},
    {'name': '[AN] AMZ-IAP-Country-IAP Revenue',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/iap/export/'
            '?breakdown=country&chart_type=revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Data,IAP Revenue']},
    {'name': '[AN] AMZ-IAP-Country-IAP Units',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/iap/export/?breakdown=country&chart_type=units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Data,IAP Units']},
    {'name': '[AN] AMZ-IAP-Country-Refunds',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/iap/export/'
            '?breakdown=country&chart_type=refund_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Data,Refunds']},
    {'name': '[AN] AMZ-IAP-IAP Items-All',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/iap/export/?breakdown=ipp&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'IAP Items,Date,IAP Revenue,IAP Units,Refunds']},
    {'name': '[AN] AMZ-IAP-Country-All',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/iap/export/?breakdown=country&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Country,Date,IAP Revenue,IAP Units,Refunds']},
    # -------------  AD Revenue  -----------------------
    {'name': '[ADV] AMZAdRevenue-Country-Ad Revenue',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/ad_revenue/export/?chart_type=revenue'
            '&data_break_down=country&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,Ad Revenue', 'Breakdown,Country']},
    {'name': '[ADV] AMZAdRevenue-Ad Platform-Ad Revenue',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/ad_revenue/export/?chart_type=revenue'
            '&data_break_down=ad_account&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,Ad Revenue', 'Breakdown,Ad Platform']},
    {'name': '[ADV] AMZAdRevenue-Site-Ad Revenue',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/ad_revenue/export/?chart_type=revenue'
            '&data_break_down=ad_item&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,Ad Revenue', 'Breakdown,Site']},
    # -------------  AD Expense  -----------------------
    {'name': '[ADV] AMZAdExpense-Country-Ad Expense',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/ad_expense/export/?chart_type=expense'
            '&data_break_down=country&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,Ad Expense', 'Breakdown,Country']},
    {'name': '[ADV] AMZAdExpense-Ad Platform-Ad Expense',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/ad_expense/export/?chart_type=expense'
            '&data_break_down=ad_account&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,Ad Expense', 'Breakdown,Ad Platform']},
    {'name': '[ADV] AMZAdExpense-Campaign-Ad Expense',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/ad_expense/export/?chart_type=expense'
            '&data_break_down=ad_item&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,Ad Expense', 'Breakdown,Campaign']},
    # =============  WP Single App  ============================
    # -------------  Download  -----------------------
    {'name': '[AN] WinPhone-Download-Country-Download',
     'url': '#{https}/dashboard/#{wpAccountId}/item/#{wpAccountApp1}/downloads/export/?breakdown=country'
            '&chart_type=downloads&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Data,Downloads', 'Account,#{csvWpAccount}']},
    {'name': '[AN] WinPhone-Download-Country-Refunds',
     'url': '#{https}/dashboard/#{wpAccountId}/item/#{wpAccountApp1}/downloads/export/?breakdown=country'
            '&chart_type=refunds&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Data,Refunds', 'Account,#{csvWpAccount}']},
    {'name': '[AN] WinPhone-Download-Country-Trial Donwloads',
     'url': '#{https}/dashboard/#{wpAccountId}/item/#{wpAccountApp1}/downloads/export/?breakdown=country'
            '&chart_type=trials&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Data,Trial Downloads', 'Account,#{csvWpAccount}']},
    {'name': '[AN] WinPhone-Download-Country-Beta downloads',
     'url': '#{https}/dashboard/#{wpAccountId}/item/#{wpAccountApp1}/downloads/export/?breakdown=country'
            '&chart_type=beta&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Data,Beta Downloads', 'Account,#{csvWpAccount}']},
    {'name': '[AN] WinPhone-Download-Source-All',
     'url': '#{https}/dashboard/#{wpAccountId}/item/#{wpAccountApp1}/downloads/export/?breakdown=source'
            '&chart_type=all&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Source', 'Account,#{csvWpAccount}']},
    {'name': '[AN] WinPhone-Download-Country-All',
     'url': '#{https}/dashboard/#{wpAccountId}/item/#{wpAccountApp1}/downloads/export/?breakdown=country'
            '&chart_type=all&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Metrics,all', 'Account,#{csvWpAccount}']},
    # -------------  Revenue  -----------------------
    {'name': '[AN] WinPhone-Revenue-Country-Total Revenue',
     'url': '#{https}/dashboard/#{wpAccountId}/item/#{wpAccountApp1}/revenue/export/'
            '?breakdown=country&chart_type=total_revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,Total Revenue', 'Account,#{csvWpAccount}']},
    {'name': '[AN] WinPhone-Revenue-Country-Paid Downloads',
     'url': '#{https}/dashboard/#{wpAccountId}/item/#{wpAccountApp1}/revenue/export/'
            '?breakdown=country&chart_type=sales_revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,Sales Revenue', 'Account,#{csvWpAccount}']},
    {'name': '[AN] WinPhone-Revenue-Country-In App Purchases',
     'url': '#{https}/dashboard/#{wpAccountId}/item/#{wpAccountApp1}/revenue/export/'
            '?breakdown=country&chart_type=iap_revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,IAP Revenue', 'Account,#{csvWpAccount}']},
    {'name': '[AN] WinPhone-Revenue-Country-Ad Revenue',
     'url': '#{https}/dashboard/#{wpAccountId}/item/#{wpAccountApp1}/revenue/export/'
            '?breakdown=country&chart_type=ad_revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,Ad Revenue', 'Account,#{csvWpAccount}']},
    {'name': '[AN] WinPhone-Revenue-Source-All',
     'url': '#{https}/dashboard/#{wpAccountId}/item/#{wpAccountApp1}/revenue/export/'
            '?breakdown=source&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Source', 'Account,#{csvWpAccount}']},
    {'name': '[AN] WinPhone-Revenue-Country-All',
     'url': '#{https}/dashboard/#{wpAccountId}/item/#{wpAccountApp1}/revenue/export/?breakdown=country&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Metrics,all', 'Account,#{csvWpAccount}']},
    # # -------------  IAP  -----------------------
    {'name': '[AN] WinPhone-IAP-IAP Items-IAP Revenue',
     'url': '#{https}/dashboard/#{wpAccountId}/item/#{wpAccountApp1}/iap/export/?breakdown=ipp&chart_type=revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Data,IAP Revenue']},
    {'name': '[AN] WinPhone-IAP-IAP Items-IAP Units',
     'url': '#{https}/dashboard/#{wpAccountId}/item/#{wpAccountApp1}/iap/export/?breakdown=ipp&chart_type=units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Data,IAP Units']},
    {'name': '[AN] WinPhone-IAP-IAP Items-Refunds',
     'url': '#{https}/dashboard/#{wpAccountId}/item/#{wpAccountApp1}/iap/export/'
            '?breakdown=ipp&chart_type=refund_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Data,Refunds']},
    {'name': '[AN] WinPhone-IAP-Country-IAP Revenue',
     'url': '#{https}/dashboard/#{wpAccountId}/item/#{wpAccountApp1}/iap/export/?breakdown=country&chart_type=revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Data,IAP Revenue']},
    {'name': '[AN] WinPhone-IAP-Country-IAP Units',
     'url': '#{https}/dashboard/#{wpAccountId}/item/#{wpAccountApp1}/iap/export/?breakdown=country&chart_type=units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Data,IAP Units']},
    {'name': '[AN] WinPhone-IAP-Country-Refunds',
     'url': '#{https}/dashboard/#{wpAccountId}/item/#{wpAccountApp1}/iap/export/'
            '?breakdown=country&chart_type=refund_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Data,Refunds']},
    {'name': '[AN] WinPhone-IAP-IAP Items-All',
     'url': '#{https}/dashboard/#{wpAccountId}/item/#{wpAccountApp1}/iap/export/?breakdown=ipp&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Metrics,all']},
    {'name': '[AN] WinPhone-IAP-Country-All',
     'url': '#{https}/dashboard/#{wpAccountId}/item/#{wpAccountApp1}/iap/export/?breakdown=country&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Metrics,all']},

    # =============  WinStore Single App  ============================
    # -------------  Download  -----------------------
    {'name': '[AN] WinStore-Download-Country-Download',
     'url': '#{https}/dashboard/#{wsAccountId}/item/#{wsAccountApp1}/downloads/export/?breakdown=country'
            '&chart_type=downloads&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Data,Downloads', 'Account,#{csvWsAccount}']},
    {'name': '[AN] WinStore-Download-Country-Trials',
     'url': '#{https}/dashboard/#{wsAccountId}/item/#{wsAccountApp1}/downloads/export/?breakdown=country'
            '&chart_type=trials&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Data,Trial Downloads', 'Account,#{csvWsAccount}']},
    {'name': '[AN] WinStore-Download-Country-Beta',
     'url': '#{https}/dashboard/#{wsAccountId}/item/#{wsAccountApp1}/downloads/export/?breakdown=country'
            '&chart_type=beta&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Data,Beta Downloads', 'Account,#{csvWsAccount}']},
    {'name': '[AN] WinStore-Download-Country-Refunds',
     'url': '#{https}/dashboard/#{wsAccountId}/item/#{wsAccountApp1}/downloads/export/?breakdown=country'
            '&chart_type=refunds&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Data,Refunds', 'Account,#{csvWsAccount}']},
    {'name': '[AN] WinStore-Download-Source-All',
     'url': '#{https}/dashboard/#{wsAccountId}/item/#{wsAccountApp1}/downloads/export/?breakdown=source'
            '&chart_type=all&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Source']},
    {'name': '[AN] WinStore-Download-Country-All',
     'url': '#{https}/dashboard/#{wsAccountId}/item/#{wsAccountApp1}/downloads/export/?breakdown=country'
            '&chart_type=all&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Downloads', 'Breakdown,Country', 'Metrics,all']},
    # -------------  Revenue  -----------------------
    {'name': '[AN] WinStore-Revenue-Country-Total Revenue',
     'url': '#{https}/dashboard/#{wsAccountId}/item/#{wsAccountApp1}/revenue/export/'
            '?breakdown=country&chart_type=total_revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,Total Revenue', 'Account,#{csvWsAccount}']},
    {'name': '[AN] WinStore-Revenue-Country-Paid Downloads',
     'url': '#{https}/dashboard/#{wsAccountId}/item/#{wsAccountApp1}/revenue/export/'
            '?breakdown=country&chart_type=sales_revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,Sales Revenue', 'Account,#{csvWsAccount}']},
    {'name': '[AN] WinStore-Revenue-Country-In App Purchases',
     'url': '#{https}/dashboard/#{wsAccountId}/item/#{wsAccountApp1}/revenue/export/'
            '?breakdown=country&chart_type=iap_revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,IAP Revenue', 'Account,#{csvWsAccount}']},
    {'name': '[AN] WinStore-Revenue-Country-Ad Revenue',
     'url': '#{https}/dashboard/#{wsAccountId}/item/#{wsAccountApp1}/revenue/export/'
            '?breakdown=country&chart_type=ad_revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Data,Ad Revenue', 'Account,#{csvWsAccount}']},
    {'name': '[AN] WinStore-Revenue-Source-All',
     'url': '#{https}/dashboard/#{wsAccountId}/item/#{wsAccountApp1}/revenue/export/'
            '?breakdown=source&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Source', '#{csvWsAccount}']},
    {'name': '[AN] WinStore-Revenue-Country-All',
     'url': '#{https}/dashboard/#{wsAccountId}/item/#{wsAccountApp1}/revenue/export/'
            '?breakdown=country&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,App Revenue', 'Breakdown,Country', 'Metrics,all', 'Account,#{csvWsAccount}'
                                                                         '']},
    # # -------------  IAP  -----------------------
    {'name': '[AN] WinStore-IAP-IAP Items-IAP Revenue',
     'url': '#{https}/dashboard/#{wsAccountId}/item/#{wsAccountApp1}/iap/export/?breakdown=ipp&chart_type=revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Data,IAP Revenue']},
    {'name': '[AN] WinStore-IAP-IAP Items-IAP Units',
     'url': '#{https}/dashboard/#{wsAccountId}/item/#{wsAccountApp1}/iap/export/?breakdown=ipp&chart_type=units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Data,IAP Units']},
    {'name': '[AN] WinStore-IAP-IAP Items-Refunds',
     'url': '#{https}/dashboard/#{wsAccountId}/item/#{wsAccountApp1}/iap/export/'
            '?breakdown=ipp&chart_type=refund_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Data,Refunds']},
    {'name': '[AN] WinStore-IAP-Country-IAP Revenue',
     'url': '#{https}/dashboard/#{wsAccountId}/item/#{wsAccountApp1}/iap/export/'
            '?breakdown=country&chart_type=revenue'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Data,IAP Revenue']},
    {'name': '[AN] WinStore-IAP-Country-IAP Units',
     'url': '#{https}/dashboard/#{wsAccountId}/item/#{wsAccountApp1}/iap/export/'
            '?breakdown=country&chart_type=units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Data,IAP Units']},
    {'name': '[AN] WinStore-IAP-Country-Refunds',
     'url': '#{https}/dashboard/#{wsAccountId}/item/#{wsAccountApp1}/iap/export/'
            '?breakdown=country&chart_type=refund_units'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Data,Refunds']},
    {'name': '[AN] WinStore-IAP-IAP Items-All',
     'url': '#{https}/dashboard/#{wsAccountId}/item/#{wsAccountApp1}/iap/export/?breakdown=ipp&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,IAP Items', 'Metrics,all']},
    {'name': '[AN] WinStore-IAP-Country-All',
     'url': '#{https}/dashboard/#{wsAccountId}/item/#{wsAccountApp1}/iap/export/?breakdown=country&chart_type=all'
            '&start_date=%s&end_date=%s' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,In App Purchases', 'Breakdown,Country', 'Metrics,all']},

    # -------------  GA portfolio page  -----------------------
    {'name': '[ADV] monthly total_session_duration product_id single-country',
     'url': '#{https}/ajax/comparator/ga-usage/export/?group_id=#{groupId}'
            '&breakdown=product_id&start_date=%s&end_date=%s&granularity=monthly'
            '&chart_type=all&countries=US&with_ad=f' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,GA Usage', 'Countries,United States', 'Breakdown,App', 'Metrics,All',
               'Granularity,Monthly']},

    # -------------  GA Single App page  -----------------------
    {'name': '[ADV] daily DAU country ALL',
     'url': '#{https}/dashboard/#{gaAccountId}/item/#{gaAccountApp}/ga-usage/export/?breakdown=country'
            '&start_date=%s&end_date=%s'
            '&granularity=daily&chart_type=DAU&countries=ALL' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,GA Usage', 'Countries,All Countries', 'Breakdown,Country', 'Metrics,DAU',
               'Granularity,Daily']},
    {'name': '[ADV] daily avg_session_user_day device multi-country',
     'url': '#{https}/dashboard/#{gaAccountId}/item/#{gaAccountApp}/ga-usage/export/?breakdown=device'
            '&start_date=%s&end_date=%s&granularity=daily&chart_type=avg_session_user_day'
            '&countries=AU,CA,CN,CH,US,GB' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,GA Usage', 'Countries,Australia,Canada,China,Switzerland,United States,United Kingdom',
               'Breakdown,Device', 'Metrics,Avg Sessions / User', 'Granularity,Daily']},
    {'name': '[ADV] daily avg_session_duration country single-country',
     'url': '#{https}/dashboard/#{gaAccountId}/item/#{gaAccountApp}/ga-usage/export/?breakdown=country'
            '&start_date=%s&end_date=%s'
            '&granularity=daily&chart_type=avg_session_duration&countries=US' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,GA Usage', 'Countries,United States', 'Breakdown,Country',
               'Metrics,Average Session Duration', 'Granularity,Daily']},
    {'name': '[ADV] daily total_sessions device ALL',
     'url': '#{https}/dashboard/#{gaAccountId}/item/#{gaAccountApp}/ga-usage/export/?breakdown=device'
            '&start_date=%s&end_date=%s&granularity=daily&chart_type=total_sessions&countries=ALL' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,GA Usage', 'Countries,All Countries', 'Breakdown,Device', 'Metrics,Total Sessions',
               'Granularity,Daily']},
    {'name': '[ADV] daily total_session_duration country multi-country',
     'url': '#{https}/dashboard/#{gaAccountId}/item/#{gaAccountApp}/ga-usage/export/?breakdown=country'
            '&start_date=%s&end_date=%s'
            '&granularity=daily&chart_type=total_session_duration&countries=AU,CA,CN,CH,US,GB' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,GA Usage', 'Countries,Australia,Canada,China,Switzerland,United States,United Kingdom',
               'Breakdown,Country', 'Metrics,Total Time', 'Granularity,Daily']},
    {'name': '[ADV] weekly WAU device single-country',
     'url': '#{https}/dashboard/#{gaAccountId}/item/#{gaAccountApp}/ga-usage/export/?breakdown=device'
            '&start_date=%s&end_date=%s&granularity=weekly&chart_type=WAU&countries=US' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,GA Usage', 'Countries,United States', 'Breakdown,Device', 'Metrics,WAU',
               'Granularity,Weekly']},
    {'name': '[ADV] weekly avg_session_user_week country ALL',
     'url': '#{https}/dashboard/#{gaAccountId}/item/#{gaAccountApp}/ga-usage/export/?breakdown=country'
            '&start_date=%s&end_date=%s'
            '&granularity=weekly&chart_type=avg_session_user_week&countries=ALL' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,GA Usage', 'Countries,All Countries', 'Breakdown,Country', 'Metrics,Avg Sessions / User',
               'Granularity,Weekly']},
    {'name': '[ADV] weekly avg_session_duration device multi-country',
     'url': '#{https}/dashboard/#{gaAccountId}/item/#{gaAccountApp}/ga-usage/export/?breakdown=device'
            '&start_date=%s&end_date=%s&granularity=weekly&chart_type=avg_session_duration'
            '&countries=AU,CA,CN,CH,US,GB' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,GA Usage', 'Countries,Australia,Canada,China,Switzerland,United States,United Kingdom',
               'Breakdown,Device', 'Metrics,Average Session Duration', 'Granularity,Weekly']},
    {'name': '[ADV] weekly total_sessions country single-country',
     'url': '#{https}/dashboard/#{gaAccountId}/item/#{gaAccountApp}/ga-usage/export/?breakdown=country'
            '&start_date=%s&end_date=%s'
            '&granularity=weekly&chart_type=total_sessions&countries=US' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,GA Usage', 'Countries,United States', 'Breakdown,Country', 'Metrics,Total Sessions',
               'Granularity,Weekly']},
    {'name': '[ADV] weekly total_session_duration device ALL',
     'url': '#{https}/dashboard/#{gaAccountId}/item/#{gaAccountApp}/ga-usage/export/?breakdown=device'
            '&start_date=%s&end_date=%s'
            '&granularity=weekly&chart_type=total_session_duration&countries=ALL' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,GA Usage', 'Countries,All Countries', 'Breakdown,Device', 'Metrics,Total Time',
               'Granularity,Weekly']},
    {'name': '[ADV] monthly MAU country multi-country',
     'url': '#{https}/dashboard/#{gaAccountId}/item/#{gaAccountApp}/ga-usage/export/?breakdown=country'
            '&start_date=%s&end_date=%s'
            '&granularity=monthly&chart_type=MAU&countries=AU,CA,CN,CH,US,GB' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,GA Usage', 'Countries,Australia,Canada,China,Switzerland,United States,United Kingdom',
               'Breakdown,Country', 'Metrics,MAU', 'Granularity,Monthly']},
    {'name': '[ADV] monthly avg_session_user_month device single-country',
     'url': '#{https}/dashboard/#{gaAccountId}/item/#{gaAccountApp}/ga-usage/export/?breakdown=device'
            '&start_date=%s&end_date=%s'
            '&granularity=monthly&chart_type=avg_session_user_month&countries=US' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,GA Usage', 'Countries,United States', 'Breakdown,Device',
               'Metrics,Avg Sessions / User', 'Granularity,Monthly']},
    {'name': '[ADV] monthly avg_session_duration country ALL',
     'url': '#{https}/dashboard/#{gaAccountId}/item/#{gaAccountApp}/ga-usage/export/?breakdown=country'
            '&start_date=%s&end_date=%s'
            '&granularity=monthly&chart_type=avg_session_duration&countries=ALL' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,GA Usage', 'Countries,All Countries', 'Breakdown,Country',
               'Metrics,Average Session Duration', 'Granularity,Monthly']},
    {'name': '[ADV] monthly total_sessions device multi-country',
     'url': '#{https}/dashboard/#{gaAccountId}/item/#{gaAccountApp}/ga-usage/export/?breakdown=device'
            '&start_date=%s&end_date=%s&granularity=monthly'
            '&chart_type=total_sessions&countries=AU,CA,CN,CH,US,GB' % (env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,GA Usage', 'Countries,Australia,Canada,China,Switzerland,United States,United Kingdom',
               'Breakdown,Device', 'Metrics,Total Sessions', 'Granularity,Monthly']},
    {'name': '[ADV] monthly total_session_duration country single-country',
     'url': '#{https}/dashboard/#{gaAccountId}/item/#{gaAccountApp}/ga-usage/export/?breakdown=country'
            '&start_date=%s&end_date=%s'
            '&granularity=monthly&chart_type=total_session_duration&countries=US' % (
                env_var['start_date1'], env_var['end_date1']),
     'check': ['Report,GA Usage', 'Countries,United States', 'Breakdown,Country', 'Metrics,Total Time',
               'Granularity,Monthly']},

    #  -----------------------  Intelligence Download CSV  ------------------------------
    # {'name': 'Intelligence - Store - TopApps - Downloads',
    #  'url': '#{https}/intelligence/top-app-report/?device=iphone&country_id=143456&category_id=6020&'
    #         'date=2015-08-22&end_date=2015-08-22&granularity=daily&aggregation=app',
    #  'check': ['Rank', 'Category', 'Store', 'Device', 'Type', 'Country', 'Period', 'Version', 'App ID']},
    # {'name': 'Intelligence - Store - TopPublisher - Downloads',
    #  'url': '#{https}/intelligence/top-publisher-report/?device=iphone&country_id=143456&category_id=6020&'
    #         'date=2015-08-21&end_date=2015-08-21&granularity=daily',
    #  'check': ['Rank', 'Category', 'Store', 'Device', 'Type', 'Country', 'Period', 'Version', 'Publisher ID',
    #            'Publisher Name', 'Value']},
    # {'name': '[INT-WEB] Intelligence - Store - PYP - Downloads',
    #  'url': '#{https}/intelligence/top-pyp-report/?device=all&country_id=34'
    #         '&date=2015-07-01~2015-07-31&'
    #         'category_id=1',
    #  'check': ['App Annie Store Intelligence', 'Pick Your Publishers', 'Publisher', 'Store', 'Downloads', 'Revenue',
    #            'Data Availability', 'Company']},
    # {'name': '[INT-WEB] Intelligence - Store - PYA - Downloads',
    #  'url': '#{https}/intelligence/top-pya-report/?device=all&country_id=34'
    #         '&date=2015-07-01~2015-07-31',
    #  'check': ['App Annie Store Intelligence', 'Pick Your Apps', 'App', 'Store', 'Downloads', 'Revenue',
    #            'Data Availability', 'Publisher', 'Unified App']},
    # {'name': '[INT-WEB] Intelligence - Usage - PYA - Downloads',
    #  'url': '#{https}/intelligence/apps/usage/export/?&device=ios&country_id=143441&granularity=weekly&'
    #         'start_date=2015-08-09&end_date=2015-08-15',
    #  'check': ['App Annie Usage Intelligence', 'Pick Your Apps', 'Platform', 'Device', 'Country',
    #            'Period', 'App ID', 'App Name']},
    # {'name': '[INT-WEB] Intelligence - Store - AppHistory - Downloads',
    #  'url': '#{https}/intelligence/app-report/553834731/?&platform=ios&country_id=143456&granularity=daily&'
    #         'start_date=2015-07-01&end_date=2015-07-31',
    #  'check': ['App Annie Store Intelligence', 'Device', 'Period', 'Revenue', 'Downloads']},
    # {'name': '[INT-WEB] Intelligence - Usage - AppHistory - Downloads',
    #  'url': '#{https}/apps/ios/app/553834731/usage/export/?&country_id=143441&granularity=weekly&'
    #         'chart_type=penetration&start_date=2015-02-15&end_date=2015-08-15',
    #  'check': ['App Annie Usage Intelligence', 'Usage Intelligence App', 'Platform', 'Device',
    #            'Country', 'Period', 'App ID,App Name']},
    # {'name': '[INT-WEB] Intelligence - Store - AppCBD - Downloads',
    #  'url': '#{https}/intelligence/app-cbd-report/553834731/?&device=ios&granularity=daily&start_date=2015-07-01&'
    #         'end_date=2015-07-31',
    #  'check': ['App Annie Store Intelligence', 'Country Breakdown', 'Country', 'Downloads', 'Revenue']},
    # {'name': '[INT-WEB] Intelligence - Usage - AppCBD - Downloads',
    #  'url': '#{https}/apps/ios/app/553834731/usage/breakdown/country/export/?&device=ios&granularity=weekly&'
    #         'chart_type=penetration&start_date=2015-06-28&end_date=2015-10-10',
    #  'check': ['App Annie Usage Intelligence', 'App Country Breakdown', 'Install Penetration',
    #            'Usage Penetration', 'Share of Users']},
    # {'name': '[INT-WEB] Intelligence - Audience - Demographics - Downloads',
    #  'url': '#{https}/apps/ios/app/553834731/demographics/export/?methodology=user_base&device=iphone&'
    #         'country_id=143441&chart_type=percent&end_month=2016-01-01',
    #  'check': ['Platform', 'Country', 'Language', 'Start Date', 'End Date', 'App ID',
    #            'App Name', 'Gender - Index Female', 'Age - Index 13-24', 'Gender - % Female', 'Age - % 13-24']},
    # {'name': '[INT-WEB] Intelligence - Audience - RelatedApps - Downloads',
    #  'url': '#{https}/apps/ios/app/553834731/cross_app_usage/export/?methodology=user_base&device=iphone'
    #         '&country_id=143441&category_id=36&end_month=2016-01-01',
    #  'check': ['Platform', 'Country', 'Language', 'Start Date', 'End Date', 'App ID', 'App Name',
    #            'Cross-App Category', 'Cross-App Name', 'Affinity', 'Cross-App Usage']},
    # {'name': '[INT-WEB] Intelligence - Usage - TopChar - App Used - Downloads',
    #  'url': '#{https}/intelligence/usage/top/iphone/export/?country_id=143462&category_id=6012&granularity=weekly'
    #         '&user_segmentation=app_used&segment_app_id=422689480&segment_app_market=ios'
    #         '&start_date=2016-01-10&end_date=2016-01-16',
    #  'check': ['App Annie Usage Intelligence', 'Usage Intelligence Top Apps', 'Platform', 'Device', 'Country',
    #            'Segment Users By', 'App ID', 'App Name', 'Gmail', 'Usage Penetration', 'Install Penetration']},
    # {'name': '[INT-WEB] Intelligence - Usage - PYA - Age&Gender - Downloads',
    #  'url': '#{https}/intelligence/apps/usage/export/?&device=iphone&country_id=143441&granularity=weekly'
    #         '&user_segmentation=males_13_24&start_date=2016-01-10&end_date=2016-01-16',
    #  'check': ['App Annie Usage Intelligence', 'Usage Intelligence Pick Your Apps', 'Platform', 'Device', 'Country',
    #            'Segment Users By', 'Males 13 to 24', 'App ID', 'Usage Penetration', 'Install Penetration']},
    # {'name': '[INT-WEB] Intelligence - Usage - Retention - Downloads',
    #  'url': '#{https}/intelligence/usage/retention/export/?app_id=20600000578686&country=9&month=2016-03-01',
    #  'check': ['App Annie Usage Intelligence', 'Usage Intelligence User Retention', 'Platform', 'Device', 'Country',
    #            'Period', 'Day 0', 'Day 1', 'Day 7', 'Day 14', 'Day 30']},
    # {'name': '[INT-WEB] Intelligence - MKT - advertiser - app - Downloads',
    #  'url': '#{https}/app/934596429/intelligence/marketing/advertiser/export/?device=iphone&country=JP'
    #         '&granularity=weekly&date=2016-07-10',
    #  'check': ['App Annie Marketing Intelligence', 'Marketing Intelligence Advertiser App Overview', 'Ad Platform',
    #            'Device', 'Country', 'Period', 'Share of Network', 'First Seen', 'Last Seen', 'Creatives']},
    # {'name': '[INT-WEB] Intelligence - MKT - Creatives - androidTablet - filterByAdvertiserApp - Downloads',
    #  'url': '#{https}/intelligence/marketing/creatives/export/advertiser/?device=android_tablet&country=US&'
    #         'category=1&network=101&granularity=weekly&date=2016-08-14&app_id=20600004583866&formats=-1&'
    #         'dimensions=-1&min_active_days=1',
    #  'check': ['App Annie Marketing Intelligence', 'Marketing Intelligence Creatives', 'Country', 'Ad Platform',
    #            'Creative', 'Advertiser App ID', 'Advertiser App Name', 'Category', 'Format', 'Dimension',
    #            'Apps Seen In', 'Share of Network', 'Share of Advertiser', 'First Seen', 'Last Seen',
    #            'Advertiser: Last Empire-War Z', 'Active (Days)']},
    # {'name': '[INT-WEB] Intelligence - MKT - Creatives - iphone - filterByPublisher - Downloads',
    #  'url': '#{https}/intelligence/marketing/creatives/export/publisher/?device=iphone&country=GB&category=36&'
    #         'network=136&granularity=monthly&date=2016-06-01&app_id=284882215&formats=-1&dimensions=-1'
    #         '&min_active_days=1',
    #  'check': ['App Annie Marketing Intelligence', 'Marketing Intelligence Creatives', 'App Seen In: Facebook',
    #            'Country', 'Ad Platform', 'Creative', 'Advertiser App ID', 'Advertiser App Name', 'Category',
    #            'Format', 'Dimension', 'Apps Seen In', 'Share of Network', 'Share of Advertiser', 'First Seen',
    #            'Last Seen', 'Active (Days)', 'Publisher ID', 'Publisher Name', 'Company Name']},
    # {'name': '[INT-WEB] Intelligence - MKT - Creatives - AllNetwork - iPad - filterByPublisher - Downloads',
    #  'url': '#{https}/intelligence/marketing/creatives/export/advertiser/?device=ipad&country=US&category=6014&'
    #         'network=1&granularity=monthly&date=2016-05-01&app_id=727296976&formats=-1&dimensions=-1&'
    #         'min_active_days=1',
    #  'check': ['App Annie Marketing Intelligence', 'Marketing Intelligence Creatives', 'Advertiser: Cookie Jam',
    #            'Country', 'Ad Platform', 'Period', 'Creative', 'Advertiser App ID', 'Advertiser App Name',
    #            'Category', 'Format', 'Dimension', 'Apps Seen In', 'First Seen', 'Last Seen', 'Active (Days)',
    #            'Publisher ID', 'Publisher Name', 'Company Name']},
    # {'name': '[INT-WEB] Intelligence - MKT - Advertisers - iPhone - Overall - Month - Downloads',
    #  'url': '#{https}/intelligence/marketing/advertisers/export/?device=iphone&country=GB&category=36&network=136&'
    #         'granularity=monthly&date=2016-06-01',
    #  'check': ['App Annie Marketing Intelligence', 'Marketing Intelligence Advertisers', 'Platform', 'Device',
    #            'Country', 'Ad Platform', 'Period', 'Advertiser App ID', 'Advertiser App Name', 'Category',
    #            '# Ad Platforms', 'Ad Platforms (Advertised In)', 'Apps Seen In', 'Creatives', 'Campaigns',
    #            'Share of Network', 'Share of Network (Change %)', 'Publisher Share of Network',
    #            'Publisher Share of Network (Change %)', 'Publisher ID', 'Publisher Name', 'Company Name']},
    # {'name': '[INT-WEB] Intelligence - MKT - Advertisers - AndroidPhone - Games - Month - Downloads',
    #  'url': '#{https}/intelligence/marketing/advertisers/export/?device=android_phone&country=JP&category=2&'
    #         'network=142&granularity=monthly&date=2016-06-01',
    #  'check': ['App Annie Marketing Intelligence', 'Marketing Intelligence Advertisers', 'Platform', 'Device',
    #            'Country', 'Ad Platform', 'Period', 'Advertiser App ID', 'Advertiser App Name', 'Category',
    #            '# Ad Platforms', 'Ad Platforms (Advertised In)', 'Apps Seen In', 'Creatives', 'Campaigns',
    #            'Share of Network', 'Share of Network (Change %)', 'Publisher Share of Network',
    #            'Publisher Share of Network (Change %)', 'Publisher ID', 'Publisher Name']},
    # {'name': '[INT-WEB] Intelligence - MKT - Advertisers - AllNetwork - iPad - Overall - Month - Downloads',
    #  'url': '#{https}/intelligence/marketing/advertisers/export/?device=ipad&country=US&category=6014&network=1&'
    #         'granularity=monthly&date=2016-05-01',
    #  'check': ['App Annie Marketing Intelligence', 'Marketing Intelligence Advertisers', 'Platform', 'Device',
    #            'Country', 'Ad Platform', 'Period', 'Advertiser App ID', 'Advertiser App Name', 'Category',
    #            '# Ad Platforms', 'Ad Platforms (Advertised In)', 'Apps Seen In', 'Creatives', 'Campaigns',
    #            'Publisher ID', 'Publisher Name']},
    # {'name': '[INT-WEB] Intelligence - MKT - AdMonetization - iPad - Application - Week - Downloads',
    #  'url': '#{https}/intelligence/marketing/ad-monetization/export/?device=ipad&country=DE&category=100&'
    #         'network=110&granularity=monthly&date=2016-06-01',
    #  'check': ['App Annie Marketing Intelligence', 'Marketing Intelligence Ad Monetization', 'Platform', 'Device',
    #            'Country', 'Ad Platform', 'Period', 'App ID', 'App Name', 'Category', 'Downloads Rank',
    #            '# Ad Platforms', 'Ad Platforms (Integrated)', 'Share of Network', 'Share of Network (Change %)',
    #            'Publisher ID', 'Publisher Name', 'Company Name', 'Parent Company Name']},
    # {'name': '[INT-WEB] Intelligence - MKT - AdMonetization - AndroidPhone - Family - Week - Downloads',
    #  'url': '#{https}/intelligence/marketing/ad-monetization/export/?device=android_phone&country=KR&category=56&'
    #         'network=111&granularity=weekly&date=2016-06-12',
    #  'check': ['App Annie Marketing Intelligence', 'Marketing Intelligence Ad Monetization', 'Platform', 'Device',
    #            'Country', 'Ad Platform', 'Period', 'App ID', 'App Name', 'Category', 'Downloads Rank',
    #            '# Ad Platforms', 'Ad Platforms (Integrated)', 'Share of Network', 'Share of Network (Change %)',
    #            'Publisher ID', 'Publisher Name', 'Company Name', 'Parent Company Name']},
    # {'name': '[INT-WEB] Inelligence - Mkt - AdMonetization - AllNetwork - AndroidTablet - Week - Downloads',
    #  'url': '#{https}/intelligence/marketing/ad-monetization/export/?device=android_tablet&country=US&category=2&'
    #         'network=1&granularity=weekly&date=2016-06-05',
    #  'check': ['App Annie Marketing Intelligence', 'Marketing Intelligence Ad Monetization', 'Platform', 'Device',
    #            'Country', 'Ad Platform', 'Period', 'App ID', 'App Name', 'Category', 'Downloads Rank',
    #            '# Ad Platforms', 'Ad Platforms (Integrated)', 'Publisher ID', 'Publisher Name', 'Company Name']},

]
