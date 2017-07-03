from selenium import webdriver
import os


def create_modheaders_plugin(add_or_modify_headers=None):
    """Create modheaders extension

    kwargs:
        plugin_path (str): absolute plugin path
        add_or_modify_headers (dict): ie. {"Header-Name": "Header Value"}

    return str -> plugin path
    """
    import string
    import zipfile

    plugin_path = '/tmp/modheaders_plugin.zip'

    if os.path.exists(plugin_path):
        return plugin_path

    if add_or_modify_headers is None:
        add_or_modify_headers = {}

    manifest_json = """
    {
        "version": "1.0.0",
        "manifest_version": 2,
        "name": "Chrome HeaderModV",
        "permissions": [
            "webRequest",
            "tabs",
            "unlimitedStorage",
            "storage",
            "<all_urls>",
            "webRequestBlocking"
        ],
        "background": {
            "scripts": ["background.js"]
        },
        "minimum_chrome_version":"58.0.0"
    }
    """

    background_js = string.Template("""
    function callbackFn(details) {
        var add_or_modify_headers = ${add_or_modify_headers};

        // modify headers
        for (var i = 0; i < details.requestHeaders.length; ++i) {
            if (add_or_modify_headers.hasOwnProperty(details.requestHeaders[i].name)) {
                details.requestHeaders[i].value = add_or_modify_headers[details.requestHeaders[i].name];
                delete add_or_modify_headers[details.requestHeaders[i].name];
            }
        }
        // add headers
        for (var prop in add_or_modify_headers) {
            details.requestHeaders.push(
                {name: prop, value: add_or_modify_headers[prop]}
            );
        }

        return {requestHeaders: details.requestHeaders};
    }

    chrome.webRequest.onBeforeSendHeaders.addListener(
                callbackFn,
                {urls: ["<all_urls>"]},
                ['blocking', 'requestHeaders']
    );
    """).substitute(add_or_modify_headers=add_or_modify_headers)
    with zipfile.ZipFile(plugin_path, 'w') as zp:
        zp.writestr("manifest.json", manifest_json)
        zp.writestr("background.js", background_js)
    #import pdb;pdb.set_trace()
    return plugin_path


options = webdriver.ChromeOptions()

# options.binary_location = '/Users/jundongli-ext/Downloads/chromedriver'

mod_headers_plugin_path = create_modheaders_plugin({'Referer': 'www.appannie.com'})
options.add_extension(mod_headers_plugin_path)

#driver = webdriver.Chrome('/Users/jundongli-ext/Downloads/chromedriver')

#options.add_argument('headless')
options.add_argument('window-size=1200x600')

chrome_driver = '/Users/jundongli-ext/Downloads/chromedriver'
driver = webdriver.Chrome(executable_path=chrome_driver, chrome_options=options)
driver.get("http://baidu.com/")
driver.save_screenshot("codingpy.png")

driver = webdriver.Chrome('/Users/jundongli-ext/Downloads/chromedriver')



