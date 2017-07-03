# Copyright (c) 2015 App Annie Inc. All rights reserved.
# coding=utf-8
# ==============  Please read bellow before modify the cases =================


# cases should be modified by QA with any new feature deployed
# if there is no QA available, dev also can do that, but please ask any QA to review the cases
# before push to master, please test it on your local enviroument or staging


# The variable in URL that defined as #{variable_name} will be read from settings.coffee
# For example: '#{https}/dashboard/#{appAccountId}/' equals to settings.https + '/dashboard/' + settings.appAccountId
# while settings.https is calculated from 'https://' + settings.domain + '.appannie.com'


# demo cases:
# { 'name': '<Description, or page title>',
# 'url': '<URL>',
#   'check': ['<static css selector>', '<another>', ...,
#           <'dynamic css selector: after ajax call'>, <'another'>, ...]},
from tests.quick_smoke.smoke_utils import get_env_var

env_var = get_env_var()
BREADCRUMB_COMPANY = env_var['BREADCRUMB_COMPANY']
BREADCRUMB_PUBLISHER = env_var['BREADCRUMB_PUBLISHER']
BREADCRUMB_UA_NO_LINK = env_var['BREADCRUMB_UA_NO_LINK']
BREADCRUMB_UA_LINK = env_var['BREADCRUMB_UA_LINK']
BREADCRUMB_ITEM_SINGLE = env_var['BREADCRUMB_ITEM_SINGLE']
BREADCRUMB_APP_EDITION = env_var['BREADCRUMB_APP_EDITION']
JUMP_TO_LINK = '.table-jump-to'
ASSET_ICON = '.asset-icon'
ASSET_NAME = '.asset-name'
PUB_ACCOUNT = '.publisher-with-platform'
COMPANY_INFO = '.company-info'
PRICE = '.price.price-iap'
RELEASE_DATE = '.date.tbl-col-date'
GLOBAL_SIDEBAR = '.global-sidebar'
GLOBAL_SIDEBAR_HOME = '[data-name="dashboard_home"]'
GLOBAL_SIDEBAR_MY_APP_ANALYTICS = '[data-name="my_app_analytics"]'
GLOBAL_SIDEBAR_MARKET_INTELLIGENCE = '[data-name="market_intelligence"]'
LEARN_MENU = '.hi-learn'
USER_MENU_PAID = '.hi-user-paid'
USER_MENU_FREE = '.hi-user-free'

FULL_MODE = [GLOBAL_SIDEBAR, GLOBAL_SIDEBAR_HOME, GLOBAL_SIDEBAR_MY_APP_ANALYTICS, GLOBAL_SIDEBAR_MARKET_INTELLIGENCE,
             LEARN_MENU]
FULL_MODE_FREE = FULL_MODE + [USER_MENU_FREE]
FULL_MODE_PAID = FULL_MODE + [USER_MENU_PAID]
MINI_SIDEBAR = '.min-menu'
MINI_MODE = [MINI_SIDEBAR, LEARN_MENU, USER_MENU_PAID]
cases_after_login = [
    # ==============  Home =================
    {'name': '[CROSS] Home',
     'url': '#{https}/',
     'check': ['#hero']},
    {'name': '[CROSS] Home-failover',
     'url': '#{https}/home-failover/',
     'check': ['.page_home']},
    {'name': '[CROSS] Product Home',
     'url': '#{https}/dashboard/home/',
     'check': ['.dashboard-quicklink', '.link-content.carousel.slide'] + FULL_MODE_PAID},
    # {'name': '[CROSS] get started page',
    #  'url': '#{https}/dashboard/home/?activate=1',
    #  'check': ['#get-started']},

    # ==============  Onboarding =================
    {'name': '[CROSS] Onboarding Welcome Page',
     'url': '#{https}/explore/welcome/',
     'check': ["ul.menu li.current a[href='/explore/welcome/']",
               'div.explore.left', 'div.explore.right']},
    {'name': '[CROSS] Onboarding Market Data Page',
     'url': '#{https}/explore/marketdata/',
     'check': ["ul.menu li.current a[href='/explore/marketdata/']", 'a.info-card[card-id="md_ftf_tc"]']},
    {'name': '[CROSS] Onboarding Analytics Page',
     'url': '#{https}/explore/analytics/',
     'check': ["ul.menu li.current a[href='/explore/analytics/']", 'a.info-card[card-id="an_ftf_ca"]']},

    # =============  An App Comparator  ============================
    # -------------  Downloads  -----------------------
    {'name': '[AN] Comparator Downloads Product',
     'url': '#{https}/comparator/downloads/',
     'check': ['.comparator-container', '.table-row', '.col-app', '.main-row'] + FULL_MODE_PAID},
    {'name': '[AN] Comparator Downloads Product',
     'url': '#{https}/comparator/downloads/?breakdown=product',
     'check': ['.comparator-container', '.table-row', '.col-app', '.main-row']},
    {'name': '[AN] Comparator Downloads Product',
     'url': '#{https}/comparator/downloads/?breakdown=country',
     'check': ['.comparator-container', '.table-row', '.col-country', '.main-row']},
    {'name': '[AN] Comparator Downloads Product',
     'url': '#{https}/comparator/downloads/?breakdown=platform',
     'check': ['.comparator-container', '.table-row', '.col-platform', '.main-row']},
    {'name': '[AN] Comparator Downloads Product',
     'url': '#{https}/comparator/downloads/?breakdown=publisher',
     'check': ['.comparator-container', '.table-row', '.col-publisher', '.main-row']},
    {'name': '[AN] Comparator Downloads Product',
     'url': '#{https}/comparator/downloads/?breakdown=source',
     'check': ['.comparator-container', '.table-row', '.main-row']},
    # -------------  Revenue  -----------------------
    {'name': '[AN] Comparator Revenue Product',
     'url': '#{https}/comparator/revenue/',
     'check': ['.comparator-container', '.table-row', '.col-app', '.main-row']},
    {'name': '[AN] Comparator Revenue Product',
     'url': '#{https}/comparator/revenue/?breakdown=product',
     'check': ['.comparator-container', '.table-row', '.col-app', '.main-row']},
    {'name': '[AN] Comparator Revenue Product',
     'url': '#{https}/comparator/revenue/?breakdown=country',
     'check': ['.comparator-container', '.table-row', '.col-country', '.main-row']},
    {'name': '[AN] Comparator Revenue Product',
     'url': '#{https}/comparator/revenue/?breakdown=platform',
     'check': ['.comparator-container', '.table-row', '.col-platform', '.main-row']},
    {'name': '[AN] Comparator Revenue Product',
     'url': '#{https}/comparator/revenue/?breakdown=publisher',
     'check': ['.comparator-container', '.table-row', '.col-publisher', '.main-row']},
    {'name': '[AN] Comparator Revenue Product',
     'url': '#{https}/comparator/revenue/?breakdown=source',
     'check': ['.comparator-container', '.table-row', '.main-row']},
    # -------------  Usage  ------------------
    {'name': '[AN] Comparator Usage Product',
     'url': '#{https}/comparator/itc-usage/',
     'check': ['.comparator-container', '.table-row', '.col-app', '.main-row']},
    {'name': '[AN] Comparator Usage Product',
     'url': '#{https}/comparator/itc-usage/?breakdown=product_id',
     'check': ['.comparator-container', '.table-row', '.col-app', '.main-row']},
    {'name': '[AN] Comparator Usage Country',
     'url': '#{https}/comparator/itc-usage/?breakdown=country',
     'check': ['.comparator-container', '.table-row', '.main-row']},
    {'name': '[AN] Comparator Usage Platform',
     'url': '#{https}/comparator/itc-usage/?breakdown=platform',
     'check': ['.comparator-container', '.table-row', '.col-platform', '.main-row']},
    {'name': '[AN] Comparator Usage Publisher',
     'url': '#{https}/comparator/itc-usage/?breakdown=publisher',
     'check': ['.comparator-container', '.table-row', '.col-publisher', '.main-row']},
    # -------------  Overview  -----------------------
    {'name': '[AN] Comparator Overview Product',
     'url': '#{https}/comparator/',
     'check': ['.comparator-container', '.table-row', '.col-app', '.main-row']},
    {'name': '[AN] Comparator Overview Product',
     'url': '#{https}/comparator/?breakdown=product',
     'check': ['.comparator-container', '.table-row', '.col-app', '.main-row']},
    {'name': '[AN] Comparator Overview Product',
     'url': '#{https}/comparator/?breakdown=country',
     'check': ['.comparator-container', '.table-row', '.col-country', '.main-row']},
    {'name': '[AN] Comparator Overview Product',
     'url': '#{https}/comparator/?breakdown=platform',
     'check': ['.comparator-container', '.table-row', '.col-platform', '.main-row']},
    {'name': '[AN] Comparator Overview Product',
     'url': '#{https}/comparator/?breakdown=publisher',
     'check': ['.comparator-container', '.table-row', '.col-publisher', '.main-row']},

    # ================= AN Account pages ==================
    # ------------App Account------------
    {'name': '[AN] itc Dashboard',
     'url': '#{https}/dashboard/#{itcAccountId}/',
     'check': ['.comparator-container', '.table-row'] + FULL_MODE_PAID},
    {'name': '[AN] amazon Dashboard',
     'url': '#{https}/dashboard/#{amzAccountId}/',
     'check': ['.comparator-container', '.table-row']},
    {'name': '[AN] google-play Dashboard',
     'url': '#{https}/dashboard/#{gpAccountId}/',
     'check': ['.comparator-container', '.table-row']},
    {'name': '[AN] windows-phone Dashboard',
     'url': '#{https}/dashboard/#{wpAccountId}/',
     'check': ['.comparator-container', '.table-row']},
    {'name': '[AN] windows-store Dashboard',
     'url': '#{https}/dashboard/#{wsAccountId}/',
     'check': ['.comparator-container', '.table-row']},
    {'name': '[AN]  app share',
     'url': '#{https}/dashboard/shared/?vertical=apps',
     'check': ['tbody:nth-child(2) td.no-permission', 'tbody:nth-child(4) td.no-permission'],
     'env': ['production', 'staging']},

    # =============== SS pages =====================
    # ------------Top------------
    {'name': '[SS] ios Top',
     'url': '#{https}/apps/ios/top-chart/',
     'check': ['div.dashboard-table'] + FULL_MODE_PAID,
     'env': ['production', 'staging']},
    {'name': '[SS] appletv Top',
     'url': '#{https}/apps/appletv/top-chart/',
     'check': ['div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[SS] google-play Top',
     'url': '#{https}/apps/google-play/top-chart/',
     'check': ['div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[SS] amazon Top',
     'url': '#{https}/apps/amazon-appstore/top-chart/',
     'check': ['div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[SS] windows-phone Top',
     'url': '#{https}/apps/windows-phone/top-chart/',
     'check': ['div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[SS] mac Top',
     'url': '#{https}/apps/mac/top-chart/',
     'check': ['div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[SS] windows Top',
     'url': '#{https}/apps/windows-store/top-chart/',
     'check': ['div.dashboard-table'],
     'env': ['production', 'staging']},
    # ------------Single Feed-----------
    {'name': '[SS] ios Single Free',
     'url': '#{https}/apps/ios/top-chart/?country=US&feed=Free',
     'check': ['div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[SS] ios Single Paid',
     'url': '#{https}/apps/ios/top-chart/?country=US&feed=Paid',
     'check': ['div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[SS] ios Single Grossing',
     'url': '#{https}/apps/ios/top-chart/?country=US&feed=Grossing',
     'check': ['div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[SS] Googleplay Single Free',
     'url': '#{https}/apps/google-play/top-chart/?country=US&feed=Free',
     'check': ['div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[SS] Googleplay Single Paid',
     'url': '#{https}/apps/google-play/top-chart/?country=US&feed=Paid',
     'check': ['div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[SS] Googleplay Single Grossing',
     'url': '#{https}/apps/google-play/top-chart/?country=US&feed=Grossing',
     'check': ['div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[SS] Googleplay Single New Free',
     'url': '#{https}/apps/google-play/top-chart/?country=US&feed=New%2DFree',
     'check': ['div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[SS] Googleplay Single New Paid',
     'url': '#{https}/apps/google-play/top-chart/?country=US&feed=New%2DPaid',
     'check': ['div.dashboard-table'],
     'env': ['production', 'staging']},

    # ------------Top matrix------------
    # We check that we have the correct tab selected, and that the matrix table is present.
    # Selenium thinks table.table-matrix as a whole is always invisible, so we check an item inside the table instead.
    {'name': '[SS] ios Top Matrix - United States',
     'url': '#{https}/apps/ios/matrix/',
     'check': ['li.top_ios.current', 'table.table-matrix tr td div.matrix_icon']},
    {'name': '[SS] ios Top Matrix - Overall',
     'url': '#{https}/apps/ios/matrix/?category=overall',
     'check': ['li.top_ios.current', 'table.table-matrix tr td div.matrix_icon']},

    {'name': '[SS] google-play Top Matrix - United States',
     'url': '#{https}/apps/google-play/matrix/',
     'check': ['li.top_gp.current', 'table.table-matrix tr td div.matrix_icon']},
    {'name': '[SS] google-play Top Matrix - Overall',
     'url': '#{https}/apps/google-play/matrix/?category=overall',
     'check': ['li.top_gp.current', 'table.table-matrix tr td div.matrix_icon']},

    {'name': '[SS] mac Top Matrix - United States',
     'url': '#{https}/apps/mac/matrix/',
     'check': ['li.top_mac.current', 'table.table-matrix tr td div.matrix_icon']},
    {'name': '[SS] mac Top Matrix - Overall',
     'url': '#{https}/apps/mac/matrix/?category=mac-overall',
     'check': ['li.top_mac.current', 'table.table-matrix tr td div.matrix_icon']},

    # ------------ Keyword ranks ------------
    {'name': '[ASO] Keyword Ranks - All stores',
     'url': '#{https}/intelligence/marketing/aso/all-stores/keyword-top/',
     'check': ['#aa-app', 'li.top_ios.current']},
    {'name': '[ASO] Keyword Ranks - iOS',
     'url': '#{https}/intelligence/marketing/aso/ios/keyword-top/',
     'check': ['#aa-app', 'li.top_ios.current']},
    {'name': '[ASO] Keyword Ranks - Google Play',
     'url': '#{https}/intelligence/marketing/aso/google-play/keyword-top/',
     'check': ['#aa-app', 'li.top_gp.current']},

    # ------------ Keyword Compare ------------
    # TODO: check whether results are available when the page is fully implemented
    {'name': '[ASO] Keyword Compare',
     'url': '#{https}/intelligence/marketing/aso/keyword-compare/',
     'check': ['#aa-app', '.dashboard-sub-header'],
     'env': ['production', 'staging']},

    # ------------Search------------
    {'name': '[SS] ios App Search',
     'url': '#{https}/search/?q=iFOREX&vertical=apps&market=ios',
     'check': ['.aa-popup-container', '.search-result-left'] + MINI_MODE},
    {'name': '[SS] appletv App Search',
     'url': '#{https}/search/?q=netflix&vertical=apps&market=appletv',
     'check': ['.aa-popup-container', '.search-result-left']},
    {'name': '[SS] google-play App Search',
     'url': '#{https}/search/?q=iFOREX&vertical=apps&market=google-play',
     'check': ['.aa-popup-container', '.search-result-left']},
    {'name': '[SS] amazon App Search',
     'url': '#{https}/search/?q=tomcat&vertical=apps&market=amazon-appstore&page=last',
     'check': ['.aa-popup-container', '.search-result-left']},
    {'name': '[SS] mac App Search',
     'url': '#{https}/search/?q=tomcat&vertical=apps&market=mac',
     'check': ['.aa-popup-container', '.search-result-left']},
    {'name': '[SS] windows phone Search',
     'url': '#{https}/search/?q=Jmeter&vertical=apps&market=windows-phone',
     'check': ['.aa-popup-container', '.search-result-left']},
    {'name': '[SS] windows store Search',
     'url': '#{https}/search/?q=Jmeter&vertical=apps&market=windows-store',
     'check': ['.aa-popup-container', '.search-result-left']},

    # =============== DNA pages ====================
    {'name': '[INT-WEB] DNA Company Publishers',
     'url': '#{https}/company/supercell/',
     'check': ['.main-app-content', '.price_with_iap', BREADCRUMB_COMPANY, ASSET_ICON, ASSET_NAME, JUMP_TO_LINK,
               PUB_ACCOUNT, PRICE, RELEASE_DATE] + MINI_MODE},
    {'name': '[INT-WEB] DNA Company Apps',
     'url': '#{https}/company/#{companySlug}/publishers/',
     'check': ['.main-app-content', '.number_with_unit', BREADCRUMB_COMPANY]},
    {'name': '[INT-WEB] DNA  Unified App',
     'url': '#{https}/apps/all-stores/app/#{uaApp1}/',
     'check': ['.main-app-content', '.price-iap', BREADCRUMB_COMPANY, BREADCRUMB_UA_NO_LINK,
               BREADCRUMB_APP_EDITION, ASSET_ICON, ASSET_NAME, JUMP_TO_LINK, COMPANY_INFO, PRICE, RELEASE_DATE]},
    {'name': '[INT-WEB] DNA  Unified App - INT',
     'url': '#{https}/apps/all-stores/app/#{uaApp1}/intelligence/',
     'check': ['div.dashboard-table', 'td.percentage-with-bar', BREADCRUMB_COMPANY, BREADCRUMB_UA_NO_LINK,
               BREADCRUMB_APP_EDITION]},
    {'name': '[INT-WEB] DNA  App Franchise',
     'url': '#{https}/apps/all-stores/franchise/#{franchiseSlug}/',
     'check': ['.main-app-content', '.price-iap', '.name.ng-binding']},
    {'name': '[INT-WEB] DNA Publisher - ios',
     'url': '#{https}/apps/ios/publisher/rovio-entertainment-ltd/',
     'check': ['.item.ng-binding', '.price-iap', BREADCRUMB_COMPANY, BREADCRUMB_ITEM_SINGLE, ASSET_ICON, ASSET_NAME,
               JUMP_TO_LINK, PRICE, RELEASE_DATE]},
    {'name': '[INT-WEB] DNA  appletv Publisher',
     'url': '#{https}/apps/appletv/publisher/netflix-inc/',
     'check': ['.item.ng-binding', '.price-iap', BREADCRUMB_COMPANY, BREADCRUMB_ITEM_SINGLE, ASSET_ICON, ASSET_NAME,
               JUMP_TO_LINK, PRICE, RELEASE_DATE]},
    {'name': '[INT-WEB] DNA Publisher - gp',
     'url': '#{https}/apps/google-play/publisher/20200000195109/',
     'check': ['.item.ng-binding', '.price-iap', BREADCRUMB_COMPANY, BREADCRUMB_ITEM_SINGLE, ASSET_ICON, ASSET_NAME,
               JUMP_TO_LINK, PRICE, RELEASE_DATE]},
    {'name': '[INT-WEB] DNA  amazon Publisher',
     'url': '#{https}/apps/amazon-appstore/publisher/30200000017466/',
     'check': ['.item.ng-binding', '.price-iap', BREADCRUMB_COMPANY, BREADCRUMB_ITEM_SINGLE, ASSET_ICON, ASSET_NAME,
               JUMP_TO_LINK, PRICE, RELEASE_DATE]},
    {'name': '[INT-WEB] DNA  windows phone Publisher',
     'url': '#{https}/apps/windows-phone/publisher/electronic-arts/',
     'check': ['.item.ng-binding', '.price-iap', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE, ASSET_ICON, ASSET_NAME,
               JUMP_TO_LINK, PRICE, RELEASE_DATE]},
    {'name': '[INT-WEB] DNA  windows store Publisher',
     'url': '#{https}/apps/windows-store/publisher/microsoft-studios/',
     'check': ['.item.ng-binding', '.price-iap', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE, ASSET_ICON, ASSET_NAME,
               JUMP_TO_LINK, PRICE, RELEASE_DATE]},

    # ../tests/quick_smoke/cases/cases_web.py========== AD Account pages ==================
    {'name': '[ADV] Ad Revenue Dashboard - Ad Platform',
     'url': '#{https}/ad_dashboard/ad_revenue/',
     'check': ['.aa-dashboard-container', '.money-num']},
    {'name': '[ADV] Ad Revenue Dashboard - country',
     'url': '#{https}/ad_dashboard/ad_revenue/?data_break_down=country',
     'check': ['.aa-dashboard-container', '.money-num']},
    {'name': '[ADV] Ad Revenue Dashboard - store',
     'url': '#{https}/ad_dashboard/ad_revenue/?data_break_down=store',
     'check': ['.aa-dashboard-container', '.money-num']},
    {'name': '[ADV] Ad Revenue Dashboard - app ',
     'url': '#{https}/ad_dashboard/ad_revenue/?data_break_down=app',
     'check': ['.aa-dashboard-container', '.money-num']},
    {'name': '[ADV] Ad Revenue Dashboard - site',
     'url': '#{https}/ad_dashboard/ad_revenue/?data_break_down=ad_item',
     'check': ['.aa-dashboard-container', '.money-num']},
    {'name': '[ADV] Ad Expense Dashboard - Ad Platform',
     'url': '#{https}/ad_dashboard/ad_expense/',
     'check': ['.aa-dashboard-container', '.money-num']},
    {'name': '[ADV] Ad Expense Dashboard - country',
     'url': '#{https}/ad_dashboard/ad_expense/?data_break_down=country',
     'check': ['.aa-dashboard-container', '.money-num']},
    {'name': '[ADV] Ad Expense Dashboard - store',
     'url': '#{https}/ad_dashboard/ad_expense/?data_break_down=store',
     'check': ['.aa-dashboard-container', '.money-num']},
    {'name': '[ADV] Ad Expense Dashboard - app',
     'url': '#{https}/ad_dashboard/ad_expense/?data_break_down=app',
     'check': ['.aa-dashboard-container', '.money-num']},
    {'name': '[ADV] Ad Expense Dashboard - site',
     'url': '#{https}/ad_dashboard/ad_expense/?data_break_down=ad_item',
     'check': ['.aa-dashboard-container', '.money-num'],
     'env': ['production', 'staging']},

    # ================= SingleAssets pages ==================
    # ------------ITC------------
    # --AN--
    {'name': '[AN] itc Downloads',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/downloads/',
     'check': ['.aa-dashboard-container', '.number-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[AN] itc Revenue',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/revenue/',
     'check': ['.aa-dashboard-container', '.table-row', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[AN] itc IAP',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp2}/iap/',
     'check': ['.aa-dashboard-container', '.money-num',
               'a.option[data-id=subscription_units]', 'a.option[data-id=renewal_units]',
               BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    # {'name': '[AN] itc analytics Store Page Views',
    #  'url': '#{https}/dashboard/50320/item/568017486/appstoreviews/',
    #  'check': ['.aa-dashboard-container', '.number-num',
    #            'a.option[data-id=installations_per_views]']},
    {'name': '[AN] itc analytics Store Page Views',
     'url': '#{https}/dashboard/#{sharedItcAccountId}/item/#{itcAccountApp}/storeviews/',
     'check': ['.aa-dashboard-container', '.number-num',
               'a.option[data-id=app_store_views]', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[AN] itc analytics Paying Users',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp}/payingusers/',
     'check': ['.aa-dashboard-container', '.number-num',
               'a.option[data-id=paying_users]', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[AN] itc analytics Usage',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp}/itc-usage/',
     'check': ['.aa-dashboard-container', '.table-row',
               'a.option[data-id=active_last_30_days]', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    # --Ad--
    {'name': '[ADV] itc Ad Revenue - site',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp}/ad_revenue/',
     'check': ['.chart-render', '.money-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[ADV] itc Ad Expense - campaign',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{itcAccountApp}/ad_expense/',
     'check': ['.chart-render', '.money-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    # --SS--
    {'name': '[SS] itc Detail',
     'url': '#{https}/apps/ios/app/#{iosAppSlug}/details/?account_id=#{itcAccountId}',
     'check': ['#app_content', '.ss-report-note', '.app-screenshots', "#app_sidebar .links",
               '.app-content-shade.shade', '.app-content-shade.read-more-shade',
               "#app_sidebar .app-info-version", "#app_sidebar .app-info-iap",
               "#app_sidebar .app-info-rating", "#app_sidebar .about_app", BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION]},
    # {'name': '[SS] iMessage Detail',
    #  'url': '#{https}/apps/ios/app/#{iosiMessageId}/details/',
    #  'check': ['#app_content', '.ss-report-note', '.app-screenshots', "#app_sidebar .links",
    #            "#app_sidebar .app-info-version", "#app_sidebar .about_app",
    #            ".data-section .item.ng-scope.ng-binding",
    #            BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION]},
    {'name': '[SS] itc Daily Rank',
     'url': '#{https}/apps/ios/app/#{iosAppSlug}/app-ranking/?account_id=#{itcAccountId}',
     'check': ['#ranks', 'tr.stores', BREADCRUMB_COMPANY, BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[SS] itc Rank History',
     'url': '#{https}/apps/ios/app/#{iosAppSlug}/rank-history/?account_id=#{itcAccountId}',
     'check': ['#aa-app', '.aa-chart-options', '.rank-timezone-container', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION]},
    {'name': '[SS] itc Rank History hourly download',
     'url': '#{https}/apps/ios/app/#{iosAppSlug}/rank-history/'
            '?vtype=hour&view=rank&account_id=#{itcAccountId}&start_date=%s&end_date=%s' % (
                env_var['start_date3'], env_var['end_date3']),
     'check': ['#aa-app', '.aa-chart-options', '.highcharts-container svg',
               '.rank-timezone-container', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION]},
    {'name': '[SS] itc Rank History hourly gross',
     'url': '#{https}/apps/ios/app/#{iosAppSlug}/rank-history/'
            '?vtype=hour&view=grossing&account_id=#{itcAccountId}&start_date=%s&end_date=%s' % (
                env_var['start_date3'], env_var['end_date3']),
     'check': ['#aa-app', '.aa-chart-options', '.highcharts-container svg',
               '.rank-timezone-container', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION]},
    {'name': '[ASO] itc Keywords',
     'url': '#{https}/apps/ios/app/#{iosAppSlug}/keywords/?account_id=#{itcAccountId}',
     'check': ['.dashboard-view-container', '.rank-change', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[SS] itc Featured',
     'url': '#{https}/apps/ios/app/#{ownIOSAppSlug}/featured/?account_id=#{itcAccountId}',
     'check': ['.dashboard-sub-header', 'div.metrics-picker', 'div.control-group',
               'div.dashboard-table', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE],
     'env': ['production', 'staging']},
    {'name': '[SS] itc Ratings',
     'url': '#{https}/apps/ios/app/#{ownIOSAppSlug}/ratings/?account_id=#{itcAccountId}',
     'check': ['#rating_container', '.store-ratings', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[SS] itc Reviews',
     'url': '#{https}/apps/ios/app/#{ownIOSAppSlug}/reviews/?account_id=#{itcAccountId}',
     'check': ['.aa-info-columns-app', '.ratings-summary', '.chart-render', BREADCRUMB_PUBLISHER,
               BREADCRUMB_ITEM_SINGLE]},
    {'name': '[SS] itc Events',
     'url': '#{https}/apps/ios/app/#{ownIOSAppSlug}/events/?account_id=#{itcAccountId}',
     'check': ['#events_list', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[SS] itc Timeline',
     'url': '#{https}/apps/ios/app/#{ownIOSAppSlug}/timeline/?account_id=#{itcAccountId}',
     'check': ['#aa-app', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[SS] itc Native app Detail',
     'url': '#{https}/apps/ios/app/#{nativeAppId}/details/',
     'check': ['a[data-clipboard-text="#{nativeAppId}"]', BREADCRUMB_COMPANY, BREADCRUMB_UA_LINK,
               BREADCRUMB_APP_EDITION]},
    # --Int--
    {'name': '[INT-WEB] App Intelligence - History',
     'url': '#{https}/apps/ios/app/#{ownIOSAppSlug}/intelligence/?account_id=#{itcAccountId}',
     'check': ['.dashboard-table', 'th.number', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE] + MINI_MODE},
    {'name': '[INT-WEB] App Intelligence - Country',
     'url': '#{https}/apps/ios/app/#{ownIOSAppSlug}/intelligence/?account_id=#{itcAccountId}'
            '&data_break_down=countrybreakdown',
     'check': ['.dashboard-table', 'th.number', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},

    # --App Bundle--
    {'name': '[SS] App Bundle - Details',
     'url': '#{https}/apps/ios/app/#{iosAppBundleId}/details/',
     'check': ['#app_content', '.ss-report-note', '.app-screenshots', "#app_sidebar .links",
               "#app_sidebar .about_app", BREADCRUMB_COMPANY, BREADCRUMB_ITEM_SINGLE],
     'env': ['production', 'staging']},

    # ------------GP------------
    # --AN--
    {'name': '[AN] google-play Downloads',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/downloads/',
     'check': ['.aa-dashboard-container', '.number-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE] + MINI_MODE},
    {'name': '[AN] google-play Revenue',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/revenue/',
     'check': ['.aa-dashboard-container', '.table-row', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[AN] google-play IAP',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/iap/',
     'check': ['.aa-dashboard-container', '.money-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[AN] google-play Store Page Views',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/storeviews/',
     'check': ['.aa-dashboard-container', '.number-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    # --Ad--
    {'name': '[ADV] google-play Ad Revenue - country',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/ad_revenue/?data_break_down=country',
     'check': ['.chart-render', '.money-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[ADV] google-play Ad Expense - country',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/ad_expense/?data_break_down=country',
     'check': ['.chart-render', '.money-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    # --SS--
    {'name': '[SS] google-play Detail',
     'url': '#{https}/apps/google-play/app/#{gpApp1}/details/?account_id=#{gpAccountId}',
     'check': ['#app_content', '.ss-report-note', '.app-screenshots', "#app_sidebar .links",
               '.app-content-shade.read-more-shade',
               "#app_sidebar .app-info-version", "#app_sidebar .app-info-rating",
               "#app_sidebar .about_app", BREADCRUMB_COMPANY, BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION]},
    {'name': '[SS] google-play Daily Rank',
     'url': '#{https}/apps/google-play/app/#{gpApp}/app-ranking/?account_id=#{gpAccountId}',
     'check': ['#ranks', '.data-table .stores', BREADCRUMB_COMPANY, BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[SS] google-play Rank History',
     'url': '#{https}/apps/google-play/app/#{gpApp}/rank-history/?account_id=#{gpAccountId}',
     'check': ['#aa-app', '.aa-chart-options', '.rank-timezone-container', BREADCRUMB_COMPANY, BREADCRUMB_UA_LINK,
               BREADCRUMB_APP_EDITION]},
    {'name': '[ASO] google-play Keywords',
     'url': '#{https}/apps/google-play/app/#{gpApp}/keywords/?account_id=#{gpAccountId}',
     'check': ['.dashboard-view-container', '.rank-change', BREADCRUMB_COMPANY, BREADCRUMB_UA_LINK,
               BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[SS] google-play Featured',
     'url': '#{https}/apps/google-play/app/#{gpApp}/featured/?account_id=#{gpAccountId}',
     'check': ['.dashboard-sub-header', 'div.metrics-picker', 'div.control-group',
               'div.dashboard-table', 'tr.main-row.table-row', BREADCRUMB_COMPANY, BREADCRUMB_UA_LINK,
               BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']
     },
    {'name': '[SS] google-play Advanced Feature',
     'url': '#{https}/apps/google-play/app/#{gpApp}/featured/',
     'check': ['.dashboard-sub-header', 'div.metrics-picker', 'div.control-group',
               'div.dashboard-table', 'tr.main-row.table-row',
               BREADCRUMB_COMPANY, BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[SS] google-play Reviews',
     'url': '#{https}/apps/google-play/app/#{gpApp}/reviews/?account_id=#{gpAccountId}',
     'check': ['.aa-info-columns-app', '.ratings-summary', '.chart-render', BREADCRUMB_COMPANY, BREADCRUMB_UA_LINK,
               BREADCRUMB_APP_EDITION]},
    {'name': '[SS] google-play Timeline',
     'url': '#{https}/apps/google-play/app/#{gpApp}/timeline/?account_id=#{gpAccountId}',
     'check': ['#aa-app', BREADCRUMB_COMPANY, BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION]},
    # --Int--
    {'name': '[INT-WEB] google-play Intelligence - history',
     'url': '#{https}/apps/google-play/app/#{gpApp}/intelligence/?account_id=#{gpAccountId}',
     'check': ['.dashboard-table', 'th.number', BREADCRUMB_COMPANY, BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION]},
    {'name': '[INT-WEB] google-play Intelligence - country',
     'url': '#{https}/apps/google-play/app/#{gpApp}/intelligence/?account_id=#{gpAccountId}'
            '&data_break_down=countrybreakdown',
     'check': ['.dashboard-table', 'th.number', BREADCRUMB_COMPANY, BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION]},
    # ------------AMZ------------
    # --AN--
    {'name': '[AN] amazon Downloads',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/downloads/',
     'check': ['.aa-dashboard-container', '.number-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[AN] amazon Revenue',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/revenue/',
     'check': ['.aa-dashboard-container', '.table-row', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[AN] amazon IAP',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/iap/',
     'check': ['.aa-dashboard-container', '.money-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    # --Ad--
    {'name': '[ADV] amazon Ad Revenue - Ad Platform',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/ad_revenue/?data_break_down=ad_account',
     'check': ['.chart-render', '.money-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[ADV] amazon Ad Expense - Ad Platform',
     'url': '#{https}/dashboard/#{amzAccountId}/item/#{amzAccountApp}/ad_expense/?data_break_down=ad_account',
     'check': ['.chart-render', '.money-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    # --SS--
    {'name': '[SS] amazon Detail',
     'url': '#{https}/apps/amazon-appstore/app/#{amazonApp}/details/?account_id=#{amzAccountId}',
     'check': ['#app_content', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[SS] amazon Daily Rank',
     'url': '#{https}/apps/amazon-appstore/app/#{amazonApp}/app-ranking/?account_id=#{amzAccountId}',
     'check': ['#ranks', '.stores', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE],
     'env': ['production', 'staging']},
    {'name': '[SS] amazon Rank History',
     'url': '#{https}/apps/amazon-appstore/app/#{amazonApp}/rank-history/?account_id=#{amzAccountId}',
     'check': ['#aa-app', '.aa-chart-options', '.rank-timezone-container', BREADCRUMB_PUBLISHER,
               BREADCRUMB_ITEM_SINGLE]},
    {'name': '[SS] amazon Reviews',
     'url': '#{https}/apps/amazon-appstore/app/#{amzAccountApp}/reviews/?account_id=#{amzAccountId}',
     'check': ['.aa-info-columns-app', '.ratings-summary', '.chart-render', BREADCRUMB_PUBLISHER,
               BREADCRUMB_ITEM_SINGLE]},
    {'name': '[SS] amazon Timeline',
     'url': '#{https}/apps/amazon-appstore/app/#{amazonApp}/timeline/?account_id=#{amzAccountId}',
     'check': ['#aa-app', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},

    # ------------Apple TV------
    # --AN--
    {'name': '[AN] appleTV Downloads',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/downloads/',
     'check': ['.aa-dashboard-container', '.number-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[AN] appleTV Revenue',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/revenue/',
     'check': ['.aa-dashboard-container', '.table-row', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[AN] appleTV IAP',
     'url': '#{https}/dashboard/#{itcAccountId}/item/#{appleTvAccountApp}/iap/',
     'check': ['.aa-dashboard-container', 'a.option[data-id=subscription_units]', 'a.option[data-id=renewal_units]',
               ]},

    # --SS--
    {'name': '[SS] appletv Detail',
     'url': '#{https}/apps/appletv/app/#{appleTVSlug}/details/',
     'check': ['#app_content', '.ss-report-note', '.app-screenshots', "#app_sidebar .links",
               "#app_sidebar .app-info-version", "#app_sidebar .app-info-iap", "#app_sidebar .app-info-rating",
               "#app_sidebar .about_app", BREADCRUMB_COMPANY, BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION]},
    {'name': '[SS] appletv Daily Rank',
     'url': '#{https}/apps/appletv/app/#{appleTVSlug}/app-ranking/',
     'check': ['#ranks', '.data-table .stores', BREADCRUMB_COMPANY, BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[SS] appletv Rank History',
     'url': '#{https}/apps/appletv/app/#{appleTVSlug}/rank-history/',
     'check': ['#aa-app', '.aa-chart-options', '.rank-timezone-container', BREADCRUMB_COMPANY, BREADCRUMB_UA_LINK,
               BREADCRUMB_APP_EDITION]},
    {'name': '[SS] appletv Ratings',
     'url': '#{https}/apps/appletv/app/#{appleTVSlug}/ratings',
     'check': ['#rating_container', '.store-ratings', BREADCRUMB_COMPANY, BREADCRUMB_UA_LINK,
               BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[SS] appletv Timeline',
     'url': '#{https}/apps/appletv/app/#{appleTVSlug}/timeline',
     'check': ['#aa-app', BREADCRUMB_COMPANY, BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION]},

    # ------------Windows Phone------------
    # --AN--
    {'name': '[AN] WP Downloads',
     'url': '#{https}/dashboard/#{wpAccountId}/item/#{wpAccountApp2}/downloads/',
     'check': ['.dashboard-meta.x-clear', '.number-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[AN] WP Revenue',
     'url': '#{https}/dashboard/#{wpAccountId}/item/#{wpAccountApp2}/revenue/',
     'check': ['.dashboard-meta.x-clear', '.money-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    # --SS--
    {'name': '[SS] SS windows phone Detail',
     'url': '#{https}/apps/windows-phone/app/#{wpAppSlug}/details/',
     'check': ['#app_content', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[SS] SS windows phone Daily Rank',
     'url': '#{https}/apps/windows-phone/app/#{wpAppSlug}/app-ranking/',
     'check': ['#ranks', '#app_rankings', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[SS] SS windows phone Rank History',
     'url': '#{https}/apps/windows-phone/app/#{wpAppSlug}/rank-history/',
     'check': ['#aa-app', '.aa-chart-options', '.rank-timezone-container', BREADCRUMB_PUBLISHER,
               BREADCRUMB_ITEM_SINGLE]},
    {'name': '[SS] SS windows phone Reviews',
     'url': '#{https}/apps/windows-phone/app/#{wpAppSlug}/reviews/',
     'check': ['.aa-info-columns-app', '.ratings-summary', '.chart-render', BREADCRUMB_PUBLISHER,
               BREADCRUMB_ITEM_SINGLE]},
    {'name': '[SS] SS windows phone Timeline',
     'url': '#{https}/apps/windows-phone/app/#{wpAppSlug}/timeline/',
     'check': ['#aa-app', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},

    # ------------Windows Store------------
    # --AN--
    {'name': '[AN] WS Downloads',
     'url': '#{https}/dashboard/#{wsAccountId}/item/#{wsAccountApp2}/downloads/',
     'check': ['.dashboard-meta.x-clear', '.number-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[AN] WS Revenue',
     'url': '#{https}/dashboard/#{wsAccountId}/item/#{wsAccountApp2}/revenue/',
     'check': ['.dashboard-meta.x-clear', '.money-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    # --SS--
    {'name': '[SS] SS windows store Detail',
     'url': '#{https}/apps/windows-store/app/#{wsAppSlug}/details/',
     'check': ['#app_content', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[SS] SS windows store Daily Rank',
     'url': '#{https}/apps/windows-store/app/#{wsAppSlug}/app-ranking/',
     'check': ['#ranks', '#app_rankings', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[SS] SS windows store Rank History',
     'url': '#{https}/apps/windows-store/app/#{wsAppSlug}/rank-history/',
     'check': ['#aa-app', '.aa-chart-options', '.rank-timezone-container', BREADCRUMB_PUBLISHER,
               BREADCRUMB_ITEM_SINGLE]},
    {'name': '[SS] SS windows store Reviews',
     'url': '#{https}/apps/windows-store/app/#{wsAppSlug}/reviews/',
     'check': ['.aa-info-columns-app', '.ratings-summary', '.chart-render', BREADCRUMB_PUBLISHER,
               BREADCRUMB_ITEM_SINGLE]},
    {'name': '[SS] SS windows store Timeline',
     'url': '#{https}/apps/windows-store/app/#{wsAppSlug}/timeline/',
     'check': ['#aa-app', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},

    # ------------Google Analytics Usage------------
    # --comparator usage--
    {'name': '[ADV] Usage',
     'url': '#{https}/comparator/usage/',
     'check': ['tr.main-row.table-row', 'div.app-groups-container', 'div.dashboard-chart', 'div.dashboard-table']},
    {'name': '[ADV] Usage country all-country daily DAU-chart',
     'url': '#{https}/comparator/usage/?countries=ALL&breakdown=country&'
            'chart_type=DAU&granularity=daily&start_date=#{start_date9}&end_date=#{end_date9}',
     'check': ['tr.main-row.table-row', 'div.app-groups-container', 'div.dashboard-chart', 'div.dashboard-table']},
    {'name': '[ADV] Usage country multi-country weekly total_session_duration-chart ',
     'url': '#{https}/comparator/usage/?countries=US,DE,IT,SG,KR,GB&'
            'breakdown=country&chart_type=total_session_duration&granularity=weekly&start_date=#{start_date9}'
            '&end_date=#{end_date9}',
     'check': ['tr.main-row.table-row', 'div.app-groups-container', 'div.dashboard-chart', 'div.dashboard-table']},
    {'name': '[ADV] Usage country one-country monthly avg_session_user_month-chart ',
     'url': '#{https}/comparator/usage/?countries=US&'
            'breakdown=country&chart_type=avg_session_user_month&granularity=monthly&start_date=#{start_date9}&'
            'end_date=#{end_date9}',
     'check': ['tr.main-row.table-row', 'div.app-groups-container', 'div.dashboard-chart', 'div.dashboard-table']},
    {'name': '[ADV] Usage publisher all-country daily total_sessions-chart',
     'url': '#{https}/comparator/usage/?countries=ALL&breakdown=publisher&'
            'chart_type=total_sessions&granularity=daily&start_date=#{start_date9}&end_date=#{end_date9}',
     'check': ['tr.main-row.table-row', 'div.app-groups-container', 'div.dashboard-chart', 'div.dashboard-table']},
    {'name': '[ADV] Usage product_id all-country daily avg_session_duration-chart ',
     'url': '#{https}/comparator/usage/?countries=ALL&'
            'breakdown=product_id&chart_type=avg_session_duration&granularity=daily&start_date=#{start_date9}&'
            'end_date=#{end_date9}',
     'check': ['tr.main-row.table-row', 'div.app-groups-container', 'div.dashboard-chart', 'div.dashboard-table']},
    {'name': '[ADV] Usage platform all-country daily DAU-chart ',
     'url': '#{https}/comparator/usage/?countries=ALL&'
            'breakdown=platform&chart_type=DAU&granularity=daily&start_date=#{start_date9}&end_date=#{end_date9}',
     'check': ['tr.main-row.table-row', 'div.app-groups-container', 'div.dashboard-chart', 'div.dashboard-table']},

    # ================= SS new featured pages ==================
    # feature history
    {'name': '[SS] Feature History Featured Visibility ios',
     'url': '#{https}/apps/ios/app/389801252/featured/?report=feature-history',
     'check': ['div.chart-render', 'div.dashboard-table', 'div.dashboard-chart',
               'div.control-group', 'tr.main-row.table-row'],
     'env': ['production', 'staging']},
    {'name': '[SS] Feature History Frequency ios',
     'url': '#{https}/apps/ios/app/389801252/featured/?'
            'report=feature-history&chart_type=frequency',
     'check': ['div.chart-render', 'div.dashboard-table', 'div.dashboard-chart',
               'div.control-group', 'tr.main-row.table-row'],
     'env': ['production', 'staging']},
    {'name': '[SS] Feature History Featured Visibility gp',
     'url': '#{https}/apps/google-play/app/com.instagram.android/featured/?report=feature-history',
     'check': ['div.chart-render', 'div.dashboard-table', 'div.dashboard-chart',
               'div.control-group', 'tr.main-row.table-row'],
     'env': ['production', 'staging']},
    {'name': '[SS] Feature History Frequency gp',
     'url': '#{https}/apps/google-play/app/com.instagram.android/featured/?'
            'report=feature-history&chart_type=frequency',
     'check': ['div.chart-render', 'div.dashboard-table', 'div.dashboard-chart',
               'div.control-group', 'tr.main-row.table-row'],
     'env': ['production', 'staging']},
    # daily feature
    {'name': '[SS] Daily Feature ios',
     'url': '#{https}/apps/ios/app/389801252/featured/?'
            'report=daily-features&date=2016-11-10',
     'check': ['.dashboard-sub-header', 'div.metrics-picker', 'div.control-group',
               'div.dashboard-table', 'tr.main-row.table-row'],
     'env': ['production', 'staging']},
    {'name': '[SS] Daily Feature gp',
     'url': '#{https}/apps/google-play/app/com.instagram.android/featured/?'
            'report=daily-features&date=2016-11-10',
     'check': ['.dashboard-sub-header', 'div.metrics-picker', 'div.control-group',
               'div.dashboard-table', 'tr.main-row.table-row'],
     'env': ['production', 'staging']},

    # ================= Shared SingleAssets pages ==================
    # ------------ITC------------
    # --AN--
    {'name': '[AN] Shared itc Downloads',
     'url': '#{https}/dashboard/#{sharedItcAccountId}/item/#{itcAccountApp2}/downloads/',
     'check': ['.aa-dashboard-container', '.number-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[AN] Shared itc Revenue',
     'url': '#{https}/dashboard/#{sharedItcAccountId}/item/#{itcAccountApp2}/revenue/',
     'check': ['.aa-dashboard-container', '.table-row', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[AN] Shared itc IAP',
     'url': '#{https}/dashboard/#{sharedItcAccountId}/item/#{itcAccountApp2}/iap/',
     'check': ['.aa-dashboard-container', '.money-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    # --Ad--
    {'name': '[ADV] Shared itc Ad Revenue',
     'url': '#{https}/dashboard/#{sharedItcAccountId}/item/#{itcAccountApp}/ad_revenue/',
     'check': ['.chart-render', '.money-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[ADV] Shared itc Ad Expense',
     'url': '#{https}/dashboard/#{sharedItcAccountId}/item/#{itcAccountApp}/ad_expense/',
     'check': ['.chart-render', '.money-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    # --SS--
    {'name': '[SS] Shared itc Detail',
     'url': '#{https}/apps/ios/app/#{ownIOSAppSlug}/details/?account_id=#{sharedItcAccountId}',
     'check': ['#app_content', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[SS] Shared itc Daily Rank',
     'url': '#{https}/apps/ios/app/#{ownIOSAppSlug}/app-ranking/?account_id=#{sharedItcAccountId}',
     'check': ['#ranks', '.stores', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE],
     'env': ['production', 'staging']},
    {'name': '[SS] Shared itc Rank History',
     'url': '#{https}/apps/ios/app/#{ownIOSAppSlug}/rank-history/?account_id=#{sharedItcAccountId}',
     'check': ['#aa-app', '.aa-chart-options', '.rank-timezone-container', BREADCRUMB_PUBLISHER,
               BREADCRUMB_ITEM_SINGLE]},
    {'name': '[ASO] Shared itc Keywords',
     'url': '#{https}/apps/ios/app/#{iosAppSlug}/keywords/?account_id=#{sharedItcAccountId}',
     'check': ['.dashboard-view-container', '.rank-change', BREADCRUMB_PUBLISHER, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[SS] Shared itc Featured',
     'url': '#{https}/apps/ios/app/#{ownIOSAppSlug}/featured/?account_id=#{sharedItcAccountId}',
     'check': ['.dashboard-sub-header', 'div.metrics-picker', 'div.control-group',
               'div.dashboard-table', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE],
     'env': ['production', 'staging']},
    {'name': '[SS] Shared itc Ratings',
     'url': '#{https}/apps/ios/app/#{ownIOSAppSlug}/ratings/?account_id=#{sharedItcAccountId}',
     'check': ['#rating_container', '.store-ratings', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[SS] Shared itc Reviews',
     'url': '#{https}/apps/ios/app/#{ownIOSAppSlug}/reviews/?account_id=#{sharedItcAccountId}',
     'check': ['.aa-info-columns-app', '.ratings-summary', '.chart-render', BREADCRUMB_PUBLISHER,
               BREADCRUMB_ITEM_SINGLE]},
    # ------------GP------------
    # --AN--
    {'name': '[AN] Shared google-play Downloads',
     'url': '#{https}/dashboard/#{sharedGpAccountId}/item/#{sharedGpAccountApp}/downloads/',
     'check': ['.aa-dashboard-container', '.number-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[AN] Shared google-play Revenue',
     'url': '#{https}/dashboard/#{sharedGpAccountId}/item/#{sharedGpAccountApp}/revenue/',
     'check': ['.aa-dashboard-container', '.table-row', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[AN] Shared google-play IAP',
     'url': '#{https}/dashboard/#{sharedGpAccountId}/item/#{sharedGpAccountApp}/iap/',
     'check': ['.aa-dashboard-container', '.money-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    # --Ad--
    {'name': '[ADV] Shared google-play Ad Revenue',
     'url': '#{https}/dashboard/#{sharedGpAccountId}/item/#{sharedGpAccountApp}/ad_revenue/',
     'check': ['.chart-render', '.money-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[ADV] Shared google-play Ad Expense',
     'url': '#{https}/dashboard/#{sharedGpAccountId}/item/#{sharedGpAccountApp}/ad_expense/',
     'check': ['.chart-render', '.money-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    # --SS--
    {'name': '[SS] Shared google-play Detail',
     'url': '#{https}/apps/google-play/app/#{gpApp}/details/?account_id=#{sharedGpAccountId}',
     'check': ['#app_content', BREADCRUMB_COMPANY, BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION]},
    {'name': '[SS] Shared google-play Daily Rank',
     'url': '#{https}/apps/google-play/app/#{gpApp}/app-ranking/?account_id=#{sharedGpAccountId}',
     'check': ['#ranks', '.data-table .stores', BREADCRUMB_COMPANY, BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[SS] Shared google-play Rank History',
     'url': '#{https}/apps/google-play/app/#{gpApp}/rank-history/?account_id=#{sharedGpAccountId}',
     'check': ['#aa-app', '.aa-chart-options', '.rank-timezone-container', BREADCRUMB_COMPANY, BREADCRUMB_UA_LINK,
               BREADCRUMB_APP_EDITION]},
    {'name': '[ASO] Shared google-play Keywords',
     'url': '#{https}/apps/google-play/app/#{gpApp}/keywords/?account_id=#{sharedGpAccountId}',
     'check': ['.dashboard-view-container', '.rank-change', BREADCRUMB_COMPANY, BREADCRUMB_UA_LINK,
               BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[SS] Shared google-play Featured',
     'url': '#{https}/apps/google-play/app/#{gpApp}/featured/?account_id=#{sharedGpAccountId}',
     'check': ['.dashboard-sub-header', 'div.metrics-picker', 'div.control-group',
               'div.dashboard-table', 'tr.main-row.table-row',
               BREADCRUMB_COMPANY, BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[SS] Shared google-play Reviews',
     'url': '#{https}/apps/google-play/app/#{gpApp}/reviews/?account_id=#{sharedGpAccountId}',
     'check': ['.aa-info-columns-app', '.ratings-summary', '.chart-render', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION]},
    # ------------AMZ------------
    # --AN--
    {'name': '[AN] Shared amazon Downloads',
     'url': '#{https}/dashboard/#{sharedAmzAccountId}/item/#{sharedAmzAccountApp}/downloads/',
     'check': ['.aa-dashboard-container', '.number-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[AN] Shared amazon Revenue',
     'url': '#{https}/dashboard/#{sharedAmzAccountId}/item/#{sharedAmzAccountApp}/revenue/',
     'check': ['.aa-dashboard-container', '.table-row', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[AN] Shared amazon IAP',
     'url': '#{https}/dashboard/#{sharedAmzAccountId}/item/#{sharedAmzAccountApp}/iap/',
     'check': ['.aa-dashboard-container', '.money-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    # --Ad--
    {'name': '[ADV] Shared amazon Ad Revenue',
     'url': '#{https}/dashboard/#{sharedAmzAccountId}/item/#{sharedAmzAccountApp}/ad_revenue/',
     'check': ['.chart-render', '.money-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[ADV] Shared amazon Ad Expense',
     'url': '#{https}/dashboard/#{sharedAmzAccountId}/item/#{sharedAmzAccountApp}/ad_expense/',
     'check': ['.chart-render', '.money-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    # --SS--
    {'name': '[SS] Shared amazon Detail',
     'url': '#{https}/apps/amazon-appstore/app/#{amazonApp}/details/?account_id=#{sharedAmzAccountId}',
     'check': ['#app_content', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[SS] Shared amazon Daily Rank',
     'url': '#{https}/apps/amazon-appstore/app/#{amazonApp}/app-ranking/?account_id=#{sharedAmzAccountId}',
     'check': ['#ranks', '.stores', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE],
     'env': ['production', 'staging']},
    {'name': '[SS] Shared amazon Rank History',
     'url': '#{https}/apps/amazon-appstore/app/#{amazonApp}/rank-history/?account_id=#{sharedAmzAccountId}',
     'check': ['#aa-app', '.aa-chart-options', '.rank-timezone-container', BREADCRUMB_PUBLISHER,
               BREADCRUMB_ITEM_SINGLE]},
    {'name': '[SS] Shared amazon Reviews',
     'url': '#{https}/apps/amazon-appstore/app/#{amzAccountApp}/reviews/?account_id=#{sharedAmzAccountId}',
     'check': ['.aa-info-columns-app', '.ratings-summary', '.chart-render', BREADCRUMB_PUBLISHER,
               BREADCRUMB_ITEM_SINGLE]},

    # ------------WP------------
    # --AN--
    {'name': '[AN] Shared windows-phone Salad Bar Finder Downloads',
     'url': '#{https}/dashboard/#{sharedWpAccountId}/item/#{sharedWpAccountApp1}/downloads/',
     'check': ['.dashboard-meta.x-clear', '.number-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[AN] Shared windows-phone Salad Bar Finder Revenue',
     'url': '#{https}/dashboard/#{sharedWpAccountId}/item/#{sharedWpAccountApp1}/revenue/',
     'check': ['.dashboard-meta.x-clear', '.table-row', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[AN] Shared windows-phone Salad Bar Finder IAP',
     'url': '#{https}/dashboard/#{sharedWpAccountId}/item/#{sharedWpAccountApp1}/iap/',
     'check': ['.aa-dashboard-container', '.money-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    # --SS--
    {'name': '[SS] Shared windows-phone Salad Bar Finder Detail',
     'url': '#{https}/apps/windows-phone/app/#{SharedWpAppSlug}/details/?account_id=#{sharedWpAccountId}',
     'check': ['#app_content', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[SS] Shared windows-phone Salad Bar Finder Daily Rank',
     'url': '#{https}/apps/windows-phone/app/#{SharedWpAppSlug}/app-ranking/?account_id=#{sharedWpAccountId}',
     'check': ['#ranks', '#app_rankings', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE],
     'env': ['production', 'staging']},
    {'name': '[SS] Shared windows-phone Salad Bar Finder Rank History',
     'url': '#{https}/apps/windows-phone/app/#{SharedWpAppSlug}/rank-history/?account_id=#{sharedWpAccountId}',
     'check': ['#aa-app', '.aa-chart-options', '.rank-timezone-container', BREADCRUMB_PUBLISHER,
               BREADCRUMB_ITEM_SINGLE]},
    {'name': '[SS] Shared windows-phone Salad Bar Finder Reviews',
     'url': '#{https}/apps/windows-phone/app/#{SharedWpAppSlug}/reviews/?account_id=#{sharedWpAccountId}',
     'check': ['.aa-info-columns-app', '.ratings-summary', '.chart-render', BREADCRUMB_PUBLISHER,
               BREADCRUMB_ITEM_SINGLE]},
    # ------------WS------------
    # --AN--
    {'name': '[AN] Shared windows-store Power Sauce Downloads',
     'url': '#{https}/dashboard/#{sharedWsAccountId}/item/#{wsAccountApp2}/downloads/',
     'check': ['.dashboard-meta.x-clear', '.number-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[AN] Shared windows-phone Power Sauce Revenue',
     'url': '#{https}/dashboard/#{sharedWsAccountId}/item/#{wsAccountApp2}/revenue/',
     'check': ['.dashboard-meta.x-clear', '.table-row', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[AN] Shared windows-phone Power Sauce IAP',
     'url': '#{https}/dashboard/#{sharedWsAccountId}/item/#{wsAccountApp2}/iap/',
     'check': ['.aa-dashboard-container', '.money-num', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    # --SS--
    {'name': '[SS] Shared windows-store Power Sauce Detail',
     'url': '#{https}/apps/windows-store/app/#{SharedWsAppSlug}/details/?account_id=#{sharedWsAccountId}',
     'check': ['#app_content', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE]},
    {'name': '[SS] Shared windows-store Power Sauce Daily Rank',
     'url': '#{https}/apps/windows-store/app/#{SharedWsAppSlug}/app-ranking/?account_id=#{sharedWsAccountId}',
     'check': ['#ranks', '#app_rankings', BREADCRUMB_PUBLISHER, BREADCRUMB_ITEM_SINGLE],
     'env': ['production', 'staging']},
    {'name': '[SS] Shared windows-store Power Sauce Rank History',
     'url': '#{https}/apps/windows-store/app/#{SharedWsAppSlug}/rank-history/?account_id=#{sharedWsAccountId}',
     'check': ['#aa-app', '.aa-chart-options', '.rank-timezone-container', BREADCRUMB_PUBLISHER,
               BREADCRUMB_ITEM_SINGLE]},
    {'name': '[SS] Shared windows-store Power Sauce Reviews',
     'url': '#{https}/apps/windows-store/app/#{SharedWsAppSlug}/reviews/?account_id=#{sharedWsAccountId}',
     'check': ['.aa-info-columns-app', '.ratings-summary', '.chart-render', BREADCRUMB_PUBLISHER,
               BREADCRUMB_ITEM_SINGLE]},

    # ------------In app analytics------------
    # --GA--
    {'name': '[ADV] Usage',
     'url': '#{https}/dashboard/#{gaAccountId}/item/#{gaAccountApp}/usage/',
     'check': ['div.data-section', 'div.aa-dashboard-container', 'div.dashboard-chart', 'div.dashboard-table',
               BREADCRUMB_PUBLISHER, BREADCRUMB_APP_EDITION]},
    {'name': '[ADV] Usage country all-country daily DAU-chart',
     'url': '#{https}/dashboard/#{gaAccountId}/item/#{gaAccountApp}/usage/?countries=ALL&breakdown=country&'
            'chart_type=DAU&granularity=daily&start_date=#{start_date9}&end_date=#{end_date9}',
     'check': ['div.data-section', 'div.aa-dashboard-container', 'div.dashboard-chart', 'div.dashboard-table',
               BREADCRUMB_PUBLISHER, BREADCRUMB_APP_EDITION]},
    {'name': '[ADV] Usage country multi-country weekly total_session_duration-chart ',
     'url': '#{https}/dashboard/#{gaAccountId}/item/#{gaAccountApp}/usage/?countries=US,DE,IT,SG,KR,GB&'
            'breakdown=country&chart_type=total_session_duration&granularity=weekly&start_date=#{start_date9}'
            '&end_date=#{end_date9}',
     'check': ['div.data-section', 'div.aa-dashboard-container', 'div.dashboard-chart', 'div.dashboard-table',
               BREADCRUMB_PUBLISHER, BREADCRUMB_APP_EDITION]},
    {'name': '[ADV] Usage country one-country monthly avg_session_user_month-chart ',
     'url': '#{https}/dashboard/#{gaAccountId}/item/#{gaAccountApp}/usage/?countries=US'
            'breakdown=country&chart_type=avg_session_user_month&granularity=monthly&start_date=#{start_date9}'
            '&end_date=#{end_date9}',
     'check': ['div.data-section', 'div.aa-dashboard-container', 'div.dashboard-chart', 'div.dashboard-table',
               BREADCRUMB_PUBLISHER, BREADCRUMB_APP_EDITION]},
    {'name': '[ADV] Usage devicetype one-country daily total_sessions-chart',
     'url': '#{https}/dashboard/#{gaAccountId}/item/#{gaAccountApp}/usage/?countries=US&breakdown=device_type&'
            'chart_type=total_sessions&granularity=daily&start_date=#{start_date9}&end_date=#{end_date9}',
     'check': ['div.data-section', 'div.aa-dashboard-container', 'div.dashboard-chart', 'div.dashboard-table',
               BREADCRUMB_PUBLISHER, BREADCRUMB_APP_EDITION]},
    {'name': '[ADV] Usage devicetype all-country weekly avg_session_duration-chart ',
     'url': '#{https}/dashboard/#{gaAccountId}/item/#{gaAccountApp}/usage/?countries=ALL&'
            'breakdown=device_type&chart_type=avg_session_duration&granularity=weekly&start_date=#{start_date9}'
            '&end_date=#{end_date9}',
     'check': ['div.data-section', 'div.aa-dashboard-container', 'div.dashboard-chart', 'div.dashboard-table',
               BREADCRUMB_PUBLISHER, BREADCRUMB_APP_EDITION]},

    # ===============  Account Management ==================
    # ------------Settings------------
    {'name': '[INT-WEB] INT Data Availablity',
     'url': '#{https}/account/intelligence/contract/',
     'check': ['.account-container', '#int-contract-list'] + MINI_MODE},
    {'name': '[INT-WEB] INT Users',
     'url': '#{https}/account/intelligence/',
     'check': ['.account-container', '.sharing-user-name']},
    {'name': '[AN] Account List',
     'url': '#{https}/account/list/',
     'check': ['.aa-table-simple', '.col-assets']},
    {'name': '[AN] Sharing List',
     'url': '#{https}/account/sharing/',
     'check': ['#account-container', '.sharing-list']},
    {'name': '[AN] Apps List',
     'url': '#{https}/account/apps/',
     'check': ['.account-section-body', '.app-name']},
    {'name': '[AN] Export',
     'url': '#{https}/account/export/#!/account/#{itcAccountId}/',
     'check': ['#tabform', '.itc']},
    {'name': '[AN] User Settings',
     'url': '#{https}/account/settings/',
     'check': ['#tabform']},
    {'name': '[AN] API Key',
     'url': '#{https}/account/api/key/',
     'check': ['.api-key-usage-info']},
    {'name': '[AN] Partner API',
     'url': '#{https}/account/api/partner/',
     'check': ['.account-api-partner', '.partner-list'],
     'env': ['production', 'staging']},
    {'name': '[AN] Services',
     'url': '#{https}/account/services/',
     'check': ['.account-services', '.service-list']},
    {'name': '[ASO] Keywords Management',
     'url': '#{https}/account/keywords/management/',
     'check': ['.aso-keyword-management-container']},

    # ------------AN Account Details------------
    {'name': '[AN] itc account details',
     'url': '#{https}/account/ios/#{itcAccountId}/',
     'check': ['.aa-table-simple', '.asset-name']},
    {'name': '[AN] windows-phone account details',
     'url': '#{https}/account/windows-phone/#{wpAccountId}/',
     'check': ['.aa-table-assets-list', '.asset-name']},
    {'name': '[AN] windows-store account details',
     'url': '#{https}/account/windows-store/#{wsAccountId}/',
     'check': ['.aa-table-assets-list', '.asset-name']},
    # ------------Ad Account Details------------
    {'name': '[ADV] jumptapPub account details',
     'url': '#{https}/account/ad-network/#{jumptapPubAccountId}/',
     'check': ['.aa-table-assets-list', '.asset-name'],
     'env': ['production', 'staging']},
    {'name': '[ADV] Facebook parent account details',
     'url': '#{https}/account/ad-network/facebook/#{facebookUserId}/',
     'check': ['.aa-table-assets-list', '.asset-name']},
    {'name': '[ADV] Facebook child account details',
     'url': '#{https}/account/ad-network/#{facebookAccountId}/',
     'check': ['.aa-table-details-profile']},
    {'name': '[ADV] Google Analytics account details',
     'url': '#{https}/account/in-app-analytics/#{gaAccountId}/',
     'check': ['.account-page-body', 'input.item-filter']},
    # ------------App Details------------
    {'name': '[AN] itc app details',
     'url': '#{https}/account/connection/app/ios/#{itcAccountApp}/#{itcAccountId}/',
     'check': ['#account-container', '.asset-name']},
    {'name': '[AN] windows-phone Salad Bar Finder details',
     'url': '#{https}/account/connection/app/windows-phone/#{wpAccountApp1}/#{wpAccountId}/',
     'check': ['#account-container', '.asset-name']},
    {'name': '[AN] windows-store Power Sauce details',
     'url': '#{https}/account/connection/app/windows-store/#{wsAccountApp2}/#{wsAccountId}/',
     'check': ['#account-container', '.asset-name']},

    # ===============  Team ==================
    {'name': '[AN] Team List',
     'url': '#{https}/account/teams/',
     'check': ['.page_teams', '.team-name']},
    {'name': '[AN] Team Detail - Member List',
     'url': '#{https}/account/teams/#{teamAccount2}/members/',
     'check': ['.page_teams', '.member-name']},
    {'name': '[AN] Team Detail - Shared Assets',
     'url': '#{https}/account/teams/#{teamAccount2}/sharings/',
     'check': ['.page_teams', '.aa-icon']},

    # ===============  Sharing ==================
    {'name': '[AN] Sharing List - Data Shared with',
     'url': '#{https}/account/sharing/#!/sending',
     'check': ['.page_sharing', 'tr[data-id="#{teamAccount2}"] .team-name',
               'tr[data-id="#{shareToAccount}"] .user-email']},
    {'name': '[AN] Sharing List - Data Receiving from',
     'url': '#{https}/account/sharing/#!/receiving',
     'check': ['.page_sharing', 'tr[data-id="#{teamAccount1}"] .team-name',
               'tr[data-id="#{shareFromAccount}"] .user-email'],
     'env': ['production', 'staging']},
    {'name': '[AN] Sharing Detail - To User',
     'url': '#{https}/account/sharing/to-#{shareToAccount}/',
     'check': ['.page_sharing', '.app-name.app']},
    {'name': '[AN] Sharing Detail - From User',
     'url': '#{https}/account/sharing/from-#{shareFromAccount}/',
     'check': ['.page_sharing', '.app-name.app']},

    # =========================INT App Comparator===========================
    {'name': '[INT-WEB] App Comparator',
     'url': '#{https}/intelligence/apps/comparator/',
     'check': ['div.app-groups-container', 'div.highcharts-container'],
     'env': ['production', 'staging']},
    # =========================INT Store Top Apps===============
    {'name': '[INT-WEB] Store Top Apps ios - All',
     'url': '#{https}/intelligence/top/?feed=all&aggregation=unified&device=ios&country=%s&category=lifestyle'
            '&granularity=daily' % env_var['countryCode2'],
     'check': ['.filter-container', '.table-container', '.icon-info', '.main-info', '.app-v2', '.ng-scope'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store Top Apps iphone - Free',
     'url': '#{https}/intelligence/top/?feed=Free&aggregation=unified&device=iphone&country=%s&category=lifestyle'
            '&granularity=weekly' % env_var['countryCode2'],
     'check': ['.icon-info', '.main-info', '.ng-scope'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store Top Apps - ios - Paid',
     'url': '#{https}/intelligence/top/?feed=Paid&aggregation=unified&device=ios&country=%s&category=lifestyle'
            '&granularity=daily' % env_var['countryCode2'],
     'check': ['.icon-info', '.main-info', '.ng-scope'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store Top Apps - ipad - Grossing',
     'url': '#{https}/intelligence/top/?feed=Grossing&aggregation=app&device=ipad&country=%s&category=lifestyle'
            '&granularity=monthly' % env_var['countryCode2'],
     'check': ['.icon-info', '.main-info', '.ng-scope'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store Top Apps - GP - All',
     'url': '#{https}/intelligence/apps/google-play/top/?aggregation=app&feed=all&country=%s'
            '&category=application%%2Flifestyle&granularity=daily' % env_var['countryCode2'],
     'check': ['.icon-info', '.main-info', '.ng-scope'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store Top Apps - GP - Free',
     'url': '#{https}/intelligence/apps/google-play/top/?aggregation=app&feed=Free&country=%s'
            '&category=application%%2Flifestyle&granularity=weekly' % env_var['countryCode2'],
     'check': ['.icon-info', '.main-info', '.ng-scope'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store Top Apps GP - Paid',
     'url': '#{https}/intelligence/apps/google-play/top/?aggregation=unified&feed=Paid&country=%s'
            '&category=application%%2Flifestyle&granularity=monthly' % env_var['countryCode2'],
     'check': ['.icon-info', '.main-info', '.ng-scope'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store Top Apps - GP - Grossing',
     'url': '#{https}/intelligence/apps/google-play/top/?aggregation=unified&feed=Grossing&country=%s'
            '&category=application%%2Flifestyle&granularity=monthly' % env_var['countryCode2'],
     'check': ['.icon-info', '.main-info', '.ng-scope'],
     'env': ['production', 'staging']},
    # ====================INT Store Top Publishers======================
    {'name': '[INT-WEB] Store Top Publishers - IOS - All',
     'url': '#{https}/intelligence/top-publishers/?feed=all&device=ios&country=%s&category=lifestyle'
            '&granularity=daily' % env_var['countryCode2'],
     'check': ['.table-container', '.app-v2'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store Top Publishers - IOS - Free',
     'url': '#{https}/intelligence/top-publishers/?feed=Free&device=iphone&country=%s&category=lifestyle'
            '&granularity=weekly' % env_var['countryCode2'],
     'check': ['.table-container', '.app-v2'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store Top Publishers - IOS - Paid',
     'url': '#{https}/intelligence/top-publishers/?feed=Paid&device=ipad&country=%s&category=lifestyle'
            '&granularity=monthly' % env_var['countryCode2'],
     'check': ['.table-container', '.app-v2'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store Top Publishers - IOS - Grossing',
     'url': '#{https}/intelligence/top-publishers/?feed=Grossing&device=ios&country=%s&category=lifestyle'
            '&granularity=monthly' % env_var['countryCode2'],
     'check': ['.table-container', '.app-v2'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store Top Publishers - GP - All',
     'url': '#{https}/intelligence/publishers/google-play/top/?feed=all&country=%s&category=application'
            '%%2Flifestyle&granularity=daily' % env_var['countryCode2'],
     'check': ['.table-container', '.app-v2'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store Top Publishers - GP - Free',
     'url': '#{https}/intelligence/publishers/google-play/top/?feed=Free&country=%s&category=application'
            '%%2Flifestyle&granularity=weekly' % env_var['countryCode2'],
     'check': ['.table-container', '.app-v2'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store Top Publishers - GP - Paid',
     'url': '#{https}/intelligence/publishers/google-play/top/?feed=Paid&country=%s&category=application'
            '%%2Flifestyle&granularity=monthly' % env_var['countryCode2'],
     'check': ['.table-container', '.app-v2'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store Top Publishers - GP - Grossing',
     'url': '#{https}/intelligence/publishers/google-play/top/?feed=Grossing&country=%s&category=application'
            '%%2Flifestyle&granularity=monthly' % env_var['countryCode2'],
     'check': ['.table-container', '.app-v2'],
     'env': ['production', 'staging']},
    # =====================Store PYC================
    {'name': '[INT-WEB] Store PYC - all',
     'url': '#{https}/intelligence/apps/pyp/?device=all&category_id=1',
     'check': ['.ss-top-chart', 'div.asset-name'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store PYC - ios ',
     'url': '#{https}/intelligence/apps/pyp/?device=ios&category_id=6014',
     'check': ['.ss-top-chart', 'div.asset-name'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store PYC - iphone',
     'url': '#{https}/intelligence/apps/pyp/?device=iphone&category_id=100',
     'check': ['.ss-top-chart', 'div.asset-name'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store PYC - ipad',
     'url': '#{https}/intelligence/apps/pyp/?device=ipad&category_id=6018',
     'check': ['.ss-top-chart', 'div.asset-name'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store PYC - gp',
     'url': '#{https}/intelligence/apps/pyp/?device=google-play&category_id=56',
     'check': ['.ss-top-chart', 'div.asset-name'],
     'env': ['production', 'staging']},
    # =====================Store PYA================
    {'name': '[INT-WEB] Store PYA - all',
     'url': '#{https}/intelligence/apps/pya/?device=all',
     'check': ['.ss-top-chart', 'div.app-link-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store PYA - ios',
     'url': '#{https}/intelligence/apps/pya/?device=ios',
     'check': ['.ss-top-chart', 'div.app-link-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store PYA - iphone',
     'url': '#{https}/intelligence/apps/pya/?device=iphone',
     'check': ['.ss-top-chart', 'div.app-link-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store PYA - ipad',
     'url': '#{https}/intelligence/apps/pya/?device=ipad',
     'check': ['.ss-top-chart', 'div.app-link-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store PYA - gp',
     'url': '#{https}/intelligence/apps/pya/?device=google-play',
     'check': ['.ss-top-chart', 'div.app-link-container'],
     'env': ['production', 'staging']},
    # ===================Store Market Size==========================
    # TODO: Date Range should update
    {'name': '[INT-WEB] Intelligence market size CBD - ios - all - weekly',
     'url': '#{https}/intelligence/ios/market-size/?data_break_down=country&device=ios&countries=%s'
            '&category=lifestyle&price=all&sort_by=value&granularity=weekly'
            '&date=2016-07-24~2017-01-28' % env_var['countryCode2'],
     'check': ['div.filter-item', 'div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence market size CBD - iphone - free - monthly',
     'url': '#{https}/intelligence/ios/market-size/?data_break_down=country&device=iphone&countries=%s'
            '&category=medical&price=free&sort_by=changeInPercent&granularity=monthly'
            '&date=2016-01-01~2016-12-31' % env_var['countryCode2'],
     'check': ['div.filter-item', 'div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence market size  CBD - ipad - paid - weekly',
     'url': '#{https}/intelligence/ios/market-size/?data_break_down=country&device=ipad&countries=%s'
            '&category=social&price=paid&sort_by=changeInValue&granularity=weekly'
            '&date=2016-07-24~2017-01-28' % env_var['countryCode2'],
     'check': ['div.filter-item', 'div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence market size CBD - GP - all - monthly',
     'url': '#{https}/intelligence/google-play/market-size/?data_break_down=country&countries=%s'
            '&category=lifestyle&price=all&iap=all&sort_by=value&device=google-play&granularity=monthly'
            '&date=2016-01-01~2016-12-31' % env_var['countryCode2'],
     'check': ['div.filter-item', 'div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence market size CBD - GP - free - weekly',
     'url': '#{https}/intelligence/google-play/market-size/?data_break_down=country&countries=%s'
            '&category=medical&price=free&iap=all&sort_by=changeInPercent&device=google-play&granularity=weekly'
            '&date=2016-07-24~2017-01-28' % env_var['countryCode2'],
     'check': ['div.filter-item', 'div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence market size CBD - GP - paid - monthly',
     'url': '#{https}/intelligence/google-play/market-size/?data_break_down=country&countries=%s'
            '&category=social&price=paid&iap=all&sort_by=changeInValue&device=google-play&granularity=monthly'
            '&date=2016-01-01~2016-12-31' % env_var['countryCode2'],
     'check': ['div.filter-item', 'div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence market size CBD - all - weekly',
     'url': '#{https}/intelligence/ios/market-size/?data_break_down=category&device=ios&countries=%s'
            '&category=lifestyle&price=all&sort_by=changeInValue&granularity=weekly'
            '&date=2016-07-24~2017-01-28' % env_var['countryCode2'],
     'check': ['div.filter-item', 'div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence market size CBD - free - monthly',
     'url': '#{https}/intelligence/ios/market-size/?data_break_down=category&device=iphone&countries=%s'
            '&category=social&price=free&sort_by=changeInPercent&granularity=monthly'
            '&date=2016-01-01~2016-12-31' % env_var['countryCode2'],
     'check': ['div.filter-item', 'div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence market size CBD - paid - weekly',
     'url': '#{https}/intelligence/ios/market-size/?data_break_down=category&device=ipad&countries=%s'
            '&category=medical&price=paid&sort_by=value&granularity=weekly'
            '&date=2016-07-24~2017-01-28' % env_var['countryCode2'],
     'check': ['div.filter-item', 'div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence market size CBD - free - GP - monthly',
     'url': '#{https}/intelligence/google-play/market-size/?data_break_down=category&countries=%s'
            '&category=lifestyle&price=free&iap=all&sort_by=value&device=google-play&granularity=monthly'
            '&date=2016-01-01~2016-12-31' % env_var['countryCode2'],
     'check': ['div.filter-item', 'div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence market size CBD - paid - GP - weekly',
     'url': '#{https}/intelligence/google-play/market-size/?data_break_down=category&countries=%s'
            '&category=medical&price=paid&iap=all&sort_by=changeInPercent&device=google-play&granularity=weekly'
            '&date=2016-07-24~2017-01-28' % env_var['countryCode2'],
     'check': ['div.filter-item', 'div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence market size CBD - paid - GP - monthly',
     'url': '#{https}/intelligence/google-play/market-size/?data_break_down=category&countries=%s'
            '&category=social&price=paid&iap=all&sort_by=changeInValue&device=google-play&granularity=monthly'
            '&date=2016-01-01~2016-12-31' % env_var['countryCode2'],
     'check': ['div.filter-item', 'div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence market size DBD - all - ios - weekly',
     'url': '#{https}/intelligence/ios/market-size/?data_break_down=device&device=ios&countries=%s'
            '&category=lifestyle&price=all&sort_by=value&granularity=weekly'
            '&date=2016-07-24~2017-01-28' % env_var['countryCode2'],
     'check': ['div.filter-item', 'div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence market size DBD - free - ios - monthly',
     'url': '#{https}/intelligence/ios/market-size/?data_break_down=device&device=ios&countries=%s'
            '&category=medical&price=free&sort_by=changeInPercent&granularity=monthly'
            '&date=2016-01-01~2016-12-31' % env_var['countryCode2'],
     'check': ['div.filter-item', 'div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence market size DBD - paid - ios - weekly',
     'url': '#{https}/intelligence/ios/market-size/?data_break_down=device&device=ios&countries=%s'
            '&category=social&price=paid&sort_by=changeInValue&granularity=weekly'
            '&date=2016-07-24~2017-01-28' % env_var['countryCode2'],
     'check': ['div.filter-item', 'div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence market size DBD - all - GP - monthly',
     'url': '#{https}/intelligence/google-play/market-size/?data_break_down=device&countries=%s'
            '&category=lifestyle&price=all&iap=all&sort_by=value&device=google-play&granularity=monthly'
            '&date=2016-01-01~2016-12-31' % env_var['countryCode2'],
     'check': ['div.filter-item', 'div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence market size DBD - free - GP - weekly',
     'url': '#{https}/intelligence/google-play/market-size/?data_break_down=device&countries=%s'
            '&category=medical&price=free&iap=all&sort_by=changeInPercent&device=google-play&granularity=weekly'
            '&date=2016-07-24~2017-01-28' % env_var['countryCode2'],
     'check': ['div.filter-item', 'div.dashboard-table'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence market size DBD - paid - GP - monthly',
     'url': '#{https}/intelligence/google-play/market-size/?data_break_down=device&countries=%s'
            '&category=social&price=paid&iap=all&sort_by=changeInValue&device=google-play&granularity=monthly'
            '&date=2016-01-01~2016-12-31' % env_var['countryCode2'],
     'check': ['div.filter-item', 'div.dashboard-table'],
     'env': ['production', 'staging']},
    # ========================Store Unified/Single App Level====================
    {'name': '[INT-WEB] INT - GP - App Device - daily',
     'url': '#{https}/apps/google-play/app/com.king.candycrushsaga/intelligence/?data_break_down=apphistory'
            '&country=SE&granularity=daily',
     'check': ['div.filter-container', 'div.chart-render', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT - GP - App Device - weekly',
     'url': '#{https}/apps/google-play/app/com.king.candycrushsaga/intelligence/?data_break_down=apphistory'
            '&country=SE&granularity=weekly',
     'check': ['div.filter-container', 'div.chart-render', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT - GP - App Device - monthly',
     'url': '#{https}/apps/google-play/app/com.king.candycrushsaga/intelligence/?data_break_down=apphistory'
            '&country=SE&granularity=monthly',
     'check': ['div.filter-container', 'div.chart-render', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT - IOS - App Device - daily',
     'url': '#{https}/apps/ios/app/candy-crush-saga/intelligence/?country=SE&granularity=daily',
     'check': ['div.filter-container', 'div.chart-render', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT - IOS - App Device - weekly',
     'url': '#{https}/apps/ios/app/candy-crush-saga/intelligence/?country=SE&granularity=weekly',
     'check': ['div.filter-container', 'div.chart-render', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT - IOS - App Device - monthly',
     'url': '#{https}/apps/ios/app/candy-crush-saga/intelligence/?country=SE&granularity=monthly',
     'check': ['div.filter-container', 'div.chart-render', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT - GP - App - CBD - daily',
     'url': '#{https}/apps/google-play/app/com.king.candycrushsaga/intelligence/?data_break_down=countrybreakdown'
            '&granularity=daily',
     'check': ['div.filter-container', 'div.dashboard-table', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT - GP - App - CBD - weekly',
     'url': '#{https}/apps/google-play/app/com.king.candycrushsaga/intelligence/?data_break_down=countrybreakdown'
            '&granularity=weekly',
     'check': ['div.filter-container', 'div.dashboard-table', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT - GP - App - CBD - monthly',
     'url': '#{https}/apps/google-play/app/com.king.candycrushsaga/intelligence/?data_break_down=countrybreakdown'
            '&granularity=monthly',
     'check': ['div.filter-container', 'div.dashboard-table', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT - IOS - App - CBD - daily',
     'url': '#{https}/apps/ios/app/candy-crush-saga/intelligence/?data_break_down=countrybreakdown&device=ios'
            '&granularity=daily',
     'check': ['div.filter-container', 'div.dashboard-table', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT - IOS - App - CBD - weekly',
     'url': '#{https}/apps/ios/app/candy-crush-saga/intelligence/?data_break_down=countrybreakdown&device=iphone'
            '&granularity=weekly',
     'check': ['div.filter-container', 'div.dashboard-table', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT - IOS - App - CBD - monthly',
     'url': '#{https}/apps/ios/app/candy-crush-saga/intelligence/?data_break_down=countrybreakdown&device=ipad'
            '&granularity=monthly',
     'check': ['div.filter-container', 'div.dashboard-table', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Unified App history - daily',
     'url': '#{https}/apps/all-stores/app/#{uaApp1}/intelligence/?data_break_down=history&granularity=daily',
     'check': ['.main-app-content', '.chart-render', 'div.dashboard-table', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_NO_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Unified App history - weekly',
     'url': '#{https}/apps/all-stores/app/#{uaApp1}/intelligence/?data_break_down=history&granularity=weekly',
     'check': ['.main-app-content', '.chart-render', 'div.dashboard-table', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_NO_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Unified App history - monthly',
     'url': '#{https}/apps/all-stores/app/#{uaApp1}/intelligence/?data_break_down=history&granularity=monthly',
     'check': ['.main-app-content', '.chart-render', 'div.dashboard-table', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_NO_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Unified App country breakdown',
     'url': '#{https}/apps/all-stores/app/#{uaApp1}/intelligence/?data_break_down=countrybreakdown'
            '&granularity=daily',
     'check': ['.main-app-content', 'div.dashboard-table', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_NO_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    # ==============  Store - Companies & Publishers =================
    {'name': '[INT-WEB] Store - Company Device Breakdown - ios - daily',
     'url': '#{https}/company/facebook/intelligence/?data_break_down=device&device=ios&country=BE'
            '&granularity=daily&date=2017-03-11~2017-04-11&chart_type=downloads&aggregate_app=on'
            '&page_size=100&order_by=downloads&order_type=desc&page_number=0&category=social',
     'check': ['.aa-dashboard-table-container', '.highcharts-container', '.filter-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store - Company Device Breakdown - ios - monthly',
     'url': '#{https}/company/facebook/intelligence/?data_break_down=device&device=ios&country=BE'
            '&granularity=monthly&date=2016-09-01~2017-01-31&chart_type=downloads&aggregate_app=on'
            '&page_size=100&order_by=downloads&order_type=desc&page_number=0&category=social',
     'check': ['.aa-dashboard-table-container', '.highcharts-container', '.filter-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store - Company Device Breakdown - gp - weekly',
     'url': '#{https}/company/facebook/intelligence/?data_break_down=device&device=google-play&country=BE'
            '&granularity=weekly&date=2017-01-01~2017-02-25&chart_type=downloads&aggregate_app=on'
            '&page_size=100&order_by=downloads&order_type=desc&page_number=0&category=social',
     'check': ['.aa-dashboard-table-container', '.highcharts-container', '.filter-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store - Company Device Breakdown - gp - monthly',
     'url': '#{https}/company/facebook/intelligence/?data_break_down=device&device=google-play&country=BE'
            '&granularity=monthly&date=2016-09-01~2017-01-31&chart_type=downloads&aggregate_app=on'
            '&page_size=100&order_by=downloads&order_type=desc&page_number=0&category=social',
     'check': ['.aa-dashboard-table-container', '.highcharts-container', '.filter-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store - Company App Breakdown - ios - daily',
     'url': '#{https}/company/facebook/intelligence/?data_break_down=app&device=ios&country=BE'
            '&granularity=daily&date=2017-03-01~2017-03-31&chart_type=downloads&aggregate_app=on'
            '&page_size=100&order_by=downloads&order_type=desc&page_number=0&category=social',
     'check': ['.aa-dashboard-table-container', '.highcharts-container', '.filter-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store - Company App Breakdown - ipad - weekly',
     'url': '#{https}/company/facebook/intelligence/?data_break_down=app&device=ipad&country=BE'
            '&granularity=weekly&date=2017-01-01~2017-02-25&chart_type=downloads&aggregate_app=on'
            '&page_size=100&order_by=downloads&order_type=desc&page_number=0&category=social',
     'check': ['.aa-dashboard-table-container', '.highcharts-container', '.filter-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store - Company App Breakdown - gp - weekly',
     'url': '#{https}/company/facebook/intelligence/?data_break_down=app&device=google-play&country=BE'
            '&granularity=weekly&date=2017-01-01~2017-02-25&chart_type=downloads&aggregate_app=on'
            '&page_size=100&order_by=downloads&order_type=desc&page_number=0&category=social',
     'check': ['.aa-dashboard-table-container', '.highcharts-container', '.filter-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store - Company App Breakdown - gp - monthly',
     'url': '#{https}/company/facebook/intelligence/?data_break_down=app&device=google-play&country=BE'
            '&granularity=monthly&date=2016-09-01~2017-01-31&chart_type=downloads&aggregate_app=on'
            '&page_size=100&order_by=downloads&order_type=desc&page_number=0&category=social',
     'check': ['.aa-dashboard-table-container', '.highcharts-container', '.filter-container'],
     'env': ['production', 'staging']},

    {'name': '[INT-WEB] Store - Publishers - ios - device breakdown',
     'url': '#{https}/apps/ios/publisher/284882218/intelligence/?data_break_down=history&country=BE'
            '&category=social-networking&granularity=daily&date_range_picker=2017-01-06~2017-02-05'
            '&chart_type=download&table_query=',
     'check': ['.text.tbl-col-text', 'td.number.tbl-col-number',
               '.highcharts-container'],
     'env': ['production', 'staging']},
    # {'name': '[INT-WEB] Store - Publishers - ios - country breakdown',
    #  'url': '#{https}/apps/ios/publisher/284882218/intelligence/?data_break_down=countrybreakdown'
    #         '&device=ios&category=6005&granularity=daily&date_range_picker=2017-01-06~2017-02-05'
    #         '&table_query=',
    #  'check': ['.row-sorted.number.tbl-col-number', '.link.tbl-col-link'],
    #  'env': ['production', 'staging']},
    # {'name': '[INT-WEB] Store - Publishers - ios - country breakdown',
    #  'url': '#{https}/apps/ios/publisher/284882218/intelligence/?data_break_down=countrybreakdown'
    #         '&device=iphone&category=6005&granularity=weekly&week-range-picker=2016-08-14~2017-02-05'
    #         '&table_query=',
    #  'check': ['.row-sorted.number.tbl-col-number', '.link.tbl-col-link'],
    #  'env': ['production', 'staging']},
    # {'name': '[INT-WEB] Store - Publishers - ios - country breakdown',
    #  'url': '#{https}/apps/ios/publisher/284882218/intelligence/?data_break_down=countrybreakdown'
    #         '&device=ipad&category=6005&granularity=monthly&month-range-picker=2016-02-01~2017-02-05'
    #         '&table_query=',
    #  'check': ['.row-sorted.number.tbl-col-number', '.link.tbl-col-link'],
    #  'env': ['production', 'staging']},
    {'name': '[INT-WEB] Store - Publishers - gp - device breakdown',
     'url': '#{https}/apps/google-play/publisher/20200000193769/intelligence/?data_break_down=history'
            '&country=BE&category=application/social&granularity=daily&date_range_picker=2017-01-06~2017-02-05'
            '&chart_type=download&table_query=',
     'check': ['.text.tbl-col-text', 'td.number.tbl-col-number',
               '.highcharts-container'],
     'env': ['production', 'staging']},
    # {'name': '[INT-WEB] Store - Publishers - gp - country breakdown',
    #  'url': '#{https}/apps/google-play/publisher/20200000193769/intelligence/?data_break_down=countrybreakdown'
    #         '&device=google-play&category=31&granularity=weekly&week-range-picker=2016-08-14~2017-02-04'
    #         '&table_query=',
    #  'check': ['.row-sorted.number.tbl-col-number', '.link.tbl-col-link'],
    #  'env': ['production', 'staging']},
    {'name': '[INT-WEB] DNA  ios Publisher - INT - history',
     'url': '#{https}/apps/ios/publisher/298910979/intelligence/',
     'check': ['.main-app-content', '.percentage-with-bar', BREADCRUMB_COMPANY, BREADCRUMB_ITEM_SINGLE],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] DNA  ios Publisher - INT - country',
     'url': '#{https}/apps/ios/publisher/298910979/intelligence/?data_break_down=countrybreakdown',
     'check': ['.main-app-content', '.percentage-with-bar', BREADCRUMB_COMPANY, BREADCRUMB_ITEM_SINGLE],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] DNA  ios Publisher - INT - app',
     'url': '#{https}/apps/ios/publisher/298910979/intelligence/?data_break_down=appbreakdown&country=BE',
     'check': ['.main-app-content', '.percentage-with-bar', BREADCRUMB_COMPANY, BREADCRUMB_ITEM_SINGLE],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] DNA  google-play Publisher - INT - history',
     'url': '#{https}/apps/google-play/publisher/20200000195109/intelligence/',
     'check': ['div.dashboard-table', 'tr.table-row', BREADCRUMB_COMPANY, BREADCRUMB_ITEM_SINGLE],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] DNA  google-play Publisher - INT - country',
     'url': '#{https}/apps/google-play/publisher/20200000195109/intelligence/?data_break_down=countrybreakdown',
     'check': ['div.dashboard-table', 'tr.table-row', BREADCRUMB_COMPANY, BREADCRUMB_ITEM_SINGLE],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] DNA  google-play Publisher - INT - app',
     'url': '#{https}/apps/google-play/publisher/20200000195109/intelligence/?data_break_down=appbreakdown&country=BE',
     'check': ['div.dashboard-table', 'tr.table-row', BREADCRUMB_COMPANY, BREADCRUMB_ITEM_SINGLE],
     'env': ['production', 'staging']},
    # =====================Audience  CAU=========================
    {'name': '[INT-WEB] INT - Audience - CAU - GP',
     'url': '#{https}/apps/google-play/app/20600000009072/intelligence/cross-app-usage/',
     'check': ['.avatar', '.app-icon', 'span.value'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT - Audience - CAU - iOS',
     'url': '#{https}/apps/ios/app/284882215/intelligence/cross-app-usage/',
     'check': ['.avatar', '.app-icon', 'span.value'],
     'env': ['production', 'staging']},
    # =====================Audience Demographics=========================
    {'name': '[INT-WEB] INT - Audience - Demographics',
     'url': '#{https}/apps/ios/app/284882215/intelligence/demographics/',
     'check': ['span.row-value', 'span.row-title'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT - Audience - CAU - GP',
     'url': '#{https}/apps/google-play/app/20600000009072/intelligence/demographics/',
     'check': ['span.row-value', 'span.row-title'],
     'env': ['production', 'staging']},
    # ======================Usage Top Apps================
    {'name': '[INT-WEB] Intelligence usage top chart user segment - IOS - weekly',
     'url': '#{https}/intelligence/usage/top/?device=ios&country=JP'
            '&granularity=weekly&user_segmentation=all_users&sort_by=value',
     'check': ['div.dashboard-table.int-usage-top-chart-table', '.filter-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage top chart user segment - IOS - monthly',
     'url': '#{https}/intelligence/usage/top/?device=ios&country=JP'
            '&granularity=monthly&user_segmentation=all_users&sort_by=changeInPercent',
     'check': ['div.dashboard-table.int-usage-top-chart-table', '.filter-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage top chart user segment - iphone - weekly',
     'url': '#{https}/intelligence/usage/top/?device=iphone&country=JP'
            '&granularity=weekly&user_segmentation=all_25_44&sort_by=value',
     'check': ['div.dashboard-table.int-usage-top-chart-table', '.filter-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage top chart user segment - iphone - monthly',
     'url': '#{https}/intelligence/usage/top/?device=iphone&country=JP'
            '&granularity=monthly&user_segmentation=females_13_24&sort_by=changeInPercent',
     'check': ['div.dashboard-table.int-usage-top-chart-table', '.filter-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage top chart user segment - android - weekly',
     'url': '#{https}/intelligence/usage/top/ios/?device=android_tablet&country=JP&category=21'
            '&granularity=weekly&user_segmentation=all_users&sort_by=value&table_query='
            '&platform=android',
     'check': ['div.dashboard-table.int-usage-top-chart-table', '.filter-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage top chart user segment - android - monthly',
     'url': '#{https}/intelligence/usage/top/ios/?device=android_tablet&country=JP&category=21'
            '&granularity=monthly&user_segmentation=all_users&sort_by=changeInPercent&table_query='
            '&platform=android',
     'check': ['div.dashboard-table.int-usage-top-chart-table', '.filter-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage top chart user segment - ipad - weekly',
     'url': '#{https}/intelligence/usage/top/?device=ipad&country=CZ'
            '&granularity=weekly&user_segmentation=all_users&sort_by=value',
     'check': ['div.dashboard-table.int-usage-top-chart-table', '.filter-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage top chart user segment - ipad - monthly',
     'url': '#{https}/intelligence/usage/top/?device=ipad&country=CZ'
            '&granularity=monthly&user_segmentation=all_users&sort_by=changeInPercent',
     'check': ['div.dashboard-table.int-usage-top-chart-table', '.filter-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage top chart user segment - android - weekly',
     'url': '#{https}/intelligence/usage/top/android/?device=iphone&country=JP&category=6012'
            '&granularity=weekly&user_segmentation=females_13_24&sort_by=value&platform=ios'
            '#device=android&country=JP&category=21&granularity=weekly&user_segmentation=all_users'
            '&sort_by=value',
     'check': ['div.dashboard-table.int-usage-top-chart-table', '.filter-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage top chart user segment - android_phone - all_users - monthly',
     'url': '#{https}/intelligence/usage/top/android/?device=iphone&country=JP&category=6012'
            '&granularity=weekly&user_segmentation=females_13_24&sort_by=value&platform=ios'
            '#device=android_phone&country=JP&category=21&granularity=monthly&user_segmentation=all_users'
            '&sort_by=changeInPercent',
     'check': ['div.dashboard-table.int-usage-top-chart-table', '.filter-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage top chart user segment - android_phone - females_13_24 - weekly',
     'url': '#{https}/intelligence/usage/top/android/?device=iphone&country=JP&category=6012'
            '&granularity=weekly&user_segmentation=females_13_24&sort_by=value&platform=ios'
            '#device=android_phone&country=JP&category=21&granularity=weekly'
            '&user_segmentation=females_13_24&sort_by=value',
     'check': ['div.dashboard-table.int-usage-top-chart-table', '.filter-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage top chart user segment - android_phone - males_25_44 - monthly',
     'url': '#{https}/intelligence/usage/top/android/?device=iphone&country=JP&category=6012'
            '&granularity=weekly&user_segmentation=females_13_24&sort_by=value&platform=ios'
            '#device=android_phone&country=JP&category=21&granularity=monthly&user_segmentation=males_25_44'
            '&sort_by=changeInPercent',
     'check': ['div.dashboard-table.int-usage-top-chart-table', '.filter-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage top chart user segment - android_phone - app_used - weekly',
     'url': '#{https}/intelligence/usage/top/android/?device=iphone&country=JP&category=6012'
            '&granularity=weekly&user_segmentation=females_13_24&sort_by=value&platform=ios'
            '#device=android_phone&country=JP&category=21&granularity=weekly&user_segmentation=app_used'
            '&sort_by=value&table_query=&segment_app_id=&segment_app_market=',
     'check': ['div.dashboard-table.int-usage-top-chart-table', '.filter-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage top chart user segment - android_phone - app_used - monthly',
     'url': '#{https}/intelligence/usage/top/android/?device=iphone&country=JP&category=6012'
            '&granularity=weekly&user_segmentation=females_13_24&sort_by=value&platform=ios'
            '#device=android_phone&country=JP&category=21&granularity=monthly&user_segmentation=app_used'
            '&sort_by=changeInPercent&table_query=&segment_app_id=&segment_app_market=',
     'check': ['div.dashboard-table.int-usage-top-chart-table', '.filter-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage top chart user segment - android_tablet - all_users - weekly',
     'url': '#{https}/intelligence/usage/top/android/?device=iphone&country=JP&category=6012'
            '&granularity=weekly&user_segmentation=females_13_24&sort_by=value&platform=ios'
            '#device=android_tablet&country=JP&category=21&granularity=weekly&user_segmentation=all_users'
            '&sort_by=value',
     'check': ['div.dashboard-table.int-usage-top-chart-table', '.filter-container'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage top chart user segment - android_tablet - all_users - monthly',
     'url': '#{https}/intelligence/usage/top/android/?device=iphone&country=JP&category=6012'
            '&granularity=weekly&user_segmentation=females_13_24&sort_by=value&platform=ios'
            '#device=android_tablet&country=JP&category=21&granularity=monthly&user_segmentation=all_users'
            '&sort_by=changeInPercent',
     'check': ['div.dashboard-table.int-usage-top-chart-table', '.filter-container'],
     'env': ['production', 'staging']},
    # ========================Usage PYA=====================
    {'name': '[INT-WEB] Intelligence usage pya user segment app used - IOS - weekly',
     'url': '#{https}/intelligence/apps/usage/?device=ios&android_country=JP&granularity=weekly'
            '&user_segmentation=all_users&sort_by=value&table_query=&country=JP',
     'check': ['img.app-icon', 'span.value', '.aa-progress'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage pya user segment app used - iphone - all_users - weekly',
     'url': '#{https}/intelligence/apps/usage/?device=iphone&android_country=JP&granularity=weekly'
            '&user_segmentation=all_users&sort_by=changeInPercent&table_query=&country=JP',
     'check': ['img.app-icon', 'span.value', '.aa-progress'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage pya user segment app used - iphone - monthly',
     'url': '#{https}/intelligence/apps/usage/?device=iphone&android_country=JP&granularity=monthly'
            '&user_segmentation=app_used&sort_by=value&table_query='
            '&segment_app_id=&segment_app_market=&country=JP',
     'check': ['img.app-icon', 'span.value', '.aa-progress'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage pya user segment app used - iphone - monthly',
     'url': '#{https}/intelligence/apps/usage/?device=iphone&android_country=JP&granularity=monthly'
            '&user_segmentation=all_13_24&sort_by=value&table_query=&country=JP',
     'check': ['img.app-icon', 'span.value', '.aa-progress'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage pya user segment app used - iphone - females_13_24 - weekly',
     'url': '#{https}/intelligence/apps/usage/?device=iphone&android_country=JP&granularity=weekly'
            '&user_segmentation=females_13_24&sort_by=changeInPercent&table_query=&country=JP',
     'check': ['img.app-icon', 'span.value', '.aa-progress'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage pya user segment app used - iphone - males_25_44 - weekly',
     'url': '#{https}/intelligence/apps/usage/?device=iphone&android_country=JP&granularity=weekly'
            '&user_segmentation=males_25_44&sort_by=value&table_query=&country=JP',
     'check': ['img.app-icon', 'span.value', '.aa-progress'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage pya user segment app used - ipad - all_users - monthly',
     'url': '#{https}/intelligence/apps/usage/?device=ipad&android_country=JP&granularity=monthly'
            '&user_segmentation=all_users&sort_by=changeInPercent&table_query=&country=US',
     'check': ['img.app-icon', 'span.value', '.aa-progress'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage pya user segment app used - Android - all_users - weekly',
     'url': '#{https}/intelligence/apps/usage/?device=android&android_country=JP&granularity=weekly'
            '&user_segmentation=all_users&sort_by=value&table_query=&country=JP',
     'check': ['img.app-icon', 'span.value', '.aa-progress'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage pya user segment app used - android_tablet - all_users - monthly',
     'url': '#{https}/intelligence/apps/usage/?device=android_tablet&android_country=JP&granularity=monthly'
            '&user_segmentation=all_users&sort_by=changeInPercent&table_query=&country=JP',
     'check': ['img.app-icon', 'span.value', '.aa-progress'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage pya user segment app used - android_phone - all_users - monthly',
     'url': '#{https}/intelligence/apps/usage/?device=android_phone&android_country=JP&granularity=monthly'
            '&user_segmentation=all_users&sort_by=changeInPercent&table_query=&country=CZ',
     'check': ['img.app-icon', 'span.value', '.aa-progress'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage pya user segment app used - android_phone - all_13_24 - weekly',
     'url': '#{https}/intelligence/apps/usage/?device=android_phone&android_country=JP&granularity=weekly'
            '&user_segmentation=all_13_24&sort_by=changeInPercent&table_query=&country=JP',
     'check': ['img.app-icon', 'span.value', '.aa-progress'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage pya user segment app used - android_phone - females_13_24 - weekly',
     'url': '#{https}/intelligence/apps/usage/?device=android_phone&android_country=JP&granularity=weekly'
            '&user_segmentation=females_13_24&sort_by=value&table_query=&country=JP',
     'check': ['img.app-icon', 'span.value', '.aa-progress'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage pya user segment app used - android_phone - males_45_plus - monthly',
     'url': '#{https}/intelligence/apps/usage/?device=android_phone&android_country=JP&granularity=monthly'
            '&user_segmentation=males_45_plus&sort_by=value&table_query=&country=JP',
     'check': ['img.app-icon', 'span.value', '.aa-progress'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence usage pya user segment app used - android_phone - app_used - monthly',
     'url': '#{https}/intelligence/apps/usage/?device=android_phone&android_country=JP&granularity=monthly'
            '&user_segmentation=app_used&sort_by=value&table_query=&segment_app_id=&segment_app_market=&country=JP',
     'check': ['img.app-icon', 'span.value', '.aa-progress'],
     'env': ['production', 'staging']},
    # ===================Usage App Retention====================
    {'name': '[INT-WEB] Intelligence usage retention - Android',
     'url': '#{https}/intelligence/usage/retention/',
     'check': ['div.picker-container.clearfix', 'div.data-error-container'],
     'env': ['production', 'staging']},
    # ===================Usage App Device& App CBD====================
    {'name': '[INT-WEB]  usage app level - IOS - daily',
     'url': '#{https}/apps/ios/app/553834731/usage/?data_break_down=device&country=US&granularity=daily'
            '&chart_type=penetration&table_query=',
     'check': ['div.int-usage-table', 'div.table-mesg', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB]  usage app level - IOS - weekly',
     'url': '#{https}/apps/ios/app/553834731/usage/?data_break_down=device&country=US&granularity=weekly'
            '&chart_type=penetration&table_query=',
     'check': ['div.int-usage-table', 'div.table-mesg', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB]  usage app level - IOS - monthly',
     'url': '#{https}/apps/ios/app/553834731/usage/?data_break_down=device&country=US&granularity=monthly'
            '&chart_type=penetration&table_query=',
     'check': ['div.int-usage-table', 'div.table-mesg', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB]  usage country breakdown - IOS - daily',
     'url': '#{https}/apps/ios/app/553834731/usage/?data_break_down=country&device=ios&granularity=daily'
            '&chart_type=penetration&table_query=',
     'check': ['div.int-usage-table', 'div[data-name="data_break_down"]', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB]  usage country breakdown - IOS - weekly',
     'url': '#{https}/apps/ios/app/553834731/usage/?data_break_down=country&device=iphone&granularity=weekly'
            '&chart_type=penetration&table_query=',
     'check': ['div.int-usage-table', 'div[data-name="data_break_down"]', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB]  usage country breakdown - IOS - monthly',
     'url': '#{https}/apps/ios/app/553834731/usage/?data_break_down=country&device=ipad&granularity=monthly'
            '&chart_type=penetration&table_query=',
     'check': ['div.int-usage-table', 'div[data-name="data_break_down"]', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB]  usage app level - Android - daily',
     'url': '#{https}/apps/google-play/app/20600000578686/usage/?data_break_down=device&country=JP'
            '&granularity=daily&chart_type=penetration&table_query=',
     'check': ['div.int-usage-table', 'div.table-mesg', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB]  usage app level - Android - weekly',
     'url': '#{https}/apps/google-play/app/20600000578686/usage/?data_break_down=device&country=JP'
            '&granularity=weekly&chart_type=penetration&table_query=',
     'check': ['div.int-usage-table', 'div.table-mesg', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB]  usage app level - Android - monthly',
     'url': '#{https}/apps/google-play/app/20600000578686/usage/?data_break_down=device&country=JP'
            '&granularity=monthly&chart_type=penetration&table_query=',
     'check': ['div.int-usage-table', 'div.table-mesg', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB]  usage country breakdown - Android - daily',
     'url': '#{https}/apps/google-play/app/20600000578686/usage/?data_break_down=country&device=android'
            '&granularity=daily&chart_type=penetration&table_query=',
     'check': ['div.int-usage-table', 'div[data-name="data_break_down"]', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB]  usage country breakdown - Android - weekly',
     'url': '#{https}/apps/google-play/app/20600000578686/usage/?data_break_down=country&device=android_phone'
            '&granularity=weekly&chart_type=penetration&table_query=',
     'check': ['div.int-usage-table', 'div[data-name="data_break_down"]', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB]  usage country breakdown - Android - monthly',
     'url': '#{https}/apps/google-play/app/20600000578686/usage/?data_break_down=country&device=android_tablet'
            '&granularity=monthly&chart_type=penetration&table_query=',
     'check': ['div.int-usage-table', 'div[data-name="data_break_down"]', BREADCRUMB_COMPANY,
               BREADCRUMB_UA_LINK, BREADCRUMB_APP_EDITION],
     'env': ['production', 'staging']},
    # =======================INT MKT Creative==============================
    {'name': '[INT-WEB] INT MKT creative - iphone - admob - weekly',
     'url': '#{https}/intelligence/marketing/creatives/?view=list&device=iphone&country=JP&category=overall'
            '&network=admob&granularity=weekly&picker_type=advertiser&formats=-1&dimensions=-1'
            '&min_active_days=1&is_visible=0&order_by=creative_share&order_type=desc&page_number=0'
            '&page_size=100&app_id=',
     'check': ['.img-view', '.app-icon', 'span.value'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT MKT Creative - ipad - admob - weekly',
     'url': '#{https}/intelligence/marketing/creatives/?view=list&device=ipad&country=JP&category=overall'
            '&network=admob&granularity=weekly&picker_type=advertiser&formats=-1&dimensions=-1'
            '&min_active_days=1&is_visible=0&order_by=creative_share&order_type=desc&page_number=0'
            '&page_size=100&app_id=',
     'check': ['.img-view', '.app-icon', 'span.value'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT MKT Creative - android_phone - all - weekly',
     'url': '#{https}/intelligence/marketing/creatives/?view=list&device=android_phone&country=JP&category=game'
            '&network=all&granularity=weekly&picker_type=advertiser&formats=-1&dimensions=-1'
            '&min_active_days=1&is_visible=0&order_by=pub_count&order_type=desc&page_number=0'
            '&page_size=100&app_id=',
     'check': ['.img-view', '.app-icon', '.app-link'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT MKT Creative - iphone - all - weekly',
     'url': '#{https}/intelligence/marketing/creatives/?view=list&device=iphone&country=JP'
            '&category=overall&network=all&granularity=weekly&picker_type=advertiser'
            '&formats=-1&dimensions=-1&min_active_days=1&is_visible=0&order_by=pub_count'
            '&order_type=desc&page_number=0&page_size=100&app_id=',
     'check': ['.dashboard-meta.int-creatives-frame', '.table-container', '.aa-disclaimer'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT MKT Creative - ipad - weekly',
     'url': '#{https}/intelligence/marketing/creatives/?view=list&device=ipad&country=JP'
            '&category=applications&network=adcolony&granularity=weekly&picker_type=advertiser'
            '&formats=3&dimensions=-1&min_active_days=1&is_visible=0&order_by=pub_count'
            '&order_type=desc&page_number=0&page_size=100&app_id=',
     'check': ['.dashboard-meta.int-creatives-frame', '.table-container', '.aa-disclaimer'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT MKT Creative - android_phone - weekly',
     'url': '#{https}/intelligence/marketing/creatives/?view=list&device=android_phone&country=JP'
            '&category=family&network=admob&granularity=weekly&picker_type=advertiser'
            '&formats=2&dimensions=-1&min_active_days=1&is_visible=0&order_by=pub_count'
            '&order_type=desc&page_number=0&page_size=100&app_id=',
     'check': ['.dashboard-meta.int-creatives-frame', '.table-container', '.aa-disclaimer'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT MKT Creatives - android_tablet - weekly',
     'url': '#{https}/intelligence/marketing/creatives/?view=list&device=android_tablet&country=JP'
            '&category=game&network=chartboost&granularity=weekly&picker_type=advertiser'
            '&formats=2&dimensions=2&min_active_days=1&is_visible=0&order_by=pub_count'
            '&order_type=desc&page_number=0&page_size=100&app_id=',
     'check': ['.dashboard-meta.int-creatives-frame', '.table-container', '.aa-disclaimer'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT MKT Creatives - iphone - weekly',
     'url': '#{https}/intelligence/marketing/creatives/?view=list&device=iphone&country=JP'
            '&category=books&network=facebook&granularity=weekly&picker_type=publisher'
            '&formats=-1&dimensions=1&min_active_days=1&is_visible=0&order_by=pub_count'
            '&order_type=desc&page_number=0&page_size=100&app_id=',
     'check': ['.dashboard-meta.int-creatives-frame', '.table-container', '.aa-disclaimer'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT MKT Creatives - ipad - weekly',
     'url': '#{https}/intelligence/marketing/creatives/?view=list&device=ipad&country=JP'
            '&category=music&network=inmobi&granularity=weekly&picker_type=publisher'
            '&formats=2&dimensions=-1&min_active_days=1&is_visible=0&order_by=pub_count'
            '&order_type=desc&page_number=0&page_size=100&app_id=',
     'check': ['.dashboard-meta.int-creatives-frame', '.table-container', '.aa-disclaimer'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT MKT Creatives - android_phone - weekly',
     'url': '#{https}/intelligence/marketing/creatives/?view=list&device=android_phone&country=JP'
            '&category=family&network=ironsource&granularity=weekly&picker_type=publisher'
            '&formats=3&dimensions=2&min_active_days=1&is_visible=0&order_by=pub_count'
            '&order_type=desc&page_number=0&page_size=100&app_id=',
     'check': ['.dashboard-meta.int-creatives-frame', '.table-container', '.aa-disclaimer'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT MKT Creatives - android_tablet - weekly',
     'url': '#{https}/intelligence/marketing/creatives/?view=list&device=android_tablet&country=JP'
            '&category=application&network=twitter&granularity=weekly&picker_type=publisher'
            '&formats=3&dimensions=2&min_active_days=1&is_visible=0&order_by=pub_count'
            '&order_type=desc&page_number=0&page_size=100&app_id=',
     'check': ['.dashboard-meta.int-creatives-frame', '.table-container', '.aa-disclaimer'],
     'env': ['production', 'staging']},
    # ==========================INT MKT Advertisers===============
    {'name': '[INT-WEB] INT MKT Advertisers - iphone - weekly',
     'url': '#{https}/intelligence/marketing/advertisers/?device=iphone&country=JP&category=overall'
            '&network=admob&granularity=weekly&sort_by=value&order_by=app_sov&order_type=desc'
            '&page_number=0&page_size=100',
     'check': ['.app-icon', 'a.current'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT MKT Advertisers - android-phone - weekly',
     'url': '#{https}/intelligence/marketing/advertisers/?device=android_phone&country=JP&category=game'
            '&network=adcolony&granularity=weekly&sort_by=change&order_by=app_sov&order_type=desc'
            '&page_number=0&page_size=100',
     'check': ['.app-icon', 'a.current'],
     'env': ['production', 'staging']},
    # ==========================INT MKT Ad-Monetization===============
    {'name': '[INT-WEB] INT MKT Ad-Monetization - iphone - weekly',
     'url': '#{https}/intelligence/marketing/ad-monetization/?device=iphone&country=JP&category=overall'
            '&network=admob&granularity=weekly&sort_by=value&order_by=app_sov'
            '&order_type=desc&page_number=0&page_size=100',
     'check': ['.app-icon', 'span.rank_text', 'a.current'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] INT MKT Ad-Monetization - android_phone - weekly',
     'url': '#{https}/intelligence/marketing/ad-monetization/?device=android_phone&country=JP&category=family'
            '&network=chartboost&granularity=weekly&sort_by=change&order_by=app_sov'
            '&order_type=desc&page_number=0&page_size=100',
     'check': ['.app-icon', 'span.rank_text', 'a.current'],
     'env': ['production', 'staging']},
    # =========================INT MKT - App Level===========================
    {'name': '[INT-WEB] Intelligence MKT - advertiser app ios',
     'url': '#{https}/apps/ios/app/#{iosMktIntApp1}/intelligence/marketing/',
     'check': ['.asset-icon', '.product-name'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence marketing advertiser app android',
     'url': '#{https}/apps/google-play/app/#{gpMktIntApp1}/intelligence/marketing/',
     'check': ['.asset-icon', '.product-name'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence - MKT - advertiser app - ipad - weekly',
     'url': '#{https}/apps/ios/app/mobile-strike/intelligence/marketing/?view_type=advertiser'
            '&data_break_down=network&device=ipad&country=JP&category=overall&network=admob&granularity=weekly'
            '&date=2017-02-19&sort_by=value&order_by=app_sov&order_type=desc&page_number=0&page_size=100',
     'check': ['.asset-icon', '.product-name'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence - MKT - advertiser app - iphone - monthly',
     'url': '#{https}/apps/ios/app/mobile-strike/intelligence/marketing/?view_type=advertiser'
            '&data_break_down=network&device=iphone&country=JP&category=overall&network=admob&granularity=monthly'
            '&date=2017-01-01&sort_by=value&order_by=app_sov&order_type=desc&page_number=0&page_size=100',
     'check': ['.asset-icon', '.product-name'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence - MKT - advertiser app - iphone - weekly',
     'url': '#{https}/apps/ios/app/mobile-strike/intelligence/marketing/?view_type=advertiser'
            '&data_break_down=ad_monetization&device=iphone&country=JP&category=overall&network=all'
            '&sort_by=change&order_by=app_sov&order_type=desc&page_number=0&page_size=100&granularity=weekly'
            '&date=2017-02-19',
     'check': ['.app-icon', '.product-name'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence - MKT - advertiser - app - android_phone - weekly',
     'url': '#{https}/apps/google-play/app/com.hcg.cok.gp/intelligence/marketing/?view_type=advertiser'
            '&data_break_down=network&device=android_phone&country=JP&category=overall&network=admob'
            '&granularity=weekly&date=2017-02-19&sort_by=value&order_by=app_sov&order_type=desc'
            '&page_number=0&page_size=100',
     'check': ['.asset-icon', '.product-name'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence - MKT - advertiser - app - android_phone - monthly',
     'url': '#{https}/apps/google-play/app/com.hcg.cok.gp/intelligence/marketing/?view_type=advertiser'
            '&data_break_down=network&device=android_phone&country=JP&category=overall&network=admob'
            '&granularity=monthly&date=2017-01-01&sort_by=value&order_by=app_sov&order_type=desc'
            '&page_number=0&page_size=100',
     'check': ['.asset-icon', '.product-name'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence - MKT - advertiser - app - android_phone - weekly',
     'url': '#{https}/apps/google-play/app/com.hcg.cok.gp/intelligence/marketing/?view_type=advertiser'
            '&data_break_down=ad_monetization&device=android_phone&country=JP&category=overall&network=admob'
            '&granularity=weekly&date=2017-02-19&sort_by=value&order_by=app_sov&order_type=desc'
            '&page_number=0&page_size=100',
     'check': ['.app-icon', '.product-name'],
     'env': ['production', 'staging']},
    # ================ Verify email =================
    {'name': '[ADV] Verify email',
     'url': '#{https}/account/verify-email/',
     'check': ['.uc-con-box-white .text-center']},
    # ================ INT & File & Sample Interface =================
    {'name': '[INT-WEB] file_repository_sample_interface',
     'url': '#{https}/intelligence/file-repositories/AppAnnie_internal',
     'check': ['.folder', '.update-date', '.size'],
     'env': ['production']},
    # ================ INT MKT - Ad platform overview =================
    {'name': '[INT-WEB] Intelligence iOS Ad Platforms - ios - monthly',
     'url': '#{https}/intelligence/marketing/ad-platforms/?market=ios&granularity=monthly&date=2017-02-01',
     'check': ['.ng-isolate-scope', 'div.asset-name'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence iOS Ad Platforms CBD - ios - monthly',
     'url': '#{https}/intelligence/marketing/ad-platforms/?market=ios&country=JP&category=overall&granularity=monthly'
            '&date=2017-02-01&network=admob&data_break_down=country',
     'check': ['.ng-isolate-scope', '.percentage-with-bar-wrap'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence iOS Ad Platforms - ios - weekly',
     'url': '#{https}/intelligence/marketing/ad-platforms/?market=ios&granularity=weekly&date=2017-03-12',
     'check': ['.ng-isolate-scope', 'div.asset-name'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence iOS Ad Platforms CBD - ios - weekly',
     'url': '#{https}/intelligence/marketing/ad-platforms/?market=ios&country=JP&category=overall&granularity=weekly'
            '&network=admob&data_break_down=country&date=2017-03-12',
     'check': ['.ng-isolate-scope', '.percentage-with-bar-wrap'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence Android Ad Platforms - android - monthly',
     'url': '#{https}/intelligence/marketing/ad-platforms/?market=android&granularity=monthly&date=2017-02-01',
     'check': ['.ng-isolate-scope', 'div.asset-name'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence Android Ad Platforms CBD - android - monthly',
     'url': '#{https}/intelligence/marketing/ad-platforms/?market=android&country=JP&category=overall&date=2017-02-01'
            '&granularity=monthly&network=chartboost&data_break_down=country',
     'check': ['.ng-isolate-scope', '.percentage-with-bar-wrap'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence Android Ad Platforms - android - weekly',
     'url': '#{https}/intelligence/marketing/ad-platforms/?market=android&granularity=weekly&date=2017-03-12',
     'check': ['.ng-isolate-scope', 'div.asset-name'],
     'env': ['production', 'staging']},
    {'name': '[INT-WEB] Intelligence Android Ad Platforms CBD - android - weekly',
     'url': '#{https}/intelligence/marketing/ad-platforms/?market=android&country=JP&category=overall'
            '&granularity=weekly&network=chartboost&data_break_down=country&date=2017-03-12',
     'check': ['.ng-isolate-scope', '.percentage-with-bar-wrap'],
     'env': ['production', 'staging']},
]

cases_not_login = [
    # ==============  Home =================
    # {'name': '[CROSS] Home',
    #  'url': '#{https}/',
    #  'check': ['#HOM-hero']},
    {'name': '[CROSS] HHome-failover',
     'url': '#{https}/home-failover/',
     'check': ['.page_home']},
    {'name': '[CROSS] HLogout',
     'url': '#{https}/account/logout/',
     'check': ['#login-button']},
    # ==============  Overlay =================
    {'name': '[CROSS] Hnot-login app Dashboard',
     'url': '#{https}/dashboard/?vertical=apps',
     'check': ['#email']},
    {'name': '[ADV] Hnot-login ad revenue Dashboard',
     'url': '#{https}/ad_dashboard/ad_revenue/',
     'check': ['#email']},
    {'name': '[ADV] Hnot-login ad expense Dashboard',
     'url': '#{https}/ad_dashboard/ad_expense/',
     'check': ['#email']},
    # # ==============  Demo =================
    {'name': '[AN] demo itc Dashboard',
     'url': '#{https}/dashboard/64936/',
     'check': ['#email']},
    {'name': '[AN] demo itc single assets - Downloads',
     'url': '#{https}/dashboard/64936/item/#{itcAccountApp2}/downloads/',
     'check': ['#email']},
    {'name': '[AN] demo itc single assets - Store views',
     'url': '#{https}/dashboard/64936/item/#{itcAccountApp2}/storeviews/',
     'check': ['#email']},
    {'name': '[AN] demo google play single assets - Store views',
     'url': '#{https}/dashboard/#{gpAccountId}/item/#{gpAccountApp2}/storeviews/',
     'check': ['#email']},
    {'name': '[AN] demo itc single assets - Paying users',
     'url': '#{https}/dashboard/64936/item/#{itcAccountApp2}/payingusers/',
     'check': ['#email']},
    {'name': '[AN] demo itc single assets - Usage',
     'url': '#{https}/dashboard/64936/item/#{itcAccountApp2}/itc-usage/',
     'check': ['#email']},
    {'name': '[AN] demo Ad Revenue Dashboard',
     'url': '#{https}/ad_dashboard/ad_revenue/?demo=1',
     'check': ['#email']},
    # ==============  Index =================
    {'name': '[SS] Index Ranking',
     'url': '#{https}/indexes/all-stores/rank/?category=overall',
     'check': ['#email'],
     'env': ['production', 'staging']},
    # ['Index Reports',
    #  'url': '#{https}/indexes/all-stores/report/',
    #  'check': ['.page_index-insights', '._ribbon_title']},
    # ==============  INT Campaign page =================
    {'name': '[INT-WEB] Top Publisher - iphone',
     'url': '#{https}/apps/ios/publisher-demo/?device=iphone',
     'check': ['#email']},
    # ================  Login & register & forget password =================
    {'name': '[CROSS] Register',
     'url': '#{https}/account/register/',
     'check': ['#register-form']},
    {'name': '[CROSS] Login',
     'url': '#{https}/account/login/',
     'check': ['#email']},
    {'name': '[CROSS] Forget Password',
     'url': '#{https}/account/password-reset/',
     'check': ['#password-reset-form']},

]

cases_app_summary = [
    {'name': '[SS] SS IOS App Summary Page General Info',
     'url': '#{https}/apps/ios/app/#{iosAppSlug3}/',
     'check': ['div.app-info-mask div.app-logo', 'div.app-info-mask div.headline', 'div.store-icon-dropdown img',
               'div.content-override a[data-ga-action="Open Publisher"]', 'div#rankHistoryChart',
               'span.att-val .open-popup-link', 'div#middle-page a#appRankHistory', 'div#middle-page a#featured',
               'div#middle-page a#appStoreOptimization', 'div#middle-page a#appReviewsAndRatings',
               'div#app-description div[class="headline"]',
               'div#featured div.feature-bar', 'div#top-keywords div.headline', 'div#review-ratings div.headline',
               'div#review-ratings div.ratings-mask', 'div#explore-aa a[data-ga-action="Click Register"] button']},
    {'name': '[SS] SS google-play App Summary Page General Info',
     'url': '#{https}/apps/google-play/app/#{gpApp}/',
     'check': ['div.app-info-mask div.app-logo', 'div.app-info-mask div.headline', 'div.store-icon-dropdown img',
               'div.content-override a[data-ga-action="Open Publisher"]', 'div#rankHistoryChart',
               'span.att-val .open-popup-link', 'div#middle-page a#appRankHistory', 'div#middle-page a#featured',
               'div#middle-page a#appStoreOptimization', 'div#middle-page a#appReviewsAndRatings',
               'div.screenshots-container a.screenshot', 'div#app-description div[class="headline"]',
               'div#featured div.feature-bar', 'div#top-keywords div.headline', 'div#review-ratings div.headline',
               'div#review-ratings div.ratings-mask', 'div#explore-aa a[data-ga-action="Click Register"] button']},
    {'name': '[SS] SS Amazon App Summary Page General Info',
     'url': '#{https}/apps/amazon-appstore/app/#{amazonApp}/',
     'check': ['div.app-info-mask div.app-logo', 'div.app-info-mask div.headline', 'div.store-icon-dropdown img',
               'div.content-override a[data-ga-action="Open Publisher"]', 'div#rankHistoryChart',
               'span.att-val .open-popup-link', 'div#middle-page a#appRankHistory', 'div#middle-page a#featured',
               'div#middle-page a#appStoreOptimization', 'div#middle-page a#appReviewsAndRatings',
               'div.screenshots-container a.screenshot', 'div#app-description div[class="headline"]',
               'div#explore-aa a[data-ga-action="Click Register"] button']},
    {'name': '[SS] SS Win Phone App Summary Page General Info',
     'url': '#{https}/apps/windows-phone/app/#{wpAppSlug}/',
     'check': ['div.app-info-mask div.app-logo', 'div.app-info-mask div.headline', 'div.store-icon-dropdown img',
               'div.content-override a[data-ga-action="Open Publisher"]', 'div#rankHistoryChart',
               'span.att-val .open-popup-link', 'div#middle-page a#appRankHistory', 'div#middle-page a#featured',
               'div#middle-page a#appStoreOptimization', 'div#middle-page a#appReviewsAndRatings',
               'div.screenshots-container a.screenshot', 'div#app-description div[class="headline"]',
               'div#explore-aa a[data-ga-action="Click Register"] button']},

    {'name': '[SS] SS Mac App Summary Page General Info',
     'url': '#{https}/apps/mac/app/#{macAppSlug}/',
     'check': ['div.app-info-mask div.app-logo', 'div.app-info-mask div.headline', 'div.store-icon-dropdown img',
               'div.content-override a[data-ga-action="Open Publisher"]', 'div#rankHistoryChart',
               'span.att-val .open-popup-link', 'div#middle-page a#appRankHistory', 'div#middle-page a#featured',
               'div#middle-page a#appStoreOptimization', 'div#middle-page a#appReviewsAndRatings',
               'div#app-description a.screenshot div.img-mask', 'div#app-description div[class="headline"]',
               'div#review-ratings div.headline', 'div#review-ratings div.ratings-mask',
               'div#explore-aa a[data-ga-action="Click Register"] button']},

    {'name': '[SS] SS Win Store App Summary Page General Info',
     'url': '#{https}/apps/windows-store/app/#{wsAppSlug}/',
     'check': ['div.app-info-mask div.app-logo', 'div.app-info-mask div.headline', 'div.store-icon-dropdown img',
               'div.content-override a[data-ga-action="Open Publisher"]', 'div#rankHistoryChart',
               'span.att-val .open-popup-link', 'div#middle-page a#appRankHistory', 'div#middle-page a#featured',
               'div#middle-page a#appStoreOptimization', 'div#middle-page a#appReviewsAndRatings',
               'div#app-description a.screenshot div.img-mask', 'div#app-description div[class="headline"]',
               'div#explore-aa a[data-ga-action="Click Register"] button']},
]

cases_mkt = [
    # ==============  Pricing =================
    {'name': '[MKT] Pricing',
     'url': '#{https}/pricing/',
     'check': ['.page-pricing', '#market-data-tab']},
    # ==============  Tours =================
    {'name': '[MKT] App Analytics Tour',
     'url': '#{https}/tours/app-analytics-platform/',
     'check': ['#AAP-hero']},
    {'name': '[MKT] Market data intelligence Tour',
     'url': '#{https}/tours/market-data-intelligence/',
     'check': ['#EMD-hero']},
    {'name': '[MKT] Store Stats Tour',
     'url': '#{https}/tours/app-store-optimization/',
     'check': ['#MD-hero']},
    # ==============  Insights =================
    {'name': '[MKT] Insights',
     'url': '#{https}/insights/',
     'check': ['#react-app']},
    # ==============  About =================
    {'name': '[MKT] About',
     'url': '#{https}/about/',
     'check': ['#ABT-hero']},
    {'name': '[MKT] About Leadership',
     'url': '#{https}/about/leadership/',
     'check': ['#LDR-hero']},
    {'name': '[MKT] About Careers',
     'url': '#{https}/about/careers/',
     'check': ['#hero', '#careers', '#leadershipcta']},
    {'name': '[MKT] About Partnerships',
     'url': '#{https}/about/partnerships/',
     'check': ['#PTR-hero']},
    {'name': '[MKT] About Press',
     'url': '#{https}/about/press/',
     'check': ['#hero']},
    {'name': '[MKT] About Contact',
     'url': '#{https}/about/contact/',
     'check': ['#CON-hero']},
    # ==============  Customers =================
    {'name': '[MKT] Customers',
     'url': '#{https}/customers',
     'check': ['#CM-hero']},
    # ==============  Top Apps ==================
    {'name': '[MKT] Top Apps',
     'url': '#{https}/apps/ios/top/',
     'check': ['div.page-module.top_chart', '#free', '#paid', '#grossing', 'a.cta-button.btn-aa_blue-deep'],
     'env': ['production', 'staging']},
    # ============== Home =======================
    {'name': '[MKT] Home',
     'url': '#{https}/',
     'check': ['#hero', 'li a[data-lang="en"].active', '#capabilities', '#products']},
    # ============== Suite Pages =======================
    {'name': '[MKT] Suite Discover',
     'url': '#{https}/solutions/discover-app-market-insights',
     'check': ['#hero', '#caption-id-growth', '#caption-find-understand']},
    {'name': '[MKT] Suite Strategize',
     'url': '#{https}/solutions/strategize-mobile-app-development/',
     'check': ['#hero', '#caption-create-a-global-expansion', '#caption-bolster']},
    {'name': '[MKT] Suite Acquire',
     'url': '#{https}/solutions/acquire-mobile-users/',
     'check': ['#hero', '#caption-develop-a-data-driven-keyword', '#app-store-optimization']},
    {'name': '[MKT] Suite Engage',
     'url': '#{https}/solutions/engage-mobile-app-users/',
     'check': ['#hero', '#caption-uncover-best-practices', '#caption-easily-evaluate']},
    {'name': '[MKT] Suite Monetize',
     'url': '#{https}/solutions/monetize-mobile-app-data/',
     'check': ['#hero', '#caption2']},

    # Support link is not part of CMS project so not sure who is maintaining this site.
    # ==============  Support  =================
    # {'name': '[MKT] Support',
    # 'url': 'http://support.appannie.com/home',
    # 'check': ['#introductory_text']},
    # {'name': '[MKT] Support categories',
    # 'url': 'http://support.appannie.com/categories/20082753-Analytics-API',
    # 'check': ['.forum_tabs']},
    # {'name': '[MKT] Support entries',
    # 'url': 'http://support.appannie.com/entries/23224038-1-Quick-Start',
    # 'check': ['.entry-container']},
]
cases_mkt_language_switch = [
    # ============== Localization ==========
    # ==============  Home =================
    {'name': '[MKT] Home-ru',
     'url': '#{https}/',
     'language': 'ru',
     'check': ['#hero', 'input[placeholder="Поиск по приложениям"]', 'li a[data-lang="ru"].active',
               '#capabilities']},
    {'name': '[MKT] Home-cn',
     'url': '#{https}/',
     'language': 'cn',
     'check': ['#hero', 'input[placeholder="搜索应用"]', 'li a[data-lang="cn"].active', '#capabilities']},
    {'name': '[MKT] Home-kr',
     'url': '#{https}/',
     'language': 'kr',
     'check': ['#hero', 'input[placeholder="앱 검색"]', 'li a[data-lang="kr"].active', '#capabilities']},
    {'name': '[MKT] Home-jp',
     'url': '#{https}/',
     'language': 'jp',
     'check': ['#hero', 'input[placeholder="アプリを探す"]', 'li a[data-lang="jp"].active', '#capabilities']},
    {'name': '[MKT] Home-fr',
     'url': '#{https}/',
     'language': 'fr',
     'check': ['#hero', 'input[placeholder="Parcourir les apps"]', 'li a[data-lang="fr"].active',
               '#capabilities']},
    {'name': '[MKT] Home-de',
     'url': '#{https}/',
     'language': 'de',
     'check': ['#hero', 'input[placeholder="Apps durchsuchen"]', 'li a[data-lang="de"].active', '#capabilities']},
    # ==============  Tours =================
    {'name': '[MKT] Market Data Intelligence Tour - ru',
     'url': '#{https}/tours/market-data-intelligence',
     'language': 'ru',
     'check': ['#EMD-hero', 'input[placeholder="Поиск по приложениям"]', 'li a[data-lang="ru"].active']},
    {'name': '[MKT] Market Data Intelligence Tour - cn',
     'url': '#{https}/tours/market-data-intelligence',
     'language': 'cn',
     'check': ['#EMD-hero', 'input[placeholder="搜索应用"]', 'li a[data-lang="cn"].active']},
    {'name': '[MKT] Market Data Intelligence Tour - kr',
     'url': '#{https}/tours/market-data-intelligence',
     'language': 'kr',
     'check': ['#EMD-hero', 'input[placeholder="앱 검색"]', 'li a[data-lang="kr"].active']},
    {'name': '[MKT] Market Data Intelligence Tour - jp',
     'url': '#{https}/tours/market-data-intelligence',
     'language': 'jp',
     'check': ['#EMD-hero', 'input[placeholder="アプリを探す"]', 'li a[data-lang="jp"].active']},
    {'name': '[MKT] Market Data Intelligence Tour - fr',
     'url': '#{https}/tours/market-data-intelligence',
     'language': 'fr',
     'check': ['#EMD-hero', 'input[placeholder="Parcourir les apps"]', 'li a[data-lang="fr"].active']},
    {'name': '[MKT] Market Data Intelligence Tour - de',
     'url': '#{https}/tours/market-data-intelligence',
     'language': 'de',
     'check': ['#EMD-hero', 'input[placeholder="Apps durchsuchen"]', 'li a[data-lang="de"].active']},
]
cases_error_page = [
    # ==============  Error page =================
    {'name': '[CROSS] 404 Error Page',
     'url': '#{https}/123456/',
     'check': ['.page_error']},
]

cases_unverified = [
    {'name': '[CROSS] unverified itc Rank History',
     'url': '#{https}/apps/ios/app/454638411/rank-history/',
     'check': ['.uc-con-box-white .text-center']},
]

cases_sns = [
    {'name': '[SNS] Newsfeed Home',
     'url': '#{https}/newsfeed/',
     'check': ['[title="Newsfeed"]', '.selected.btn.dropdown-toggle .ng-scope', '.sc-feedback'] + FULL_MODE_FREE},
    {'name': '[SNS] Bookmark',
     'url': '#{https}/newsfeed/#/bookmark',
     'check': ['[title="Newsfeed"]', '.selected.btn.dropdown-toggle .ng-scope', '.app-name', '.sc-bookmark .active']},
    {'name': '[SNS] Following',
     'url': '#{https}/newsfeed/#/following',
     'check': ['[title="Newsfeed"]', '.nav-tabs a[href="#/following"]', '.following-container .aa-btn-follow',
               '.change-text']},
    {'name': '[SNS] Recommendation',
     'url': '#{https}/newsfeed/#/recommendation',
     'check': ['[title="Newsfeed"]', '.nav-tabs a[href="#/following"]', '.following-container .aa-btn-follow',
               '.app-info>a']},
    {'name': '[SNS] Preference',
     'url': '#{https}/newsfeed/#/preference',
     'check': ['[title="Newsfeed"]', '#preference_apps_0', '.explore-devices + .select2 .select2-selection__choice',
               '.set-rank-update']},
    {'name': '[SNS] App Detail Page Following Button',
     'url': '#{https}/apps/ios/app/#{iosAppSlug}/details/',
     'check': ['.aa-btn-follow']
     }
]

cases_content_filter_us = [
    {
        'name': '[SS] sensitive ios app detail',
        'url': '#{https}/apps/ios/app/#{sensitiveIOSAppSlug}/details/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive ios daily rank',
        'url': '#{https}/apps/ios/app/#{sensitiveIOSAppSlug}/app-ranking/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive ios rank history',
        'url': '#{https}/apps/ios/app/#{sensitiveIOSAppSlug}/rank-history/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[ASO] sensitive ios keywords',
        'url': '#{https}/apps/ios/app/#{sensitiveIOSAppSlug}/keywords/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive ios features',
        'url': '#{https}/apps/ios/app/#{sensitiveIOSAppSlug}/features/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive ios rating',
        'url': '#{https}/apps/ios/app/#{sensitiveIOSAppSlug}/ratings/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive ios reviews',
        'url': '#{https}/apps/ios/app/#{sensitiveIOSAppSlug}/reviews/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive gp app detail',
        'url': '#{https}/apps/google-play/app/#{sensitiveGpApp}/details/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive gp daily rank',
        'url': '#{https}/apps/google-play/app/#{sensitiveGpApp}/app-ranking/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive gp rank history',
        'url': '#{https}/apps/google-play/app/#{sensitiveGpApp}/rank-history/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[ASO] sensitive gp keywords',
        'url': '#{https}/apps/google-play/app/#{sensitiveGpApp}/keywords/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive gp features',
        'url': '#{https}/apps/google-play/app/#{sensitiveGpApp}/features/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive gp reviews',
        'url': '#{https}/apps/google-play/app/#{sensitiveGpApp}/reviews/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive amz app detail',
        'url': '#{https}/apps/amazon-appstore/app/#{sensitiveAmazonApp}/details/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive amz daily rank',
        'url': '#{https}/apps/amazon-appstore/app/#{sensitiveAmazonApp}/app-ranking/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive amz rank history',
        'url': '#{https}/apps/amazon-appstore/app/#{sensitiveAmazonApp}/rank-history/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive wp app detail',
        'url': '#{https}/apps/windows-phone/app/#{sensitiveWpApp}/details/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive wp daily rank',
        'url': '#{https}/apps/windows-phone/app/#{sensitiveWpApp}/app-ranking/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive wp rank history',
        'url': '#{https}/apps/windows-phone/app/#{sensitiveWpApp}/rank-history/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive wp reviews',
        'url': '#{https}/apps/windows-phone/app/#{sensitiveWpApp}/reviews/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive mac app detail',
        'url': '#{https}/apps/mac/app/#{sensitiveMacAppSlug}/details/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive mac daily rank',
        'url': '#{https}/apps/mac/app/#{sensitiveMacAppSlug}/app-ranking/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive mac rank history',
        'url': '#{https}/apps/mac/app/#{sensitiveMacAppSlug}/rank-history/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive mac rating',
        'url': '#{https}/apps/mac/app/#{sensitiveMacAppSlug}/ratings/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive win app detail',
        'url': '#{https}/apps/windows-store/app/#{sensitiveWsApp}/details/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive win daily rank',
        'url': '#{https}/apps/windows-store/app/#{sensitiveWsApp}/app-ranking/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive win rank history',
        'url': '#{https}/apps/windows-store/app/#{sensitiveWsApp}/rank-history/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive win reviews',
        'url': '#{https}/apps/windows-store/app/#{sensitiveWsApp}/reviews/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] sensitive other android app detail',
        'url': '#{https}/apps/other-android/app/zi-you-men-32/details/',
        'check': ['.name.ng-binding']
    },
]

cases_content_filter_cn = [
    # below url should be filtered
    {
        'name': '[SS] sensitive ios app detail',
        'url': '#{https}/apps/ios/app/#{sensitiveIOSAppSlug}/details/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive ios daily rank',
        'url': '#{https}/apps/ios/app/#{sensitiveIOSAppSlug}/app-ranking/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive ios rank history',
        'url': '#{https}/apps/ios/app/#{sensitiveIOSAppSlug}/rank-history/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[ASO] sensitive ios keywords',
        'url': '#{https}/apps/ios/app/#{sensitiveIOSAppSlug}/keywords/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive ios features',
        'url': '#{https}/apps/ios/app/#{sensitiveIOSAppSlug}/features/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive ios rating',
        'url': '#{https}/apps/ios/app/#{sensitiveIOSAppSlug}/ratings/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive ios reviews',
        'url': '#{https}/apps/ios/app/#{sensitiveIOSAppSlug}/reviews/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive gp app detail',
        'url': '#{https}/apps/google-play/app/#{sensitiveGpApp}/details/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive gp daily rank',
        'url': '#{https}/apps/google-play/app/#{sensitiveGpApp}/app-ranking/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive gp rank history',
        'url': '#{https}/apps/google-play/app/#{sensitiveGpApp}/rank-history/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[ASO] sensitive gp keywords',
        'url': '#{https}/apps/google-play/app/#{sensitiveGpApp}/keywords/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive gp features',
        'url': '#{https}/apps/google-play/app/#{sensitiveGpApp}/features/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive gp reviews',
        'url': '#{https}/apps/google-play/app/#{sensitiveGpApp}/reviews/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive amz app detail',
        'url': '#{https}/apps/amazon-appstore/app/#{sensitiveAmazonApp}/details/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive amz daily rank',
        'url': '#{https}/apps/amazon-appstore/app/#{sensitiveAmazonApp}/app-ranking/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive amz rank history',
        'url': '#{https}/apps/amazon-appstore/app/#{sensitiveAmazonApp}/rank-history/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive wp app detail',
        'url': '#{https}/apps/windows-phone/app/#{sensitiveWpApp}/details/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive wp daily rank',
        'url': '#{https}/apps/windows-phone/app/#{sensitiveWpApp}/app-ranking/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive wp rank history',
        'url': '#{https}/apps/windows-phone/app/#{sensitiveWpApp}/rank-history/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive wp reviews',
        'url': '#{https}/apps/windows-phone/app/#{sensitiveWpApp}/reviews/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive mac app detail',
        'url': '#{https}/apps/mac/app/#{sensitiveMacAppSlug}/details/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive mac daily rank',
        'url': '#{https}/apps/mac/app/#{sensitiveMacAppSlug}/app-ranking/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive mac rank history',
        'url': '#{https}/apps/mac/app/#{sensitiveMacAppSlug}/rank-history/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive mac rating',
        'url': '#{https}/apps/mac/app/#{sensitiveMacAppSlug}/ratings/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive win app detail',
        'url': '#{https}/apps/windows-store/app/#{sensitiveWsApp}/details/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive win daily rank',
        'url': '#{https}/apps/windows-store/app/#{sensitiveWsApp}/app-ranking/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive win rank history',
        'url': '#{https}/apps/windows-store/app/#{sensitiveWsApp}/rank-history/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive win reviews',
        'url': '#{https}/apps/windows-store/app/#{sensitiveWsApp}/reviews/',
        'check': ['div.error-wrapper']
    },
    {
        'name': '[SS] sensitive other android app detail',
        'url': '#{https}/apps/other-android/app/zi-you-men-32/details/',
        'check': ['div.error-wrapper']
    },
    # below page should not be filtered
    {
        'name': '[SS] non-sensitive ios app detail',
        'url': '#{https}/apps/ios/app/game-of-war-fire-age/details/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive ios daily rank',
        'url': '#{https}/apps/ios/app/facebook-messenger/app-ranking/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive ios rank history',
        'url': '#{https}/apps/ios/app/minecraft-pocket-edition/rank-history/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[ASO] non-sensitive ios keywords',
        'url': '#{https}/apps/ios/app/#{iosAppSlug}/keywords/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive ios features',
        'url': '#{https}/apps/ios/app/candy-crush-saga/features/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive ios rating',
        'url': '#{https}/apps/ios/app/pandora-radio/ratings/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive ios reviews',
        'url': '#{https}/apps/ios/app/facebook/reviews/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive gp app detail',
        'url': '#{https}/apps/google-play/app/com.mojang.minecraftpe/details/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive gp daily rank',
        'url': '#{https}/apps/google-play/app/com.facebook.orca/app-ranking/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive gp rank history',
        'url': '#{https}/apps/google-play/app/com.supercell.clashofclans/rank-history/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[ASO] non-sensitive gp keywords',
        'url': '#{https}/apps/google-play/app/com.machinezone.gow/keywords/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive gp features',
        'url': '#{https}/apps/google-play/app/com.king.candycrushsaga/features/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive gp reviews',
        'url': '#{https}/apps/google-play/app/com.supercell.boombeach/reviews/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive amz app detail',
        'url': '#{https}/apps/amazon-appstore/app/B00992CF6W/details/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive amz daily rank',
        'url': '#{https}/apps/amazon-appstore/app/B0094BB4TW/app-ranking/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive amz rank history',
        'url': '#{https}/apps/amazon-appstore/app/B0067VKQLE/rank-history/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive wp app detail',
        'url': '#{https}/apps/windows-phone/app/facebook-messenger/details/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive wp daily rank',
        'url': '#{https}/apps/windows-phone/app/plants-vs-zombies/app-ranking/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive wp rank history',
        'url': '#{https}/apps/windows-phone/app/facebook-41/rank-history/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive wp reviews',
        'url': '#{https}/apps/windows-phone/app/pandora-5/reviews/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive mac app detail',
        'url': '#{https}/apps/mac/app/os-x-yosemite/details/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive mac daily rank',
        'url': '#{https}/apps/mac/app/garageband/app-ranking/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive mac rank history',
        'url': '#{https}/apps/mac/app/kindle/rank-history/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive mac rating',
        'url': '#{https}/apps/mac/app/bundle-for-ms-office-templates/ratings/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive win app detail',
        'url': '#{https}/apps/windows-store/app/facebook-4/details/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive win daily rank',
        'url': '#{https}/apps/windows-store/app/#{appleTVSlug}-2/app-ranking/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive win rank history',
        'url': '#{https}/apps/windows-store/app/order-chaos-2/rank-history/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive win reviews',
        'url': '#{https}/apps/windows-store/app/7z/reviews/',
        'check': ['.name.ng-binding']
    },
    {
        'name': '[SS] non-sensitive other android app detail',
        'url': '#{https}/apps/other-android/app/360qing-li-da-shi/details/',
        'check': ['.name.ng-binding']
    },
]

debug_cases_after_login = [
]

debug_cases_not_login = [
    # ==============  Home =================
    # {'name': 'Home-failover',
    #  'url': '#{https}/home-failover/',
    #  'check': ['.page_home']},
]

debug_cases_unverified = [
    # ['Home',
    #  'url': '#{https}/cn/',
    #  'check': ['.home_campaign']},

]
