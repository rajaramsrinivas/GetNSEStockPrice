import sys
import argparse
from GoogleApi import GoogleApi
from YahooApi import YahooApi
#import email_base
parser = argparse.ArgumentParser(description='Gets stock prices of scrips listed in NSE')
parser.add_argument('scrips', metavar='s',
                    action="store",
                    help='Comma separated list of scrips by scrip_code in NSE')
MAX_RETRIES = 5

def get_stock_price(scrips, api_preference='Google', retries=0):
    """
        Fetches stock prices of scrips supplied as a list of strings
    """
    api_obj = None
    if retries > MAX_RETRIES:
        print >> sys.stderr, "Retries exceeded"
        return None
    if api_preference == 'Google':
        api_obj = GoogleApi()
    else:
        api_obj = YahooApi()
    scrip_data = None
    try:
        scrip_data = api_obj.get_data(scrips)
    except Exception, err_msg:
        email_base.send_mail('%s API call failed with error msg %s'%(api_preference, err_msg))
        if api_preference == 'Google':
            return get_stock_price(scrips, api_preference='Yahoo', retries=retries+1)
        else:
            return get_stock_price(scrips, api_preference='Google',retries=retries+1)
    return scrip_data

if __name__ == '__main__':
    args = parser.parse_args()
    print get_stock_price (args.scrips.split(','))
