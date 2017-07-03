# Copyright (c) 2016 App Annie Inc. All rights reserved.

# -*- coding: utf-8 -*-
from tests.quick_smoke.smoke_utils import get_env_var

env_var = get_env_var()

EXPORT_BUTTON = 'aa-dropdown-trigger .btn-action-secondary'
EXPORT_CSV = 'li:nth-of-type(1) .primary-info.ng-binding'
EXPORT_XLSX = 'li:nth-of-type(2) .primary-info.ng-binding'

storestats_async_csv_cases = [
    # Top chart ios csv
    {'name': '[SS] top chart - US - %s - ios - iphone - iap all - All' % env_var['async_category']['ios']['name'],
     'url': '#{https}/apps/ios/top-chart/?country=US&category=%s&feed=All' % env_var['async_category']['ios']['id'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Report,Top Charts', 'Market,iOS', 'Country,United States', 'Device,iPhone',
               'Category,%s' % env_var['async_category']['ios']['name'], 'In App Purchases,all',
               'Rank,Platform,Device,Category,Type,Country,Period,App ID,Package Name,App Name,Publisher ID,'
               'Publisher Name,Change(Rank)'],
     'env': ['production', 'staging']},
    {'name': '[SS] top chart - US - %s - ios - iphone - iap all - Free' % env_var['async_category']['ios']['name'],
     'url': '#{https}/apps/ios/top-chart/?country=US&category=%s&feed=Free' % env_var['async_category']['ios']['id'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Report,Top Charts', 'Market,iOS', 'Country,United States', 'Device,iPhone',
               'Category,%s' % env_var['async_category']['ios']['name'], 'Type,Free', 'In App Purchases,all',
               'Platform,Device,Type,Country,Period,App ID,Package Name,App Name,Publisher ID,Publisher Name,'
               'Free Rank,Free Rank Change,Grossing Rank,Grossing Rank Change,Price,Category,'
               'Star Rating (Since Update),Ratings (Since Update),Star Rating (Since Release),'
               'Ratings (Since Release),Release Date,Last Updated'],
     'env': ['production', 'staging']},
    {'name': '[SS] top chart - US - %s - ios - iphone - iap all - Paid' % env_var['async_category']['ios']['name'],
     'url': '#{https}/apps/ios/top-chart/?country=US&category=%s&feed=Paid' % env_var['async_category']['ios']['id'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Report,Top Charts', 'Market,iOS', 'Country,United States', 'Device,iPhone',
               'Category,%s' % env_var['async_category']['ios']['name'], 'Type,Paid', 'In App Purchases,all',
               'Platform,Device,Type,Country,Period,App ID,Package Name,App Name,Publisher ID,Publisher Name,'
               'Paid Rank,Paid Rank Change,Grossing Rank,Grossing Rank Change,Price,Category,'
               'Star Rating (Since Update),Ratings (Since Update),Star Rating (Since Release),'
               'Ratings (Since Release),Release Date,Last Updated'],
     'env': ['production', 'staging']},
    {'name': '[SS] top chart - US - %s - ios - iphone - iap all - Grossing' % env_var['async_category']['ios']['name'],
     'url': '#{https}/apps/ios/top-chart/?country=US&category=%s&feed=Grossing' %
            env_var['async_category']['ios']['id'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Report,Top Charts', 'Market,iOS', 'Country,United States', 'Device,iPhone',
               'Category,%s' % env_var['async_category']['ios']['name'], 'Type,Grossing', 'In App Purchases,all',
               'Platform,Device,Type,Country,Period,App ID,Package Name,App Name,Publisher ID,Publisher Name,'
               'Grossing Rank,Grossing Rank Change,Free Rank,Free Rank Change,Paid Rank,Paid Rank Change,'
               'Price,Category,Star Rating (Since Update),Ratings (Since Update),Star Rating (Since Release),'
               'Ratings (Since Release),Release Date,Last Updated'],
     'env': ['production', 'staging']},
    # Top chart gp csv
    {'name': '[SS] top chart - US - %s - gp - iap all - All' % env_var['async_category']['gp']['name'],
     'url': '#{https}/apps/google-play/top-chart/?country=US&category=%s&feed=All' %
            env_var['async_category']['gp']['id'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Report,Top Charts', 'Market,Google Play', 'Country,United States', 'Device,N/A',
               'Category,%s' % env_var['async_category']['gp']['name'], 'In App Purchases,all',
               'Rank,Platform,Device,Category,Type,Country,Period,App ID,Package Name,App Name,Publisher ID,'
               'Publisher Name,Change(Rank)'],
     'env': ['production', 'staging']},
    {'name': '[SS] top chart - US - %s - gp - iap all - Free' % env_var['async_category']['gp']['name'],
     'url': '#{https}/apps/google-play/top-chart/?country=US&category=%s&feed=Free' %
            env_var['async_category']['gp']['id'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Report,Top Charts', 'Market,Google Play', 'Country,United States', 'Device,N/A',
               'Category,%s' % env_var['async_category']['gp']['name'], 'Type,Free', 'In App Purchases,all',
               'Platform,Device,Type,Country,Period,App ID,Package Name,App Name,Publisher ID,Publisher Name,'
               'Free Rank,Free Rank Change,Grossing Rank,Grossing Rank Change,New Free Rank,'
               'New Free Rank Change,Price,Category,'
               'Star Rating (Since Release),Ratings (Since Release),Release Date,Last Updated'],
     'env': ['production', 'staging']},
    {'name': '[SS] top chart - US - %s - gp - iap all - Paid' % env_var['async_category']['gp']['name'],
     'url': '#{https}/apps/google-play/top-chart/?country=US&category=%s&feed=Paid' %
            env_var['async_category']['gp']['id'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Report,Top Charts', 'Market,Google Play', 'Country,United States', 'Device,N/A',
               'Category,%s' % env_var['async_category']['gp']['name'], 'Type,Paid', 'In App Purchases,all',
               'Platform,Device,Type,Country,Period,App ID,Package Name,App Name,Publisher ID,Publisher Name,'
               'Paid Rank,Paid Rank Change,Grossing Rank,Grossing Rank Change,New Paid Rank,'
               'New Paid Rank Change,Price,Category,'
               'Star Rating (Since Release),Ratings (Since Release),Release Date,Last Updated'],
     'env': ['production', 'staging']},
    {'name': '[SS] top chart - US - %s - gp - iap all - Grossing' % env_var['async_category']['gp']['name'],
     'url': '#{https}/apps/google-play/top-chart/?country=US&category=%s&feed=Grossing' %
            env_var['async_category']['gp']['id'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Report,Top Charts', 'Market,Google Play', 'Country,United States', 'Device,N/A',
               'Category,%s' % env_var['async_category']['gp']['name'], 'Type,Grossing', 'In App Purchases,all',
               'Platform,Device,Type,Country,Period,App ID,Package Name,App Name,Publisher ID,Publisher Name,'
               'Grossing Rank,Grossing Rank Change,Free Rank,Free Rank Change,Paid Rank,Paid Rank Change,'
               'New Free Rank,New Free Rank Change,New Paid Rank,New Paid Rank Change,Price,Category,'
               'Star Rating (Since Release),Ratings (Since Release),Release Date,Last Updated'],
     'env': ['production', 'staging']},
    {'name': '[SS] top chart - US - %s - gp - iap all - New Free' % env_var['async_category']['gp']['name'],
     'url': '#{https}/apps/google-play/top-chart/?country=US&category=%s&feed=New-Free' %
            env_var['async_category']['gp']['id'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Report,Top Charts', 'Market,Google Play', 'Country,United States', 'Device,N/A',
               'Category,%s' % env_var['async_category']['gp']['name'], 'Type,New Free', 'In App Purchases,all',
               'Platform,Device,Type,Country,Period,App ID,Package Name,App Name,Publisher ID,Publisher Name,'
               'New Free Rank,New Free Rank Change,Free Rank,Free Rank Change,'
               'Grossing Rank,Grossing Rank Change,Price,Category,'
               'Star Rating (Since Release),Ratings (Since Release),Release Date,Last Updated'],
     'env': ['production', 'staging']},
    {'name': '[SS] top chart - US - %s - gp - iap all - New Paid' % env_var['async_category']['gp']['name'],
     'url': '#{https}/apps/google-play/top-chart/?country=US&category=%s&feed=New-Paid' %
            env_var['async_category']['gp']['id'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Report,Top Charts', 'Market,Google Play', 'Country,United States', 'Device,N/A',
               'Category,%s' % env_var['async_category']['gp']['name'], 'Type,New Paid', 'In App Purchases,all',
               'Platform,Device,Type,Country,Period,App ID,Package Name,App Name,Publisher ID,Publisher Name,'
               'New Paid Rank,New Paid Rank Change,Paid Rank,Paid Rank Change,'
               'Grossing Rank,Grossing Rank Change,Price,Category,'
               'Star Rating (Since Release),Ratings (Since Release),Release Date,Last Updated'],
     'env': ['production', 'staging']},
    # Top chart appletv csv
    {'name': '[SS] top chart - US - Overall - appletv - iap all - All',
     'url': '#{https}/apps/appletv/top-chart/?country=US&category=%s&feed=All' %
            env_var['async_category']['appletv']['id'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Report,Top Charts', 'Market,TV Store', 'Country,United States', 'Device,N/A',
               'Category,%s' % env_var['async_category']['appletv']['name'], 'In App Purchases,all',
               'Rank,Platform,Device,Category,Type,Country,Period,App ID,Package Name,App Name,Publisher ID,'
               'Publisher Name,Change(Rank)'],
     'env': ['production', 'staging']},
    # Top chart mac csv
    {'name': '[SS] top chart - US - Overall - mac - iap all - All',
     'url': '#{https}/apps/mac/top-chart/?country=US&category=%s&feed=All' %
            env_var['async_category']['mac']['id'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Report,Top Charts', 'Market,Mac', 'Country,United States', 'Device,N/A',
               'Category,%s' % env_var['async_category']['mac']['name'], 'In App Purchases,all',
               'Rank,Platform,Device,Category,Type,Country,Period,App ID,Package Name,App Name,Publisher ID,'
               'Publisher Name,Change(Rank)'],
     'env': ['production', 'staging']},
    # Top chart amazon csv
    {'name': '[SS] top chart - US - Overall - amazon - All',
     'url': '#{https}/apps/amazon-appstore/top-chart/?country=US&category=%s&feed=All' %
            env_var['async_category']['amazon']['id'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Report,Top Charts', 'Market,Amazon', 'Country,United States', 'Device,N/A',
               'Category,%s' % env_var['async_category']['amazon']['name'], 'In App Purchases,all',
               'Rank,Platform,Device,Category,Type,Country,Period,App ID,Package Name,App Name,Publisher ID,'
               'Publisher Name,Change(Rank)'],
     'env': ['production', 'staging']},
    # Top chart wp csv
    {'name': '[SS] top chart - US - Overall - wp - All',
     'url': '#{https}/apps/windows-phone/top-chart/?country=US&category=%s&feed=All' %
            env_var['async_category']['wp']['id'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Report,Top Charts', 'Market,Windows Phone', 'Country,United States', 'Device,N/A',
               'Category,%s' % env_var['async_category']['wp']['name'], 'In App Purchases,all',
               'Rank,Platform,Device,Category,Type,Country,Period,App ID,Package Name,App Name,Publisher ID,'
               'Publisher Name,Change(Rank)'],
     'env': ['production', 'staging']},
    # Top chart windows csv
    {'name': '[SS] top chart - US - Overall - windows - x86 - iap all - All',
     'url': '#{https}/apps/windows-store/top-chart/?country=US&category=%s&feed=All' %
            env_var['async_category']['win']['id'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Report,Top Charts', 'Market,Windows Store', 'Country,United States', 'Device,x86',
               'Category,%s' % env_var['async_category']['win']['name'], 'In App Purchases,all',
               'Rank,Platform,Device,Category,Type,Country,Period,App ID,Package Name,App Name,Publisher ID,'
               'Publisher Name,Change(Rank)'],
     'env': ['production', 'staging']},
    # SS new feature iOS daily feature
    {'name': '[SS] new feature - US - All - iOS - iphone - All',
     'url': '#{https}/apps/ios/app/#{iosAppSlug}/featured/?'
            'report=daily-features&chart_type=reach&country=US&device=iphone&date=2017-01-05',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Report,Daily Features', 'App ID,553834731', 'App,Candy Crush Saga', 'Market,iOS',
               'Country,United States', 'Category Page,ALL', 'Device,iPhone', 'Type,ALL',
               'App ID,App Name,Publisher ID,Publisher Name,Date,Device,Country,Category Page,Type,'
               'Creative,Subtitle,Row,Position,Depth,Path,Featured Visibility'],
     'env': ['production', 'staging']},
    # # SS new feature gp daily feature
    {'name': '[SS] new feature - US - All - gp - All',
     'url': '#{https}/apps/google-play/app/20600001580962/featured/?'
            'chart_type=reach&country=US&report=daily-features&date=2017-01-06',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Report,Daily Features', 'App ID,com.supercell.clashofclans', 'App,Clash of Clans',
               'Market,Google Play', 'Country,United States', 'Category Page,ALL', 'Device,Android', 'Type,ALL',
               'App ID,App Name,Publisher ID,Publisher Name,Date,Device,Country,Category Page,'
               'Type,Creative,Subtitle,Row,Position,Depth,Path,Featured Visibility'],
     'env': ['production', 'staging']},
    # SS new feature iOS feature history
    {'name': '[SS] new feature - US - All - iOS - iphone - All',
     'url': '#{https}/apps/ios/app/#{iosAppSlug}/featured/?report=feature-history'
            '&chart_type=reach&country=US&device=iphone&start_date=2016-12-07&end_date=2017-01-06',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Report,Featured History', 'App ID,553834731', 'App,Candy Crush Saga', 'Market,iOS',
               'Country,United States', 'Category Page,ALL', 'Type,ALL', 'Device,iPhone',
               'App ID,App Name,Publisher ID,Publisher Name,Date,Country,'
               'Category Page,Type,Device,Frequency,Visibility Score'],
     'env': ['production', 'staging']},
    # # SS new feature gp feature history
    {'name': '[SS] new feature - US - All - gp - All',
     'url': '#{https}/apps/google-play/app/20600001580962/featured/?'
            'chart_type=reach&country=US&report=feature-history&start_date=2016-12-07&end_date=2017-01-06',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Report,Featured History', 'App ID,com.supercell.clashofclans', 'App,Clash of Clans',
               'Market,Google Play', 'Country,United States', 'Category Page,ALL', 'Type,ALL', 'Device,Android',
               'App ID,App Name,Publisher ID,Publisher Name,Date,Country,Category Page,'
               'Type,Device,Frequency,Visibility Score'],
     'env': ['production', 'staging']},

    # ASO Keyword Explorer CSV download for iOS market
    {'name': '[ASO] Keyword Explorer - iOS - iPhone - US - Netflix CSV Download',
     'url': '#{https}/intelligence/marketing/aso/ios/keyword-top/?country=US&device=iphone&word=netflix',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Report,Keyword Explorer (ASO)', 'Market,iOS', 'Country,United States', 'Device,iPhone',
               'Keyword,netflix',
               'Rank,Platform,Device,Country,Keyword,Date,App ID,Package code,App Name,Publisher ID,Publisher Name,'
               'Has IAP,Estimated Downloads,Estimated Downloads Period,Estimated Revenue,Estimated Revenue Period,'
               'Traffic Share,Has Keyword In Title,Last Update,Category Rank,Category,Star Rating,Ratings'],
     'env': ['production', 'staging']},
    # ASO Keyword Explorer CSV download for Google Play market
    {'name': '[ASO] Keyword Explorer - gp - US - Netflix CSV Download',
     'url': '#{https}/intelligence/marketing/aso/google-play/keyword-top/?country=US&word=netflix',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Report,Keyword Explorer (ASO)', 'Market,Google Play', 'Country,United States', 'Device,-',
               'Keyword,netflix',
               'Rank,Platform,Device,Country,Keyword,Date,App ID,Package code,App Name,Publisher ID,Publisher Name,'
               'Has IAP,Estimated Downloads,Estimated Downloads Period,Estimated Revenue,Estimated Revenue Period,'
               'Traffic Share,Has Keyword In Title,Last Update,Category Rank,Category,Star Rating,Ratings'],
     'env': ['production', 'staging']},

    # ASO Single app page Keyword/ASO CSV download for iOS market
    {'name': '[ASO] Single app keyword page - iOS - iPhone - US - Facebook CSV Download',
     'url': '#{https}/apps/ios/app/facebook/keywords/?countries=US&device=iphone',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Report,Keywords / ASO', 'App,Facebook', 'Market,iOS', 'Country,United States', 'Device,iPhone',
               'Platform,Device,Country,App ID,Package code,App Name,Publisher ID,Publisher Name,Date,'
               'Keyword,Ranking,Results,Search Volume,Difficulty,Search volume / Difficulty,Traffic Share'],
     'env': ['production', 'staging']},
    # ASO Single app page Keyword/ASO CSV download for Google Play market
    {'name': '[ASO] Single app keyword page - gp - US - Facebook CSV Download',
     'url': '#{https}/apps/google-play/app/20600000009072/keywords/?countries=US',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Report,Keywords / ASO', 'App,Facebook', 'Market,Google Play', 'Country,United States', 'Device,-',
               'Platform,Device,Country,App ID,Package code,App Name,Publisher ID,Publisher Name,Date,'
               'Keyword,Ranking,Results,Search Volume,Difficulty,Search volume / Difficulty,Traffic Share'],
     'env': ['production', 'staging']},
]

int_async_csv_cases = [
    # =========================INT App Comparator===========================
    {'name': '[INT-CSV] App Comparator',
     'url': '#{https}/intelligence/apps/comparator/',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Store          ,Device            ,Country              ,Period          ,App Id         ,'
               'Package Name      ,App                 ,App Category      ,Publisher ID          ,'
               'Publisher Name          ,Company Name           ,Parent Company Name          ,'
               'App Name (Unified)        ,App Franchise           ,Unified App ID          ,App Franchise ID      ,'
               'Company ID          ,Parent Company ID          ,Downloads          ,Revenue          ,'
               'Usage Penetration    ,Install Penetration          ,Install Base      ,Open Rate          ,'
               'Active Users                  ,Total Minutes       ,Avg Sessions Per User             ,'
               'Avg Session Duration              ,Avg Time Per User            ,Avg Active Days              ,'
               '% Active Days                   ,Share of Category Time          ,MB Per User                  ,'
               'MB Per Session'],
     'env': ['production', 'staging']},
    # ===============================INT Store Top Apps=======================================
    {'name': '[INT-CSV] Store Top Apps - ios - All',
     'url': '#{https}/intelligence/top/?feed=all&aggregation=unified&device=ios&country=%s'
            '&category=lifestyle&granularity=daily' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Top Unified Apps Charts',
               '"Rank","Category","Store","Device","Type","Country","Period","Version","App ID","App Name",'
               '"Is Unified","Value","Change (%)","Change (Rank)","Change (Value)","Unit","Value Type","AppURL",'
               '"App IAP","App Category","Star Rating","Ratings","App Release Date","Last Update","Publisher ID",'
               '"Publisher Name","Company Name","Parent Company Name","App Franchise","App Franchise ID",'
               '"Company ID","Parent Company ID","HQ Country"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store Top Apps - iphone - Free',
     'url': '#{https}/intelligence/top/?feed=Free&aggregation=unified&device=iphone&country=%s'
            '&category=lifestyle&granularity=weekly' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Top Unified Apps Charts',
               '"Rank","Category","Store","Device","Type","Country","Period","Version","App ID","App Name",'
               '"Is Unified","Value","Change (%)","Change (Rank)","Change (Value)","Unit","Value Type","AppURL",'
               '"App IAP","App Category","Star Rating","Ratings","App Release Date","Last Update","Publisher ID",'
               '"Publisher Name","Company Name","Parent Company Name","App Franchise","App Franchise ID",'
               '"Company ID","Parent Company ID","HQ Country"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store Top Apps - ipad - Grossing',
     'url': '#{https}/intelligence/top/?feed=Grossing&aggregation=app&device=ipad&country=%s'
            '&category=lifestyle&granularity=daily' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Top Apps Charts',
               '"Rank","Category","Store","Device","Type","Country","Period","Version","App ID","App Name","Value",'
               '"Change (%)","Change (Rank)","Change (Value)","Unit","Value Type","AppURL","App IAP","App Category",'
               '"Star Rating","Ratings","App Device","Current Price","App Release Date","Last Update","Publisher ID",'
               '"Publisher Name","Company Name","Parent Company Name","App Name (Unified)","App Franchise",'
               '"Unified App ID","App Franchise ID","Company ID","Parent Company ID"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store Top Apps - ios - Paid',
     'url': '#{https}/intelligence/top/?feed=Paid&aggregation=app&device=ios&country=%s'
            '&category=lifestyle&granularity=monthly' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Top Apps Charts',
               '"Rank","Category","Store","Device","Type","Country","Period","Version","App ID","App Name","Value",'
               '"Change (%)","Change (Rank)","Change (Value)","Unit","Value Type","AppURL","App IAP","App Category",'
               '"Star Rating","Ratings","App Device","Current Price","App Release Date","Last Update","Publisher ID",'
               '"Publisher Name","Company Name","Parent Company Name","App Name (Unified)","App Franchise",'
               '"Unified App ID","App Franchise ID","Company ID","Parent Company ID"'
               ],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store Top Apps - GP - All',
     'url': '#{https}/intelligence/apps/google-play/top/?aggregation=app&feed=all&country=%s'
            '&category=application%%2Flifestyle&granularity=daily' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Top Apps Charts',
               '"Rank","Category","Store","Device","Type","Country","Period","Version","App ID","App Name","Value",'
               '"Change (%)","Change (Rank)","Change (Value)","Unit","Value Type","AppURL","App IAP","App Category",'
               '"Star Rating","Ratings","App Device","Current Price","App Release Date","Last Update","Publisher ID",'
               '"Publisher Name","Company Name","Parent Company Name","App Name (Unified)","App Franchise",'
               '"Unified App ID","App Franchise ID","Company ID","Parent Company ID"'
               ],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store Top Apps - GP - Free',
     'url': '#{https}/intelligence/apps/google-play/top/?aggregation=app&feed=Free&country=%s'
            '&category=application%%2Flifestyle&granularity=daily' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Top Apps Charts',
               '"Rank","Category","Store","Device","Type","Country","Period","Version","App ID","App Name","Value",'
               '"Change (%)","Change (Rank)","Change (Value)","Unit","Value Type","AppURL","App IAP","App Category",'
               '"Star Rating","Ratings","App Device","Current Price","App Release Date","Last Update","Publisher ID",'
               '"Publisher Name","Company Name","Parent Company Name","App Name (Unified)","App Franchise",'
               '"Unified App ID","App Franchise ID","Company ID","Parent Company ID"'
               ],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store Top Apps - GP - Paid',
     'url': '#{https}/intelligence/apps/google-play/top/?aggregation=unified&feed=Paid&country=%s'
            '&category=application%%2Flifestyle&granularity=weekly' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Top Unified Apps Charts',
               '"Rank","Category","Store","Device","Type","Country","Period","Version","App ID","App Name",'
               '"Is Unified","Value","Change (%)","Change (Rank)","Change (Value)","Unit","Value Type",'
               '"AppURL","App IAP","App Category","Star Rating","Ratings","App Release Date","Last Update",'
               '"Publisher ID","Publisher Name","Company Name","Parent Company Name","App Franchise",'
               '"App Franchise ID","Company ID","Parent Company ID","HQ Country"'
               ],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store Top Apps - GP - Grossing',
     'url': '#{https}/intelligence/apps/google-play/top/?aggregation=unified&feed=Grossing&country=%s'
            '&category=application%%2Flifestyle&granularity=monthly' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Top Unified Apps Charts',
               '"Rank","Category","Store","Device","Type","Country","Period","Version","App ID","App Name",'
               '"Is Unified","Value","Change (%)","Change (Rank)","Change (Value)","Unit","Value Type",'
               '"AppURL","App IAP","App Category","Star Rating","Ratings","App Release Date","Last Update",'
               '"Publisher ID","Publisher Name","Company Name","Parent Company Name","App Franchise",'
               '"App Franchise ID","Company ID","Parent Company ID","HQ Country"'
               ],
     'env': ['production', 'staging']},
    # ====================INT Store Top publish======================
    {'name': '[INT-CSV] Store Top publish - iOS - All',
     'url': '#{https}/intelligence/top-publishers/?feed=all&device=ios&country=%s&category=lifestyle'
            '&granularity=daily' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Top Publishers Charts',
               '"Rank","Category","Store","Device","Type","Country","Period","Version","Publisher ID",'
               '"Publisher Name","Value","Change (%)","Change (Rank)","Change (Value)","Unit","Value Type",'
               '"Publisher URL","Star Rating","Ratings","Apps","Company Name","Parent Company Name","Company ID",'
               '"Parent Company ID"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store Top publish - iOS - Free',
     'url': '#{https}/intelligence/top-publishers/?feed=Free&device=iphone&country=%s&category=lifestyle'
            '&granularity=weekly' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Top Publishers Charts',
               '"Rank","Category","Store","Device","Type","Country","Period","Version","Publisher ID",'
               '"Publisher Name","Value","Change (%)","Change (Rank)","Change (Value)","Unit","Value Type",'
               '"Publisher URL","Star Rating","Ratings","Apps","Company Name","Parent Company Name","Company ID",'
               '"Parent Company ID"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store Top publish - iOS - Paid',
     'url': '#{https}/intelligence/top-publishers/?feed=Paid&device=ipad&country=%s&category=lifestyle'
            '&granularity=monthly' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Top Publishers Charts',
               '"Rank","Category","Store","Device","Type","Country","Period","Version","Publisher ID",'
               '"Publisher Name","Value","Change (%)","Change (Rank)","Change (Value)","Unit","Value Type",'
               '"Publisher URL","Star Rating","Ratings","Apps","Company Name","Parent Company Name",'
               '"Company ID","Parent Company ID"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store Top publish - iOS - Grossing',
     'url': '#{https}/intelligence/publishers/google-play/top/?feed=Grossing&country=%s&category=application'
            '%%2Flifestyle&granularity=monthly' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Top Publishers Charts',
               '"Rank","Category","Store","Device","Type","Country","Period","Version","Publisher ID",'
               '"Publisher Name","Value","Change (%)","Change (Rank)","Change (Value)","Unit","Value Type",'
               '"Publisher URL","Star Rating","Ratings","Apps","Company Name","Parent Company Name","Company ID",'
               '"Parent Company ID"'],
     'env': ['production', 'staging']},
    # =====================Store PYC================
    {'name': '[INT-CSV] Store PYC - all',
     'url': '#{https}/intelligence/apps/pyp/?device=all&category_id=1',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Publisher,Store,Device,Country,Period,Downloads,Revenue,Currency,'
               'Data Availability,Category,Company'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store PYC - ios',
     'url': '#{https}/intelligence/apps/pyp/?device=ios&category_id=6014',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Publisher,Store,Device,Country,Period,Downloads,Revenue,Currency,'
               'Data Availability,Category,Company'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store PYC - iphone',
     'url': '#{https}/intelligence/apps/pyp/?device=iphone&category_id=100',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Publisher,Store,Device,Country,Period,Downloads,Revenue,Currency,'
               'Data Availability,Category,Company'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store PYC - ipad',
     'url': '#{https}/intelligence/apps/pyp/?device=ipad&category_id=6018',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Publisher,Store,Device,Country,Period,Downloads,Revenue,Currency,'
               'Data Availability,Category,Company'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store PYC - gp',
     'url': '#{https}/intelligence/apps/pyp/?device=google-play&category_id=56',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Publisher,Store,Device,Country,Period,Downloads,Revenue,Currency,'
               'Data Availability,Category,Company'],
     'env': ['production', 'staging']},
    # =====================Store PYA================
    {'name': '[INT-CSV] Store PYA - all',
     'url': '#{https}/intelligence/apps/pya/?device=all',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App,Store,Device,Country,Period,Downloads,Revenue,Currency,Data Availability,Publisher,Unified App'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store PYA - ios',
     'url': '#{https}/intelligence/apps/pya/?device=ios',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App,Store,Device,Country,Period,Downloads,Revenue,Currency,Data Availability,Publisher,Unified App'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store PYA - iphone',
     'url': '#{https}/intelligence/apps/pya/?device=iphone',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App,Store,Device,Country,Period,Downloads,Revenue,Currency,Data Availability,Publisher,Unified App'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store PYA - ipad',
     'url': '#{https}/intelligence/apps/pya/?device=ipad',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App,Store,Device,Country,Period,Downloads,Revenue,Currency,Data Availability,Publisher,Unified App'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store PYA - gp',
     'url': '#{https}/intelligence/apps/pya/?device=google-play',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App,Store,Device,Country,Period,Downloads,Revenue,Currency,Data Availability,Publisher,Unified App'],
     'env': ['production', 'staging']},
    # =======================Market Size========================
    # TODO: Data range
    {'name': '[INT-CSV] market size CBD - ios - weekly',
     'url': '#{https}/intelligence/ios/market-size/?data_break_down=country&device=ios&countries=%s'
            '&category=lifestyle&price=all&sort_by=value&granularity=weekly'
            '&date=2016-07-24~2017-01-28' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Market Size Store Intelligence - Country Breakdown',
               '"Store","Device","Country","Price","Period","App Category","Downloads","Downloads Change (%)",'
               '"Downloads Change (Value)","Downloads Share","Revenue","Revenue Change (%)",'
               '"Revenue Change (Value)","Revenue Share","Currency"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] market size CBD - iphone - monthly',
     'url': '#{https}/intelligence/ios/market-size/?data_break_down=country&device=iphone&countries=%s'
            '&category=medical&price=free&sort_by=changeInPercent&granularity=monthly'
            '&date=2016-01-01~2016-12-31' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Market Size Store Intelligence - Country Breakdown',
               '"Store","Device","Country","Price","Period","App Category","Downloads","Downloads Change (%)",'
               '"Downloads Change (Value)","Downloads Share","Revenue","Revenue Change (%)",'
               '"Revenue Change (Value)","Revenue Share","Currency"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] market size CBD - ipad - weekly',
     'url': '#{https}/intelligence/ios/market-size/?data_break_down=country&device=ipad&countries=%s'
            '&category=social&price=paid&sort_by=changeInValue&granularity=weekly'
            '&date=2016-07-24~2017-01-28' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Market Size Store Intelligence - Country Breakdown',
               '"Store","Device","Country","Price","Period","App Category","Downloads","Downloads Change (%)",'
               '"Downloads Change (Value)","Downloads Share","Revenue","Revenue Change (%)",'
               '"Revenue Change (Value)","Revenue Share","Currency"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] market size CBD - all - gp - monthly',
     'url': '#{https}/intelligence/google-play/market-size/?data_break_down=country&countries=%s'
            '&category=lifestyle&price=all&iap=all&sort_by=value&device=google-play&granularity=monthly'
            '&date=2016-01-01~2016-12-31' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Market Size Store Intelligence - Country Breakdown',
               '"Store","Device","Country","Price","Period","App Category","Downloads","Downloads Change (%)",'
               '"Downloads Change (Value)","Downloads Share","Revenue","Revenue Change (%)",'
               '"Revenue Change (Value)","Revenue Share","Currency"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] market size CBD - free - gp - weekly',
     'url': '#{https}/intelligence/google-play/market-size/?data_break_down=country&countries=%s'
            '&category=medical&price=free&iap=all&sort_by=changeInPercent&device=google-play&granularity=weekly'
            '&date=2016-07-24~2017-01-28' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Market Size Store Intelligence - Country Breakdown',
               '"Store","Device","Country","Price","Period","App Category","Downloads","Downloads Change (%)",'
               '"Downloads Change (Value)","Downloads Share","Revenue","Revenue Change (%)",'
               '"Revenue Change (Value)","Revenue Share","Currency"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] market size CBD - paid - gp - monthly',
     'url': '#{https}/intelligence/google-play/market-size/?data_break_down=country&countries=%s'
            '&category=social&price=paid&iap=all&sort_by=changeInValue&device=google-play&granularity=monthly'
            '&date=2016-01-01~2016-12-31' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Market Size Store Intelligence - Country Breakdown',
               '"Store","Device","Country","Price","Period","App Category","Downloads","Downloads Change (%)",'
               '"Downloads Change (Value)","Downloads Share","Revenue","Revenue Change (%)",'
               '"Revenue Change (Value)","Revenue Share","Currency"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] market size category break down - all - ios - weekly',
     'url': '#{https}/intelligence/ios/market-size/?data_break_down=category&device=ios&countries=%s'
            '&category=lifestyle&price=all&sort_by=changeInValue&granularity=weekly'
            '&date=2016-07-24~2017-01-28' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Market Size Store Intelligence - Category Breakdown',
               '"Store","Device","Country","Price","Period","App Category","Downloads","Downloads Change (%)",'
               '"Downloads Change (Value)","Downloads Share","Revenue","Revenue Change (%)",'
               '"Revenue Change (Value)","Revenue Share","Currency"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] market size category break down - free - iphone - monthly',
     'url': '#{https}/intelligence/ios/market-size/?data_break_down=category&device=iphone&countries=%s'
            '&category=social&price=free&sort_by=changeInPercent&granularity=monthly'
            '&date=2016-01-01~2016-12-31' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Market Size Store Intelligence - Category Breakdown',
               '"Store","Device","Country","Price","Period","App Category","Downloads","Downloads Change (%)",'
               '"Downloads Change (Value)","Downloads Share","Revenue","Revenue Change (%)",'
               '"Revenue Change (Value)","Revenue Share","Currency"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] market size category break down - paid - ipad - weekly',
     'url': '#{https}/intelligence/ios/market-size/?data_break_down=category&device=ipad&countries=%s'
            '&category=medical&price=paid&sort_by=value&granularity=weekly'
            '&date=2016-07-24~2017-01-28' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Market Size Store Intelligence - Category Breakdown',
               '"Store","Device","Country","Price","Period","App Category","Downloads","Downloads Change (%)",'
               '"Downloads Change (Value)","Downloads Share","Revenue","Revenue Change (%)",'
               '"Revenue Change (Value)","Revenue Share","Currency"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] market size category break down - free - gp - monthly',
     'url': '#{https}/intelligence/google-play/market-size/?data_break_down=category&countries=%s'
            '&category=lifestyle&price=free&iap=all&sort_by=value&device=google-play&granularity=monthly'
            '&date=2016-01-01~2016-12-31' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Market Size Store Intelligence - Category Breakdown',
               '"Store","Device","Country","Price","Period","App Category","Downloads","Downloads Change (%)",'
               '"Downloads Change (Value)","Downloads Share","Revenue","Revenue Change (%)",'
               '"Revenue Change (Value)","Revenue Share","Currency"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] market size category break down - paid - gp - weekly',
     'url': '#{https}/intelligence/google-play/market-size/?data_break_down=category&countries=%s'
            '&category=medical&price=paid&iap=all&sort_by=changeInPercent&device=google-play&granularity=weekly'
            '&date=2016-07-24~2017-01-28' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Market Size Store Intelligence - Category Breakdown',
               '"Store","Device","Country","Price","Period","App Category","Downloads","Downloads Change (%)",'
               '"Downloads Change (Value)","Downloads Share","Revenue","Revenue Change (%)",'
               '"Revenue Change (Value)","Revenue Share","Currency"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] market size category break down - paid - gp - monthly',
     'url': '#{https}/intelligence/google-play/market-size/?data_break_down=category&countries=%s'
            '&category=social&price=paid&iap=all&sort_by=changeInValue&device=google-play&granularity=monthly'
            '&date=2016-01-01~2016-12-31' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Market Size Store Intelligence - Category Breakdown',
               '"Store","Device","Country","Price","Period","App Category","Downloads","Downloads Change (%)",'
               '"Downloads Change (Value)","Downloads Share","Revenue","Revenue Change (%)",'
               '"Revenue Change (Value)","Revenue Share","Currency"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] market size device break down - all - ios - weekly',
     'url': '#{https}/intelligence/ios/market-size/?data_break_down=device&device=ios&countries=%s'
            '&category=lifestyle&price=all&sort_by=value&granularity=weekly'
            '&date=2016-07-24~2017-01-28' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Market Size Store Intelligence - Device Breakdown',
               '"Store","Device","Country","Price","Period","App Category","Downloads","Downloads Change (%)",'
               '"Downloads Change (Value)","Downloads Share","Revenue","Revenue Change (%)",'
               '"Revenue Change (Value)","Revenue Share","Currency"'
               ],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] market size device break down - free - ios - monthly',
     'url': '#{https}/intelligence/ios/market-size/?data_break_down=device&device=ios&countries=%s'
            '&category=social&price=free&sort_by=changeInPercent&granularity=monthly'
            '&date=2016-01-01~2016-12-31' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Market Size Store Intelligence - Device Breakdown',
               '"Store","Device","Country","Price","Period","App Category","Downloads","Downloads Change (%)",'
               '"Downloads Change (Value)","Downloads Share","Revenue","Revenue Change (%)",'
               '"Revenue Change (Value)","Revenue Share","Currency"'
               ],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] market size device break down - paid - ios - weekly',
     'url': '#{https}/intelligence/ios/market-size/?data_break_down=device&device=ios&countries=%s'
            '&category=social&price=paid&sort_by=changeInValue&granularity=weekly'
            '&date=2016-07-24~2017-01-28' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Market Size Store Intelligence - Device Breakdown',
               '"Store","Device","Country","Price","Period","App Category","Downloads","Downloads Change (%)",'
               '"Downloads Change (Value)","Downloads Share","Revenue","Revenue Change (%)",'
               '"Revenue Change (Value)","Revenue Share","Currency"'
               ],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] market size device break down - all - gp - monthly',
     'url': '#{https}/intelligence/google-play/market-size/?data_break_down=device&countries=%s'
            '&category=lifestyle&price=all&iap=all&sort_by=value&device=google-play&granularity=monthly'
            '&date=2016-01-01~2016-12-31' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Market Size Store Intelligence - Device Breakdown',
               '"Store","Device","Country","Price","Period","App Category","Downloads","Downloads Change (%)",'
               '"Downloads Change (Value)","Downloads Share","Revenue","Revenue Change (%)",'
               '"Revenue Change (Value)","Revenue Share","Currency"'
               ],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] market size device break down - free - gp - weekly',
     'url': '#{https}/intelligence/google-play/market-size/?data_break_down=device&countries=%s'
            '&category=medical&price=free&iap=all&sort_by=changeInPercent&device=google-play&granularity=weekly'
            '&date=2016-07-24~2017-01-28' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Market Size Store Intelligence - Device Breakdown',
               '"Store","Device","Country","Price","Period","App Category","Downloads","Downloads Change (%)",'
               '"Downloads Change (Value)","Downloads Share","Revenue","Revenue Change (%)",'
               '"Revenue Change (Value)","Revenue Share","Currency"'
               ],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] market size device break down - paid - gp - monthly',
     'url': '#{https}/intelligence/google-play/market-size/?data_break_down=device&countries=%s'
            '&category=social&price=paid&iap=all&sort_by=changeInValue&device=google-play&granularity=monthly'
            '&date=2016-01-01~2016-12-31' % env_var['countryCode2'],
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Market Size Store Intelligence - Device Breakdown',
               '"Store","Device","Country","Price","Period","App Category","Downloads","Downloads Change (%)",'
               '"Downloads Change (Value)","Downloads Share","Revenue","Revenue Change (%)",'
               '"Revenue Change (Value)","Revenue Share","Currency"'
               ],
     'env': ['production', 'staging']},
    # ========================Store Unified/Single App Level====================
    {'name': '[INT-CSV] INT - GP - App Device - daily',
     'url': '#{https}/apps/google-play/app/com.king.candycrushsaga/intelligence/?data_break_down=apphistory'
            '&country=SE&granularity=daily',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence App Device',
               'Store,Device,Country,Period,App ID,App Name,Publisher ID,Publisher Name,Downloads,Revenue,Currency'
               ],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] INT - GP - App Device - weekly',
     'url': '#{https}/apps/google-play/app/com.king.candycrushsaga/intelligence/?data_break_down=apphistory'
            '&country=SE&granularity=weekly',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence App Device',
               'Store,Device,Country,Period,App ID,App Name,Publisher ID,Publisher Name,Downloads,Revenue,Currency'
               ],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] INT - GP - App Device - monthly',
     'url': '#{https}/apps/google-play/app/com.king.candycrushsaga/intelligence/?data_break_down=apphistory'
            '&country=SE&granularity=monthly',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence App Device',
               'Store,Device,Country,Period,App ID,App Name,Publisher ID,Publisher Name,Downloads,Revenue,Currency'
               ],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] INT - IOS - App Device - daily',
     'url': '#{https}/apps/ios/app/candy-crush-saga/intelligence/?country=SE&granularity=daily',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence App Device',
               'Store,Device,Country,Period,App ID,App Name,Publisher ID,Publisher Name,Downloads,Revenue,Currency'
               ],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] INT - IOS - App Device - weekly',
     'url': '#{https}/apps/ios/app/candy-crush-saga/intelligence/?country=SE&granularity=weekly',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence App Device',
               'Store,Device,Country,Period,App ID,App Name,Publisher ID,Publisher Name,Downloads,Revenue,Currency'
               ],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] INT - IOS - App Device - monthly',
     'url': '#{https}/apps/ios/app/candy-crush-saga/intelligence/?country=SE&granularity=monthly',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence App Device',
               'Store,Device,Country,Period,App ID,App Name,Publisher ID,Publisher Name,Downloads,Revenue,Currency'
               ],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] INT - GP - App - CBD - daily',
     'url': '#{https}/apps/google-play/app/com.king.candycrushsaga/intelligence/?data_break_down=countrybreakdown'
            '&granularity=daily',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence App Country Breakdown',
               'Store,Device,Country,Period,App ID,App Name,Publisher ID,Publisher Name,Downloads,Revenue,Currency'
               ],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] INT - GP - App - CBD - weekly',
     'url': '#{https}/apps/google-play/app/com.king.candycrushsaga/intelligence/?data_break_down=countrybreakdown'
            '&granularity=weekly',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence App Country Breakdown',
               'Store,Device,Country,Period,App ID,App Name,Publisher ID,Publisher Name,Downloads,Revenue,Currency'
               ],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] INT - GP - App - CBD - monthly',
     'url': '#{https}/apps/google-play/app/com.king.candycrushsaga/intelligence/?data_break_down=countrybreakdown'
            '&granularity=monthly',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence App Country Breakdown',
               'Store,Device,Country,Period,App ID,App Name,Publisher ID,Publisher Name,Downloads,Revenue,Currency'
               ],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] INT - IOS - App - CBD - daily',
     'url': '#{https}/apps/ios/app/candy-crush-saga/intelligence/?data_break_down=countrybreakdown&device=ios'
            '&granularity=daily',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence App Country Breakdown',
               'Store,Device,Country,Period,App ID,App Name,Publisher ID,Publisher Name,Downloads,Revenue,Currency'
               ],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] INT - IOS - App - CBD - weekly',
     'url': '#{https}/apps/ios/app/candy-crush-saga/intelligence/?data_break_down=countrybreakdown&device=iphone'
            '&granularity=weekly',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence App Country Breakdown',
               'Store,Device,Country,Period,App ID,App Name,Publisher ID,Publisher Name,Downloads,Revenue,Currency'
               ],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] INT - IOS - App - CBD - monthly',
     'url': '#{https}/apps/ios/app/candy-crush-saga/intelligence/?data_break_down=countrybreakdown&device=ipad'
            '&granularity=monthly',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence App Country Breakdown',
               'Store,Device,Country,Period,App ID,App Name,Publisher ID,Publisher Name,Downloads,Revenue,Currency'
               ],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Unified App history - daily',
     'url': '#{https}/apps/all-stores/app/#{uaApp1}/intelligence/?data_break_down=history&granularity=daily',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Unified App Device',
               'Device,Country,Period,Unified App,Unified App ID,Revenue,Downloads,Currency'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Unified App history - weekly',
     'url': '#{https}/apps/all-stores/app/#{uaApp1}/intelligence/?data_break_down=history&granularity=weekly',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Unified App Device',
               'Device,Country,Period,Unified App,Unified App ID,Revenue,Downloads,Currency'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Unified App history - monthly',
     'url': '#{https}/apps/all-stores/app/#{uaApp1}/intelligence/?data_break_down=history&granularity=monthly',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Unified App Device',
               'Device,Country,Period,Unified App,Unified App ID,Revenue,Downloads,Currency'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Unified App country breakdown - daily',
     'url': '#{https}/apps/all-stores/app/#{uaApp1}/intelligence/?data_break_down=countrybreakdown'
            '&granularity=daily',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Unified App Country Breakdown',
               'Country,Store,Device,Period,Unified App,Unified App ID,Downloads,Revenue,Currency'],
     'env': ['production', 'staging']},

    # ==============  Store - Companies & Publishers =================
    {'name': '[INT-CSV] Store - Company - all devices - Device Breakdown - daily',
     'url': '#{https}/company/tencent/intelligence/?data_break_down=device&device=all&country=SE'
            '&category=overall&granularity=daily&date=2017-02-01~2017-02-22&chart_type=downloads'
            '&aggregate_app=on&page_size=100&order_by=downloads&order_type=desc&page_number=0',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Company Device Breakdown',
               '"Device","Country","Category","Period","Company ID","Company Name","Downloads",'
               '"Revenue","Currency","Event"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store - Company - all devices - Device Breakdown - weekly',
     'url': '#{https}/company/tencent/intelligence/?data_break_down=device&device=all&country=SE'
            '&category=overall&granularity=weekly&date=2017-01-01~2017-02-11&chart_type=downloads'
            '&aggregate_app=on&page_size=100&order_by=downloads&order_type=desc&page_number=0',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Company Device Breakdown',
               '"Device","Country","Category","Period","Company ID","Company Name","Downloads",'
               '"Revenue","Currency","Event"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store - Company - ios - Device Breakdown - daily',
     'url': '#{https}/company/google/intelligence/?data_break_down=device&device=ios&country=BE'
            '&category=lifestyle&granularity=daily&date=2017-02-01~2017-02-28&chart_type=downloads'
            '&aggregate_app=on&page_size=100&order_by=downloads&order_type=desc&page_number=0',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Company Device Breakdown',
               '"Device","Country","Category","Period","Company ID","Company Name","Downloads",'
               '"Revenue","Currency","Event"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store - Company - ios - Device Breakdown - monthly',
     'url': '#{https}/company/google/intelligence/?data_break_down=device&device=ios&country=BE'
            '&category=lifestyle&granularity=monthly&date=2016-12-01~2017-02-28&chart_type=downloads'
            '&aggregate_app=on&page_size=100&order_by=downloads&order_type=desc&page_number=0',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Company Device Breakdown',
               '"Device","Country","Category","Period","Company ID","Company Name","Downloads",'
               '"Revenue","Currency","Event"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store - Company - gp - Device Breakdown - weekly',
     'url': '#{https}/company/tencent/intelligence/?data_break_down=device&device=google-play&country=SE&'
            'category=overall&granularity=weekly&date=2017-01-29~2017-03-04&chart_type=downloads'
            '&aggregate_app=on&page_size=100&order_by=downloads&order_type=desc&page_number=0',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Company Device Breakdown',
               '"Device","Country","Category","Period","Company ID","Company Name","Downloads",'
               '"Revenue","Currency","Event"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store - Company - gp - Device Breakdown - monthly',
     'url': '#{https}/company/tencent/intelligence/?data_break_down=device&device=google-play&country=SE'
            '&category=overall&granularity=monthly&date=2016-08-01~2017-01-31&chart_type=downloads'
            '&aggregate_app=on&page_size=100&order_by=downloads&order_type=desc&page_number=0',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Company Device Breakdown',
               '"Device","Country","Category","Period","Company ID","Company Name","Downloads",'
               '"Revenue","Currency","Event"'],
     'env': ['production', 'staging']},

    {'name': '[INT-CSV] Store - Company - all devices - App Breakdown - weekly',
     'url': '#{https}/company/tencent/intelligence/?data_break_down=app&device=all&country=SE&'
            'category=overall&granularity=weekly&date=2017-01-01~2017-02-11&chart_type=downloads&'
            'aggregate_app=on&page_size=100&order_by=downloads&order_type=desc&page_number=0',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Company App Breakdown',
               '"App","Device","Country","Category","Period","Downloads","Revenue","Currency","Is Unified",'
               '"App ID","App Code","AppURL","Publisher ID","Publisher Name","Company ID","Company Name",'
               '"Parent Company ID","Parent Company Name","App Category","App Name (Unified)",'
               '"Unified App ID","App Franchise","App Franchise ID","HQ Country"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store - Company - all devices - App Breakdown - monthly',
     'url': '#{https}/company/tencent/intelligence/?data_break_down=app&device=all&country=SE'
            '&category=overall&granularity=monthly&date=2016-07-01~2017-01-31&chart_type=downloads'
            '&aggregate_app=on&page_size=100&order_by=downloads&order_type=desc&page_number=0',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Company App Breakdown',
               '"App","Device","Country","Category","Period","Downloads","Revenue","Currency","Is Unified",'
               '"App ID","App Code","AppURL","Publisher ID","Publisher Name","Company ID","Company Name",'
               '"Parent Company ID","Parent Company Name","App Category","App Name (Unified)",'
               '"Unified App ID","App Franchise","App Franchise ID","HQ Country"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store - Company - ios - App Breakdown - daily',
     'url': '#{https}/company/tencent/intelligence/?data_break_down=app&device=ios&country=SE'
            '&category=overall&granularity=daily&date=2017-02-01~2017-02-22&chart_type=downloads'
            '&aggregate_app=on&page_size=100&order_by=downloads&order_type=desc&page_number=0',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Company App Breakdown',
               '"App","Device","Country","Category","Period","Downloads","Revenue","Currency","Is Unified",'
               '"App ID","App Code","AppURL","Publisher ID","Publisher Name","Company ID","Company Name",'
               '"Parent Company ID","Parent Company Name","App Category","App Name (Unified)",'
               '"Unified App ID","App Franchise","App Franchise ID","HQ Country"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store - Company - ios - App Breakdown - weekly',
     'url': '#{https}/company/tencent/intelligence/?data_break_down=app&device=ios&country=SE'
            '&category=overall&granularity=weekly&date=2017-01-01~2017-02-11&chart_type=downloads'
            '&aggregate_app=on&page_size=100&order_by=downloads&order_type=desc&page_number=0',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Company App Breakdown',
               '"App","Device","Country","Category","Period","Downloads","Revenue","Currency","Is Unified",'
               '"App ID","App Code","AppURL","Publisher ID","Publisher Name","Company ID","Company Name",'
               '"Parent Company ID","Parent Company Name","App Category","App Name (Unified)",'
               '"Unified App ID","App Franchise","App Franchise ID","HQ Country"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store - Company - gp - App Breakdown - weekly',
     'url': '#{https}/company/tencent/intelligence/?data_break_down=app&device=google-play&country=SE'
            '&category=overall&granularity=weekly&date=2017-01-01~2017-01-28&chart_type=downloads'
            '&aggregate_app=on&page_size=100&order_by=downloads&order_type=desc&page_number=0',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Company App Breakdown',
               '"App","Device","Country","Category","Period","Downloads","Revenue","Currency","Is Unified",'
               '"App ID","App Code","AppURL","Publisher ID","Publisher Name","Company ID","Company Name",'
               '"Parent Company ID","Parent Company Name","App Category","App Name (Unified)",'
               '"Unified App ID","App Franchise","App Franchise ID","HQ Country"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store - Company - gp - App Breakdown - monthly',
     'url': '#{https}/company/tencent/intelligence/?data_break_down=app&device=google-play&country=SE'
            '&category=overall&granularity=monthly&date=2016-08-01~2017-01-31&chart_type=downloads'
            '&aggregate_app=on&page_size=100&order_by=downloads&order_type=desc&page_number=0',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Store Intelligence', 'Report,Store Intelligence Company App Breakdown',
               '"App","Device","Country","Category","Period","Downloads","Revenue","Currency","Is Unified",'
               '"App ID","App Code","AppURL","Publisher ID","Publisher Name","Company ID","Company Name",'
               '"Parent Company ID","Parent Company Name","App Category","App Name (Unified)",'
               '"Unified App ID","App Franchise","App Franchise ID","HQ Country"'],
     'env': ['production', 'staging']},

    {'name': '[INT-CSV] Store - Publishers - ios - CBD - daily',
     'url': '#{https}/apps/ios/publisher/284882218/intelligence/?data_break_down=countrybreakdown'
            '&device=ios&category=social-networking&granularity=daily&date_range_picker=2017-01-06~2017-02-05'
            '&table_query=',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Country,Store,Device,Period,Publisher ID,Publisher Name,Category,Downloads,Revenue,Currency'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store - Publishers - ios - CBD - weekly',
     'url': '#{https}/apps/ios/publisher/284882218/intelligence/?data_break_down=countrybreakdown'
            '&device=iphone&category=social-networking&granularity=weekly&week-range-picker=2017-01-01~2017-05-05'
            '&table_query=',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Country,Store,Device,Period,Publisher ID,Publisher Name,Category,Downloads,Revenue,Currency'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store - Publishers - ios - CBD - monthly',
     'url': '#{https}/apps/ios/publisher/284882218/intelligence/?data_break_down=countrybreakdown'
            '&device=ipad&category=social-networking&granularity=monthly&month-range-picker=2016-02-01~2017-02-05'
            '&table_query=',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Country,Store,Device,Period,Publisher ID,Publisher Name,Category,Downloads,Revenue,Currency'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store - Publishers - gp - CBD - weekly',
     'url': '#{https}/apps/google-play/publisher/20200000193769/intelligence/?data_break_down=countrybreakdown'
            '&device=google-play&category=application/social&granularity=weekly'
            '&week-range-picker=2016-08-14~2017-02-05'
            '&table_query=',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Country,Store,Device,Period,Publisher ID,Publisher Name,Category,Downloads,Revenue,Currency'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Store - Publishers - gp - app breakdown - monthly',
     'url': '#{https}/apps/google-play/publisher/20200000193769/intelligence/?data_break_down=appbreakdown'
            '&country=BE&device=google-play&category=application/social&granularity=monthly'
            '&month-range-picker=2016-02-01~2017-02-05'
            '&table_query=',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App,Store,Device,Country,Period,Publisher ID,Publisher Name,Category,Downloads,Revenue,Currency'],
     'env': ['production', 'staging']},

    # =====================Audience  CAU=========================

    {'name': '[INT-CSV] Intelligence - Audience - CAU - Downloads - GP',
     'url': '#{https}/apps/google-play/app/20600000009072/intelligence/cross-app-usage/',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Audience Intelligence', 'Report,Audience Intelligence App Cross-App Usage',
               'Platform,Device,Country,Start Date,End Date,App ID,App Name,App Category, Publisher ID,'
               'Publisher Name,Rank,Affinity,Cross-App Usage,Cross-App ID,Cross-App Name,Cross-App Category,'
               'Cross-App Publisher ID,Cross-App Publisher Name'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Intelligence - Audience - CAU - Downloads - iOS',
     'url': '#{https}/apps/ios/app/284882215/intelligence/cross-app-usage/',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Audience Intelligence', 'Report,Audience Intelligence App Cross-App Usage',
               'Platform,Device,Country,Start Date,End Date,App ID,App Name,App Category, Publisher ID,'
               'Publisher Name,Rank,Affinity,Cross-App Usage,Cross-App ID,Cross-App Name,Cross-App Category,'
               'Cross-App Publisher ID,Cross-App Publisher Name'],
     'env': ['production', 'staging']},

    # =====================Audience Demographics=========================

    {'name': '[INT-CSV] Intelligence - Audience - Demographics - Downloads',
     'url': '#{https}/apps/ios/app/facebook/intelligence/demographics/',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Audience Intelligence', 'Report,Audience Intelligence App Demographics',
               'Platform,Device,Country,Start Date,End Date,App ID,App Name,App Category,App Device,'
               'Publisher ID,Publisher Name,Gender - Index Male,Gender - Index Female,Age - Index 13-24,'
               'Age - Index 25-44,Age - Index 45+,Gender - % Male,Gender - % Female,Age - % 13-24,'
               'Age - % 25-44,Age - % 45+'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Intelligence - Audience - Demographics - Downloads',
     'url': '#{https}/apps/google-play/app/20600000009072/intelligence/demographics/',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Audience Intelligence', 'Report,Audience Intelligence App Demographics',
               'Platform,Device,Country,Start Date,End Date,App ID,App Name,App Category,App Device,'
               'Publisher ID,Publisher Name,Gender - Index Male,Gender - Index Female,Age - Index 13-24,'
               'Age - Index 25-44,Age - Index 45+,Gender - % Male,Gender - % Female,Age - % 13-24,'
               'Age - % 25-44,Age - % 45+'],
     'env': ['production', 'staging']},
    # ======================Usage Top Apps================
    {'name': '[INT-CSV] usage top chart user segment - ios - weekly',
     'url': '#{https}/intelligence/usage/top/?device=ios&country=JP'
            '&granularity=weekly&user_segmentation=all_users&sort_by=value',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Usage Intelligence', 'Report,Usage Intelligence Top Apps',
               'Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,'
               'Company Name,Parent Company Name,App Name (Unified),App Franchise,Unified App ID,App Franchise ID,'
               'Company ID,Parent Company ID,Usage Penetration,Install Penetration,Open Rate,Active Users,'
               'Total Minutes,Avg Sessions Per User,Avg Session Duration,Avg Time Per User'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] usage top chart user segment - ipad - monthly',
     'url': '#{https}/intelligence/usage/top/?device=ipad&country=CZ'
            '&granularity=monthly&user_segmentation=all_users&sort_by=changeInPercent',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Usage Intelligence', 'Report,Usage Intelligence Top Apps',
               'Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,'
               'Company Name,Parent Company Name,App Name (Unified),App Franchise,Unified App ID,App Franchise ID,'
               'Company ID,Parent Company ID,Usage Penetration,Install Penetration,Open Rate,Active Users,'
               'Total Minutes,Avg Sessions Per User,Avg Session Duration,Avg Time Per User'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] usage top chart user segment - iphone - weekly',
     'url': '#{https}/intelligence/usage/top/android/?device=iphone&country=JP'
            '&granularity=weekly&user_segmentation=all_users&sort_by=value',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Usage Intelligence', 'Report,Usage Intelligence Top Apps',
               'Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,'
               'Company Name,Parent Company Name,App Name (Unified),App Franchise,Unified App ID,'
               'App Franchise ID,Company ID,Parent Company ID,Usage Penetration,Install Penetration,'
               'Open Rate,Active Users,Total Minutes,Avg Sessions Per User,Avg Session Duration,'
               'Avg Time Per User,Avg Active Days,% Active Days,Share of Category Time,'
               'MB Per User,MB Per Session'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] usage top chart user segment - Android - weekly',
     'url': '#{https}/intelligence/usage/top/android/?device=iphone&country=JP'
            '&granularity=weekly&user_segmentation=all_users&sort_by=value&table_query=&platform=ios&'
            '#device=android&country=BE&category=21&&user_segmentation=all_users'
            '&sort_by=value&table_query=',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Usage Intelligence', 'Report,Usage Intelligence Top Apps',
               'Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,'
               'Company Name,Parent Company Name,App Name (Unified),App Franchise,Unified App ID,'
               'App Franchise ID,Company ID,Parent Company ID,Usage Penetration,Install Penetration,'
               'Open Rate,Active Users,Total Minutes,Avg Sessions Per User,Avg Session Duration,'
               'Avg Time Per User,Avg Active Days,% Active Days,Share of Category Time,'
               'MB Per User,MB Per Session']},
    {'name': '[INT-CSV] usage top chart user segment - Android - monthly',
     'url': '#{https}/intelligence/usage/top/android/?device=iphone&country=JP'
            '&granularity=monthly&user_segmentation=all_users&sort_by=value&table_query=&platform=ios&'
            '#device=android_tablet&country=BE&category=21&user_segmentation=all_users'
            '&sort_by=value&table_query=',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Usage Intelligence', 'Report,Usage Intelligence Top Apps',
               'Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,'
               'Company Name,Parent Company Name,App Name (Unified),App Franchise,Unified App ID,'
               'App Franchise ID,Company ID,Parent Company ID,Usage Penetration,Install Penetration,'
               'Open Rate,Active Users,Total Minutes,Avg Sessions Per User,Avg Session Duration,'
               'Avg Time Per User,Avg Active Days,% Active Days,Share of Category Time,'
               'MB Per User,MB Per Session'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] usage top chart user segment - Android - weekly',
     'url': '#{https}/intelligence/usage/top/android/?device=iphone&country=JP&category=6012'
            '&granularity=weekly&user_segmentation=females_13_24&sort_by=value&platform=ios'
            '#device=android&country=BE&category=21&granularity=weekly&user_segmentation=all_users'
            '&sort_by=value',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Usage Intelligence', 'Report,Usage Intelligence Top Apps',
               'Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,'
               'Company Name,Parent Company Name,App Name (Unified),App Franchise,Unified App ID,'
               'App Franchise ID,Company ID,Parent Company ID,Usage Penetration,Install Penetration,'
               'Open Rate,Active Users,Total Minutes,Avg Sessions Per User,Avg Session Duration,'
               'Avg Time Per User,Avg Active Days,% Active Days,Share of Category Time,'
               'MB Per User,MB Per Session'], 'env': ['production', 'staging']},
    # ======================Usage PYA=====================
    {'name': '[INT-CSV] usage pya user segment app used - IOS - monthly',
     'url': '#{https}/intelligence/apps/usage/?device=ios&android_country=BE&granularity=monthly'
            '&user_segmentation=all_users&sort_by=value&table_query=&country=BE',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,'
               'Company Name,Parent Company Name,App Name (Unified),App Franchise,Unified App ID,'
               'App Franchise ID,Company ID,Parent Company ID,Usage Penetration,Install Penetration,Open Rate,'
               'Active Users,Total Minutes,Avg Sessions Per User,Avg Session Duration,Avg Time Per User'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] usage pya user segment app used - ipad - weekly',
     'url': '#{https}/intelligence/apps/usage/?device=ipad&android_country=BE&granularity=weekly'
            '&user_segmentation=all_users&sort_by=value&table_query=&country=BE',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,'
               'Company Name,Parent Company Name,App Name (Unified),App Franchise,Unified App ID,'
               'App Franchise ID,Company ID,Parent Company ID,Usage Penetration,Install Penetration,Open Rate,'
               'Active Users,Total Minutes,Avg Sessions Per User,Avg Session Duration,Avg Time Per User'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] usage pya user segment app used - iphone - weekly',
     'url': '#{https}/intelligence/apps/usage/?device=iphone&android_country=JP&granularity=weekly'
            '&user_segmentation=females_13_24&sort_by=changeInPercent&table_query=&country=JP',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,'
               'Company Name,Parent Company Name,App Name (Unified),App Franchise,Unified App ID,'
               'App Franchise ID,Company ID,Parent Company ID,Usage Penetration,Install Penetration,Open Rate,'
               'Active Users,Total Minutes,Avg Sessions Per User,Avg Session Duration,Avg Time Per User'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] usage pya user segment app used - iphone - weekly',
     'url': '#{https}/intelligence/apps/usage/?device=iphone&android_country=JP&granularity=weekly'
            '&user_segmentation=males_25_44&sort_by=value&table_query=&country=JP',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,'
               'Company Name,Parent Company Name,App Name (Unified),App Franchise,Unified App ID,'
               'App Franchise ID,Company ID,Parent Company ID,Usage Penetration,Install Penetration,Open Rate,'
               'Active Users,Total Minutes,Avg Sessions Per User,Avg Session Duration,Avg Time Per User'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] usage pya user segment app used - Android - monthly',
     'url': '#{https}/intelligence/apps/usage/?device=android&android_country=BE&granularity=monthly'
            '&user_segmentation=all_users&sort_by=changeInPercent&table_query=&country=BE',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,Company Name,'
               'Parent Company Name,App Name (Unified),App Franchise,Unified App ID,App Franchise ID,Company ID,'
               'Parent Company ID,Usage Penetration,Install Penetration,Open Rate,Active Users,Total Minutes,'
               'Avg Sessions Per User,Avg Session Duration,Avg Time Per User,Avg Active Days,% Active Days,'
               'Share of Category Time,MB Per User,MB Per Session'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] usage pya user segment app used - android_phone - weekly',
     'url': '#{https}/intelligence/apps/usage/?device=android_phone&android_country=BE&granularity=weekly'
            '&user_segmentation=all_13_24&sort_by=value&table_query=&country=BE',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,Company Name,'
               'Parent Company Name,App Name (Unified),App Franchise,Unified App ID,App Franchise ID,Company ID,'
               'Parent Company ID,Usage Penetration,Install Penetration,Open Rate,Active Users,Total Minutes,'
               'Avg Sessions Per User,Avg Session Duration,Avg Time Per User,Avg Active Days,% Active Days,'
               'Share of Category Time,MB Per User,MB Per Session'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] usage pya user segment app used - android_phone - weekly',
     'url': '#{https}/intelligence/apps/usage/?device=android_phone&android_country=JP&granularity=weekly'
            '&user_segmentation=females_13_24&sort_by=value&table_query=&country=JP',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,Company Name,'
               'Parent Company Name,App Name (Unified),App Franchise,Unified App ID,App Franchise ID,Company ID,'
               'Parent Company ID,Usage Penetration,Install Penetration,Open Rate,Active Users,Total Minutes,'
               'Avg Sessions Per User,Avg Session Duration,Avg Time Per User,Avg Active Days,% Active Days,'
               'Share of Category Time,MB Per User,MB Per Session'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] usage pya user segment app used - android_tablet - monthly',
     'url': '#{https}/intelligence/apps/usage/?device=android_tablet&android_country=BE&granularity=monthly'
            '&user_segmentation=all_users&sort_by=changeInPercent&table_query=&country=BE',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,Company Name,'
               'Parent Company Name,App Name (Unified),App Franchise,Unified App ID,App Franchise ID,Company ID,'
               'Parent Company ID,Usage Penetration,Install Penetration,Open Rate,Active Users,Total Minutes,'
               'Avg Sessions Per User,Avg Session Duration,Avg Time Per User,Avg Active Days,% Active Days,'
               'Share of Category Time,MB Per User,MB Per Session'],
     'env': ['production', 'staging']},
    # ===================Usage App Device& App CBD====================
    {'name': '[INT-CSV]  usage app level - IOS - daily',
     'url': '#{https}/apps/ios/app/553834731/usage/?data_break_down=device&country=US&granularity=daily'
            '&chart_type=penetration&table_query=',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,'
               'Company Name,Parent Company Name,App Name (Unified),App Franchise,Unified App ID,'
               'App Franchise ID,Company ID,Parent Company ID,Usage Penetration,Install Penetration,Open Rate,'
               'Active Users,Total Minutes,Avg Sessions Per User,Avg Session Duration,Avg Time Per User'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV]  usage app level - IOS - weekly',
     'url': '#{https}/apps/ios/app/553834731/usage/?data_break_down=device&country=US&granularity=weekly'
            '&chart_type=penetration&table_query=',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,'
               'Company Name,Parent Company Name,App Name (Unified),App Franchise,Unified App ID,'
               'App Franchise ID,Company ID,Parent Company ID,Usage Penetration,Install Penetration,Open Rate,'
               'Active Users,Total Minutes,Avg Sessions Per User,Avg Session Duration,Avg Time Per User'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV]  usage app level - IOS - monthly',
     'url': '#{https}/apps/ios/app/553834731/usage/?data_break_down=device&country=US&granularity=monthly'
            '&chart_type=penetration&table_query=',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,'
               'Company Name,Parent Company Name,App Name (Unified),App Franchise,Unified App ID,'
               'App Franchise ID,Company ID,Parent Company ID,Usage Penetration,Install Penetration,Open Rate,'
               'Active Users,Total Minutes,Avg Sessions Per User,Avg Session Duration,Avg Time Per User'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV]  usage CBD - IOS - daily',
     'url': '#{https}/apps/ios/app/553834731/usage/?data_break_down=country&device=ios&granularity=daily'
            '&chart_type=penetration&table_query=',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,'
               'Company Name,Parent Company Name,App Name (Unified),App Franchise,Unified App ID,'
               'App Franchise ID,Company ID,Parent Company ID,Usage Penetration,Active Users,Share of Users,'
               'Install Penetration,Share of Installs,Open Rate'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV]  usage CBD - iphone - weekly',
     'url': '#{https}/apps/ios/app/553834731/usage/?data_break_down=country&device=iphone&granularity=weekly'
            '&chart_type=penetration&table_query=',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,'
               'Company Name,Parent Company Name,App Name (Unified),App Franchise,Unified App ID,'
               'App Franchise ID,Company ID,Parent Company ID,Usage Penetration,Active Users,Share of Users,'
               'Install Penetration,Share of Installs,Open Rate'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV]  usage CBD - ipad - monthly',
     'url': '#{https}/apps/ios/app/553834731/usage/?data_break_down=country&device=ipad&granularity=monthly'
            '&chart_type=penetration&table_query=',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,'
               'Company Name,Parent Company Name,App Name (Unified),App Franchise,Unified App ID,'
               'App Franchise ID,Company ID,Parent Company ID,Usage Penetration,Active Users,Share of Users,'
               'Install Penetration,Share of Installs,Open Rate'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV]  usage app level - Android - daily',
     'url': '#{https}/apps/google-play/app/20600000578686/usage/?data_break_down=device&country=JP'
            '&granularity=daily&chart_type=penetration&table_query=',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,'
               'Company Name,Parent Company Name,App Name (Unified),App Franchise,Unified App ID,'
               'App Franchise ID,Company ID,Parent Company ID,Usage Penetration,Install Penetration,'
               'Open Rate,Active Users,Total Minutes,Avg Sessions Per User,Avg Session Duration,'
               'Avg Time Per User,Avg Active Days,% Active Days,Share of Category Time,MB Per User,MB Per Session'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV]  usage app level - Android - weekly',
     'url': '#{https}/apps/google-play/app/20600000578686/usage/?data_break_down=device&country=JP'
            '&granularity=weekly&chart_type=penetration&table_query=',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,'
               'Company Name,Parent Company Name,App Name (Unified),App Franchise,Unified App ID,'
               'App Franchise ID,Company ID,Parent Company ID,Usage Penetration,Install Penetration,'
               'Open Rate,Active Users,Total Minutes,Avg Sessions Per User,Avg Session Duration,'
               'Avg Time Per User,Avg Active Days,% Active Days,Share of Category Time,MB Per User,MB Per Session'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV]  usage app level - Android - monthly',
     'url': '#{https}/apps/google-play/app/20600000578686/usage/?data_break_down=device&country=JP'
            '&granularity=monthly&chart_type=penetration&table_query=',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,'
               'Company Name,Parent Company Name,App Name (Unified),App Franchise,Unified App ID,'
               'App Franchise ID,Company ID,Parent Company ID,Usage Penetration,Install Penetration,'
               'Open Rate,Active Users,Total Minutes,Avg Sessions Per User,Avg Session Duration,'
               'Avg Time Per User,Avg Active Days,% Active Days,Share of Category Time,MB Per User,MB Per Session'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV]  usage CBD - Android - daily',
     'url': '#{https}/apps/google-play/app/20600000578686/usage/?data_break_down=country&device=android'
            '&granularity=daily&chart_type=penetration&table_query=',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,'
               'Company Name,Parent Company Name,App Name (Unified),App Franchise,Unified App ID,'
               'App Franchise ID,Company ID,Parent Company ID,Usage Penetration,Share of Users,'
               'Install Penetration,Open Rate,Active Users,Total Minutes,Avg Sessions Per User,'
               'Avg Session Duration,Avg Time Per User,Avg Active Days,% Active Days,'
               'Share of Category Time,MB Per User,MB Per Session'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV]  usage CBD - android_phone - weekly',
     'url': '#{https}/apps/google-play/app/20600000578686/usage/?data_break_down=country&device=android_phone'
            '&granularity=weekly&chart_type=penetration&table_query=',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,'
               'Company Name,Parent Company Name,App Name (Unified),App Franchise,Unified App ID,'
               'App Franchise ID,Company ID,Parent Company ID,Usage Penetration,Share of Users,'
               'Install Penetration,Open Rate,Active Users,Total Minutes,Avg Sessions Per User,'
               'Avg Session Duration,Avg Time Per User,Avg Active Days,% Active Days,'
               'Share of Category Time,MB Per User,MB Per Session'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV]  usage CBD - android_tablet - monthly',
     'url': '#{https}/apps/google-play/app/20600000578686/usage/?data_break_down=country&device=android_tablet'
            '&granularity=monthly&chart_type=penetration&table_query=',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['Platform,Device,Country,Period,App ID,App Name,App Category,Publisher ID,Publisher Name,'
               'Company Name,Parent Company Name,App Name (Unified),App Franchise,Unified App ID,'
               'App Franchise ID,Company ID,Parent Company ID,Usage Penetration,Share of Users,'
               'Install Penetration,Open Rate,Active Users,Total Minutes,Avg Sessions Per User,'
               'Avg Session Duration,Avg Time Per User,Avg Active Days,% Active Days,'
               'Share of Category Time,MB Per User,MB Per Session'],
     'env': ['production', 'staging']},
    # ===========================INT MKT Creative==============================
    # {'name': '[INT-CSV] INT MKT Creative',
    #  'url': '#{https}/intelligence/marketing/creatives/?view=list&device=iphone&country=JP'
    #         '&category=overall&network=all&granularity=weekly&picker_type=advertiser'
    #         '&formats=-1&dimensions=-1&min_active_days=1&is_visible=0&order_by=pub_count'
    #         '&order_type=desc&page_number=0&page_size=100&app_id=',
    #  'click': [EXPORT_BUTTON, EXPORT_CSV],
    #  'check': ['App Annie Marketing Intelligence', 'Report,Marketing Intelligence Creatives',
    #            '"Platform","Device","Country","Ad Platform","Period","Creative","Advertiser App ID",'
    #            '"Advertiser App Name","Category","Format","Dimension","Apps Seen In","Top Countries Seen In",'
    #            '"First Seen","Last Seen","Active (Days)","Publisher ID","Publisher Name","Company Name",'
    #            '"Parent Company Name","App Name (Unified)","App Franchise","Unified App ID",'
    #            '"App Franchise ID","Company ID","Parent Company ID"'],
    #  'env': ['production', 'staging']},
    {'name': '[INT-CSV] INT MKT Creative - ipad - weekly',
     'url': '#{https}/intelligence/marketing/creatives/?view=list&device=ipad&country=JP'
            '&category=applications&network=adcolony&granularity=weekly&picker_type=advertiser'
            '&formats=3&dimensions=-1&min_active_days=1&is_visible=0&order_by=pub_count'
            '&order_type=desc&page_number=0&page_size=100&app_id=',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Marketing Intelligence', 'Report,Marketing Intelligence Creatives',
               '"Platform","Device","Country","Ad Platform","Period","Creative","Advertiser App ID",'
               '"Advertiser App Name","Category","Format","Dimension","Apps Seen In","Share of Network",'
               '"Share of Advertiser","Top Countries Seen In","First Seen","Last Seen","Active (Days)",'
               '"Publisher ID","Publisher Name","Company Name","Parent Company Name","App Name (Unified)",'
               '"App Franchise","Unified App ID","App Franchise ID","Company ID","Parent Company ID"'
               ],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] INT MKT Creative - android_table - weekly',
     'url': '#{https}/intelligence/marketing/creatives/?view=list&device=android_tablet&country=JP'
            '&category=game&network=chartboost&granularity=weekly&picker_type=advertiser'
            '&formats=2&dimensions=2&min_active_days=1&is_visible=0&order_by=pub_count'
            '&order_type=desc&page_number=0&page_size=100&app_id=',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Marketing Intelligence', 'Report,Marketing Intelligence Creatives',
               '"Platform","Device","Country","Ad Platform","Period","Creative","Advertiser App ID",'
               '"Advertiser App Name","Category","Format","Dimension","Apps Seen In","Share of Network",'
               '"Share of Advertiser","Top Countries Seen In","First Seen","Last Seen","Active (Days)",'
               '"Publisher ID","Publisher Name","Company Name","Parent Company Name","App Name (Unified)",'
               '"App Franchise","Unified App ID","App Franchise ID","Company ID","Parent Company ID"'],
     'env': ['production', 'staging']},

    # ========================== INT MKT Advertisers===============
    {'name': '[INT-CSV] Intelligence Advertisers- Downloads - iphone - weekly',
     'url': '#{https}/intelligence/marketing/advertisers/?device=iphone&country=JP&category=overall'
            '&network=admob&granularity=weekly&sort_by=value&order_by=app_sov&order_type=desc&page_number=0'
            '&page_size=100',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Marketing Intelligence', 'Report,Marketing Intelligence Advertisers',
               '"Platform","Device","Country","Ad Platform","Period","Advertiser App ID","Advertiser App Name",'
               '"Category","# Ad Platforms","Ad Platforms (Advertised In)","Apps Seen In","Creatives","Campaigns",'
               '"Share of Network","Share of Network (Change %)","Publisher Share of Network",'
               '"Publisher Share of Network (Change %)","Publisher ID","Publisher Name","Company Name",'
               '"Parent Company Name","App Name (Unified)","App Franchise","Unified App ID","App Franchise ID",'
               '"Company ID","Parent Company ID"'],
     'env': ['production', 'staging']},
    # ==========================INT MKT Ad Monetization==============
    {'name': '[INT-CSV] Intelligence Ad Monetization - Downloads - iphone - weekly',
     'url': '#{https}/intelligence/marketing/ad-monetization/?device=iphone&country=JP&category=overall'
            '&network=admob&granularity=weekly&sort_by=value&order_by=app_sov&order_type=desc'
            '&page_number=0&page_size=100',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Marketing Intelligence', 'Report,Marketing Intelligence Ad Monetization',
               '"Platform","Device","Country","Ad Platform","Period","App ID","App Name","Category",'
               '"Downloads Rank","# Ad Platforms","Ad Platforms (Integrated)","Share of Network",'
               '"Share of Network (Change %)","Publisher ID","Publisher Name","Company Name",'
               '"Parent Company Name","App Name (Unified)","App Franchise","Unified App ID",'
               '"App Franchise ID","Company ID","Parent Company ID"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Intelligence Ad Monetization - Downloads - android_phone - weekly',
     'url': '#{https}/intelligence/marketing/ad-monetization/?device=android_phone&country=JP&category=application'
            '&network=facebook&granularity=weekly&sort_by=value&order_by=app_sov&order_type=desc'
            '&page_number=0&page_size=100',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Marketing Intelligence', 'Report,Marketing Intelligence Ad Monetization',
               '"Platform","Device","Country","Ad Platform","Period","App ID","App Name","Category",'
               '"Downloads Rank","# Ad Platforms","Ad Platforms (Integrated)","Share of Network",'
               '"Share of Network (Change %)","Publisher ID","Publisher Name","Company Name",'
               '"Parent Company Name","App Name (Unified)","App Franchise","Unified App ID",'
               '"App Franchise ID","Company ID","Parent Company ID"'],
     'env': ['production', 'staging']},
    # =========================INT MKT - App Level===========================
    {'name': '[INT-CSV] Intelligence marketing advertiser app - ios',
     'url': '#{https}/apps/ios/app/#{iosMktIntApp1}/intelligence/marketing/',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Marketing Intelligence', 'Report,Marketing Intelligence Advertiser App Overview',
               '"Ad Platform","Device","Country","Period","App ID","App Name","App Category","Share of Network",'
               '"Share of Network (Change %)","First Seen","Last Seen","Creatives","Publisher ID","Publisher Name",'
               '"Company Name","Parent Company Name","App Name (Unified)","App Franchise","Unified App ID",'
               '"App Franchise ID","Company ID","Parent Company ID"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Intelligence marketing advertiser app - android',
     'url': '#{https}/apps/google-play/app/#{gpMktIntApp1}/intelligence/marketing/',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Marketing Intelligence', 'Report,Marketing Intelligence Advertiser App Overview',
               '"Ad Platform","Device","Country","Period","App ID","App Name","App Category","Share of Network",'
               '"Share of Network (Change %)","First Seen","Last Seen","Creatives","Publisher ID","Publisher Name",'
               '"Company Name","Parent Company Name","App Name (Unified)","App Franchise","Unified App ID",'
               '"App Franchise ID","Company ID","Parent Company ID"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Intelligence marketing advertiser app - ipad - weekly',
     'url': '#{https}/apps/ios/app/mobile-strike/intelligence/marketing/?view_type=advertiser'
            '&data_break_down=network&device=ipad&country=JP&category=overall&network=all'
            '&sort_by=value&order_by=app_sov&order_type=desc&page_number=0&page_size=100&granularity=weekly',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Marketing Intelligence', 'Report,Marketing Intelligence Advertiser App Overview',
               '"Ad Platform","Device","Country","Period","App ID","App Name","App Category","Share of Network",'
               '"Share of Network (Change %)","First Seen","Last Seen","Creatives","Publisher ID",'
               '"Publisher Name","Company Name","Parent Company Name","App Name (Unified)",'
               '"App Franchise","Unified App ID","App Franchise ID","Company ID","Parent Company ID"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Intelligence marketing advertiser app - iphone - weekly',
     'url': '#{https}/apps/ios/app/mobile-strike/intelligence/marketing/?view_type=advertiser'
            '&data_break_down=network&device=iphone&country=JP&category=overall&network=all'
            '&sort_by=value&order_by=app_sov&order_type=desc&page_number=0&page_size=100&granularity=weekly',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Marketing Intelligence', 'Report,Marketing Intelligence Advertiser App Overview',
               '"Ad Platform","Device","Country","Period","App ID","App Name","App Category","Share of Network",'
               '"Share of Network (Change %)","First Seen","Last Seen","Creatives","Publisher ID",'
               '"Publisher Name","Company Name","Parent Company Name","App Name (Unified)",'
               '"App Franchise","Unified App ID","App Franchise ID","Company ID","Parent Company ID"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Intelligence marketing advertiser app - android - network - weekly',
     'url': '#{https}/apps/google-play/app/com.hcg.cok.gp/intelligence/marketing/?view_type=advertiser'
            '&data_break_down=network&device=android_phone&country=JP&category=overall&network=admob'
            '&granularity=weekly&sort_by=value&order_by=app_sov&order_type=desc&page_number=0&page_size=100',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Marketing Intelligence', 'Report,Marketing Intelligence Advertiser App Overview',
               '"Ad Platform","Device","Country","Period","App ID","App Name","App Category","Share of Network",'
               '"Share of Network (Change %)","First Seen","Last Seen","Creatives","Publisher ID",'
               '"Publisher Name","Company Name","Parent Company Name","App Name (Unified)",'
               '"App Franchise","Unified App ID","App Franchise ID","Company ID","Parent Company ID"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Intelligence marketing advertiser app - android - monthly',
     'url': '#{https}/apps/google-play/app/com.hcg.cok.gp/intelligence/marketing/?view_type=advertiser'
            '&data_break_down=network&device=android_tablet&country=JP&category=overall&network=admob'
            '&granularity=monthly&sort_by=value&order_by=app_sov&order_type=desc&page_number=0&page_size=100',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Marketing Intelligence', 'Report,Marketing Intelligence Advertiser App Overview',
               '"Ad Platform","Device","Country","Period","App ID","App Name","App Category","Share of Network",'
               '"Share of Network (Change %)","First Seen","Last Seen","Creatives","Publisher ID",'
               '"Publisher Name","Company Name","Parent Company Name","App Name (Unified)",'
               '"App Franchise","Unified App ID","App Franchise ID","Company ID","Parent Company ID"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Intelligence marketing advertiser app - android - ad_monetization',
     'url': '#{https}/apps/google-play/app/com.hcg.cok.gp/intelligence/marketing/?view_type=advertiser'
            '&data_break_down=ad_monetization&device=android_phone&country=JP&category=overall&network=admob'
            '&granularity=weekly&sort_by=value&order_by=app_sov&order_type=desc&page_number=0&page_size=100',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Marketing Intelligence', 'Report,Marketing Intelligence Advertiser App - Seen In Breakdown',
               '"Platform","Device","Country","Ad Platform","Period","App ID","App Name","App Category",'
               '"# Ad Platforms","Ad Platforms (Integrated)","Share of Impressions",'
               '"Share of Impressions (Change %)","First Seen","Last Seen","Active (Days)",'
               '"Publisher ID","Publisher Name","Company Name","Parent Company Name",'
               '"App Name (Unified)","App Franchise","Unified App ID","App Franchise ID",'
               '"Company ID","Parent Company ID"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Intelligence marketing advertiser app - ios - ad_monetization',
     'url': '#{https}/apps/ios/app/mobile-strike/intelligence/marketing/?view_type=advertiser'
            '&data_break_down=ad_monetization&country=JP&granularity=weekly&device=iphone&category=overall'
            '&network=admob&sort_by=value&order_by=app_sov&order_type=desc&page_number=0&page_size=100',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Marketing Intelligence', 'Report,Marketing Intelligence Advertiser App - Seen In Breakdown',
               '"Platform","Device","Country","Ad Platform","Period","App ID","App Name","App Category",'
               '"# Ad Platforms","Ad Platforms (Integrated)","Share of Impressions",'
               '"Share of Impressions (Change %)","First Seen","Last Seen","Active (Days)",'
               '"Publisher ID","Publisher Name","Company Name","Parent Company Name",'
               '"App Name (Unified)","App Franchise","Unified App ID","App Franchise ID",'
               '"Company ID","Parent Company ID"'],
     'env': ['production', 'staging']},

    # =========================INT MKT - Ad Platforms===========================
    {'name': '[INT-CSV] Intelligence - MKT - Ad Platforms - Android - monthly',
     'url': '#{https}/intelligence/marketing/ad-platforms/?market=android&granularity=monthly&date=2017-02-01',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Marketing Intelligence', 'Report,Marketing Intelligence Ad Platforms',
               '"Ad Platform","Platform","Country","Period","App Category","Apps Analyzed","Apps Integrated",'
               '"% Apps Integrated","% Top 100 Apps Integrated","% Downloads Reached","CPI - 25","CPI - 50",'
               '"CPI - 75","Avg CTR","Avg CVR","Avg Install Rate"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Intelligence - MKT - Ad Platforms - Android - weekly',
     'url': '#{https}/intelligence/marketing/ad-platforms/?market=android&granularity=weekly&date=2017-03-12',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Marketing Intelligence', 'Report,Marketing Intelligence Ad Platforms',
               '"Ad Platform","Platform","Country","Period","App Category","Apps Analyzed","Apps Integrated",'
               '"% Apps Integrated","% Top 100 Apps Integrated","% Downloads Reached","CPI - 25","CPI - 50",'
               '"CPI - 75","Avg CTR","Avg CVR","Avg Install Rate"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Intelligence - MKT - Ad Platforms - iOS - monthly',
     'url': '#{https}/intelligence/marketing/ad-platforms/?market=ios&granularity=monthly&date=2017-02-01',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Marketing Intelligence', 'Report,Marketing Intelligence Ad Platforms',
               '"Ad Platform","Platform","Country","Period","App Category","Apps Analyzed","Apps Integrated",'
               '"% Apps Integrated","% Top 100 Apps Integrated","% Downloads Reached","CPI - 25","CPI - 50",'
               '"CPI - 75","Avg CTR","Avg CVR","Avg Install Rate"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Intelligence - MKT - Ad Platforms - iOS - weekly',
     'url': '#{https}/intelligence/marketing/ad-platforms/?market=ios&granularity=weekly&date=2017-03-12',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Marketing Intelligence', 'Report,Marketing Intelligence Ad Platforms',
               '"Ad Platform","Platform","Country","Period","App Category","Apps Analyzed","Apps Integrated",'
               '"% Apps Integrated","% Top 100 Apps Integrated","% Downloads Reached","CPI - 25","CPI - 50",'
               '"CPI - 75","Avg CTR","Avg CVR","Avg Install Rate"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Intelligence - MKT - Ad Platforms CBD - Android - monthly',
     'url': '#{https}/intelligence/marketing/ad-platforms/?market=android&country=JP&category=overall'
            '&date=2017-02-01&granularity=monthly&network=chartboost&data_break_down=country',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Marketing Intelligence', 'Report,Marketing Intelligence Ad Platforms - Country Breakdown',
               '"Country","Platform","Ad Platform","Period","App Category","Apps Analyzed","Apps Integrated",'
               '"% Apps Integrated","% Top 100 Apps Integrated","% Downloads Reached",'
               '"Ad Platform #1 - by SDK integration","Ad Platform #2 - by SDK integration",'
               '"Ad Platform #3 - by SDK integration","Ad Platform #4 - by SDK integration",'
               '"Ad Platform #5 - by SDK integration","CPI - 25","CPI - 50","CPI - 75","Avg CTR","Avg CVR",'
               '"Avg Install Rate"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Intelligence - MKT - Ad Platforms CBD - Android - weekly',
     'url': '#{https}/intelligence/marketing/ad-platforms/?market=android&country=JP&category=overall'
            '&granularity=weekly&network=chartboost&data_break_down=country&date=2017-03-12',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Marketing Intelligence', 'Report,Marketing Intelligence Ad Platforms - Country Breakdown',
               '"Country","Platform","Ad Platform","Period","App Category","Apps Analyzed","Apps Integrated",'
               '"% Apps Integrated","% Top 100 Apps Integrated","% Downloads Reached",'
               '"Ad Platform #1 - by SDK integration","Ad Platform #2 - by SDK integration",'
               '"Ad Platform #3 - by SDK integration","Ad Platform #4 - by SDK integration",'
               '"Ad Platform #5 - by SDK integration","CPI - 25","CPI - 50","CPI - 75","Avg CTR","Avg CVR",'
               '"Avg Install Rate"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Intelligence - MKT - Ad Platforms CBD - iOS- monthly',
     'url': '#{https}/intelligence/marketing/ad-platforms/?market=ios&country=JP&category=overall&granularity=monthly'
            '&date=2017-02-01&network=admob&data_break_down=country',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Marketing Intelligence', 'Report,Marketing Intelligence Ad Platforms - Country Breakdown',
               '"Country","Platform","Ad Platform","Period","App Category","Apps Analyzed","Apps Integrated",'
               '"% Apps Integrated","% Top 100 Apps Integrated","% Downloads Reached",'
               '"Ad Platform #1 - by SDK integration","Ad Platform #2 - by SDK integration",'
               '"Ad Platform #3 - by SDK integration","Ad Platform #4 - by SDK integration",'
               '"Ad Platform #5 - by SDK integration","CPI - 25","CPI - 50","CPI - 75","Avg CTR","Avg CVR",'
               '"Avg Install Rate"'],
     'env': ['production', 'staging']},
    {'name': '[INT-CSV] Intelligence - MKT - Ad Platforms CBD - iOS - weekly',
     'url': '#{https}/intelligence/marketing/ad-platforms/?market=ios&country=JP&category=overall&granularity=weekly'
            '&network=admob&data_break_down=country&date=2017-03-12',
     'click': [EXPORT_BUTTON, EXPORT_CSV],
     'check': ['App Annie Marketing Intelligence', 'Report,Marketing Intelligence Ad Platforms - Country Breakdown',
               '"Country","Platform","Ad Platform","Period","App Category","Apps Analyzed","Apps Integrated",'
               '"% Apps Integrated","% Top 100 Apps Integrated","% Downloads Reached",'
               '"Ad Platform #1 - by SDK integration","Ad Platform #2 - by SDK integration",'
               '"Ad Platform #3 - by SDK integration","Ad Platform #4 - by SDK integration",'
               '"Ad Platform #5 - by SDK integration","CPI - 25","CPI - 50","CPI - 75","Avg CTR","Avg CVR",'
               '"Avg Install Rate"'],
     'env': ['production', 'staging']},
]

debug_csv_cases = [
]

async_csv_cases = storestats_async_csv_cases + int_async_csv_cases
# async_csv_cases = debug_csv_cases
