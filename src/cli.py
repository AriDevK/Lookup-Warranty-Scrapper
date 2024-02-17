import argparse
from utils import clear
from scrapper import search
from colored import fg, bg, attr
from prettytable import PrettyTable 


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-mf", "--manufacturer", help="Product manufacturer", default='')
    parser.add_argument("-sl", "--serial", help="Product serial", default='')
    parser.add_argument("-md", "--model", help="Product model", default='')
    parser.add_argument("-pt", "--pretty", help="Show result on a pretty format", action=argparse.BooleanOptionalAction, default=False)

    args = parser.parse_args()
    result = search(args.manufacturer, args.serial, args.model)
    clear()

    if result is None:
        output = '{}'
        if args.pretty:
            txt_styles = bg("#FFFFFF") + fg("#FF0000") + attr("bold")
            txt_reset = attr("reset")
            output = txt_styles + output + txt_reset
        
        print(output.format('Any data has been recovered'))
    else:
        banner = ''
        output = f'''
        Manufacturer: {result.manufacturer}
        Serial Number: {result.serial_number}
        Date Purchased: {result.date_purchased}
        Warranty Expiration: {result.warranty_expiration}
        '''

        if args.pretty:
            tb = PrettyTable(['Data','Value']) 
            tb.add_row(['Manufacturer', result.manufacturer])
            tb.add_row(['Serial Number', result.serial_number])
            tb.add_row(['Date Purchased', result.date_purchased])
            tb.add_row(['Warranty Expiration', result.warranty_expiration])
            output = tb

            with open('./pretty_banner.txt', 'r') as f:
                banner = ''.join(f.readlines())
                print(banner)

        print(output)
